"""
Email ingestor for Incident Escalation Advisor.
"""
from src.api.schemas import IncidentIn
from src.utils.logger import logger

def ingest_email(incident: IncidentIn) -> dict:
    """Ingest incident from email source."""
    logger.info(f"Ingesting email incident: {incident.subject}")
    return incident.dict()