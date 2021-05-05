from services.common import get_yiyan_data


async def get_yiyan() -> []:
    url = 'https://api.muxiaoguo.cn/api/yiyan'
    return await get_yiyan_data(url)