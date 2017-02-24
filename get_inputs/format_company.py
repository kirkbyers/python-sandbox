'''Get data from db and format to be used to be fed forward'''
from pg import DB
import pandas as pd

STOCKS_DB = DB(dbname='Stocks')

def select_company_day(table_name, date):
    '''Select row where date is date'''
    query = STOCKS_DB.query('Select * from "' + table_name + '" where date=\'' + date + '\'')
    if query.getresult():
        return query.getresult()[0]
    else:
        return False

def select_closing_day(table_name, date):
    '''Returns close of row of date'''
    query = STOCKS_DB.query('Select close from "' + table_name + '" where date=\'' + date + '\'')
    if query.dictresult():
        return query.dictresult()[0]['close']
    else:
        return False

def format_company(table_name, start_date, end_date):
    '''Returns Data read for feedforward'''
    history_span = pd.date_range(start=start_date, end=end_date)
    total = []
    vals = []
    dates = []
    for date in history_span:
        data_point_result = []
        # Only weekdays valid
        if date.weekday() < 5:
            entry_date_range = pd.date_range(end=date, periods=8, freq="D")
            day_closing_cost = select_closing_day('TWTR_HISTORY', date.strftime('%Y-%m-%d'))
            if day_closing_cost:
                vals.append(day_closing_cost)
                dates.append(date)
                #Get the last week of weekdays
                for single_date in entry_date_range[:7]:
                    if single_date.weekday() < 5:
                        single_history_row = select_company_day(table_name, single_date.strftime('%Y-%m-%d'))
                        if single_history_row:
                            data_point_result.append(float(single_history_row[1]))
                            data_point_result.append(float(single_history_row[2]))
                            data_point_result.append(float(single_history_row[3]))
                            data_point_result.append(float(single_history_row[4]))
                            data_point_result.append(float(single_history_row[5]))
                            data_point_result.append(float(single_history_row[6]))
                            data_point_result.append(float(single_history_row[7]))
                            data_point_result.append(float(single_history_row[8]))
                            data_point_result.append(float(single_history_row[9]))
                            data_point_result.append(float(single_history_row[10]))
                            data_point_result.append(float(single_history_row[11]))
                            #Uncomment to varify dates
                            #data_point_result.append(single_history_row[12])
                        else:
                            print single_date

                if len(data_point_result) == 55:
                    total.append(data_point_result)
                else:
                    print len(data_point_result), date

    result = {}
    result['X'] = total
    result['Y'] = vals
    result['dates'] = dates
    return result
