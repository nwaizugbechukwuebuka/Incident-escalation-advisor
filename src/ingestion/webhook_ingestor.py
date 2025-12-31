"""
Webhook ingestor for Incident Escalation Advisor.
"""
from src.api.schemas import IncidentIn
from src.utils.logger import logger

def ingest_webhook(incident: IncidentIn) -> dict:
    """Ingest incident from webhook source."""
    logger.info(f"Ingesting webhook incident: {incident.subject}")
    return incident.dict()