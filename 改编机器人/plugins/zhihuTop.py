__plugin_name__ = '知乎热搜'
__plugin_usage__ = r"""

返回知乎热搜
"""

from nonebot import on_command, CommandSession, on_natural_language, NLPSession, IntentCommand
from aiocqhttp import MessageSegment

from services.zhihuTop import get_zhTop


@on_command('zhTop', aliases=('知乎', '知乎热搜'))
async def zhihuTop(session: CommandSession):
    data = await get_zhTop()
    msg = ''
    for item in data:
        msg = msg + item['query'] + '\nurl:' + item['url'] + '\n'
    await session.send(MessageSegment.text(msg))


@on_natural_language(keywords={'知乎'})
async def _(session: NLPSession):
    # 返回意图命令，前两个参数必填，分别表示置信度和意图命令名
    return IntentCommand(90.0, 'zhTop')
