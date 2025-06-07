
# 🧠 Stock Analysis Agent

A lightweight Python tool for basic stock analysis using live market data. Get fast buy/hold/sell suggestions based on technical and fundamental metrics—all in the terminal.

## 🔍 Features

- Live price fetch using `yfinance`
- Simple moving average calculations
- ROI projections
- Price-to-fair-value assessment
- Markdown log history by date
- CLI loop with logging

## 📁 Project Structure
```markdown
stock-analysis-agent/
├── src/
│   ├── agent.py          # Core logic and recommendation engine
│   ├── calculator.py     # ROI and moving average utilities
│   ├── data\_fetcher.py   # yFinance data interface
│   ├── logger.py         # Markdown log writer
│   └── main.py           # CLI entrypoint
├── logs/                 # Daily analysis logs in Markdown
├── README.md             # Project documentation
├── requirements.txt      # Python dependencies
└── .gitignore            # File exclusions

````

## 🧪 Example

```bash
$ python src/main.py
📝 Enter Stock Ticker: AAPL

📈 Analysis for AAPL:
💲 Current Price: $183.25
📊 20-Day Moving Average: $179.40
📈 Price Assessment: Above average (Potentially Overvalued)
💰 Projected ROI for 5% Increase: 5.0%
💰 Projected ROI for 10% Increase: 10.0%

📚 Fundamentals: {'P/E Ratio': 27.5, 'EPS': 6.4, 'Market Cap': 2.9e+12, 'Forward P/E': 25.2}

✅ Recommendation: Avoid - Potentially Overvalued
````

## ✅ How to Run

1. Clone the repo:

   ```bash
   git clone https://github.com/yourusername/stock-analysis-agent.git
   cd stock-analysis-agent
   ```

2. Create and activate a virtual environment:

   ```bash
   python -m venv venv
   source venv/bin/activate  # or venv\Scripts\activate on Windows
   ```

3. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

4. Run the agent:

   ```bash
   python src/main.py
   ```

## 🧾 Logs

Each analysis is saved in a dated Markdown file under `logs/`.
Example: `logs/2025-06-05-stock-log.md`

## 🔧 Requirements

* Python 3.8+
* [`yfinance`](https://pypi.org/project/yfinance/)

To install:

```bash
pip install yfinance
```

## 💼 Author

**Michael Novakoski**
Connect on [LinkedIn](https://www.linkedin.com/in/michael-novakoski-801168134)
\#Python #Finance #StockAnalysis #Automation #OpenSource
