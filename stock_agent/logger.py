import datetime
from pathlib import Path

# --- Logging Utility ---
# This module provides a function to log stock analysis results to a Markdown file.

# Create a logs directory if it doesn’t exist
LOG_DIR = Path("logs")
LOG_DIR.mkdir(exist_ok=True)

def log_analysis(result: dict):
    """
    Log the stock analysis to a markdown file for easy review.
    Each log entry is timestamped and includes all key analysis metrics.
    """
    today = datetime.date.today().isoformat()
    log_file = LOG_DIR / f"{today}-stock-log.md"

    # Open the log file in append mode and write the analysis in Markdown format
    with open(log_file, "a", encoding="utf-8") as f:
        f.write(f"\n## 📈 Stock Analysis – {datetime.datetime.now().isoformat()}\n")
        f.write(f"**Ticker:** {result['ticker']}\n")
        f.write(f"**Current Price:** ${result['current_price']}\n")
        f.write(f"**20-Day Moving Average:** ${result['moving_average_20']}\n")
        f.write(f"**Price Assessment:** {result['price_assessment']}\n")
        f.write(f"**Projected ROI (5% Gain):** {result['roi_5_percent_gain']}\n")
        f.write(f"**Projected ROI (10% Gain):** {result['roi_10_percent_gain']}\n")
        f.write(f"**Fundamentals:** {result['fundamentals']}\n")
        f.write(f"**Recommendation:** {result['recommendation']}\n")
        f.write("---\n")

    print(f"\n📁 Analysis logged to: {log_file}")
