from aiocache import cached

from .common import fetch_text



@cached(ttl=60) # 结果缓存 60 秒
async def get_current_weather_short(city: str) -> str:
    url = 'https://api.muxiaoguo.cn/api/tianqi?city=' + city + '&type=1'
    return await fetch_text(url)

