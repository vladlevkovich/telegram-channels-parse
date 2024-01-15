from redis import asyncio, Redis
from bot.config.config import settings


async def get_redis():
    rd = await asyncio.Redis(host=settings.REDIS_HOST, port=settings.REDIS_PORT)
    async with rd:
        yield rd
    # return rd

# r = asyncio.Redis
# redis = Redis(host=settings.REDIS_HOST, port=settings.REDIS_PORT)
