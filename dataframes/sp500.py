'''build sp500 df'''
import pickle
import pandas as pd

def build_sp500_df():
    '''Builds df for sp 500'''
    with open('sp500tickers.pickle', 'rb') as file:
        tickers = pickle.load(file)

    main_df = pd.DataFrame()

    for count, ticker in enumerate(tickers):
        try:
            df = pd.read_csv('data/{}.csv'.format(ticker))
            df.set_index('Date', inplace=True)

            df.rename(columns = {'Adj Close': ticker}, inplace=True)
            df.drop(['Open', 'High', 'Low', 'Close', 'Volume'], 1, inplace = True)

            if main_df.empty:
                main_df = df
            else:
                main_df = main_df.join(df, how='outer')
        except:
            pass

        if count % 10 == 0:
            print count

    print(main_df.head())
    main_df.to_csv('sp500_joined_closes.csv')
