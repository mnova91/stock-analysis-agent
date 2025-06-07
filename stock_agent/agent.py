"""
Stock Analysis Agent
--------------------
A simple Python script to analyze stocks using price data and basic fundamentals.
Provides a buy/hold/sell recommendation based on moving averages and ROI scenarios.

Author: Michael Novakoski
Date: May 2025

#Python #Finance #StockAnalysis #Automation #LinkedIn
"""

from data_fetcher import get_current_price, get_historical_prices, get_basic_fundamentals
from calculator import calculate_simple_moving_average, assess_price_against_average, calculate_roi

def analyze_stock(ticker: str) -> dict:
    """
    Analyze a stock and return a recommendation with context.
    """
    current_price = get_current_price(ticker)
    if current_price == 0.0:
        return {"error": "Failed to fetch current price. Check ticker symbol."}

    historical_prices = get_historical_prices(ticker)
    if not historical_prices:
        return {"error": "Failed to fetch historical prices."}

    fundamentals = get_basic_fundamentals(ticker)

    # Calculate Moving Average & Assessment
    sma_20 = calculate_simple_moving_average(historical_prices)
    price_assessment = assess_price_against_average(current_price, sma_20)

    # Hypothetical ROI Scenarios
    projected_roi_5 = calculate_roi(current_price, current_price * 1.05)
    projected_roi_10 = calculate_roi(current_price, current_price * 1.10)

    # Simple Decision Logic
    if "Below average" in price_assessment:
        recommendation = "Consider Buy"
    elif "Above average" in price_assessment:
        recommendation = "Avoid - Potentially Overvalued"
    else:
        recommendation = "Hold/Watch"

    return {
        "ticker": ticker.upper(),
        "current_price": current_price,
        "moving_average_20": round(sma_20, 2),
        "price_assessment": price_assessment,
        "roi_5_percent_gain": f"{projected_roi_5}%",
        "roi_10_percent_gain": f"{projected_roi_10}%",
        "fundamentals": fundamentals,
        "recommendation": recommendation
    }


if __name__ == "__main__":
    print("🔍 Welcome to the Stock Analysis Agent!")
    print("Enter a stock ticker to receive a quick analysis and recommendation.\n")
    ticker = input("📝 Enter Stock Ticker: ").strip().upper()
    result = analyze_stock(ticker)

    if "error" in result:
        print(f"❌ Error: {result['error']}")
    else:
        print(f"\n📈 Analysis for {result['ticker']}:")
        print(f"💲 Current Price: ${result['current_price']}")
        print(f"📊 20-Day Moving Average: ${result['moving_average_20']}")
        print(f"📈 Price Assessment: {result['price_assessment']}")
        print(f"💰 Projected ROI for 5% Increase: {result['roi_5_percent_gain']}")
        print(f"💰 Projected ROI for 10% Increase: {result['roi_10_percent_gain']}")
        print(f"\n📚 Fundamentals: {result['fundamentals']}")
        print(f"\n✅ Recommendation: {result['recommendation']}")

# Feel free to connect with me on LinkedIn to discuss Python, finance, and automation!
