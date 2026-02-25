#!/usr/bin/env python3
"""
Asterdex Trading Bot con Estrategia de Señales
=============================================
Señal FUERTE para BUY:
- Ratio > 0.80
- 5+ velas UP consecutivas
- Tendencia a favor

Señal para SELL:
- Ratio < 0.20
- 5+ velas DOWN consecutivas
- Tendencia en contra

Gestión de Riesgo:
- Riesgo/trade: 1%
- SL: 1%
- TP: 3%
- Máximo 3 posiciones
- Stop diario: -5%
"""
import requests
import json
import time
from datetime import datetime
import os

# Config
API_KEY = 'a8ecc704510a74ee336e5dcfa9b50edd6dfd14daedf279efffcaac311c2bceaa'
API_SECRET = '06f53fb3934bfea482e7d9d9f0a6843f42e1bb78e8c6149d01965d8e8d6f97fe'
BASE_URL = 'https://www.asterdex.com/api/v1'

# Paper trading config
PAPER_STATE_FILE = os.path.expanduser('~/zaltyko-os/scripts/trading_bot_state.json')
PAPER_BALANCE = 10000

# Strategy config
RISK_PER_TRADE = 0.01  # 1%
SL_PERCENT = 0.01  # 1%
TP_PERCENT = 0.03  # 3%
MAX_POSITIONS = 3
MAX_DAILY_LOSS = 0.05  # 5%

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
                    # Reset daily stats if new day
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
    
    def get_klines(self, symbol, interval='15m', limit=20):
        """Obtener velas"""
        r = requests.get(f"{BASE_URL}/klines", params={
            'symbol': symbol,
            'interval': interval,
            'limit': limit
        }, timeout=5)
        if r.status_code == 200:
            data = r.json()
            if not data:
                return None
            # Formato: [time, open, high, low, close, volume, ...]
            candles = []
            for d in data:
                try:
                    candles.append({
                        'time': d[0],
                        'open': float(d[1]),
                        'high': float(d[2]),
                        'low': float(d[3]),
                        'close': float(d[4]),
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
                'change': float(data.get('priceChange', 0)),
                'changePct': float(data.get('priceChangePercent', 0)),
                'high': float(data.get('highPrice', 0)),
                'low': float(data.get('lowPrice', 0)),
                'volume': float(data.get('volume', 0))
            }
        return None
    
    # ========== ANÁLISIS DE SEÑALES ==========
    def analyze_signal(self, symbol):
        """Analizar si hay señal fuerte para entrar"""
        candles = self.get_klines(symbol, interval='15m', limit=10)
        if not candles or len(candles) < 10:
            return {'signal': 'NO_DATA', 'confidence': 0}
        
        # 1. Analizar últimas 5 velas
        last_5 = candles[-5:]
        up_candles = sum(1 for c in last_5 if c['close'] > c['open'])
        
        # 2. Calcular ratio (fuerza de tendencia)
        if up_candles == 5:
            ratio = 1.0
        elif up_candles == 4:
            ratio = 0.8
        elif up_candles == 3:
            ratio = 0.6
        elif up_candles == 2:
            ratio = 0.4
        elif up_candles == 1:
            ratio = 0.2
        else:
            ratio = 0.0
        
        # 3. Analizar tendencia (media móvil simple)
        prices = [c['close'] for c in candles[-10:]]
        ma_9 = sum(prices[-9:]) / 9
        ma_21 = sum(prices[-21:]) / 21 if len(prices) >= 21 else prices[0]
        
        current_price = prices[-1]
        trend = 'UP' if current_price > ma_9 else 'DOWN'
        
        # 4. Calcular confianza
        confidence = 0
        signal = 'NEUTRAL'
        
        # BUY signal: ratio > 0.80 + 5 UP + trend UP
        if ratio >= 0.80 and up_candles >= 5 and trend == 'UP':
            signal = 'BUY'
            confidence = min(100, (ratio * 100) + (up_candles * 10))
        
        # SELL signal: ratio < 0.20 + 5 DOWN + trend DOWN
        elif ratio <= 0.20 and up_candles <= 1 and trend == 'DOWN':
            signal = 'SELL'
            confidence = min(100, ((1 - ratio) * 100) + ((5 - up_candles) * 10))
        
        # 5. Momentum (RSI simplificado)
        gains = sum(c['close'] - c['open'] for c in last_5 if c['close'] > c['open'])
        losses = sum(c['open'] - c['close'] for c in last_5 if c['close'] < c['open'])
        avg_gain = gains / 5
        avg_loss = losses / 5 if losses > 0 else 1
        rs = avg_gain / avg_loss
        rsi = 100 - (100 / (1 + rs))
        
        return {
            'symbol': symbol,
            'signal': signal,
            'confidence': round(confidence, 1),
            'ratio': ratio,
            'up_candles': up_candles,
            'trend': trend,
            'rsi': round(rsi, 1),
            'current_price': current_price,
            'ma_9': round(ma_9, 2),
            'ma_21': round(ma_21, 2)
        }
    
    def analyze_all_markets(self):
        """Analizar todos los mercados"""
        markets = ['BTCUSDT', 'ETHUSDT', 'BNBUSDT']
        analysis = {}
        
        for symbol in markets:
            analysis[symbol] = self.analyze_signal(symbol)
        
        return analysis
    
    # ========== TRADING ==========
    def calculate_position_size(self, price):
        """Calcular tamaño de posición basado en riesgo 1%"""
        risk_amount = self.balance * RISK_PER_TRADE
        # Size = Risk / (SL price - entry)
        # SL = 1%, so stop_loss = entry * 0.99
        size = risk_amount / (price * SL_PERCENT)
        return size
    
    def can_trade(self):
        """Verificar si podemos tradear"""
        # Check daily loss
        if self.daily_pnl <= -(self.balance * MAX_DAILY_LOSS):
            return False, "Stop diario alcanzado (-5%)"
        
        # Check max positions
        if len(self.positions) >= MAX_POSITIONS:
            return False, "Máximo de posiciones alcanzado"
        
        return True, "OK"
    
    def open_long(self, symbol, size=None):
        """Abrir posición LONG"""
        can_trade, reason = self.can_trade()
        if not can_trade:
            return {'error': reason}
        
        price = self.get_price(symbol)
        if not price:
            return {'error': 'No se pudo obtener precio'}
        
        # Calculate size if not provided
        if size is None:
            size = self.calculate_position_size(price)
        
        cost = size * price
        
        if cost > self.balance:
            return {'error': f'Balance insuficiente: ${self.balance:.2f} < ${cost:.2f}'}
        
        # Calcular SL y TP
        sl = price * (1 - SL_PERCENT)
        tp = price * (1 + TP_PERCENT)
        
        # Ejecutar
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
            'side': 'LONG',
            'symbol': symbol,
            'amount': round(size, 6),
            'entry': round(price, 2),
            'sl': round(sl, 2),
            'tp': round(tp, 2),
            'cost': round(cost, 2),
            'balance': round(self.balance, 2)
        }
    
    def close_position(self, symbol):
        """Cerrar posición"""
        if symbol not in self.positions:
            return {'error': 'No hay posición'}
        
        pos = self.positions[symbol]
        price = self.get_price(symbol)
        
        if not price:
            return {'error': 'No se pudo obtener precio'}
        
        if pos['side'] == 'LONG':
            pnl = (price - pos['entry_price']) * pos['amount']
            proceeds = pos['amount'] * price
        else:  # SHORT
            pnl = (pos['entry_price'] - price) * pos['amount']
            proceeds = pos['amount'] * price
        
        self.balance += proceeds
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
        """Check SL/TP triggered"""
        triggered = []
        
        for symbol, pos in list(self.positions.items()):
            price = self.get_price(symbol)
            if not price:
                continue
            
            # Check SL
            if pos['side'] == 'LONG' and price <= pos['sl']:
                triggered.append({
                    'type': 'SL',
                    'symbol': symbol,
                    'price': price,
                    'sl': pos['sl']
                })
                self.close_position(symbol)
            
            elif pos['side'] == 'SHORT' and price >= pos['sl']:
                triggered.append({
                    'type': 'SL',
                    'symbol': symbol,
                    'price': price,
                    'sl': pos['sl']
                })
                self.close_position(symbol)
            
            # Check TP
            elif pos['side'] == 'LONG' and price >= pos['tp']:
                triggered.append({
                    'type': 'TP',
                    'symbol': symbol,
                    'price': price,
                    'tp': pos['tp']
                })
                self.close_position(symbol)
            
            elif pos['side'] == 'SHORT' and price <= pos['tp']:
                triggered.append({
                    'type': 'TP',
                    'symbol': symbol,
                    'price': price,
                    'tp': pos['tp']
                })
                self.close_position(symbol)
        
        return triggered
    
    # ========== STATUS ==========
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
                pnl_pct = ((price - pos['entry_price']) / pos['entry_price']) * 100
            elif price:
                pnl = (pos['entry_price'] - price) * pos['amount']
                pnl_pct = ((pos['entry_price'] - price) / pos['entry_price']) * 100
            else:
                pnl = 0
                pnl_pct = 0
            
            status['positions'][symbol] = {
                'side': pos['side'],
                'amount': pos['amount'],
                'entry': pos['entry_price'],
                'current': price,
                'pnl': round(pnl, 2),
                'pnl_pct': round(pnl_pct, 2),
                'sl': pos['sl'],
                'tp': pos['tp']
            }
        
        return status

