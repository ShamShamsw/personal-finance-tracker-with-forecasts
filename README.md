# Beginner Project 25: Personal Finance Tracker With Forecasts

**Time:** 4-6 hours  
**Difficulty:** Intermediate Beginner  
**Focus:** CSV transaction ingestion, category mapping, monthly budget summaries, and linear cashflow forecasting

---

## Why This Project?

Managing personal finances requires more than a spreadsheet. Production-grade finance tools must import raw bank exports, normalize inconsistent transaction descriptions, categorize expenses reliably, produce month-by-month summaries, and project future balances.

This project teaches a professional data pipeline where you can:

- import transactions from CSV files exported by any bank,
- normalize and parse dates and amount fields robustly,
- apply category rules to classify each transaction automatically,
- aggregate spending by category and month,
- compute running balances across the full date range,
- forecast future cashflow using linear regression on historical net values,
- render an interactive forecast chart using Plotly,
- and persist all outputs to disk for later review.

---

## More Projects

You can access this project and more in this separate repository:

[student-interview-prep](https://github.com/ShamShamsw/student-interview-prep.git)

---

## What You Will Build

You will build a command-line finance tracker that:

1. Accepts a CSV file of bank transactions (date, description, amount).
2. Applies a configurable keyword-to-category map to each transaction.
3. Computes monthly income, expense, and net totals.
4. Builds a running balance timeline from a configurable starting balance.
5. Forecasts future monthly balances using linear regression.
6. Renders an interactive HTML forecast chart with Plotly.
7. Prints categorization counts, monthly tables, and a forecast table to the console.
8. Persists processed transactions and a run summary to disk.

---

## Requirements

- Python 3.11+
- `pandas`
- `scikit-learn`
- `plotly`

Install with:

```bash
pip install -r requirements.txt
```

---

## Example Session

```text
======================================================================
   PERSONAL FINANCE TRACKER WITH FORECASTS
======================================================================

Configuration:
   Transaction file:  data/transactions.csv
   Category map:      data/categories.json
   Starting balance:  5000.00
   Months to forecast: 3
   Forecast method:   linear regression

Startup:
   Data directory:    data/
   Outputs directory: data/outputs/
   Previously saved transactions: 0 records

Importing:
   [LOADED]  data/transactions.csv    rows=120  date_range=2024-01-01..2024-12-31

Categorizing:
   Food & Dining        42 transactions
   Housing              12 transactions
   Transportation       18 transactions
   Entertainment         9 transactions
   Salary (Income)      12 transactions
   Other                27 transactions

Monthly Summaries:
   Month         Income     Expenses        Net    Balance
   2024-01      5200.00      3840.20     1359.80    6359.80
   2024-02      5200.00      4102.55     1097.45    7457.25
   2024-03      5200.00      3955.10     1244.90    8702.15
   ...
   2024-12      5200.00      3761.30     1438.70   23481.50

Forecast (3 months ahead, linear regression):
   2025-01    predicted_balance=  24881.50
   2025-02    predicted_balance=  26281.50
   2025-03    predicted_balance=  27681.50

Summary:
   Transactions processed:    120
   Months covered:             12
   Average monthly income:   5200.00
   Average monthly expenses: 3960.91
   Average monthly net:      1239.09

Artifacts saved:
   Transactions:        data/transactions.json
   Run summary:         data/outputs/run_summary.json
   Forecast chart:      data/outputs/forecast.html
```
