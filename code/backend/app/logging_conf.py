
import logging
import sys
from logging.handlers import RotatingFileHandler


def setup_logging(log_file: str = "logs/app.log"):
    """
    Configure structured logging for the app.
    - Console output for dev
    - Rotating file logs for persistence
    """

    # Create a custom formatter
    formatter = logging.Formatter(
        fmt="%(asctime)s | %(levelname)s | %(name)s | %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S",
    )

    # Root logger
    logger = logging.getLogger()
    logger.setLevel(logging.INFO)

    # Stream handler (console)
    console_handler = logging.StreamHandler(sys.stdout)
    console_handler.setLevel(logging.INFO)
    console_handler.setFormatter(formatter)
    logger.addHandler(console_handler)

    # File handler (rotating logs)
    file_handler = RotatingFileHandler(
        log_file, maxBytes=5 * 1024 * 1024, backupCount=5, encoding="utf-8"
    )
    file_handler.setLevel(logging.INFO)
    file_handler.setFormatter(formatter)
    logger.addHandler(file_handler)

    return logger


# Initialize on import
logger = setup_logging()
