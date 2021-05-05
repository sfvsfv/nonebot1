"""
作者：杨涵文
时间：2021/5/4
"""
from nonebot.command import CommandSession
from nonebot.experimental.plugin import on_command

__plugin_name__ = 'test'
__plugin_usage__ = '用法： 对我说 "test"，我会回复 "test"'

@on_command('test')
async def _(session: CommandSession):
    await session.send('test')