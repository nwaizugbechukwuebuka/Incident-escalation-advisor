# ADR-001: LLM Selection for Incident Escalation Advisor

## Status
Accepted

## Context
The project requires a robust, accurate, and cost-effective LLM for classifying and scoring incident severity. Evaluation criteria included API availability, latency, cost, and language support.

## Decision
OpenAI's GPT-4 API is selected for its:
- High accuracy and reliability
- Broad language support
- Strong developer ecosystem

## Consequences
- Requires API key management
- Ongoing cost for API usage
- Easy integration with Python via openai package
