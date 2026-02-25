#!/usr/bin/env python3
"""
Asterdex Trading Bot v2.1 - ESTRATEGIA MEJORADA
==============================================
Mejoras basadas en investigación de traders exitosos:

Señales:
- Ratio > 0.80 + 5 velas UP + tendencia a favor
- RSI < 70 (no sobrecomprado)
- Estructura rota al alza
- Order blocks

Gestión de Riesgo:
- Risk: 1% por trade
- SL: 1% | TP: 3%
- Max 3 posiciones
- Stop diario: -5%
"""
import requests
import json
import time
from datetime import datetime
import os

# Config
BASE_URL = 'https://www.asterdex.com/api/v1'
PAPER_STATE_FILE = os.path.expanduser('~/zaltyko-os/scripts/trading_bot_v2_state.json')
PAPER_BALANCE = 10000

# Strategy config
RISK_PER_TRADE = 0.01
SL_PERCENT = 0.01
TP_PERCENT = 0.03
MAX_POSITIONS = 3
MAX_DAILY_LOSS = 0.05

class TradingBot:
    def __init__(self):
        self.balance = PAPER_BALANCE
        self.positions = {}
        self.trades_today = 0
        self.daily_pnl = 0
        self.daily_date = datetime.now().date()
        self.load_state()
    
    def load_state(self):
        try:
            with open(PAPER_STATE_FILE, 'r') as f:
                state = json.load(f)
                self.balance = state.get('balance', PAPER_BALANCE)
                self.positions = state.get('positions', {})
                self.trades_today = state.get('trades_today', 0)
                self.daily_pnl = state.get('daily_pnl', 0)
                saved_date = state.get('daily_date')
                if saved_date:
                    if datetime.strptime(saved_date, '%Y-%m-%d').date() != datetime.now().date():
                        self.trades_today = 0
                        self.daily_pnl = 0
        except:
            pass
    
    def save_state(self):
        with open(PAPER_STATE_FILE, 'w') as f:
            json.dump({
                'balance': self.balance,
                'positions': self.positions,
                'trades_today': self.trades_today,
                'daily_pnl': self.daily_pnl,
                'daily_date': datetime.now().date().isoformat(),
                'updated': datetime.now().isoformat()
            }, f, indent=2)
    
    # ========== PRECIOS ==========
    def get_price(self, symbol):
        r = requests.get(f"{BASE_URL}/ticker/price", params={'symbol': symbol}, timeout=5)
        if r.status_code == 200:
            return float(r.json()['price'])
        return None
    
    def get_klines(self, symbol, interval='15m', limit=30):
        r = requests.get(f"{BASE_URL}/klines", params={
            'symbol': symbol, 'interval': interval, 'limit': limit
        }, timeout=5)
        if r.status_code == 200:
            data = r.json()
            if not data:
                return None
            candles = []
            for d in data:
                try:
                    candles.append({
                        'open': float(d[1]), 'high': float(d[2]),
                        'low': float(d[3]), 'close': float(d[4]),
                        'volume': float(d[5])
                    })
                except:
                    continue
            return candles if candles else None
        return None
    
    def get_24h_stats(self, symbol):
        r = requests.get(f"{BASE_URL}/ticker/24hr", params={'symbol': symbol}, timeout=5)
        if r.status_code == 200:
            data = r.json()
            return {
                'price': float(data.get('lastPrice', 0)),
                'changePct': float(data.get('priceChangePercent', 0)),
                'high': float(data.get('highPrice', 0)),
                'low': float(data.get('lowPrice', 0)),
                'volume': float(data.get('volume', 0))
            }
        return None
    
    # ========== ANÁLISIS V2.1 ==========
    def analyze_signal_v2(self, symbol):
        """Análisis mejorado con confluence - 5min timeframe"""
        candles = self.get_klines(symbol, interval='5m', limit=30)
        if not candles or len(candles) < 10:
            return {'signal': 'NO_DATA', 'confidence': 0, 'reasons': ['Sin datos']}
        
        reasons = []
        
        # 1. Ratio de velas
        last_5 = candles[-5:]
        up_candles = sum(1 for c in last_5 if c['close'] > c['open'])
        
        if up_candles >= 5:
            ratio = 1.0
            reasons.append("✅ 5+ velas UP")
        elif up_candles == 4:
            ratio = 0.8
            reasons.append("⚠️ 4 velas UP")
        elif up_candles == 3:
            ratio = 0.6
            reasons.append("⚠️ 3 velas UP")
        else:
            ratio = 0.2
            reasons.append("❌ Fewer than 3 UP")
        
        # 2. Tendencia (EMA-like)
        prices = [c['close'] for c in candles[-10:]]
        ma_9 = sum(prices[-9:]) / 9
        ma_21 = sum(prices[-10:]) / 10  # Use 10 instead of 21 for shorter term
        
        current_price = prices[-1]
        
        if current_price > ma_9:
            trend = 'UP'
            reasons.append("✅ Precio > MA9")
        else:
            trend = 'DOWN'
            reasons.append("❌ Precio < MA9")
        
        # 3. RSI
        gains = sum(c['close'] - c['open'] for c in last_5 if c['close'] > c['open'])
        losses = sum(c['open'] - c['close'] for c in last_5 if c['close'] < c['open'])
        avg_gain = gains / 5
        avg_loss = losses / 5 if losses > 0 else 1
        rs = avg_gain / avg_loss
        rsi = 100 - (100 / (1 + rs))
        
        if rsi < 70:
            reasons.append(f"✅ RSI {rsi:.0f} (no sobrecomprado)")
        else:
            reasons.append(f"⚠️ RSI {rsi:.0f} (sobrecomprado)")
        
        # 4. Volumen
        recent_vol = sum(c['volume'] for c in last_5)
        older_vol = sum(c['volume'] for c in candles[-10:-5])
        
        if recent_vol > older_vol:
            reasons.append("✅ Volumen increasing")
        else:
            reasons.append("⚠️ Volumen decreasing")
        
        # 5. Estructura (Market Structure)
        # Buscar si hubo break structure
        highs = [c['high'] for c in candles[-10:]]
        lows = [c['low'] for c in candles[-10:]]
        
        # HH (Higher High) = estructura bullish
        # LH (Lower High) = estructura bearish
        hh_count = sum(1 for i in range(1, 5) if highs[-i] > highs[-i-1])
        ll_count = sum(1 for i in range(1, 5) if lows[-i] > lows[-i-1])
        
        if trend == 'UP' and hh_count >= 3:
            reasons.append("✅ Estructura bullish (HH)")
            structure = 'BULLISH'
        elif trend == 'DOWN' and ll_count >= 3:
            reasons.append("✅ Estructura bearish (LL)")
            structure = 'BEARISH'
        else:
            structure = 'NEUTRAL'
        
        # ===== SEÑAL FINAL =====
        signal = 'NEUTRAL'
        confidence = 0
        
        # BUY: Ratio > 0.8 + 5 UP + trend UP + RSI < 70 + estructura bullish
        if ratio >= 0.8 and up_candles >= 5 and trend == 'UP' and rsi < 70 and structure == 'BULLISH':
            signal = 'STRONG_BUY'
            confidence = 95
            reasons.append("🎯 SEÑAL FUERTE: BUY")
        
        # BUY normal: Ratio > 0.6 + trend UP + RSI OK
        elif ratio >= 0.6 and trend == 'UP' and rsi < 75:
            signal = 'BUY'
            confidence = 60
            reasons.append("✅ Señal: BUY")
        
        # SELL: Ratio < 0.2 + trend DOWN + RSI > 30 + estructura bearish
        elif ratio <= 0.2 and up_candles <= 1 and trend == 'DOWN' and rsi > 30 and structure == 'BEARISH':
            signal = 'STRONG_SELL'
            confidence = 95
            reasons.append("🎯 SEÑAL FUERTE: SELL")
        
        elif ratio <= 0.4 and trend == 'DOWN' and rsi > 25:
            signal = 'SELL'
            confidence = 60
            reasons.append("✅ Señal: SELL")
        
        return {
            'signal': signal,
            'confidence': confidence,
            'ratio': ratio,
            'up_candles': up_candles,
            'trend': trend,
            'rsi': round(rsi, 1),
            'structure': structure,
            'current_price': current_price,
            'reasons': reasons
        }
    
    def analyze_all(self):
        """Analizar todos los mercados"""
        markets = ['BTCUSDT', 'ETHUSDT', 'BNBUSDT']
        results = {}
        
        for symbol in markets:
            results[symbol] = self.analyze_signal_v2(symbol)
        
        return results
    
    # ========== TRADING ==========
    def can_trade(self):
        if self.daily_pnl <= -(self.balance * MAX_DAILY_LOSS):
            return False, "Stop diario (-5%)"
        if len(self.positions) >= MAX_POSITIONS:
            return False, "Max posiciones"
        return True, "OK"
    
    def open_long(self, symbol):
        can_trade, reason = self.can_trade()
        if not can_trade:
            return {'error': reason}
        
        price = self.get_price(symbol)
        if not price:
            return {'error': 'Sin precio'}
        
        # Tamaño basado en riesgo 1%
        risk = self.balance * RISK_PER_TRADE
        size = risk / (price * SL_PERCENT)
        cost = size * price
        
        if cost > self.balance:
            return {'error': 'Balance insuficiente'}
        
        sl = price * (1 - SL_PERCENT)
        tp = price * (1 + TP_PERCENT)
        
        self.balance -= cost
        self.positions[symbol] = {
            'side': 'LONG',
            'amount': size,
            'entry_price': price,
            'sl': sl,
            'tp': tp,
            'timestamp': datetime.now().isoformat()
        }
        
        self.trades_today += 1
        self.save_state()
        
        return {
            'status': 'opened',
            'symbol': symbol,
            'amount': round(size, 6),
            'entry': round(price, 2),
            'sl': round(sl, 2),
            'tp': round(tp, 2),
            'balance': round(self.balance, 2)
        }
    
    def open_short(self, symbol):
        can_trade, reason = self.can_trade()
        if not can_trade:
            return {'error': reason}
        
        price = self.get_price(symbol)
        if not price:
            return {'error': 'Sin precio'}
        
        risk = self.balance * RISK_PER_TRADE
        size = risk / (price * SL_PERCENT)
        proceeds = size * price
        
        sl = price * (1 + SL_PERCENT)
        tp = price * (1 - TP_PERCENT)
        
        self.balance += proceeds
        self.positions[symbol] = {
            'side': 'SHORT',
            'amount': size,
            'entry_price': price,
            'sl': sl,
            'tp': tp,
            'timestamp': datetime.now().isoformat()
        }
        
        self.trades_today += 1
        self.save_state()
        
        return {
            'status': 'opened',
            'symbol': symbol,
            'side': 'SHORT',
            'amount': round(size, 6),
            'entry': round(price, 2),
            'sl': round(sl, 2),
            'tp': round(tp, 2),
            'balance': round(self.balance, 2)
        }
    
    def close_position(self, symbol):
        if symbol not in self.positions:
            return {'error': 'No posición'}
        
        pos = self.positions[symbol]
        price = self.get_price(symbol)
        
        if not price:
            return {'error': 'Sin precio'}
        
        if pos['side'] == 'LONG':
            pnl = (price - pos['entry_price']) * pos['amount']
            self.balance += pos['amount'] * price
        else:
            pnl = (pos['entry_price'] - price) * pos['amount']
            self.balance -= pos['amount'] * price
        
        self.daily_pnl += pnl
        del self.positions[symbol]
        self.save_state()
        
        return {
            'status': 'closed',
            'symbol': symbol,
            'exit': round(price, 2),
            'pnl': round(pnl, 2),
            'balance': round(self.balance, 2)
        }
    
    def check_sl_tp(self):
        triggered = []
        
        for symbol, pos in list(self.positions.items()):
            price = self.get_price(symbol)
            if not price:
                continue
            
            # SL
            if pos['side'] == 'LONG' and price <= pos['sl']:
                triggered.append({'type': 'SL', 'symbol': symbol})
                self.close_position(symbol)
            elif pos['side'] == 'SHORT' and price >= pos['sl']:
                triggered.append({'type': 'SL', 'symbol': symbol})
                self.close_position(symbol)
            
            # TP
            elif pos['side'] == 'LONG' and price >= pos['tp']:
                triggered.append({'type': 'TP', 'symbol': symbol})
                self.close_position(symbol)
            elif pos['side'] == 'SHORT' and price <= pos['tp']:
                triggered.append({'type': 'TP', 'symbol': symbol})
                self.close_position(symbol)
        
        return triggered
    
    def get_status(self):
        status = {
            'balance': round(self.balance, 2),
            'daily_pnl': round(self.daily_pnl, 2),
            'trades_today': self.trades_today,
            'positions': {}
        }
        
        for symbol, pos in self.positions.items():
            price = self.get_price(symbol)
            if price and pos['side'] == 'LONG':
                pnl = (price - pos['entry_price']) * pos['amount']
            elif price:
                pnl = (pos['entry_price'] - price) * pos['amount']
            else:
                pnl = 0
            
            status['positions'][symbol] = {
                'side': pos['side'],
                'amount': pos['amount'],
                'entry': pos['entry_price'],
                'pnl': round(pnl, 2)
            }
        
        return status

