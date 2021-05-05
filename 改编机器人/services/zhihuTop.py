from aiocache import cached

from services.common import get_zhTop_data


@cached(ttl=60)
async def get_zhTop() -> []:
    url = 'https://tenapi.cn/zhihuresou/'
    return await get_zhTop_data(url)
