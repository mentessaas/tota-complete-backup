#!/usr/bin/env python3
"""
KuCoin Trading Bot
"""
import requests
import hashlib
import hmac
import time
import json
from datetime import datetime

API_KEY = "878483cd310dafb51a9817e8da1dd4e37de15638661d2b1ff0f18d78d360359a"
API_SECRET = "909acf6898599f35d0c2d6b35e1a8026ca3a26ebfa776afcdce69d1089969401"
BASE_URL = "https://api.kucoin.com"

SYMBOLS = ["XBTUSDM", "ETHUSDM", "SOLUSDM"]
BALANCE = 222
RISK_PER_TRADE = 0.01  # 1%

def kucoin_request(method, endpoint, data=None):
    """Make authenticated request to KuCoin"""
    timestamp = str(int(time.time() * 1000))
    str_to_sign = timestamp + method + endpoint + (json.dumps(data) if data else "")
    signature = hmac.new(API_SECRET.encode(), str_to_sign.encode(), hashlib.sha256).hexdigest()
    
    headers = {
        "KC-API-KEY": API_KEY,
        "KC-API-SIGN": signature,
        "KC-API-TIMESTAMP": timestamp,
        "KC-API-PASSPHRASE": "",
        "Content-Type": "application/json"
    }
    
    url = BASE_URL + endpoint
    if method == "GET":
        resp = requests.get(url, headers=headers, params=data)
    else:
        resp = requests.post(url, headers=headers, json=data)
    
    return resp.json()

def get_balance():
    """Get futures balance"""
    try:
        result = kucoin_request("GET", "/api/v1/account-overview", {"currency": "USDT"})
        return float(result.get("data", {}).get("availableBalance", 0))
    except Exception as e:
        print(f"Error getting balance: {e}")
        return BALANCE

def get_ticker(symbol):
    """Get ticker for symbol"""
    try:
        result = kucoin_request("GET", "/api/v1/market/orderbook/level1", {"symbol": symbol})
        data = result.get("data", {})
        return {
            "price": float(data.get("price", 0)),
            "size": float(data.get("size", 0)),
            "bestBid": float(data.get("bestBid", 0)),
            "bestAsk": float(data.get("bestAsk", 0))
        }
    except Exception as e:
        print(f"Error getting ticker {symbol}: {e}")
        return None

def get_candles(symbol, type="1min", size=20):
    """Get candles for analysis"""
    try:
        result = kucoin_request("GET", "/api/v1/market/candles", {"symbol": symbol, "type": type, "size": size})
        return result.get("data", [])
    except Exception as e:
        print(f"Error getting candles: {e}")
        return []

def analyze_market(symbol):
    """Analyze market and return signal"""
    candles = get_candles(symbol)
    if not candles or len(candles) < 10:
        return "NEUTRAL"
    
    # Simple analysis: check last 5 candles
    closes = [float(c[2]) for c in candles[-5:]]
    opens = [float(c[1]) for c in candles[-5:]]
    
    # Count up/down
    up_count = sum(1 for i in range(1, 5) if closes[i] > closes[i-1])
    down_count = sum(1 for i in range(1, 5) if closes[i] < closes[i-1])
    
    # Ratio signal
    ratio = up_count / 5
    
    # Current price
    current_price = float(candles[0][2])
    
    print(f"{symbol}: Price=${current_price}, Up={up_count}/5, Ratio={ratio:.2f}")
    
    # BUY: Ratio > 0.80 + 5 UP + trend up
    if ratio >= 0.80 and up_count == 5 and current_price > opens[0]:
        return "BUY"
    
    # SELL: Ratio < 0.20 + 5 DOWN + trend down
    if ratio <= 0.20 and down_count == 5 and current_price < opens[0]:
        return "SELL"
    
    return "NEUTRAL"

def place_order(symbol, side, size):
    """Place order"""
    try:
        data = {
            "symbol": symbol,
            "side": side,
            "size": str(size),
            "leverage": "10",
            "orderType": "market"
        }
        result = kucoin_request("POST", "/api/v1/futures/orders", data)
        print(f"Order placed: {side} {size} {symbol}")
        return result
    except Exception as e:
        print(f"Error placing order: {e}")
        return None

def main():
    print(f"=== KuCoin Trading Bot | {datetime.now().strftime('%Y-%m-%d %H:%M:%S')} ===")
    
    balance = get_balance()
    print(f"Balance: ${balance}")
    
    signals = {}
    for symbol in SYMBOLS:
        signal = analyze_market(symbol)
        signals[symbol] = signal
        print(f"  {symbol}: {signal}")
    
    # Execute if strong signal
    for symbol, signal in signals.items():
        if signal in ["BUY", "SELL"]:
            size = int((balance * RISK_PER_TRADE) * 10)  # With 10x leverage
            if size > 1:
                place_order(symbol, signal.lower(), size)
    
    print("=== Cycle Complete ===")

if __name__ == "__main__":
    main()
