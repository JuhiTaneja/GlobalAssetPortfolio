import pandas as pd
data=pd.read_csv('clean_global_assets.csv',index_col='Date',parse_dates=True)
returns=data.pct_change()
returns_change=returns.dropna()
returns_change.to_csv('daily_returns.csv')

import pandas as pd 
df=pd.read_csv('daily_returns.csv')
print(df.index)
print(df.columns)
df['Date']=pd.to_datetime(df['Date'])
df.set_index('Date',inplace=True)
print(df.index)






import pandas as pd 
df=pd.read_csv('daily_returns.csv')
print(df.isnull().values.any())

# annualised volatility
import numpy as np 
daily_volatility=returns_change.std()
annual_volatility=daily_volatility*np.sqrt(252)
print('Annualised Volatility:')
print(annual_volatility)

#  annualized return 
annualized_return=returns_change.mean() * 252
print("annualised returns")
print(annualized_return)

# sharpe ratio 
risk_free_rate=0.05
sharpe_ratio=(annualized_return-risk_free_rate)/annual_volatility

# correlation metrics

correlation_matrix=returns.corr()

#  saving metric to a csv file 

metrics=pd.DataFrame({'Annualized Return':annualized_return,'Annualized Volatility': annual_volatility,'Sharpe Ratio':sharpe_ratio})

metrics.to_csv('asset_metrics.csv')
correlation_matrix.to_csv('correlation_matrix.csv')

print('Metrics saved successfully')
print(metrics)

covariance_matrix=returns_change.cov()*252
print("Covariance_matrix")
print(covariance_matrix)
covariance_matrix.to_csv('covariance.csv')

# potfolio_optimisation 

import numpy as np 
import pandas as pd
data=pd.read_csv('asset_metrics.csv')
from scipy.optimize import minimize

risk_free_rate=0.05

def portfolio_performance(weights,returns,covariance):
    returns=np.array(returns)
    weights=np.array(weights)
    port_return=np.sum(returns*weights)
    port_volatility=np.sqrt(np.dot(weights.T,np.dot(covariance,weights)))
    sharpe_ratio=(port_return-risk_free_rate)/port_volatility
    return port_return,port_volatility,sharpe_ratio

def negative_sharpe(weights,returns,covariance):
    return -portfolio_performance(weights,returns,covariance)[2]


constraints=({'type':'eq','fun':lambda x:np.sum(x)-1})


bounds=tuple((0,1) for _ in range (len (annualized_return)))

init_weights=np.array(len(annualized_return)*[1/len(annualized_return)])

result=minimize(negative_sharpe,init_weights,args=(annualized_return,covariance_matrix),method='SLSQP',bounds=bounds,constraints=constraints)

optimal_weights=result.x

print("optimal potfolio weights",optimal_weights)
print("Expected Return, Volatility, Sharpe Ratio :", portfolio_performance(optimal_weights,annualized_return,covariance_matrix))

print({"Expected Return": portfolio_performance(optimal_weights,annualized_return,covariance_matrix)[1]})

# #  saving the optimal values 

weights_df=pd.DataFrame({'Assets': annualized_return.index,'Optimal Weight': optimal_weights})


port_return, port_volatility, port_sharpe = portfolio_performance(optimal_weights, annualized_return, covariance_matrix)

portfolio_summary = pd.DataFrame({
    'Metrics': ['Expected Return', 'Expected Volatility', 'Sharpe Ratio'],
    'Value': [port_return, port_volatility, port_sharpe]
})

print(portfolio_summary)


weights_df.to_csv ('optimal_portfolio.csv',index=False)
portfolio_summary.to_csv('portfolio_optimisation.csv',index=False)