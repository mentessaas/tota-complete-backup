#!/usr/bin/env python3
"""
Hyperliquid API Wrapper
Wrapper para el SDK de Hyperliquid
"""
import os
import json
from hyperliquid import HyperliquidSync

class HyperliquidAPI:
    def __init__(self, wallet_address=None, private_key=None, testnet=True):
        self.testnet = testnet
        self.base_url = "https://api.hyperliquid-testnet.xyz" if testnet else "https://api.hyperliquid.xyz"
        
        if wallet_address and private_key:
            self.exchange = HyperliquidSync(wallet_address, private_key, testnet=testnet)
        else:
            self.exchange = None
        
        # Info público
        self.info = HyperliquidSync.info(testnet=testnet)
    
    def get_meta(self):
        """Información general del exchange"""
        return self.info.meta()
    
    def get_all_mids(self):
        """Todos los precios medios"""
        return self.info.all_mids()
    
    def get_orderbook(self, coin):
        """Orderbook de un símbolo"""
        return self.info.orderbook(coin)
    
    def get_user_state(self, address):
        """Estado del usuario (balance, posiciones)"""
        if not self.exchange:
            return {"error": "No wallet connected"}
        return self.exchange.info.user_state(address)
    
    def get_positions(self, address):
        """Posiciones abiertas"""
        if not self.exchange:
            return {"error": "No wallet connected"}
        state = self.exchange.info.user_state(address)
        return state.get("position", [])
    
    def place_order(self, coin, is_buy, size, price, order_type="limit"):
        """Colocar orden"""
        if not self.exchange:
            return {"error": "No wallet connected"}
        
        order = {
            "coin": coin,
            "side": "B" if is_buy else "S",
            "size": str(size),
            "price": str(price),
            "orderType": {"limit": {"tif": "Gtc"}}
        }
        
        return self.exchange.order(order)
    
    def cancel_order(self, coin, order_id):
        """Cancelar orden"""
        if not self.exchange:
            return {"error": "No wallet connected"}
        return self.exchange.cancel(coin, order_id)
    
    def get_balance(self, address):
        """Balance del usuario"""
        if not self.exchange:
            return {"error": "No wallet connected"}
        state = self.exchange.info.user_state(address)
        return state.get("marginSummary", {})
    
    def get_funding_rate(self, coin):
        """Funding rate actual"""
        try:
            funding = self.info.funding(coin)
            return funding
        except:
            return None

# Función de test
def test_connection():
    api = HyperliquidAPI(testnet=True)
    print("✅ Conexión testnet OK")
    
    mids = api.get_all_mids()
    print(f"📊 {len(mids)} pares disponibles")
    
    # BTC
    btc_ask = mids.get("BTC", {}).get("ask", "N/A")
    print(f"BTC ask: {btc_ask}")
    
    return api

if __name__ == "__main__":
    test_connection()
