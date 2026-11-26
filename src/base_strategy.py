"""
Base Strategy Framework
All asset-class strategies inherit from this.
Includes mandatory risk and security checks.
"""
from abc import ABC, abstractmethod
from typing import Dict, Any, Optional
import logging

logger = logging.getLogger(__name__)

class BaseStrategy(ABC):
    def __init__(self, config: Dict[str, Any], risk_manager: Any):
        self.config = config
        self.risk_manager = risk_manager
        self.name = self.__class__.__name__

    @abstractmethod
    def generate_signal(self, market_data: Dict) -> Optional[Dict]:
        """Return order signal or None. Must be safe."""
        pass

    def pre_trade_check(self, signal: Dict) -> bool:
        """Mandatory security and risk gate."""
        if not self.risk_manager.check_position_size(signal):
            logger.warning(f"Risk check failed for {self.name}")
            return False
        if not self.risk_manager.check_drawdown():
            logger.warning("Max drawdown breached")
            return False
        return True

    def execute(self, market_data: Dict) -> Optional[Dict]:
        signal = self.generate_signal(market_data)
        if signal and self.pre_trade_check(signal):
            logger.info(f"Signal approved: {signal}")
            return signal
        return None
