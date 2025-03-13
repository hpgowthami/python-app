from redis import Redis
from typing import Optional
import json

redis_client = Redis(host='localhost', port=6379, db=0)

def set_cache(key: str, value: dict, expiration: Optional[int] = None) -> None:
    if expiration:
        redis_client.setex(key, expiration, json.dumps(value))
    else:
        redis_client.set(key, json.dumps(value))

def get_cache(key: str) -> Optional[dict]:
    value = redis_client.get(key)
    if value:
        return json.loads(value)
    return None