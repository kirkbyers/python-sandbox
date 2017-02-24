'''Gets stock history using pandas'''
import pickle
import requests
import pandas as pd
import bs4 as bs

def get_sandp500_tickers():
    '''Gets history of SandP500'''
    resp = requests.get('https://en.wikipedia.org/wiki/List_of_S%26P_500_companies')
    soup = bs.BeautifulSoup(resp.text, 'lxml')
    table = soup.find('table', {'class': 'wikitable sortable'})
    tickers = []
    for row in table.findAll('tr')[1:]:
        ticker = row.findAll('td')[0].text
        tickers.append(ticker)

    with open("sp500tickers.pickle", 'wb') as file:
        pickle.dump(tickers, file)

    print tickers

    return tickers
