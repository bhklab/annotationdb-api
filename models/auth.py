import os
from typing import Optional
from fastapi import Security, HTTPException, status
from fastapi.security import APIKeyHeader
from dotenv import load_dotenv

load_dotenv(override=True)

api_key_header = APIKeyHeader(name="X-API-Key", auto_error=False)


async def get_api_key(api_key: Optional[str] = Security(api_key_header)) -> str:
    """Strict authentication: Raises 401 Unauthorized if key is missing or invalid."""
    expected_token = os.getenv("API_TOKEN")
    if not api_key or not expected_token or api_key != expected_token:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid or missing API Key",
        )
    return api_key


async def get_optional_api_key(
    api_key: Optional[str] = Security(api_key_header),
) -> Optional[str]:
    """Optional authentication: Returns valid key if matched, otherwise None."""
    expected_token = os.getenv("API_TOKEN")
    if api_key and expected_token and api_key == expected_token:
        return api_key
    return None
