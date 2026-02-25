#!/usr/bin/env python3
"""
Asterdex Paper Trading Bot v2.0
Con features avanzadas: SL/TP, 24h stats, mejores métricas
"""
import requests
import json
import time
from datetime import datetime

# Config
API_KEY = 'a8ecc704510a74ee336e5dcfa9b50edd6dfd14daedf279efffcaac311c2bceaa'
API_SECRET = '06f53fb3934bfea482e7d9d9f0a6843f42e1bb78e8c6149d01965d8e8d6f97fe'
BASE_URL = 'https://www.asterdex.com/api/v1'
PAPER_STATE_FILE = '/Users/elvisvaldesinerarte/zaltyko-os/scripts/asterdex_paper_state.json'
PAPER_BALANCE = 10000

class PaperTradingBot:
    def __init__(self):
        self.balance = PAPER_BALANCE
        self.positions = {}
        self.orders = {}
        self.load_state()
    
    def load_state(self):
        try:
            with open(PAPER_STATE_FILE, 'r') as f:
                state = json.load(f)
                self.balance = state.get('balance', PAPER_BALANCE)
                self.positions = state.get('positions', {})
                self.orders = state.get('orders', {})
        except:
            pass
    
    def save_state(self):
        with open(PAPER_STATE_FILE, 'w') as f:
            json.dump({
                'balance': self.balance,
                'positions': self.positions,
                'orders': self.orders,
                'updated': datetime.now().isoformat()
            }, f, indent=2)
    
    # ========== PRECIOS ==========
    def get_price(self, symbol):
        r = requests.get(f"{BASE_URL}/ticker/price", params={'symbol': symbol})
        if r.status_code == 200:
            return float(r.json()['price'])
        return None
    
    def get_24h_stats(self, symbol):
        r = requests.get(f"{BASE_URL}/ticker/24hr", params={'symbol': symbol})
        if r.status_code == 200:
            data = r.json()
            return {
                'last': float(data.get('lastPrice', 0)),
                'change': float(data.get('priceChange', 0)),
                'changePct': float(data.get('priceChangePercent', 0)),
                'high': float(data.get('highPrice', 0)),
                'low': float(data.get('lowPrice', 0)),
                'volume': float(data.get('volume', 0)),
                'quoteVolume': float(data.get('quoteVolume', 0))
            }
        return None
    
    def get_all_prices(self):
        r = requests.get(f"{BASE_URL}/ticker/price")
        if r.status_code == 200:
            prices = {}
            for item in r.json():
                prices[item['symbol']] = float(item['price'])
            return prices
        return {}
    
    # ========== TRADING ==========
    def buy(self, symbol, amount, price=None, sl=None, tp=None):
        if price is None:
            price = self.get_price(symbol)
        
        cost = amount * price
        
        if cost > self.balance:
            return {"error": "Insufficient balance", "required": cost, "available": self.balance}
        
        self.balance -= cost
        
        # Calcular avg price si ya hay posición
        if symbol in self.positions:
            old = self.positions[symbol]
            total_amt = old['amount'] + amount
            avg_price = ((old['amount'] * old['avg_price']) + (amount * price)) / total_amt
            self.positions[symbol] = {
                'side': 'LONG',
                'amount': total_amt,
                'avg_price': avg_price,
                'entry_price': price,
                'sl': sl,
                'tp': tp
            }
        else:
            self.positions[symbol] = {
                'side': 'LONG',
                'amount': amount,
                'avg_price': price,
                'entry_price': price,
                'sl': sl,
                'tp': tp
            }
        
        self.save_state()
        
        return {
            "status": "filled",
            "side": "BUY",
            "symbol": symbol,
            "amount": amount,
            "price": price,
            "cost": cost,
            "sl": sl,
            "tp": tp,
            "balance": self.balance
        }
    
    def sell(self, symbol, amount, price=None, sl=None, tp=None):
        if price is None:
            price = self.get_price(symbol)
        
        if symbol not in self.positions:
            # Abrir SHORT
            proceeds = amount * price
            self.balance += proceeds
            self.positions[symbol] = {
                'side': 'SHORT',
                'amount': amount,
                'avg_price': price,
                'entry_price': price,
                'sl': sl,
                'tp': tp
            }
            self.save_state()
            return {
                "status": "filled",
                "side": "SELL (OPEN SHORT)",
                "symbol": symbol,
                "amount": amount,
                "price": price,
                "balance": self.balance
            }
        else:
            # Cerrar posición LONG
            self.balance += amount * price
            
            pnl = (price - self.positions[symbol]['avg_price']) * amount
            
            self.positions[symbol]['amount'] -= amount
            if self.positions[symbol]['amount'] <= 0:
                del self.positions[symbol]
            
            self.save_state()
            
            return {
                "status": "filled",
                "side": "SELL (CLOSE LONG)",
                "symbol": symbol,
                "amount": amount,
                "price": price,
                "proceeds": amount * price,
                "pnl": pnl,
                "balance": self.balance
            }
    
    def close_position(self, symbol):
        if symbol not in self.positions:
            return {"error": "No position"}
        
        pos = self.positions[symbol]
        price = self.get_price(symbol)
        
        if pos['side'] == 'LONG':
            return self.sell(symbol, pos['amount'], price)
        else:
            return self.buy(symbol, pos['amount'], price)
    
    # ========== STATUS ==========
    def get_status(self):
        prices = self.get_all_prices()
        
        status = {
            "balance": round(self.balance, 2),
            "positions": {},
            "orders": self.orders,
            "prices": {}
        }
        
        total_pnl = 0
        total_value = self.balance
        
        for symbol, pos in self.positions.items():
            current_price = prices.get(symbol, pos['avg_price'])
            
            if pos['side'] == 'LONG':
                pnl = (current_price - pos['avg_price']) * pos['amount']
            else:
                pnl = (pos['avg_price'] - current_price) * pos['amount']
            
            total_pnl += pnl
            pos_value = pos['amount'] * current_price
            total_value += pos_value
            
            # Calcular % change
            pnl_pct = (pnl / (pos['avg_price'] * pos['amount'])) * 100 if pos['avg_price'] > 0 else 0
            
            status["positions"][symbol] = {
                "side": pos['side'],
                "amount": pos['amount'],
                "avg_price": round(pos['avg_price'], 4),
                "current_price": round(current_price, 4),
                "value": round(pos_value, 2),
                "pnl": round(pnl, 2),
                "pnl_pct": round(pnl_pct, 2),
                "sl": pos.get('sl'),
                "tp": pos.get('tp')
            }
        
        status["total_pnl"] = round(total_pnl, 2)
        status["total_value"] = round(total_value, 2)
        
        # Top prices
        for sym in ['BTCUSDT', 'ETHUSDT', 'SOLUSDT', 'BNBUSDT', 'XRPUSDT']:
            if sym in prices:
                stats = self.get_24h_stats(sym)
                if stats:
                    status["prices"][sym] = {
                        "price": round(stats['last'], 2),
                        "changePct": round(stats['changePct'], 2),
                        "volume": round(stats['volume'], 0)
                    }
        
        return status
    
    def get_market_analysis(self):
        """Análisis del mercado"""
        prices = self.get_all_prices()
        analysis = {}
        
        # Assets principales
        for symbol in ['BTCUSDT', 'ETHUSDT', 'SOLUSDT']:
            stats = self.get_24h_stats(symbol)
            if stats:
                analysis[symbol] = {
                    "price": stats['last'],
                    "change_24h": stats['changePct'],
                    "high_24h": stats['high'],
                    "low_24h": stats['low'],
                    "volume_24h": stats['volume'],
                    "volatility": round(((stats['high'] - stats['low']) / stats['last']) * 100, 2)
                }
        
        return analysis
    
    def check_sl_tp(self):
        """Check SL/TP para todas las posiciones"""
        triggered = []
        prices = self.get_all_prices()
        
        for symbol, pos in list(self.positions.items()):
            current_price = prices.get(symbol)
            if not current_price:
                continue
            
            # Check SL
            if pos.get('sl'):
                if pos['side'] == 'LONG' and current_price <= pos['sl']:
                    triggered.append({'type': 'SL', 'symbol': symbol, 'price': current_price})
                elif pos['side'] == 'SHORT' and current_price >= pos['sl']:
                    triggered.append({'type': 'SL', 'symbol': symbol, 'price': current_price})
            
            # Check TP
            if pos.get('tp'):
                if pos['side'] == 'LONG' and current_price >= pos['tp']:
                    triggered.append({'type': 'TP', 'symbol': symbol, 'price': current_price})
                elif pos['side'] == 'SHORT' and current_price <= pos['tp']:
                    triggered.append({'type': 'TP', 'symbol': symbol, 'price': current_price})
        
        return triggered
    
    def reset(self):
        self.balance = PAPER_BALANCE
        self.positions = {}
        self.orders = {}
        self.save_state()

