from nonebot import on_command, CommandSession
from aiocqhttp import MessageSegment

__plugin_name__ = '百科检索 发送：百科 [词条]'
__plugin_usage__ = r"""
查询词条百科
发送：百科 [词条]
"""

from services.wikiPedia import get_wikipedia


@on_command('wikipedia', aliases=('百科'))
async def wikipedia(session: CommandSession):
    words = session.get('words', prompt='你想查询什么词条呢？')
    data = await get_wikipedia(words)
    if len(data) == 1:
        res = MessageSegment.text(data[0])
        await session.send(res)
    elif len(data) == 2:
        res = MessageSegment.text(data[0])
        img = MessageSegment.image(data[1])
        await session.send(res+img)



@wikipedia.args_parser
async def _(session: CommandSession):
    # 去掉消息首尾的空白符
    stripped_arg = session.current_arg_text.strip()
    if session.is_first_run:
        if stripped_arg:
            session.state['words'] = stripped_arg
        return

    if not stripped_arg:
        session.pause('要查询的词句不能为空哦！')
    session.state[session.current_key] = stripped_arg



