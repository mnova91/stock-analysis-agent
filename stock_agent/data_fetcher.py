import yfinance as yf

# --- Data Fetching Utilities ---
# Functions to retrieve stock price data and basic fundamentals using yfinance.

def get_current_price(ticker: str) -> float:
    """
    Fetch the most recent closing price for the given ticker.
    Returns 0.0 if data cannot be retrieved.
    """
    try:
        stock = yf.Ticker(ticker)
        price = stock.history(period="1d")['Close'].iloc[-1]
        return round(price, 2)
    except Exception as e:
        print(f"Error fetching current price for {ticker}: {e}")
        return 0.0

def get_historical_prices(ticker: str, period: str = "1mo") -> list:
    """
    Fetch historical closing prices for the given ticker and period.
    Returns a list of closing prices, or an empty list on failure.
    """
    try:
        stock = yf.Ticker(ticker)
        hist = stock.history(period=period)
        return hist['Close'].tolist()
    except Exception as e:
        print(f"Error fetching historical prices for {ticker}: {e}")
        return []

def get_basic_fundamentals(ticker: str) -> dict:
    """
    Fetch basic fundamental data for the given ticker.
    Returns a dictionary with key metrics, or empty dict on failure.
    """
    try:
        stock = yf.Ticker(ticker)
        info = stock.info
        return {
            "P/E Ratio": info.get("trailingPE", "N/A"),
            "EPS": info.get("trailingEps", "N/A"),
            "Market Cap": info.get("marketCap", "N/A"),
            "Forward P/E": info.get("forwardPE", "N/A")
        }
    except Exception as e:
        print(f"Error fetching fundamentals for {ticker}: {e}")
        return {}

if __name__ == "__main__":
    # Example usage and quick test
    ticker = "AAPL"
    print(f"Current Price for {ticker}: ${get_current_price(ticker)}")
    print(f"Historical Prices (1mo): {get_historical_prices(ticker)}")
    print(f"Fundamentals: {get_basic_fundamentals(ticker)}")
