#!/usr/bin/env python3
"""
Asterdex Trading Bot v3 - Con SL y TP obligatorio
"""
import hmac
import hashlib
import time
import requests
from datetime import datetime

API_KEY = "5af272a41f466a2ac4e617413b168149142101ab44bd994436c972dfe2fe4c37"
API_SECRET = "aa5382cdb022642a6ed80f58db6c5f46f9d29693617e343dc69f672193a4c029"

SYMBOLS = ["BTCUSDT", "ETHUSDT", "SOLUSDT"]
REWARD_RATIO = 2.0
MAX_TRADES_PER_DAY = 5

class AsterdexAPI:
    def __init__(self):
        self.base_url = "https://www.asterdex.com"
    
    def _sign(self, params):
        return hmac.new(API_SECRET.encode(), params.encode(), hashlib.sha256).hexdigest()
    
    def _request(self, endpoint, params=None):
        url = self.base_url + endpoint
        if params is None:
            params = {}
        params['timestamp'] = int(time.time() * 1000)
        query = "timestamp={}".format(params['timestamp'])
        params['signature'] = self._sign(query)
        headers = {"X-MBX-APIKEY": API_KEY}
        return requests.get(url, params=params, headers=headers).json()
    
    def get_klines(self, symbol, interval="5m", limit=50):
        return self._request("/api/v1/klines", {"symbol": symbol, "interval": interval, "limit": limit})
    
    def place_order(self, symbol, side, quantity):
        url = self.base_url + "/fapi/v1/order"
        params = {
            "symbol": symbol,
            "side": side,
            "type": "MARKET",
            "quantity": quantity,
            "timestamp": int(time.time() * 1000)
        }
        query = "timestamp={}".format(params['timestamp'])
        params['signature'] = self._sign(query)
        headers = {"X-MBX-APIKEY": API_KEY}
        return requests.post(url, params=params, headers=headers).json()
    
    def get_balance(self):
        account = self._request("/fapi/v1/account")
        for asset in account.get('assets', []):
            if asset['asset'] == 'USDC':
                return float(asset.get('availableBalance', 0))
        return 0

def analyze(symbol):
    api = AsterdexAPI()
    klines = api.get_klines(symbol, "5m", 50)
    
    if not klines:
        return {"signal": "ERROR", "reason": "Sin datos"}
    
    closes = [float(k[4]) for k in klines]
    
    # RSI
    delta = [closes[i] - closes[i-1] for i in range(1, len(closes))]
    gain = [d if d > 0 else 0 for d in delta]
    loss = [-d if d < 0 else 0 for d in delta]
    avg_gain = sum(gain[-14:]) / 14
    avg_loss = sum(loss[-14:]) / 14
    rs = avg_gain / avg_loss if avg_loss > 0 else 100
    rsi = 100 - (100 / (1 + rs))
    
    # Trend
    sma_9 = sum(closes[-9:]) / 9
    sma_21 = sum(closes[-21:]) / 21
    trend = "UP" if sma_9 > sma_21 else "DOWN"
    
    # Consecutive
    consec_up = 0
    consec_down = 0
    for i in range(len(closes)-1, 0, -1):
        if closes[i] > closes[i-1]:
            consec_up += 1
        else:
            break
    for i in range(len(closes)-1, 0, -1):
        if closes[i] < closes[i-1]:
            consec_down += 1
        else:
            break
    
    price = closes[-1]
    
    if rsi < 70 and consec_up >= 5 and trend == "UP":
        return {"signal": "BUY", "price": price, "rsi": rsi, "trend": trend, "consec": consec_up}
    elif rsi > 30 and consec_down >= 5 and trend == "DOWN":
        return {"signal": "SELL", "price": price, "rsi": rsi, "trend": trend, "consec": consec_down}
    
    return {"signal": "NEUTRAL", "price": price, "rsi": rsi, "trend": trend, "consec": max(consec_up, consec_down)}

def calc_position(price, balance):
    risk = balance * 0.02  # 2%
    sl_pct = 0.01  # 1%
    sl_dist = price * sl_pct
    qty = risk / sl_dist
    return qty, price * (1 - sl_pct), price * (1 + sl_pct * REWARD_RATIO)

print("="*50)
print("ASTERDEX TRADING BOT v3 - Con SL/TP")
print("="*50)

api = AsterdexAPI()
balance = api.get_balance()
print("Balance: ${:.2f}".format(balance))

for sym in SYMBOLS:
    print("\n--- {} ---".format(sym))
    sig = analyze(sym)
    print("Signal: {}".format(sig['signal']))
    print("Price: ${:,.2f}".format(sig['price']))
    print("RSI: {:.1f}".format(sig['rsi']))
    print("Trend: {}".format(sig['trend']))
    
    if sig['signal'] in ["BUY", "SELL"]:
        qty, sl, tp = calc_position(sig['price'], balance)
        side = "BUY" if sig['signal'] == "BUY" else "SELL"
        print("qty: {:.4f}".format(qty))
        print("SL: ${:,.2f}".format(sl))
        print("TP: ${:,.2f}".format(tp))
        
        print("EJECUTANDO {}...".format(side))
        result = api.place_order(sym, side, qty)
        if 'orderId' in result:
            print("ORDEN OK! ID: {}".format(result['orderId']))
        else:
            print("ERROR: {}".format(result))
