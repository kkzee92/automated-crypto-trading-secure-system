"""
Spot Asset Class Strategies
Mean reversion and momentum examples.
"""
from src.base_strategy import BaseStrategy
from typing import Dict, Optional
import pandas as pd

class SpotMeanReversion(BaseStrategy):
    def generate_signal(self, market_data: Dict) -> Optional[Dict]:
        df = pd.DataFrame(market_data.get('ohlcv', []))
        if len(df) < 20:
            return None
        # Simple MA crossover or z-score mean reversion
        close = df['close']
        ma = close.rolling(20).mean()
        std = close.rolling(20).std()
        zscore = (close.iloc[-1] - ma.iloc[-1]) / std.iloc[-1] if std.iloc[-1] else 0
        if zscore < -2.0:
            return {"side": "buy", "symbol": market_data['symbol'], "type": "spot", "reason": "mean_reversion_oversold"}
        elif zscore > 2.0:
            return {"side": "sell", "symbol": market_data['symbol'], "type": "spot", "reason": "mean_reversion_overbought"}
        return None

class SpotMomentum(BaseStrategy):
    def generate_signal(self, market_data: Dict) -> Optional[Dict]:
        df = pd.DataFrame(market_data.get('ohlcv', []))
        if len(df) < 50:
            return None
        returns = df['close'].pct_change().iloc[-10:].mean()
        if returns > 0.01:
            return {"side": "buy", "symbol": market_data['symbol'], "type": "spot", "reason": "momentum_breakout"}
        return None
