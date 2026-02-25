#!/usr/bin/env python3
"""
Asterdex API Connector
Compatible with Aster/Binance-style API
"""
import hmac
import hashlib
import time
import requests
from typing import Dict, List, Optional, Any

class AsterdexAPI:
    def __init__(self, api_key: str, api_secret: str, test_mode: bool = True):
        self.api_key = api_key
        self.api_secret = api_secret
        self.base_url = "https://www.asterdex.com/api"
        self.test_mode = test_mode
    
    def _sign(self, params: str) -> str:
        """Generate signature"""
        signature = hmac.new(
            self.api_secret.encode('utf-8'),
            params.encode('utf-8'),
            hashlib.sha256
        ).hexdigest()
        return signature
    
    def _request(self, method: str, endpoint: str, params: Dict = None, signed: bool = False) -> Any:
        """Make API request"""
        url = f"{self.base_url}{endpoint}"
        
        if params is None:
            params = {}
        
        if signed:
            params['timestamp'] = int(time.time() * 1000)
            query_string = f"timestamp={params['timestamp']}"
            params['signature'] = self._sign(query_string)
        
        headers = {"X-MBX-APIKEY": self.api_key}
        
        if method == "GET":
            response = requests.get(url, params=params, headers=headers)
        elif method == "POST":
            response = requests.post(url, params=params, headers=headers)
        else:
            raise ValueError(f"Method {method} not supported")
        
        return response.json()
    
    # === Public Endpoints ===
    def ping(self) -> Dict:
        """Test connection"""
        return self._request("GET", "/v1/ping")
    
    def get_time(self) -> Dict:
        """Get server time"""
        return self._request("GET", "/v1/time")
    
    def get_symbols(self) -> List[Dict]:
        """Get available symbols"""
        return self._request("GET", "/v1/exchangeInfo")
    
    def get_ticker(self, symbol: str) -> Dict:
        """Get ticker price"""
        return self._request("GET", "/v1/ticker/price", {"symbol": symbol})
    
    def get_24h_stats(self, symbol: str) -> Dict:
        """Get 24h statistics"""
        return self._request("GET", "/v1/ticker/24hr", {"symbol": symbol})
    
    def get_orderbook(self, symbol: str, limit: int = 5) -> Dict:
        """Get order book"""
        return self._request("GET", "/v1/depth", {"symbol": symbol, "limit": limit})
    
    def get_klines(self, symbol: str, interval: str = "1m", limit: int = 100) -> List:
        """Get candlestick data"""
        return self._request("GET", "/v1/klines", {
            "symbol": symbol,
            "interval": interval,
            "limit": limit
        })
    
    def get_recent_trades(self, symbol: str, limit: int = 10) -> List:
        """Get recent trades"""
        return self._request("GET", "/v1/trades", {"symbol": symbol, "limit": limit})
    
    # === Private Endpoints ===
    def get_account(self) -> Dict:
        """Get account info"""
        return self._request("GET", "/v1/account", signed=True)
    
    def get_balance(self, asset: str = None) -> List:
        """Get balance"""
        result = self._request("GET", "/v1/balance", signed=True)
        if asset and isinstance(result, list):
            for bal in result:
                if bal.get('asset', '').upper() == asset.upper():
                    return bal
        return result
    
    def place_order(self, symbol: str, side: str, order_type: str, quantity: float, 
                    price: float = None, stop_price: float = None) -> Dict:
        """Place an order"""
        params = {
            "symbol": symbol,
            "side": side.upper(),  # BUY or SELL
            "type": order_type.upper(),  # LIMIT, MARKET, STOP
            "quantity": quantity
        }
        
        if price:
            params["price"] = price
            params["timeInForce"] = "GTC"
        
        if stop_price:
            params["stopPrice"] = stop_price
        
        if self.test_mode:
            params["test"] = True
        
        return self._request("POST", "/v1/order", params, signed=True)
    
    def cancel_order(self, symbol: str, order_id: int) -> Dict:
        """Cancel an order"""
        return self._request("DELETE", "/v1/order", {
            "symbol": symbol,
            "orderId": order_id
        }, signed=True)
    
    def get_open_orders(self, symbol: str = None) -> List:
        """Get open orders"""
        params = {}
        if symbol:
            params["symbol"] = symbol
        return self._request("GET", "/v1/openOrders", params, signed=True)
    
    def get_order(self, symbol: str, order_id: int) -> Dict:
        """Get order details"""
        return self._request("GET", "/v1/order", {
            "symbol": symbol,
            "orderId": order_id
        }, signed=True)