# ========== CLI ==========
def main():
    import sys
    bot = TradingBot()
    
    if len(sys.argv) < 2:
        print("📊 TRADING BOT v2.1 - ESTRATEGIA MEJORADA")
        print("=" * 50)
        
        status = bot.get_status()
        print(f"💰 Balance: ${status['balance']}")
        print(f"📈 PnL Diario: ${status['daily_pnl']}")
        print(f"🔄 Trades hoy: {status['trades_today']}")
        
        if status['positions']:
            print("\n📌 POSICIONES:")
            for sym, pos in status['positions'].items():
                print(f"   {sym}: {pos['side']} {pos['amount']} @ ${pos['entry']} (${pos['pnl']})")
        
        print("\n📊 ANÁLISIS DE SEÑALES:")
        analysis = bot.analyze_all()
        
        for sym, sig in analysis.items():
            if sig['signal'] == 'STRONG_BUY':
                emoji = "🟢🟢"
            elif sig['signal'] == 'BUY':
                emoji = "🟢"
            elif sig['signal'] == 'STRONG_SELL':
                emoji = "🔴🔴"
            elif sig['signal'] == 'SELL':
                emoji = "🔴"
            else:
                emoji = "⚪"
            
            print(f"\n{emoji} {sym}: {sig['signal']} ({sig['confidence']}%)")
            print(f"   Trend: {sig['trend']} | RSI: {sig['rsi']} | Structure: {sig['structure']}")
            for reason in sig['reasons'][:4]:
                print(f"   {reason}")
        
        return
    
    cmd = sys.argv[1]
    
    if cmd == 'analyze':
        print(json.dumps(bot.analyze_all(), indent=2))
    
    elif cmd == 'buy' and len(sys.argv) >= 3:
        print(json.dumps(bot.open_long(sys.argv[2].upper()), indent=2))
    
    elif cmd == 'sell' and len(sys.argv) >= 3:
        print(json.dumps(bot.open_short(sys.argv[2].upper()), indent=2))
    
    elif cmd == 'close' and len(sys.argv) >= 3:
        print(json.dumps(bot.close_position(sys.argv[2].upper()), indent=2))
    
    elif cmd == 'check':
        triggered = bot.check_sl_tp()
        print(json.dumps(triggered, indent=2) if triggered else print("✅ Sin triggers"))
    
    elif cmd == 'status':
        print(json.dumps(bot.get_status(), indent=2))

if __name__ == "__main__":
    main()
