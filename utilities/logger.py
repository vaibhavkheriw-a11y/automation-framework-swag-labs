import logging
import os

LOG_DIR = os.path.join(os.path.dirname(os.path.dirname(__file__)), "reports")
LOG_FILE = os.path.join(LOG_DIR, "framework.log")

os.makedirs(LOG_DIR, exist_ok=True)

logger = logging.getLogger("CypressInfra")
logger.setLevel(logging.INFO)

if not logger.handlers:
    formatter = logging.Formatter(
        "%(asctime)s | %(levelname)s | %(name)s | %(message)s"
    )

    stream_handler = logging.StreamHandler()
    stream_handler.setFormatter(formatter)

    file_handler = logging.FileHandler(LOG_FILE, encoding="utf-8")
    file_handler.setFormatter(formatter)

    logger.addHandler(stream_handler)
    logger.addHandler(file_handler)
