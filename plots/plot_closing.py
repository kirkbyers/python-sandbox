'''Creates plot of closings costs'''
import pandas as pd
import matplotlib.pyplot as plt

def plot_closing(X, Y):
    '''Plots X vs Y'''
    df = pd.DataFrame()
    df['x'] = X
    df['y'] = Y
    df.plot(x='x', y='y', marker='.')
    plt.show()
