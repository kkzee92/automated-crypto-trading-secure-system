"""
Security Utilities
Encryption, key handling stubs, audit logging.
Never store real keys here.
"""
from cryptography.fernet import Fernet
import os
import logging
from datetime import datetime

logger = logging.getLogger(__name__)

class SecureVault:
    def __init__(self):
        key = os.getenv("VAULT_KEY")
        if not key:
            logger.warning("No VAULT_KEY set - using demo mode only")
            self.fernet = None
        else:
            self.fernet = Fernet(key.encode())

    def encrypt(self, data: str) -> str:
        if not self.fernet:
            return data  # demo
        return self.fernet.encrypt(data.encode()).decode()

    def decrypt(self, token: str) -> str:
        if not self.fernet:
            return token
        return self.fernet.decrypt(token.encode()).decode()

class AuditLogger:
    def __init__(self, log_path="audit.log"):
        self.log_path = log_path

    def log_event(self, event: str, details: dict):
        entry = {
            "timestamp": datetime.utcnow().isoformat(),
            "event": event,
            "details": details
        }
        # In production: sign and append immutably
        with open(self.log_path, "a") as f:
            f.write(str(entry) + "\n")
        logger.info(f"AUDIT: {event}")
