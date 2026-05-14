from binance.client import Client
from binance.enums import *
from config import BINANCE_API_KEY, BINANCE_API_SECRET, USE_TESTNET, ORDER_AMOUNT_USDT

if USE_TESTNET:
    client = Client(BINANCE_API_KEY, BINANCE_API_SECRET, testnet=True)
else:
    client = Client(BINANCE_API_KEY, BINANCE_API_SECRET)

def place_market_buy(symbol):
    try:
        info = client.get_symbol_info(symbol)
        step_size = float([f['stepSize'] for f in info['filters'] if f['filterType'] == 'LOT_SIZE'][0])
        quantity = ORDER_AMOUNT_USDT / float(client.get_symbol_ticker(symbol=symbol)['price'])
        quantity = round(quantity - (quantity % step_size), 8)
        order = client.order_market_buy(symbol=symbol, quantity=quantity)
        print(f"✅ Bought {quantity} {symbol} for ${ORDER_AMOUNT_USDT}")
        return order
    except Exception as e:
        print(f"❌ Binance error: {e}")
        return None
