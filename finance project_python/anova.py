import pandas as pd

data=pd.read_csv('daily_returns.csv',index_col='Date',parse_dates=True)

from scipy.stats import f_oneway

groups=[data[col].dropna() for col in ['^NSEI', '^GSPC', '^FTSE', 'GC=F', 'CL=F']]

f_stat,p_val=f_oneway(*groups)

print("Anova result")
print(f"F-statistic :{f_stat:.4f},P-val :{p_val:.4f}")

if p_val<0.05:
    print("At least one asset has a significantly different mean return")
else:
    print("No significant difference in mean returns among assets")


import pandas as pd
data={'F-statistics':[0.7724],'P-Value':[0.5430],
      'Interpretation':['No significant difference in mean returns among assets']}


anova_result=pd.DataFrame(data)
anova_result.to_csv('anova_result.csv',index=False)