# ========== CLI ==========
def main():
    import sys
    
    bot = TradingBot()
    
    if len(sys.argv) < 2:
        # Mostrar status
        print("📊 TRADING BOT - ESTRATEGIA SEÑALES")
        print("=" * 50)
        
        status = bot.get_status()
        print(f"💰 Balance: ${status['balance']}")
        print(f"📈 PnL Diario: ${status['daily_pnl']}")
        print(f"🔄 Trades hoy: {status['trades_today']}")
        
        if status['positions']:
            print("\n📌 POSICIONES:")
            for sym, pos in status['positions'].items():
                emoji = "🟢" if pos['pnl'] >= 0 else "🔴"
                print(f"   {emoji} {sym}: {pos['side']} {pos['amount']} @ ${pos['entry']} (${pos['pnl']} / {pos['pnl_pct']}%)")
        
        # Análisis de señales
        print("\n📊 ANÁLISIS DE SEÑALES:")
        analysis = bot.analyze_all_markets()
        for sym, sig in analysis.items():
            if sig['signal'] == 'BUY':
                emoji = "🟢"
            elif sig['signal'] == 'SELL':
                emoji = "🔴"
            else:
                emoji = "⚪"
            
            print(f"   {emoji} {sym}: {sig['signal']} ({sig['confidence']}%) | ratio: {sig['ratio']} | trend: {sig['trend']} | RSI: {sig['rsi']}")
        
        return
    
    cmd = sys.argv[1]
    
    if cmd == 'analyze':
        analysis = bot.analyze_all_markets()
        print(json.dumps(analysis, indent=2))
    
    elif cmd == 'buy' and len(sys.argv) >= 3:
        symbol = sys.argv[2].upper()
        result = bot.open_long(symbol)
        print(json.dumps(result, indent=2))
    
    elif cmd == 'sell' and len(sys.argv) >= 3:
        symbol = sys.argv[2].upper()
        result = bot.close_position(symbol)
        print(json.dumps(result, indent=2))
    
    elif cmd == 'check':
        triggered = bot.check_sl_tp()
        if triggered:
            print("⚠️ SL/TP triggered:")
            print(json.dumps(triggered, indent=2))
        else:
            print("✅ Sin SL/TP triggered")
    
    elif cmd == 'status':
        print(json.dumps(bot.get_status(), indent=2))
    
    elif cmd == 'reset':
        bot.balance = PAPER_BALANCE
        bot.positions.trades_today = 0
        bot.daily = {}
        bot_pnl = 0
        bot.save_state()
        print("✅ Bot reseteado")
    
    else:
        print("Comandos:")
        print("  python3 trading_bot.py           # Status + análisis")
        print("  python3 trading_bot.py analyze   # Análisis detallado")
        print("  python3 trading_bot.py buy BTCUSDT  # Abrir LONG")
        print("  python3 trading_bot.py sell BTCUSDT  # Cerrar posición")
        print("  python3 trading_bot.py check     # Check SL/TP")
        print("  python3 trading_bot.py reset    # Resetear")

if __name__ == "__main__":
    main()
