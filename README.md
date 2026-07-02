# CFA Project: Portfolio VaR & Expected Shortfall Engine

## Overview

This is a basic Python risk-management project built as part of a CFA-focused practical project series.

The project calculates the **95% Historical Value at Risk (VaR)** and **95% Historical Expected Shortfall (ES)** of a simple multi-asset portfolio using historical market data.

The aim is to connect CFA-style risk concepts with practical Python implementation.

## Portfolio

The portfolio uses five assets:

| Asset | Description | Weight |
|---|---|---:|
| AAPL | Apple Inc. | 25% |
| MSFT | Microsoft Corp. | 25% |
| JPM | JPMorgan Chase & Co. | 20% |
| GLD | SPDR Gold Shares ETF | 15% |
| SPY | SPDR S&P 500 ETF Trust | 15% |

The assumed portfolio value is:

```text
£100,000
```

## Methodology

The project follows these steps:

1. Download historical close price data using `yfinance`.
2. Calculate daily percentage returns for each asset.
3. Apply portfolio weights to calculate daily portfolio returns.
4. Calculate 95% Historical VaR from the portfolio return distribution.
5. Calculate 95% Historical Expected Shortfall from returns worse than the VaR threshold.
6. Convert the percentage risk measures into pound values.

## Historical Value at Risk

Historical VaR estimates the loss threshold at a chosen confidence level using historical portfolio returns.

For this portfolio, the 95% Historical VaR is:

```text
-1.46%
```

For a £100,000 portfolio, this equals approximately:

```text
£1,460
```

This means that, based on the historical data used, 95% of trading days had losses smaller than approximately 1.46%. Around 5% of trading days had losses worse than this threshold.

VaR is not a maximum possible loss. It only identifies the point where the worst tail of the return distribution begins.

## Historical Expected Shortfall

Expected Shortfall measures the average loss on days where losses are worse than the VaR threshold.

For this portfolio, the 95% Historical Expected Shortfall is:

```text
-2.10%
```

For a £100,000 portfolio, this equals approximately:

```text
£2,100
```

This means that, on the worst 5% of historical trading days, the portfolio lost around 2.10% on average.

Expected Shortfall gives more information about tail risk than VaR because it looks at the severity of losses beyond the VaR threshold.

## Example Output

```text
Portfolio Risk Report
---------------------
Portfolio Value: £100,000

95% Historical VaR: -1.46%
95% Historical VaR £: £1,460.00

95% Historical Expected Shortfall: -2.10%
95% Historical Expected Shortfall £: £2,100.00
```

## Project Structure

```text
.
├── data/
│   ├── close_price_data.csv
│   ├── daily_returns.csv
│   └── portfolio_returns.csv
├── src/
│   ├── data_loader.py
│   ├── returns.py
│   ├── portfolio.py
│   └── risk_metrics.py
├── main.py
├── requirements.txt
├── .gitignore
└── README.md
```

## How to Run

Install the required packages:

```bash
pip install -r requirements.txt
```

Run the full pipeline:

```bash
python main.py
```

Or run each step individually:

```bash
python src/data_loader.py
python src/returns.py
python src/portfolio.py
python src/risk_metrics.py
```

## Skills Demonstrated

- Python
- pandas
- NumPy
- yfinance
- Financial return calculations
- Portfolio weighting
- Historical Value at Risk
- Historical Expected Shortfall
- Basic risk analysis
- Clean project structure for GitHub

## Limitations

This is intentionally a basic first project.

It does not include:

- Parametric VaR
- Monte Carlo simulation
- Stress testing
- Backtesting
- Dynamic portfolio weights
- Transaction costs
- Liquidity risk
- Correlation breakdowns

Those would be suitable extensions for later CFA practical projects.
