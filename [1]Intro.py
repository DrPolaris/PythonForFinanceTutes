import matplotlib
#matplotlib.use('GTK3Agg')
import matplotlib.pyplot as plt
from matplotlib import style  # Everything is cool as long as you get beautiful graphs
import datetime as dt  # To get time series data of stock
import pandas as pd
import pandas_datareader.data as web

style.use('ggplot') #One of the many styles
#start = dt.datetime(2019,1,1)
#end = dt.datetime(2020,1,1)

#df = web.DataReader('TSLA', 'yahoo', start, end)
#df.reset_index(inplace=True)
#df.set_index("Date", inplace = True)
#df = df.drop('Symbol', axis = 1)
#df.to_csv('/home/arjun/Documents/PyScripts/Fin/tesla.csv')
df2 = pd.read_csv('tesla.csv', parse_dates=True,index_col=0)
print(df2.head())
#df2['Date']=pd.to_datetime(df2['Date'])
#df2['Date']=df2['Date'].astype('datetime64[ns]')
print(df2.info())
df2.plot()
plt.show()
# print(df.head()) #Prints 5 rows of datahead
