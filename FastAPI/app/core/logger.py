from loguru import logger
import os

LOG_DIR = "logs"
LOG_PATH = os.path.join(LOG_DIR, "app.log")

# Create log directory if it doesn't exist
os.makedirs(LOG_DIR, exist_ok=True)

# Configure Loguru logger
logger.add(
    LOG_PATH,
    rotation="1 week",       # Create a new log file every week
    retention="1 month",     # Keep log files for 1 month
    compression="zip",       # Compress old log files
    level="INFO",            # Minimum log level
    enqueue=True,            # Recommended for async apps
    backtrace=True,          # Show full tracebacks for errors
    diagnose=True            # Provide detailed error diagnostics
)
