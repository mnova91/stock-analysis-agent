from agent import analyze_stock
from logger import log_analysis  # Keep as-is


def run_agent():
    while True:
        ticker = input("\n📝 Enter Stock Ticker (or type 'exit' to quit): ").strip().upper()
        if ticker.lower() == 'exit':
            print("\n👋 Exiting Stock Agent. Have a great day!")
            break

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

            # Log the analysis for future review
            log_analysis(result)

if __name__ == "__main__":
    run_agent()
