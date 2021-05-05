from services.common import get_wikipedia_text
from aiocache import cached


@cached(ttl=60)
async def get_wikipedia(content:str) ->str:
    url="https://api.muxiaoguo.cn/api/Baike?type=Baidu&word="+content
    return await get_wikipedia_text(url)