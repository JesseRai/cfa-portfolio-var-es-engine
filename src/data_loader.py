"""
Download historical close price data for the portfolio assets.

This script uses yfinance to download daily close prices and saves them to:
data/close_price_data.csv
"""

from pathlib import Path

import yfinance as yf


TICKERS = ["AAPL", "MSFT", "JPM", "GLD", "SPY"]
START_DATE = "2021-01-01"
END_DATE = "2026-01-01"
OUTPUT_PATH = Path("data/close_price_data.csv")


def download_close_prices(
    tickers: list[str],
    start_date: str,
    end_date: str,
):
    """Download close price data from Yahoo Finance."""
    prices = yf.download(
        tickers,
        start=start_date,
        end=end_date,
        auto_adjust=False,
        progress=False,
    )

    close_prices = prices["Close"]
    return close_prices


if __name__ == "__main__":
    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)

    close_prices = download_close_prices(
        tickers=TICKERS,
        start_date=START_DATE,
        end_date=END_DATE,
    )

    print(close_prices.head())
    close_prices.to_csv(OUTPUT_PATH)

    print(f"Saved close price data to {OUTPUT_PATH}")
