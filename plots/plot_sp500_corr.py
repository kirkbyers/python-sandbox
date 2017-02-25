'''plot corr of sp500'''
import matplotlib.pyplot as plt
from matplotlib import style
import pandas as pd
import numpy as np

def plot_sp500_corr():
    '''Plots correlation spn500 from CSV in root'''
    style.use('ggplot')

    df = pd.read_csv('sp500_joined_closes.csv')
    df_corr = df.corr()

    print(df_corr.head())

    data = df_corr.values
    fig = plt.figure()
    ax = fig.add_subplot(1,1,1)

    # suggested formating for correlation
    heatmap = ax.pcolor(data, cmap=plt.cm.RdYlGn)
    fig.colorbar(heatmap)
    ax.set_xticks(np.arange(data.shape[0]) + 0.5, minor=False)
    ax.set_yticks(np.arange(data.shape[1]) + 0.5, minor=False)
    ax.invert_yaxis()
    ax.xaxis.tick_top()

    column_lables = df_corr.columns
    row_labels = df_corr.index

    ax.set_xticklabels(column_lables)
    ax.set_yticklabels(row_labels)
    plt.xticks(rotation=90)
    heatmap.set_clim(-1, 1)
    plt.tight_layout()
    plt.show()
    