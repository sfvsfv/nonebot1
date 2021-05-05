from services.common import get_caihong_data
import requests

async def get_caihong():
    url = 'https://api.muxiaoguo.cn/api/caihongpi'
    t=requests.get(url).json()
    data=t['data']['comment']
    return data