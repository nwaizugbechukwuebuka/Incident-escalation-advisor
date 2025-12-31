import sys
import os
import pytest
os.environ["LLM_API_KEY"] = "test-key"
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../../')))
from src.api.schemas import IncidentIn
from src.ingestion.email_ingestor import ingest_email
from src.intelligence.incident_classifier import classify_incident
from src.intelligence.severity_scoring import score_severity
from src.storage.repository import IncidentRepository

def test_full_pipeline(monkeypatch):
    import openai
    class DummyResponse:
        class Choice:
            def __init__(self, content):
                self.message = type("msg", (), {"content": content})
        def __init__(self, content):
            self.choices = [self.Choice(content)]
    def fake_create(*args, **kwargs):
        if "Classify" in kwargs["messages"][0]["content"]:
            return DummyResponse("IT Issue")
        else:
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
    repo = IncidentRepository()
    incident = IncidentIn(source="email", subject="Test", description="Critical outage")
    data = ingest_email(incident)
    data["classification"] = classify_incident(data)
    data["severity"] = score_severity(data)
    repo.save_incident(data)
    assert data["classification"] == "IT Issue"
    assert data["severity"] == "High"
