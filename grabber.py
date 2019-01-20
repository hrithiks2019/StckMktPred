import pandas_datareader.data as web
import datetime as dt
start = dt.datetime(2017, 5, 5)
end = dt.datetime.today()
stock = '^DJI'
df = web.DataReader(stock, 'yahoo', start, end)
df = df.rename(columns={'Adj Close': 'close'})
df = df.loc[:, ['Open', 'High', 'Low', 'close', 'Volume']]
print (df.tail())
data_source = r'stock.xlsx'
df.to_excel(data_source)


