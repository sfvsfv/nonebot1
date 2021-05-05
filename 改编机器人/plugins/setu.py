__plugin_name__ = '涩图 [hidden]'
__plugin_usage__ = r"""
随机发送setu
"""

import json

import requests
import nonebot
from nonebot import on_command, CommandSession,on_natural_language,IntentCommand

UserAgent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.89 Safari/537.36"

headers = {
    "user-agent": UserAgent
}

proxies = {
    "http": "http://www.pixiv.net",
}


@on_command('setu', aliases='色图')
async def setu(session:CommandSession):
    url = "https://api.lolicon.app/setu/?apikey=0961535560170e964e4689&r18=2&size1200=true"
    response = requests.get(url=url, headers=headers)
    data = json.loads(response.text)['data'][0]
    imgUrl = data['url']
    d=imgUrl.replace('png', 'jpg')
    print(d)
    tu = f"[CQ:image,file={d}]"
    await session.send(tu)

@on_natural_language(keywords={'色图'})
async def _():
    return IntentCommand(90, 'kua')