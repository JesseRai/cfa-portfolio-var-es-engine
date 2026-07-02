"""
Run the full Portfolio VaR and Expected Shortfall pipeline.

This script runs:
1. Download close prices
2. Calculate daily returns
3. Calculate portfolio returns
4. Calculate Historical VaR and Expected Shortfall
"""

import subprocess
import sys


SCRIPTS = [
    "src/data_loader.py",
    "src/returns.py",
    "src/portfolio.py",
    "src/risk_metrics.py",
]


if __name__ == "__main__":
    for script in SCRIPTS:
        print(f"\nRunning {script}...")
        subprocess.run([sys.executable, script], check=True)