# CLI
def main():
    import sys
    
    bot = PaperTradingBot()
    
    if len(sys.argv) < 2:
        print("📊 ASTERDEX PAPER TRADING v2.0")
        print("=" * 50)
        status = bot.get_status()
        print(f"💰 Balance: ${status['balance']}")
        print(f"📈 PnL Total: ${status['total_pnl']}")
        print(f"💵 Valor Total: ${status['total_value']}")
        
        if status['positions']:
            print("\n📌 POSICIONES:")
            for sym, pos in status['positions'].items():
                emoji = "🟢" if pos['pnl'] >= 0 else "🔴"
                print(f"   {emoji} {sym}: {pos['side']} {pos['amount']} @ ${pos['avg_price']} (PnL: ${pos['pnl']} / {pos['pnl_pct']}%)")
                if pos['sl']: print(f"       SL: ${pos['sl']}")
                if pos['tp']: print(f"       TP: ${pos['tp']}")
        
        if status['prices']:
            print("\n💵 PRECIOS:")
            for sym, data in status['prices'].items():
                emoji = "🟢" if data['changePct'] >= 0 else "🔴"
                print(f"   {emoji} {sym}: ${data['price']} ({data['changePct']}%)")
        
        return
    
    cmd = sys.argv[1]
    
    if cmd == 'status':
        status = bot.get_status()
        print(json.dumps(status, indent=2))
    
    elif cmd == 'buy' and len(sys.argv) >= 3:
        symbol = sys.argv[2].upper()
        amount = float(sys.argv[3]) if len(sys.argv) > 3 else 0.01
        sl = float(sys.argv[4]) if len(sys.argv) > 4 and sys.argv[4] != 'none' else None
        tp = float(sys.argv[5]) if len(sys.argv) > 5 and sys.argv[5] != 'none' else None
        result = bot.buy(symbol, amount, None, sl, tp)
        print(json.dumps(result, indent=2))
    
    elif cmd == 'sell' and len(sys.argv) >= 3:
        symbol = sys.argv[2].upper()
        amount = float(sys.argv[3]) if len(sys.argv) > 3 else None
        result = bot.sell(symbol, amount or 0.01)
        print(json.dumps(result, indent=2))
    
    elif cmd == 'close' and len(sys.argv) >= 3:
        symbol = sys.argv[2].upper()
        result = bot.close_position(symbol)
        print(json.dumps(result, indent=2))
    
    elif cmd == 'market' and len(sys.argv) >= 3:
        symbol = sys.argv[2].upper()
        analysis = bot.get_market_analysis()
        print(json.dumps(analysis, indent=2))
    
    elif cmd == 'check':
        triggered = bot.check_sl_tp()
        if triggered:
            print("⚠️ SL/TP triggered:")
            print(json.dumps(triggered, indent=2))
        else:
            print("✅ No SL/TP triggered")
    
    elif cmd == 'reset':
        bot.reset()
        print("✅ Balance reseteado a $10,000")
    
    else:
        print("Comandos:")
        print("  python3 asterdex_paper.py status")
        print("  python3 asterdex_paper.py buy BTCUSDT 0.01 65000 70000")
        print("  python3 asterdex_paper.py sell BTCUSDT 0.01")
        print("  python3 asterdex_paper.py close BTCUSDT")
        print("  python3 asterdex_paper.py market")
        print("  python3 asterdex_paper.py check")
        print("  python3 asterdex_paper.py reset")

if __name__ == "__main__":
    main()
