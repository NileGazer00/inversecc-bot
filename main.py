import time
from reddit_scraper import fetch_recent_posts
from sentiment_analyzer import get_sentiment
from binance_trader import place_market_buy
from config import SENTIMENT_THRESHOLD, SYMBOLS

def run_bot():
    print("🚀 InverseCC Bot started. Scanning Reddit for negative sentiment...")
    trades_log = []
    while True:
        posts = fetch_recent_posts()
        for item in posts:
            text = item['text']
            sentiment = get_sentiment(text)
            if sentiment < SENTIMENT_THRESHOLD:
                for sym in item['symbols']:
                    if sym not in trades_log:
                        print(f"🔥 Negative sentiment detected ({sentiment:.2f}) for {sym}")
                        print(f"   Text snippet: {text[:100]}...")
                        place_market_buy(sym)
                        trades_log.append(sym)
                        time.sleep(60)
        time.sleep(30)

if __name__ == "__main__":
    run_bot()
