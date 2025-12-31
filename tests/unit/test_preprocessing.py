import sys
import os
import pytest
os.environ["LLM_API_KEY"] = "test-key"
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../../')))
from src.preprocessing.text_cleaner import clean_text
from src.preprocessing.language_detector import detect_language

def test_clean_text():
    assert clean_text("  Hello   World!  ") == "Hello World!"

def test_detect_language():
    assert detect_language("This is English.") == "en"
