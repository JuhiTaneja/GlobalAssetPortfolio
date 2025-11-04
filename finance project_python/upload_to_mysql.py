import pandas as pd
from sqlalchemy import create_engine
engine=create_engine('mysql+mysqlconnector://juhi:Gwagon2025@localhost/finance_data')
csv_files=['daily_returns.csv','global_assets.csv',
           'optimal_portfolio.csv','portfolio_optimisation_returns.csv',
           'T_test_result.csv','covariance.csv','correlation_results.csv',
           'correlation_matrix.csv','confidence_interval.csv',
           'clean_global_assets.csv','asset_metrics.csv','anova_result.csv']

for files in csv_files:
    table_name=files.replace('.csv','')
    df=pd.read_csv(files)
    df.to_sql(table_name,con=engine,if_exists='replace',index=False)
    print(f"{table_name} uploaded successfully to sql")