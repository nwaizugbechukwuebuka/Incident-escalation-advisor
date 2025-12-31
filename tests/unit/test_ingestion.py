import sys
import os
os.environ["LLM_API_KEY"] = "test-key"
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../../')))
from src.ingestion.email_ingestor import ingest_email
from src.api.schemas import IncidentIn

def test_ingest_email():
    incident = IncidentIn(source="email", subject="Test", description="Test desc")
    result = ingest_email(incident)
    assert result["subject"] == "Test"
