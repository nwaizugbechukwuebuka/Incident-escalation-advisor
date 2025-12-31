"""
Logger setup for Incident Escalation Advisor.
"""
from loguru import logger
import sys

def setup_logging():
    logger.remove()
    logger.add(sys.stdout, level="INFO", format="[{time:YYYY-MM-DD HH:mm:ss}] [{level}] {message}")

# Expose logger for use in modules
setup_logging()
