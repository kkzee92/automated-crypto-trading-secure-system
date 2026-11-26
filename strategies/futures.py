"""
Futures / Perpetual Strategies
Includes funding rate awareness and liquidation risk.
"""
from src.base_strategy import BaseStrategy
from typing import Dict, Optional

class FuturesTrendFollowing(BaseStrategy):
    def generate_signal(self, market_data: Dict) -> Optional[Dict]:
        # Placeholder: EMA crossover + funding filter
        funding = market_data.get('funding_rate', 0)
        if funding > 0.001:  # high positive funding, avoid long
            return None
        # Trend logic here
        return {"side": "buy", "symbol": market_data['symbol'], "type": "futures", "leverage": 2, "reason": "trend_following"}

class FuturesMeanReversionFunding(BaseStrategy):
    def generate_signal(self, market_data: Dict) -> Optional[Dict]:
        funding = market_data.get('funding_rate', 0)
        if abs(funding) > 0.0005:
            side = "sell" if funding > 0 else "buy"
            return {"side": side, "symbol": market_data['symbol'], "type": "futures", "reason": "funding_arbitrage"}
        return None
