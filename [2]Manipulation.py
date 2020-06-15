import matplotlib
import matplotlib.pyplot as plt
from matplotlib import style
import datetime as dt
import pandas as pd
import pandas_datareader.data as web

#style.use('ggplot')
#start = dt.datetime(2016,1,1)
#end = dt.datetime(2020,1,1)

#df = web.DataReader('TSLA', 'yahoo', start, end)
#df.reset_index(inplace=True)
#df.set_index("Date", inplace = True)
#df.to_csv('/home/arjun/Documents/PyScripts/Fin/tesla.csv')
df2 = pd.read_csv('tesla.csv', parse_dates=True,index_col=0)
#df2.plot()
#plt.show()

df2['100ma'] = df2['Adj Close'].rolling(window = 100,min_periods=0).mean()
#print(df2.tail())
ax1 = plt.subplot2grid((6,1), (0,0), rowspan = 5, colspan = 1)
ax2 = plt.subplot2grid((6,1), (5,0), rowspan = 1, colspan = 1, sharex = ax1)

ax1.plot(df2.index, df2['Adj Close'])
ax1.plot(df2.index, df2['100ma'])
ax2.bar(df2.index, df2['Volume'])

plt.show()



