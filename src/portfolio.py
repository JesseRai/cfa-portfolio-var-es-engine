"""
Calculate weighted daily portfolio returns.

Input:
data/daily_returns.csv

Output:
data/portfolio_returns.csv
"""

from pathlib import Path

import numpy as np
import pandas as pd


INPUT_PATH = Path("data/daily_returns.csv")
OUTPUT_PATH = Path("data/portfolio_returns.csv")

WEIGHTS = np.array([
    0.25,  # AAPL
    0.25,  # MSFT
    0.20,  # JPM
    0.15,  # GLD
    0.15,  # SPY
])


def load_returns(filepath: Path) -> pd.DataFrame:
    """Load daily asset returns from CSV."""
    return pd.read_csv(
        filepath,
        index_col=0,
        parse_dates=True,
    )


def calculate_portfolio_returns(
    returns: pd.DataFrame,
    weights: np.ndarray,
) -> pd.Series:
    """Calculate weighted portfolio returns."""
    if len(weights) != returns.shape[1]:
        raise ValueError(
            f"Expected {returns.shape[1]} weights, received {len(weights)}."
        )

    if not np.isclose(weights.sum(), 1.0):
        raise ValueError("Portfolio weights must sum to 1.")

    portfolio_returns = returns @ weights
    portfolio_returns.name = "Portfolio Return"
    return portfolio_returns


if __name__ == "__main__":
    daily_returns = load_returns(INPUT_PATH)

    portfolio_returns = calculate_portfolio_returns(
        returns=daily_returns,
        weights=WEIGHTS,
    )

    print(portfolio_returns.head())
    portfolio_returns.to_csv(OUTPUT_PATH)

    print(f"Saved portfolio returns to {OUTPUT_PATH}")
