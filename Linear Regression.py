import pandas as pd
import quandl
import math
df = quandl.get('WIKI/GOOGL')
df = df[['Adj. Open','Adj. High','Adj. Low','Adj. Close','Adj. Volume']]
df['LH_PCT'] = (df['Adj. High'] - df['Adj. Low']) / df['Adj. Low']
df['PCT'] = (df['Adj. Close'] - df['Adj. Open']) / df['Adj. Open']

df = df[['Adj. Close','LH_PCT','PCT','Adj. Volume']]
forecast_col = 'Adj. Close'
df.fillna(-9999, inplace=True)
forecast_out = int(math.ceil(0.1*len(df)))
df['Label']=df[forecast_col].shift(-forecast_out)
print(df.head())
