#  t test between NSEI and GSPC


import pandas as pd
data=pd.read_csv('daily_returns.csv',index_col='Date',parse_dates=True)
print(data.head())

from scipy.stats import ttest_ind

nifty=data['^NSEI'].dropna()
sp500=data['^GSPC'].dropna()

t_stat,p_val=ttest_ind(nifty,sp500,equal_var=False)

print("T-test result:")
print(f"T-statistic:{t_stat:.4f},P-value:{p_val:.4f}")

if p_val<.05:
    print("mean between nifty and S&P 500 are significantly different")
else:
    print("mean between nifty and S&P 500 are not statistically different")

#  t test between FTSE and GSPC



ftse=data['^FTSE'].dropna()

t_stat,p_val=ttest_ind(sp500,ftse,equal_var=False)

print("T-test result:")
print(f"T-statistics:{t_stat:.4f},P-value:{p_val:.4f}")

if p_val<.05:
    print("mean between S&P500 and ftse are significantly different")
else:
    print("mean between ftse and S&P 500 are not statistically different")

# t test between NSEI and FTSE

nifty=data['^NSEI'].dropna()
ftse=data['^FTSE'].dropna()


t_stat,p_val=ttest_ind(nifty,ftse,equal_var=False)

print("T-test result:")
print(f"T-statistics:{t_stat:.4f},P-value:{p_val:.4f}")

if p_val<.05:
    print("mean between nifty and ftse are significantly different")
else:
    print("mean between ftse and nifty are not statistically different")


# t test between Gold and Oil 

gold=data['GC=F'].dropna()
Oil=data['CL=F'].dropna()

t_stat,p_val=ttest_ind(gold,Oil,equal_var=False)

print("T-test result:")
print(f"T-statistics:{t_stat:.4f},P-value:{p_val:.4f}")

if p_val<.05:
    print("mean between gold and oil are siginificantlly different")

else:
    print("mean betweeb gold and oil are not statistically different")


# t test between Gold and S&P500

gold=data['GC=F'].dropna()
sp500=data['^GSPC'].dropna()


t_stat,p_val=ttest_ind(gold,sp500,equal_var=False)

print("T-test result:")
print(f"T-statistics:{t_stat:.4f},P-value:{p_val:.4f}")

if p_val<.05:
    print("mean between gold and S&P500 are siginificantlly different")

else:
    print("mean betweeb gold and S&P 500 are not statistically different")

# saving of the results of the t test 


import pandas as pd 
data={'Asset1':['Nifty 50','FTSE 100','FTSE 100','Gold','Gold'],
      'Asset2':['S&P 500','S&P 500','Nifty 50','Oil','S&P 500'],
      'T Statistic':[-0.0499,1.1677,1.1584,0.8776,-0.4361],
      'P Value':[0.9602,0.2430,0.2468,0.3802,0.6628]
}

ttest_results=pd.DataFrame(data)
ttest_results['significant(p<0.05)']=ttest_results['P Value'].apply(lambda p: 'Yes' if p<0.05 else 'No')

ttest_results.to_csv('T_test_result.csv',index=False)







