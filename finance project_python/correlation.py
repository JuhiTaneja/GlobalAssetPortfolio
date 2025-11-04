import pandas as pd
from scipy.stats import pearsonr


daily_returns=pd.read_csv('daily_returns.csv',index_col='Date',parse_dates=True)

assets = ['^NSEI', '^GSPC', '^FTSE', 'GC=F', 'CL=F']

for i in range (len(assets)):
    for j in range (i+1,len(assets)):
        asset1=daily_returns[assets[i]].dropna()
        asset2=daily_returns[assets[j]].dropna()


        r,p_value =pearsonr(asset1,asset2)

        print(f"Correlation between {assets[i]} and {assets[j]}: r={r:.3f},p_value={p_value:.3f}")

        if p_value<0.05:
            print(f"--> This correlation is statistically significant .\n")
        else:
            print(f"--> This correlation is NOT statistically significant.\n")

#  saving the results 


data = {
    'Asset 1': ['^NSEI', '^NSEI', '^NSEI', '^NSEI', '^GSPC', '^GSPC', '^GSPC', '^FTSE', '^FTSE', 'GC=F'],
    'Asset 2': ['^GSPC', '^FTSE', 'GC=F', 'CL=F', '^FTSE', 'GC=F', 'CL=F', 'GC=F', 'CL=F', 'CL=F'],
    'Correlation (r)': [0.318, 0.463, -0.007, 0.055, 0.533, 0.025, 0.140, -0.018, 0.120, 0.040],
    'P-Value': [0.000, 0.000, 0.753, 0.008, 0.000, 0.220, 0.000, 0.389, 0.000, 0.053],
}


corr_results = pd.DataFrame(data)


corr_results['Significant (p<0.05)'] = corr_results['P-Value'].apply(lambda p: 'Yes' if p < 0.05 else 'No')


corr_results.to_csv('correlation_results.csv', index=False)

