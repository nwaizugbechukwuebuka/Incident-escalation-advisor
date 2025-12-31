"""
Text cleaner for incident preprocessing.
"""
import re
from src.utils.logger import logger

def clean_text(text: str) -> str:
    """Clean and normalize incident text."""
    logger.info("Cleaning text for preprocessing.")
    text = re.sub(r'\s+', ' ', text)
    text = text.strip()
    return text