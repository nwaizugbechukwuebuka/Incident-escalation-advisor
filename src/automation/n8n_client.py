"""
n8n client for automating incident escalation.
"""
import os
import httpx
from src.utils.logger import logger

N8N_WEBHOOK_URL = os.getenv("N8N_WEBHOOK_URL")

def escalate_incident(incident):
    """Trigger n8n workflow for escalation."""
    try:
        response = httpx.post(N8N_WEBHOOK_URL, json=incident.dict())
        response.raise_for_status()
        logger.info(f"n8n escalation triggered: {response.status_code}")
        return incident
    except Exception as e:
        logger.error(f"n8n escalation failed: {e}")
        raise