"""
Severity scoring using LLM for Incident Escalation Advisor.
"""
from src.llm.client import query_llm
from src.utils.logger import logger

def score_severity(incident: dict) -> str:
    """Score severity using LLM."""
    try:
        prompt = f"Score the severity of this incident: {incident['description']}"
        severity = query_llm(prompt)
        logger.info(f"Incident severity scored as: {severity}")
        return severity
    except Exception as e:
        logger.error(f"Severity scoring failed: {e}")
        return "unknown"