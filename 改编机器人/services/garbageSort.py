from aiocache import cached

from services.common import get_garbageSort_data


@cached(ttl=60)
async def get_garbageSort(keyword: str) -> str:
    url = 'https://api.muxiaoguo.cn/api/lajifl?m=' + keyword
    return await get_garbageSort_data(url)
