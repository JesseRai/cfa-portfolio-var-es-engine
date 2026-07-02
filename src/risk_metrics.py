"""
Calculate 95% Historical Value at Risk and Expected Shortfall.

Input:
data/portfolio_returns.csv
"""

from pathlib import Path

import numpy as np
import pandas as pd


INPUT_PATH = Path("data/portfolio_returns.csv")
PORTFOLIO_VALUE = 100_000
CONFIDENCE_LEVEL = 0.95


def load_portfolio_returns(filepath: Path) -> pd.Series:
    """Load weighted portfolio returns from CSV."""
    returns = pd.read_csv(
        filepath,
        index_col=0,
        parse_dates=True,
    )

    return returns.iloc[:, 0]


def historical_var(
    returns: pd.Series,
    confidence: float = 0.95,
) -> float:
    """Calculate Historical Value at Risk."""
    percentile = (1 - confidence) * 100
    return np.percentile(returns, percentile)


def historical_expected_shortfall(
    returns: pd.Series,
    confidence: float = 0.95,
) -> float:
    """Calculate Historical Expected Shortfall."""
    var = historical_var(returns, confidence)
    tail_losses = returns[returns <= var]
    return tail_losses.mean()


if __name__ == "__main__":
    portfolio_returns = load_portfolio_returns(INPUT_PATH)

    var_95 = historical_var(portfolio_returns, CONFIDENCE_LEVEL)
    es_95 = historical_expected_shortfall(portfolio_returns, CONFIDENCE_LEVEL)

    var_95_money = PORTFOLIO_VALUE * abs(var_95)
    es_95_money = PORTFOLIO_VALUE * abs(es_95)

    print("Portfolio Risk Report")
    print("---------------------")
    print(f"Portfolio Value: £{PORTFOLIO_VALUE:,.0f}")
    print()
    print(f"95% Historical VaR: {var_95:.2%}")
    print(f"95% Historical VaR £: £{var_95_money:,.2f}")
    print()
    print(f"95% Historical Expected Shortfall: {es_95:.2%}")
    print(f"95% Historical Expected Shortfall £: £{es_95_money:,.2f}")
