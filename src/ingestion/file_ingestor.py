"""
File ingestor for Incident Escalation Advisor.
"""
from src.api.schemas import IncidentIn
from src.utils.logger import logger

def ingest_file(incident: IncidentIn) -> dict:
    """Ingest incident from file source."""
    logger.info(f"Ingesting file incident: {incident.subject}")
    return incident.dict()