"""
Language detector for incident preprocessing.
"""
from langdetect import detect
from src.utils.logger import logger

def detect_language(text: str) -> str:
    """Detect language of the given text."""
    try:
        lang = detect(text)
        logger.info(f"Detected language: {lang}")
        return lang
    except Exception as e:
        logger.error(f"Language detection failed: {e}")
        return "unknown"