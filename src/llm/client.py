"""
LLM client for querying language models.
"""
import os

import openai
from src.utils.logger import logger


def query_llm(prompt: str) -> str:
    """Query the LLM with a prompt and return the response."""
    try:
        api_key = os.getenv("LLM_API_KEY")
        client = openai.OpenAI(api_key=api_key)
        response = client.chat.completions.create(
            model="gpt-4",
            messages=[{"role": "user", "content": prompt}],
            max_tokens=32,
            temperature=0.2
        )
        result = response.choices[0].message.content.strip()
        logger.info(f"LLM response: {result}")
        return result
    except Exception as e:
        logger.error(f"LLM query failed: {e}")
        return "error"