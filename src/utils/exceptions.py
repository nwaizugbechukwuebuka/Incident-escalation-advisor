"""
Custom exceptions for Incident Escalation Advisor.
"""
class IncidentEscalationError(Exception):
    """Base exception for escalation errors."""
    pass

class LLMServiceError(IncidentEscalationError):
    """Exception for LLM service errors."""
    pass
