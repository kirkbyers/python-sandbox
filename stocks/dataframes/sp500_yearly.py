'''Build'''
import datetime as dt
import pickle
import pandas as pd

def build_sp500_yearly_df(year):
    '''Given a year build a df of closing costs'''
    with open('sp500tickers.pickle', 'rb') as file:
        tickers = pickle.load(file)

    main_df = pd.DataFrame()

    for count, ticker in enumerate(tickers):
        try:
            df = pd.read_csv('data/{}.csv'.format(ticker))
            df.set_index('Date', inplace=True)

            df.rename(columns = {'Adj Close': ticker}, inplace=True)
            df.drop(['Open', 'High', 'Low', 'Close', 'Volume'], 1, inplace=True)

            if main_df.empty:
                main_df = df
            else:
                main_df = main_df.join(df, how='outer')
        except:
            pass

        if count % 10 == 0:
            print(count)

    start_date = str(year) + '-01-01'
    end_date = str(year) + '-12-31'
    
    print(main_df[start_date:end_date].head())
    main_df[start_date:end_date].to_csv('sp500_joined_closes_{}.csv'.format(year))
    return main_df[start_date:end_date]
