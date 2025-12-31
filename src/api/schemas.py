"""
Pydantic schemas for API requests and responses.
"""
from pydantic import BaseModel
from typing import Optional

class IncidentIn(BaseModel):
    source: str
    subject: str
    description: str
    status: Optional[str] = "new"

class IncidentOut(IncidentIn):
    id: int
    severity: Optional[str] = None
    classification: Optional[str] = None
