import sys
import os
os.environ["LLM_API_KEY"] = "test-key"
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../../')))
from src.intelligence.incident_classifier import classify_incident
from src.intelligence.severity_scoring import score_severity

def test_classify_incident(monkeypatch):
    import openai
    class DummyResponse:
        class Choice:
            def __init__(self, content):
                self.message = type("msg", (), {"content": content})
        def __init__(self, content):
            self.choices = [self.Choice(content)]
    def fake_create(*args, **kwargs):
        return DummyResponse("IT Issue")
    class MockCompletions:
        def create(self, *args, **kwargs):
            return fake_create(*args, **kwargs)
    class MockChat:
        def __init__(self):
            self.completions = MockCompletions()
    class MockClient:
        def __init__(self, *args, **kwargs):
            self.chat = MockChat()
    monkeypatch.setattr(openai, "OpenAI", MockClient)
    from src.intelligence.incident_classifier import classify_incident
    result = classify_incident({"description": "Server down"})
    assert result == "IT Issue"

def test_score_severity(monkeypatch):
    import openai
    class DummyResponse:
        class Choice:
            def __init__(self, content):
                self.message = type("msg", (), {"content": content})
        def __init__(self, content):
            self.choices = [self.Choice(content)]
    def fake_create(*args, **kwargs):
        return DummyResponse("High")
    class MockCompletions:
        def create(self, *args, **kwargs):
            return fake_create(*args, **kwargs)
    class MockChat:
        def __init__(self):
            self.completions = MockCompletions()
    class MockClient:
        def __init__(self, *args, **kwargs):
            self.chat = MockChat()
    monkeypatch.setattr(openai, "OpenAI", MockClient)
    from src.intelligence.severity_scoring import score_severity
    result = score_severity({"description": "Critical outage"})
    assert result == "High"
