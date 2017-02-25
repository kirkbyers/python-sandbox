'''thing'''
from collections import Counter
import pickle
import numpy as np
import pandas as pd
from sklearn import svm, cross_validation, neighbors
from sklearn.ensemble import VotingClassifier, RandomForestClassifier

def process_data_for_labels(ticker, number_days):
    '''Percent a ticker changes in Y days'''
    #Y days
    hm_days = number_days
    df = pd.read_csv('sp500_joined_closes.csv', index_col=0)
    tickers = df.columns.values.tolist()
    df.fillna(0, inplace=True)

    for i in range(1, hm_days+1):
        df['{}_{}d'.format(ticker, i)] = ((df[ticker].shift(-i) - df[ticker]) / df[ticker])

    df.fillna(0, inplace=True)
    return tickers, df

def buy_sell_hold(*args):
    '''Classify tickers by percent change'''
    cols = [c for c in args]
    # requirment to be classified as 1 or -1
    requirement = 0.022
    for col in cols:
        if col > requirement:
            return 1
        if col < -requirement:
            return -1

    return 0

def extract_featursets(ticker):
    '''Get and label percent change last 7 days for ticker'''
    tickers, df = process_data_for_labels(ticker, 7)

    df['{}_target'.format(ticker)] = list(
        map(
            buy_sell_hold,
            df['{}_1d'.format(ticker)],
            df['{}_2d'.format(ticker)],
            df['{}_3d'.format(ticker)],
            df['{}_4d'.format(ticker)],
            df['{}_5d'.format(ticker)],
            df['{}_6d'.format(ticker)],
            df['{}_7d'.format(ticker)]
        )
    )
    vals = df['{}_target'.format(ticker)].values.tolist()
    str_vals = [str(i) for i in vals]
    # Count labels
    print('Data spread:', Counter(str_vals))

    df.fillna(0, inplace=True)

    df = df.replace([np.inf, -np.inf], np.nan)
    df.dropna(inplace=True)

    df_vals = df[[ticker for ticker in tickers]].pct_change()
    df_vals = df_vals.replace([np.inf, -np.inf], 0)
    df_vals.fillna(0, inplace=True)

    X = df_vals.values
    y = vals

    return X, y, df

def fit_ticker(ticker):
    '''Train scikit to classify a ticker'''
    X, y, df = extract_featursets(ticker)

    # 75:25 train:test
    X_train, X_test, y_train, y_test = cross_validation.train_test_split(X, y, test_size = 0.25)

    # Vote to find best of 3 classifiers out of box
    clf = VotingClassifier([('lsvc', svm.LinearSVC()), ('knn', neighbors.KNeighborsClassifier()), ('rfor', RandomForestClassifier())])

    clf.fit(X_train, y_train)
    confidence = clf.score(X_test, y_test)
    print('Accuracy: {}'.format(confidence))
    predictions = clf.predict(X_test)

    print('Predicted spread: {}'.format(Counter(predictions)))

    return confidence