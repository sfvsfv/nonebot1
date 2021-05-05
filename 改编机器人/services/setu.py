from services.common import  get_setu_data


async def get_setu():
    url="https://api.lolicon.app/setu/?apikey=0961535560170e964e4689&r18=2&size1200=true"
    return await get_setu_data(url)