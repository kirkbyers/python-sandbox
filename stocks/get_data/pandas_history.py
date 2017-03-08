'''Get data for tickerlist'''
import datetime as dt
import os
import pickle
import time
import pandas as pd
import pandas_datareader.data as web

from wiki_sp500_tickers import get_sandp500_tickers

def get_data_from_yahoo(reload_sp500=False):
    '''Get data from yahoo'''
    if reload_sp500:
        tickers = get_sandp500_tickers()
    else:
        with open('sp500tickers.pickle', 'rb') as file:
            tickers = pickle.load(file)

    if not os.path.exists('data'):
        os.makedirs('data')

    #Get history from 1-1-2000 to 2-16-2017
    start = dt.datetime(2000,1,1)
    end = dt.datetime(2017,2,16)

    for ticker in tickers:
        print ticker
        #If we already have history, skip it
        if not os.path.exists('data/{}.csv'.format(ticker)):
            #Try. Some tickers aren't correct or available
            try:
                df = web.DataReader(ticker, 'yahoo', start, end)
                df.to_csv('data/{}.csv'.format(ticker))
            except:
                pass

            #Prevent timeout
            time.sleep(2)
        else:
            print('Already have {}'.format(ticker))
