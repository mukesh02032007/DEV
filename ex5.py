import matplotlib as mpl 
import matplotlib.pyplot as plt 
import seaborn as sns 
import numpy as np 
import pandas as pd 
plt.rcParams.update({'figure.figsize': (10, 7), 'figure.dpi': 120}) 
#df=pd.read_csv('a10.csv', parse_dates=['date']) 
#print(df.head())
df=pd.read_csv('a10.csv', parse_dates=['date'], index_col='date') 
# Draw Plot 
def plot_df(df, x, y, title="", xlabel='Date', ylabel='Value', dpi=100): 
    plt.figure(figsize=(16,5), dpi=dpi) 
    plt.plot(x, y, color='tab:red') 
    plt.gca().set(title=title, xlabel=xlabel, ylabel=ylabel) 
plot_df(df, x=df.index, y=df.value, title='Monthly anti-diabetic drug sales in Australia from 1992 to 2008.') 
plt.show()
