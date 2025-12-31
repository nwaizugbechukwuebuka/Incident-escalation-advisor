"""
Incident classifier using LLM for Incident Escalation Advisor.
"""
from src.llm.client import query_llm
from src.utils.logger import logger

def classify_incident(incident: dict) -> str:
    """Classify incident using LLM."""
    try:
        prompt = f"Classify the following incident: {incident['description']}"
        classification = query_llm(prompt)
        logger.info(f"Incident classified as: {classification}")
        return classification
    except Exception as e:
        logger.error(f"Classification failed: {e}")
        return "unclassified"