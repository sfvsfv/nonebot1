__plugin_name__ = '垃圾分类'
__plugin_usage__ = r"""

来看看你是什么垃圾~
"""

from nonebot import on_command, CommandSession, on_natural_language, NLPSession, IntentCommand
from aiocqhttp import MessageSegment

from services.garbageSort import get_garbageSort


@on_command('garbageSort', aliases='垃圾分类')
async def garbageSort(session: CommandSession):
    args = session.current_arg_text.strip().split(' ', 1)
    if not args[0]:
        keyword = await session.aget(key='city', prompt='请问是什么物品呢？', at_sender=True)
    else:
        keyword = args[0]
    result = await get_garbageSort(keyword)
    await session.send(MessageSegment.text(result))


@on_natural_language(keywords={'垃圾分类'})
async def _(session: NLPSession):
    # 返回意图命令，前两个参数必填，分别表示置信度和意图命令名
    return IntentCommand(90.0, 'garbageSort')
