'''A Test dumby doc'''
import pandas as pd
# from train.single_company import fit_ticker
#from plots.plot_sp500_corr import plot_sp500_corr
from dataframes.sp500_yearly import build_sp500_yearly_df

# plot_sp500_corr()
# extract_featursets('XOM')
# fit_ticker('BAC')

# build_sp500_yearly_df(2015)
df = pd.read_csv('sp500_joined_closes_2015.csv', index_col=0)

print(df.head())