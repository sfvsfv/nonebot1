__plugin_name__ = '彩虹屁'
__plugin_usage__ = r"""

跟你说了多少遍，抱怨没用，抱我。
"""

from nonebot import on_command, CommandSession, on_natural_language, NLPSession, IntentCommand
from aiocqhttp import MessageSegment

from services.caihong import get_caihong


@on_command('kua', aliases=('彩虹屁', '夸', '夸我'))
async def kua(session: CommandSession):
    msg = await get_caihong()
    await session.send(MessageSegment.text(msg))


@on_natural_language(keywords={'夸'})
async def _():
    return IntentCommand(90, 'kua')
