import sys
import os
import pytest
os.environ["LLM_API_KEY"] = "test-key"
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../../')))
from src.automation.n8n_client import escalate_incident
from src.api.schemas import IncidentIn

def test_escalate_incident(monkeypatch):
    monkeypatch.setattr("httpx.post", lambda url, json: type("Resp", (), {"raise_for_status": lambda self: None, "status_code": 200})())
    incident = IncidentIn(source="email", subject="Test", description="desc")
    result = escalate_incident(incident)
    assert result.subject == "Test"
