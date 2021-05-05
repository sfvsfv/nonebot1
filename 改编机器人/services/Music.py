from aiocache import cached

from services.common import get_music_id


@cached(ttl=60)
async def get_music(song):
    return await get_music_id(song)
