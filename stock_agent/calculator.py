# --- Stock Analysis Calculations ---
# Utility functions for financial calculations used in the Stock Analysis Agent.

def calculate_roi(buy_price: float, sell_price: float) -> float:
    """
    Calculate Return on Investment (ROI) as a percentage.
    ROI = ((sell_price - buy_price) / buy_price) * 100
    Returns 0.0 if buy_price is zero to avoid division by zero.
    """
    try:
        roi = ((sell_price - buy_price) / buy_price) * 100
        return round(roi, 2)
    except ZeroDivisionError:
        return 0.0

def calculate_simple_moving_average(prices: list, window: int = 20) -> float:
    """
    Calculate Simple Moving Average (SMA) over the given window.
    If there are fewer prices than the window, average all available prices.
    """
    if not prices:
        return 0.0  # Handle empty list gracefully
    if len(prices) < window:
        return sum(prices) / len(prices)
    else:
        return sum(prices[-window:]) / window

def assess_price_against_average(current_price: float, moving_average: float) -> str:
    """
    Provide a simple interpretation of current price relative to the moving average.
    - Above average (>5%): "Above average (Potentially Overvalued)"
    - Below average (<-5%): "Below average (Potential Discount)"
    - Within ±5%: "Near average (Stable)"
    """
    if moving_average == 0:
        return "Insufficient data for assessment"
    if current_price > moving_average * 1.05:
        return "Above average (Potentially Overvalued)"
    elif current_price < moving_average * 0.95:
        return "Below average (Potential Discount)"
    else:
        return "Near average (Stable)"

if __name__ == "__main__":
    # Example usage and quick test
    current_price = 198.53
    historical_prices = [
        190.42, 198.14, 202.52, 202.14, 194.27, 196.97, 193.16, 199.74,
        204.60, 208.37, 209.28, 210.13, 211.21, 212.50, 213.32, 205.35,
        198.88, 198.51, 196.25, 197.49, 198.53
    ]

    sma = calculate_simple_moving_average(historical_prices)
    assessment = assess_price_against_average(current_price, sma)
    projected_roi = calculate_roi(current_price, current_price * 1.10)  # Hypothetical 10% gain

    print(f"\n📊 20-Day Moving Average: ${round(sma, 2)}")
    print(f"📈 Current Price Assessment: {assessment}")
    print(f"💰 Projected ROI for 10% Increase: {projected_roi}%")
