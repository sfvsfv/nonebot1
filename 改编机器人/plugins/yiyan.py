__plugin_name__ = '一言'
__plugin_usage__ = r"""

苦到头未必是甜的，而甜到头一定是苦的 。
"""

from nonebot import on_command, CommandSession
from aiocqhttp import MessageSegment

from services.yiyan import get_yiyan


@on_command('yiyan', aliases=('一言'))
async def zhihuTop(session: CommandSession):
    msg = await get_yiyan()
    await session.send(MessageSegment.text(msg))