# === Trading Bot ===
class TradingBot:
    def __init__(self, api: AsterdexAPI):
        self.api = api
        self.positions = {}
        self.balance = 0
    
    def get_market_price(self, symbol: str) -> float:
        """Get current price"""
        ticker = self.api.get_ticker(symbol)
        return float(ticker['price'])
    
    def get_orderbook(self, symbol: str) -> Dict:
        """Get order book"""
        return self.api.get_orderbook(symbol)
    
    def analyze_signal(self, symbol: str = "BTCUSDT") -> Dict:
        """Analyze market for trading signal"""
        # Get klines
        klines = self.api.get_klines(symbol, "5m", 50)
        
        if not klines:
            return {"signal": "ERROR", "reason": "No data"}
        
        # Parse data
        closes = [float(k[4]) for k in klines]
        highs = [float(k[2]) for k in klines]
        lows = [float(k[3]) for k in klines]
        volumes = [float(k[5]) for k in klines]
        
        # Calculate indicators
        # RSI (14 periods)
        delta = [closes[i] - closes[i-1] for i in range(1, len(closes))]
        gain = [d if d > 0 else 0 for d in delta]
        loss = [-d if d < 0 else 0 for d in delta]
        avg_gain = sum(gain[-14:]) / 14
        avg_loss = sum(loss[-14:]) / 14
        rs = avg_gain / avg_loss if avg_loss > 0 else 100
        rsi = 100 - (100 / (1 + rs))
        
        # Moving averages
        sma_9 = sum(closes[-9:]) / 9
        sma_21 = sum(closes[-21:]) / 21
        
        # Trend
        trend = "UP" if sma_9 > sma_21 else "DOWN"
        
        # Consecutive candles
        consecutive_up = 0
        consecutive_down = 0
        for i in range(len(closes)-1, 0, -1):
            if closes[i] > closes[i-1]:
                consecutive_up += 1
            else:
                break
        
        for i in range(len(closes)-1, 0, -1):
            if closes[i] < closes[i-1]:
                consecutive_down += 1
            else:
                break
        
        # Signal logic
        current_price = closes[-1]
        
        signal = "NEUTRAL"
        reason = ""
        
        # Strong BUY: RSI < 70 + 5+ up + trend UP
        if rsi < 70 and consecutive_up >= 5 and trend == "UP":
            signal = "STRONG_BUY"
            reason = f"RSI={rsi:.1f}, {consecutive_up} up, trend UP"
        
        # Strong SELL: RSI > 30 + 5+ down + trend DOWN
        elif rsi > 30 and consecutive_down >= 5 and trend == "DOWN":
            signal = "STRONG_SELL"
            reason = f"RSI={rsi:.1f}, {consecutive_down} down, trend DOWN"
        
        return {
            "signal": signal,
            "reason": reason,
            "price": current_price,
            "rsi": rsi,
            "trend": trend,
            "consecutive_up": consecutive_up,
            "consecutive_down": consecutive_down,
            "sma_9": sma_9,
            "sma_21": sma_21
        }
    
    def execute_trade(self, symbol: str, side: str, quantity: float) -> Dict:
        """Execute a trade"""
        try:
            # Get current price
            price = self.get_market_price(symbol)
            
            # Place market order
            result = self.api.place_order(
                symbol=symbol,
                side=side,
                order_type="MARKET",
                quantity=quantity
            )
            
            return {
                "success": True,
                "side": side,
                "quantity": quantity,
                "price": price,
                "result": result
            }
        except Exception as e:
            return {
                "success": False,
                "error": str(e)
            }

# === Main ===
if __name__ == "__main__":
    # Credentials
    API_KEY = "5af272a41f466a2ac4e617413b168149142101ab44bd994436c972dfe2fe4c37"
    API_SECRET = "aa5382cdb022642a6ed80f58db6c5f46f9d29693617e343dc69f672193a4c029"
    
    # Initialize
    api = AsterdexAPI(API_KEY, API_SECRET, test_mode=True)
    bot = TradingBot(api)
    
    print("=" * 50)
    print("🏦 ASTERDEX TRADING BOT")
    print("=" * 50)
    
    # Test connection
    print("\n📡 Connection:", api.ping())
    
    # Get BTC price
    btc_price = bot.get_market_price("BTCUSDT")
    print(f"💰 BTC Price: ${btc_price:,.2f}")
    
    # Analyze signal
    print("\n📊 Analyzing BTCUSDT...")
    signal = bot.analyze_signal("BTCUSDT")
    print(f"   Signal: {signal['signal']}")
    print(f"   Reason: {signal.get('reason', 'N/A')}")
    print(f"   Price: ${signal.get('price', 0):,.2f}")
    print(f"   RSI: {signal.get('rsi', 0):.1f}")
    print(f"   Trend: {signal.get('trend', 'N/A')}")
    
    # Get account
    print("\n👤 Account:", api.get_account())
