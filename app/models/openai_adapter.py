from typing import Optional
import os
import httpx

async def generate_reply_openai(message: str, session_id: Optional[str] = None) -> str:
    """
    OpenAI adapter using the OpenAI Chat Completions API via httpx.
    Requires OPENAI_API_KEY environment variable.
    """
    api_key = os.getenv("OPENAI_API_KEY")
    if not api_key:
        return "OpenAI API key not configured. Set OPENAI_API_KEY."

    headers = {"Authorization": f"Bearer {api_key}", "Content-Type": "application/json"}
    payload = {
        "model": "gpt-3.5-turbo",
        "messages": [{"role": "user", "content": message}],
        "max_tokens": 150,
        "temperature": 0.7,
    }

    async with httpx.AsyncClient(timeout=30.0) as client:
        resp = await client.post("https://api.openai.com/v1/chat/completions", json=payload, headers=headers)
        resp.raise_for_status()
        data = resp.json()
    return data["choices"][0]["message"]["content"].strip()