import os
import httpx

CAST_SERVICE_URL = os.getenv("CAST_SERVICE_URL") or "http://localhost:8002/api/v1/casts"


def is_cast_present(cast_id: int) -> bool:
    result = httpx.get(f"{CAST_SERVICE_URL}/{cast_id}")
    return True if result.status_code == 200 else False
