"""
作者：杨涵文
时间：2021/4/6
"""
from nonebot.command import CommandSession
from nonebot.experimental.plugin import on_command


__plugin_name__ = 'ping'
__plugin_usage__ = '用法： 对我说 "ping"，我会回复 "pong!"'


@on_command('ping', permission=lambda sender: sender.is_superuser)
async def _(session: CommandSession):
    await session.send('pong!')