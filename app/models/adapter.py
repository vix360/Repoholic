import asyncio
import os
from typing import Optional

async def _local_dummy(message: str, session_id: Optional[str] = None) -> str:
    await asyncio.sleep(0.1)
    return f"Balasan dummy untuk: {message}"

# Choose implementation based on environment
if os.getenv("OPENAI_API_KEY"):
    try:
        from app.models.openai_adapter import generate_reply_openai as _generate_reply_impl
    except Exception:
        _generate_reply_impl = _local_dummy
else:
    _generate_reply_impl = _local_dummy

async def generate_reply(message: str, session_id: Optional[str] = None) -> str:
    """
    Unified entrypoint used by the API.
    If OPENAI_API_KEY is set, uses the OpenAI adapter; otherwise falls back to a local dummy reply.
    """
    return await _generate_reply_impl(message, session_id=session_id)