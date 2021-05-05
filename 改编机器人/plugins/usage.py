# -*- coding: utf-8 -*-
# @Time    : 2020/7/25 17:44
# @Author  : P19Y0UN9
# @File    : usage.py
# @Software: PyCharm
import nonebot
from nonebot import on_command, CommandSession


@on_command('usage', aliases=['使用帮助', '帮助', '使用方法','功能','菜单'])
async def _(session: CommandSession):
    # 获取设置了名称的插件列表
    plugins = list(filter(lambda p: p.name, nonebot.get_loaded_plugins()))

    arg = session.current_arg_text.strip().lower()
    if not arg:
        # 如果用户没有发送参数，则发送功能列表
        await session.send(
            '我的名字是Saiki，你也可以叫我齐木\n我现在支持的功能有：\n[CQ:emoji,id=127775]' + '\n[CQ:emoji,id=127775]'.join(p.name for p in plugins)+'\n'+\
            "查看具体操作发送：使用方法/帮助 [功能]\n在群聊与我对话请加上我的名字。")
        return

    # 如果发了参数则发送相应命令的使用帮助
    for p in plugins:
        if p.name.lower() == arg:
            await session.send(p.usage)