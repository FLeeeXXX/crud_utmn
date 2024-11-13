from functools import wraps
from fastapi import HTTPException


def secure_request(func):
    @wraps(func)
    async def wrapper(*args, **kwargs):
        try:
            return await func(*args, **kwargs)
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))

    return wrapper
