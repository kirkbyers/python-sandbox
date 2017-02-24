'''Gets the price history for twitter'''
from get_data.intrino_history import get_id_price_history
from pg import DB

MY_DB = DB(dbname='Stocks')

TWITER_HISTORY = get_id_price_history('TWTR')

for entry in TWITER_HISTORY:
    MY_DB.insert(
        'TWTR_HISTORY',
        ex_dividend=entry['ex_dividend'],
        volume=entry['volume'],
        adj_volume=entry['adj_volume'],
        adj_low=entry['adj_low'],
        adj_high=entry['adj_high'],
        adj_open=entry['adj_open'],
        adj_close=entry['adj_close'],
        open=entry['open'],
        close=entry['close'],
        high=entry['high'],
        low=entry['low'],
        date=entry['date'],
        split_ratio=entry['split_ratio']
    )

print MY_DB.get_tables()
print MY_DB.query('select * from "TWTR_HISTORY"')
