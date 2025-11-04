# 🌍 Global Asset Performance and Portfolio Optimization (2015–2024)

This project analyzes the **performance and interrelationship** of five major global assets , **Nifty 50, S&P 500, FTSE 100, Gold, and Crude Oil** , over the period **2015–2024**.  
It evaluates their return patterns, linkages, and diversification potential, and designs an **optimal portfolio** that balances risk and return using modern financial and statistical methods.

---

## 🎯 Objective

The main objective is to understand how global assets behave individually and collectively, assess diversification benefits, and construct an efficient portfolio using data-driven insights.  
The project integrates **Python**, **MySQL**, and **Power BI** for a complete analytics workflow ,from data collection to visualization.

---

## 🧩 Tools & Technologies Used

- **Python** → Data analysis and portfolio optimization (`pandas`, `numpy`, `scipy`)  
- **MySQL** → Structured data storage 
- **Power BI** → Interactive visualization and performance dashboard  
- **Project Report** → Included in the repository for detailed analysis, methodology, and results

---

## 🔍 Project Overview

1. **Data Collection & Storage**  
   - Historical daily data (2015–2024) was sourced using the `yfinance` library.  
   - Cleaned and organized datasets were stored in a MySQL database for consistency and accessibility.

2. **Data Analysis in Python**  
   - Cleaned and merged datasets using Pandas.  
   - Conducted correlation, ANOVA, and confidence interval analysis.  
   - Performed mean–variance optimization and calculated Sharpe ratios.  

   💡 *Even though the cleaned data is stored in MySQL, all datasets are also available inside the Python folder.  
   This allows users to directly run and verify the Python code without database setup.*

3. **Visualization with Power BI**  
   - Built an interactive dashboard that includes:  
     - **Portfolio Optimization Pie Chart** — showing the ideal asset allocation.
     - ![Portfolio Optimization](https://github.com/JuhiTaneja/GlobalAssetPortfolio/blob/main/images/portfolio_optimisation.png?raw=true)
        
     - **Cumulative Performance Trend Chart** — highlighting long-term growth of each asset.
     - ![Trend Analysis](https://github.com/JuhiTaneja/GlobalAssetPortfolio/blob/main/images/Trend_Analysis.png?raw=true)

---

## 📊 Key Insights

- **S&P 500** and **Nifty 50** showed the highest risk-adjusted returns, offering consistent long-term performance.  
- **Gold** acted as a safe-haven asset, contributing stability and diversification.  
- **Crude Oil** remained volatile and cyclical, offering limited long-term consistency.  
- The optimized portfolio (Nifty 50, S&P 500, and Gold) achieved a strong balance of growth and stability.

---

## 👩‍💻 Author

**Juhi Taneja**  
 
Interested in Data Analytics, Financial Modelling, and Visualization.  

[www.linkedin.com/in/juhi-taneja]

---

### 🌟 Note

This project demonstrates how combining **growth-oriented equities** with **safe-haven assets** can enhance portfolio efficiency.  
It represents a practical application of data analytics, finance, and visualization for understanding global asset performance.

