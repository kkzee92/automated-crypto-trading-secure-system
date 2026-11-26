"""
DeFi / On-chain Asset Class Strategies
Focus on yield, liquidity provision, and security (private key isolation).
"""
from src.base_strategy import BaseStrategy
from typing import Dict, Optional

class DeFiYieldFarming(BaseStrategy):
    def generate_signal(self, market_data: Dict) -> Optional[Dict]:
        apy = market_data.get('apy', 0)
        il_risk = market_data.get('impermanent_loss_estimate', 0)
        if apy > 0.15 and il_risk < 0.05:  # high yield, low IL
            return {"side": "provide_liquidity", "pool": market_data['pool'], "type": "defi", "reason": "yield_opportunity"}
        return None

class DeFiArbitrage(BaseStrategy):
    def generate_signal(self, market_data: Dict) -> Optional[Dict]:
        price_diff = market_data.get('cross_dex_price_diff_pct', 0)
        if abs(price_diff) > 0.5:  # >0.5% arb
            return {"side": "arbitrage", "type": "defi", "reason": "dex_arbitrage", "spread": price_diff}
        return None
