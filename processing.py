import pandas as pd
import datetime as dt
import xlrd
data_source = r'stock.xlsx'
data_source2 = r'cal.xlsx'
df = pd.read_excel(data_source, index_col='Date')
ndayforward = 2
df['day_chg'] = (df['close'].pct_change())*100
df['ndaychg'] = df['day_chg'].shift(-ndayforward)
dcriteria = (df.index >= '2000-05-05') & (df.index <= dt.datetime.today())
tcriteria = df['day_chg'] < -1
criteria = (dcriteria & tcriteria)
#print (df[criteria].tail())
#print (df[criteria].loc[:, ['close', 'ndaychg']].agg(['mean', 'median', 'std']))
dfc = (df[criteria].loc[:, ['close', 'ndaychg']].agg(['mean', 'median', 'std']))
dfc.to_excel(data_source2)
wb = xlrd.open_workbook(data_source2)
sheet = wb.sheet_by_index(0)
h = []
for row in range(sheet.nrows):
    h.append(sheet.cell_value(row, 2))
mean = h[1]
std = h[3]
dep = mean - std
inc = mean + std
print('From the Given Stock Data i presume there will be a 50 percent chance that the stock will Increase by ' + str(inc) +'\n\n\t\t\t or \n')
print('There will be a 34 percent chance that the stock will Decrease by ' + str(dep))
