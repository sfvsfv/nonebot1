

from services.common import get_joke_data
import requests

async def get_joke():
    url = 'https://api.muxiaoguo.cn/api/xiaohua'
    d=requests.get(url).json()
    print(d)
    t=d['data']['content']
    print(t)
    return str(t)
