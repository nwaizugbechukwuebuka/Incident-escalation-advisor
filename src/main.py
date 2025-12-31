"""
Main entry point for Incident Escalation Advisor.
"""
import uvicorn
from fastapi import FastAPI
from src.api.routes import router as api_router
from src.utils.logger import setup_logging

app = FastAPI(title="Incident Escalation Advisor")
setup_logging()

app.include_router(api_router)

if __name__ == "__main__":
    uvicorn.run("src.main:app", host="0.0.0.0", port=8000, reload=True)
