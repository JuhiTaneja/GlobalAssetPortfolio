import pandas as pd 
import numpy as np 
from scipy import stats

data=pd.read_csv('daily_returns.csv',index_col="Date",parse_dates=True)

Assets= ['^NSEI', '^GSPC', '^FTSE', 'GC=F', 'CL=F']

Result=[]

for asset in Assets:
    returns=data[asset].dropna()
    mean_return=np.mean(returns)
    sem=stats.sem(returns)
    conf_int=stats.t.interval(0.95,len(returns)-1,loc=mean_return,scale=sem)
    
    Result.append({'Asset':asset,
               'Mean daily returns':round(mean_return,6),
               'Lower Conf_Int':conf_int[0],
               'Upper Conf_Int':conf_int[1]})

result_df=pd.DataFrame(Result)
result_df.to_csv('confidence_interval.csv',index=False)


