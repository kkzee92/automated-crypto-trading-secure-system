# Automated Cryptocurrency Trading Information System

Secure, modular automated crypto trading information and strategy system with emphasis on cyber and data security architecture.

## Features

- Multi-asset class trading strategies (Spot, Futures/Perpetuals, Options, DeFi/Yield)
- Real-time market data ingestion (via CCXT or public APIs)
- Risk management and position sizing
- Cybersecurity architecture: encryption, key management, audit logging, least privilege
- Data security: encrypted storage, secure config, anomaly detection
- Extensible strategy framework
- Paper trading / simulation mode by default

## Architecture Overview

See [docs/ARCHITECTURE.md](docs/ARCHITECTURE.md) for full cyber and data security design.

## Quick Start

```bash
pip install -r requirements.txt
python src/main.py --mode paper --strategy spot_mean_reversion
```

**Warning**: This is for educational and informational purposes. Never use real API keys without proper security review. Trading involves substantial risk of loss.

## Security Principles

- Zero hard-coded secrets
- Environment variables + vault integration ready
- All sensitive data encrypted at rest and in transit
- Immutable audit logs
- Rate limiting and anomaly detection

## Contributing

PRs welcome. Focus on security enhancements and new strategies.

## License

MIT
