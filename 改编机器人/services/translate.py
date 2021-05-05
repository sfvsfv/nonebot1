from aiocache import cached

from services.common import translate


@cached(ttl=60)
async def get_translate(keyword: str) -> str:
    return await translate(keyword)
