import yfinance as yf


tickers = ['^GSPC', '^NSEI', '^FTSE', 'GC=F', 'CL=F']

# Download prices from Yahoo, for the last 10 years
data = yf.download(
    tickers,
    start='2015-01-01',
    end='2024-12-31',
    auto_adjust=False
)['Adj Close']


# Save it to a CSV file 
data.to_csv('global_assets.csv')


import pandas as pd 
df=pd.read_csv('global_assets.csv')
print(df.head())
print("Shape:",df.shape)
print("Collumns:",df.columns)

import pandas as pd
data=pd.read_csv('global_assets.csv',index_col='Date',parse_dates=True)
d=data.dropna()
d.to_csv('clean_global_assets.csv')

import pandas as pd 
df=pd.read_csv('clean_global_assets.csv')
print(df.head())
print("Shape :", df.shape)
print("Columns:",df.columns)








