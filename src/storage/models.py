"""
Incident storage models.
"""
from pydantic import BaseModel
from typing import Optional

class Incident(BaseModel):
    id: int
    source: str
    subject: str
    description: str
    status: Optional[str] = "new"
    severity: Optional[str] = None
    classification: Optional[str] = None
