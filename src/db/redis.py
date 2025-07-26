import redis.asyncio as redis
from src.config import Config

JWT_EXPIRY = 3600

token_blocklist = redis.Redis(
    host=Config.REDIS_HOST,
    port=Config.REDIS_PORT,
    db=0,
)

async def add_jti_to_blocklist(jti: str) -> None:
    await token_blocklist.set(name=jti, value="", ex=JWT_EXPIRY)

async def token_in_blocklist(jti: str) -> bool:
    value = await token_blocklist.get(name=jti)
    return value is not None
