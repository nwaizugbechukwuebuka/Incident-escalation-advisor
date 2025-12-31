"""
API routes for Incident Escalation Advisor.
"""
from fastapi import APIRouter, HTTPException
from src.api.schemas import IncidentIn, IncidentOut
from src.ingestion.email_ingestor import ingest_email
from src.ingestion.webhook_ingestor import ingest_webhook
from src.ingestion.file_ingestor import ingest_file
from src.intelligence.incident_classifier import classify_incident
from src.intelligence.severity_scoring import score_severity
from src.automation.n8n_client import escalate_incident
from src.storage.repository import IncidentRepository
from src.utils.logger import logger

router = APIRouter()
repo = IncidentRepository()

@router.post("/incidents/ingest", response_model=IncidentOut)
def ingest_incident(incident: IncidentIn):
    """Ingest a new incident from any source."""
    try:
        if incident.source == "email":
            data = ingest_email(incident)
        elif incident.source == "webhook":
            data = ingest_webhook(incident)
        elif incident.source == "file":
            data = ingest_file(incident)
        else:
            raise HTTPException(status_code=400, detail="Unknown source")
        classification = classify_incident(data)
        severity = score_severity(data)
        data["classification"] = classification
        data["severity"] = severity
        repo.save_incident(data)
        logger.info(f"Incident ingested: {data}")
        return data
    except Exception as e:
        logger.error(f"Error ingesting incident: {e}")
        raise HTTPException(status_code=500, detail=str(e))

@router.get("/incidents/{incident_id}", response_model=IncidentOut)
def get_incident(incident_id: int):
    """Retrieve incident details by ID."""
    incident = repo.get_incident(incident_id)
    if not incident:
        raise HTTPException(status_code=404, detail="Incident not found")
    return incident

@router.get("/incidents/", response_model=list[IncidentOut])
def list_incidents():
    """List all incidents."""
    return repo.list_incidents()

@router.post("/incidents/escalate", response_model=IncidentOut)
def escalate(incident: IncidentIn):
    """Escalate an incident using n8n automation."""
    try:
        result = escalate_incident(incident)
        logger.info(f"Incident escalated: {result}")
        return result
    except Exception as e:
        logger.error(f"Error escalating incident: {e}")
        raise HTTPException(status_code=500, detail=str(e))
