
from nonebot import on_command, CommandSession, on_natural_language, NLPSession, IntentCommand
from aiocqhttp import MessageSegment
import requests
async def get_joke():
    url = 'https://api.muxiaoguo.cn/api/xiaohua'
    d=requests.get(url).json()
    # print(d)
    t=d['data']['content']
    # print(t)
    return str(t)

@on_command('joke', aliases=('笑话', '随机笑话'))
async def joke(session: CommandSession):
    msg = await get_joke()
    await session.send(MessageSegment.text(msg))


@on_natural_language(keywords={'笑话'})
async def _(session: NLPSession):
    # 返回意图命令，前两个参数必填，分别表示置信度和意图命令名
    return IntentCommand(90.0, 'joke')
