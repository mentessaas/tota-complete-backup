#!/usr/bin/env python3
"""
Hyperliquid Trading Bot
API wrapper usando CCXT
"""
import os
import sys
from hyperliquid import HyperliquidSync

# Para usar sin wallet (solo info)
def get_markets():
    """Obtener todos los mercados disponibles"""
    hl = HyperliquidSync()
    return hl.fetch_markets()

def get_ticker(symbol):
    """Obtener ticker de un símbolo"""
    hl = HyperliquidSync()
    return hl.fetch_ticker(symbol)

def get_orderbook(symbol, limit=20):
    """Obtener orderbook"""
    hl = HyperliquidSync()
    return hl.fetch_order_book(symbol, limit)

def get_ohlcv(symbol, timeframe='1h', limit=100):
    """Obtener velas"""
    hl = HyperliquidSync()
    return hl.fetch_ohlcv(symbol, timeframe, limit=limit)

# Para usar con wallet
class HyperliquidBot:
    def __init__(self, wallet_address, private_key, testnet=True):
        self.hl = HyperliquidSync(wallet_address, private_key, testnet=testnet)
        self.testnet = testnet
    
    def get_balance(self):
        """Balance actual"""
        return self.hl.fetch_balance()
    
    def get_positions(self):
        """Posiciones abiertas"""
        return self.hl.fetch_positions()
    
    def open_long(self, symbol, amount, price=None, leverage=10):
        """Abrir posición larga"""
        # Set leverage primero
        self.hl.set_leverage(leverage, symbol)
        
        # Crear orden
        order_type = "market" if price is None else "limit"
        return self.hl.create_order(
            symbol=symbol,
            type=order_type,
            side="buy",
            amount=amount,
            price=price
        )
    
    def open_short(self, symbol, amount, price=None, leverage=10):
        """Abrir posición corta"""
        self.hl.set_leverage(leverage, symbol)
        
        order_type = "market" if price is None else "limit"
        return self.hl.create_order(
            symbol=symbol,
            type=order_type,
            side="sell",
            amount=amount,
            price=price
        )
    
    def close_position(self, symbol):
        """Cerrar posición"""
        positions = self.hl.fetch_positions(symbol)
        if not positions:
            return {"error": "No hay posiciones abiertas"}
        
        pos = positions[0]
        amount = abs(pos["contracts"])
        side = "sell" if pos["side"] == "long" else "buy"
        
        return self.hl.create_order(
            symbol=symbol,
            type="market",
            side=side,
            amount=amount
        )
    
    def set_leverage(self, leverage, symbol):
        """Configurar leverage"""
        return self.hl.set_leverage(leverage, symbol)
    
    def get_funding_rate(self, symbol):
        """Obtener funding rate"""
        return self.hl.fetch_funding_rate(symbol)

# Test
if __name__ == "__main__":
    print("🔄 Conectando a Hyperliquid testnet...")
    
    # Test público
    hl = HyperliquidSync()
    markets = hl.fetch_markets()
    print(f"✅ {len(markets)} mercados disponibles")
    
    # BTC ticker
    btc = hl.fetch_ticker("BTC/USDT")
    print(f"📊 BTC: ${btc['last']}")
    
    print("\n✅ Hyperliquid API funcionando!")
