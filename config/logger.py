import logging
from logging.handlers import RotatingFileHandler
import os


os.makedirs("logs", exist_ok=True)

logger = logging.getLogger("inventory_app")
logger.setLevel(logging.DEBUG)

formatter = logging.Formatter(
    "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
)


file_handler = RotatingFileHandler(
    "logs/app.log",
    maxBytes=1_000_000,  # 1MB
    backupCount=3
)
file_handler.setFormatter(formatter)

console_handler = logging.StreamHandler()
console_handler.setFormatter(formatter)

logger.addHandler(file_handler)
logger.addHandler(console_handler)

