"""
Main entrypoint for the automated crypto trading information system.
Supports paper mode by default.
"""
import argparse
import logging
from strategies.spot import SpotMeanReversion
from security.vault import AuditLogger, SecureVault

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--mode", default="paper", choices=["paper", "live"])
    parser.add_argument("--strategy", default="spot_mean_reversion")
    args = parser.parse_args()

    if args.mode == "live":
        logger.warning("Live mode requires full security review and real keys via vault. Aborting for safety.")
        return

    audit = AuditLogger()
    vault = SecureVault()
    audit.log_event("system_start", {"mode": args.mode, "strategy": args.strategy})

    # Demo market data
    demo_data = {
        "symbol": "BTC/USDT",
        "ohlcv": [{"close": 60000} for _ in range(30)]  # simplified
    }

    if args.strategy == "spot_mean_reversion":
        strat = SpotMeanReversion({}, risk_manager=type("RM", (), {"check_position_size": lambda s: True, "check_drawdown": lambda: True})())
        signal = strat.execute(demo_data)
        if signal:
            logger.info(f"Paper signal: {signal}")
            audit.log_event("paper_signal", signal)
        else:
            logger.info("No signal generated")

    logger.info("System cycle complete (paper mode)")

if __name__ == "__main__":
    main()
