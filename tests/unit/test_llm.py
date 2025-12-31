import sys
import os
os.environ["LLM_API_KEY"] = "test-key"
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../../')))
from src.llm.response_parser import parse_response
from src.llm.validator import validate_response

def test_parse_response():
    assert parse_response("test") == {"parsed": "test"}

def test_validate_response():
    assert validate_response("something") is True
    assert validate_response("") is False
