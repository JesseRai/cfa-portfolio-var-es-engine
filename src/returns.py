"""
Calculate daily percentage returns from close price data.

Input:
data/close_price_data.csv

Output:
data/daily_returns.csv
"""

from pathlib import Path

import pandas as pd


INPUT_PATH = Path("data/close_price_data.csv")
OUTPUT_PATH = Path("data/daily_returns.csv")


def load_price_data(filepath: Path) -> pd.DataFrame:
    """Load close price data from CSV."""
    return pd.read_csv(
        filepath,
        index_col=0,
        parse_dates=True,
    )


def calculate_daily_returns(prices: pd.DataFrame) -> pd.DataFrame:
    """Calculate simple daily percentage returns."""
    returns = prices.pct_change()
    returns = returns.dropna()
    return returns


if __name__ == "__main__":
    prices = load_price_data(INPUT_PATH)
    daily_returns = calculate_daily_returns(prices)

    print(daily_returns.head())
    daily_returns.to_csv(OUTPUT_PATH)

    print(f"Saved daily returns to {OUTPUT_PATH}")
