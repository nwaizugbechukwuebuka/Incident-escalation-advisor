"""
Helper functions for Incident Escalation Advisor.
"""
def to_snake_case(text: str) -> str:
    return ''.join(['_' + i.lower() if i.isupper() else i for i in text]).lstrip('_')
