"""
Incident repository for storage operations.
"""
from src.storage.models import Incident
from src.utils.logger import logger

class IncidentRepository:
    def __init__(self):
        self._incidents = {}
        self._id_counter = 1

    def save_incident(self, data: dict):
        data["id"] = self._id_counter
        self._incidents[self._id_counter] = data
        self._id_counter += 1
        logger.info(f"Incident saved: {data}")
        return data

    def get_incident(self, incident_id: int):
        return self._incidents.get(incident_id)

    def list_incidents(self):
        return list(self._incidents.values())
