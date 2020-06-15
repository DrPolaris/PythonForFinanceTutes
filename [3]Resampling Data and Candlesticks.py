import matplotlib
import matplotlib.pyplot as plt
from matplotlib import style
import matplotlib.dates as mdates
import datetime as dt
import pandas as pd
import pandas_datareader.data as web
import mplfinance as mpf

#style.use('ggplot')
#start = dt.datetime(2016,1,1)
#end = dt.datetime(2020,1,1)

#df = web.DataReader('TSLA', 'yahoo', start, end)
#df.reset_index(inplace=True)
#df.set_index("Date", inplace = True)
#df.to_csv('/home/arjun/Documents/PyScripts/Fin/tesla.csv')
df = pd.read_csv('tesla.csv', parse_dates=True,index_col=0)

df_ohlc = df['Adj Close'].resample('10D').ohlc()# Resamples the data
df_volume = df['Volume'].resample('10D').sum()

#print(df_ohlc.head())

#mpf.plot(df_ohlc,type = 'candle')
#ax1 = plt.subplot2grid((6,1), (0,0), rowspan = 5, colspan = 1)
#ax2 = plt.subplot2grid((6,1), (5,0), rowspan = 1, colspan = 1, sharex = ax1)
#ax1.xaxis_date()

#candlestick_ohlc(ax1, df_ohlc.values, width = 2, colorup = 'g')
#ax2.fill_between(df_volume.index.map(mdates.date2num,df_volume.values, 0))
mpf.plot(df, type = 'candle', style = 'charles')
