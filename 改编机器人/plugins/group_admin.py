# -*- coding: utf-8 -*-
# @Time    : 2020/7/25 17:36
# @Author  : P19Y0UN9
# @File    : group_admin.py
# @Software: PyCharm
from nonebot import on_request, RequestSession
from nonebot import on_notice, NoticeSession

#TO DO 有问题
# # 将函数注册为群请求处理器
# @on_request('group')
# async def _(session: RequestSession):
#     # 判断验证信息是否符合要求
#     if session.event.comment == 'hello world':
#         # 验证信息正确，同意入群
#         await session.approve()
#         return
#     # 验证信息错误，拒绝入群
#     await session.reject('请回答正确答案')
#     await session.approve()


# 将函数注册为群成员增加通知处理器
@on_notice('group_increase')
async def _(session: NoticeSession):
    # 发送欢迎消息
    await session.send('欢迎新朋友～')

#自动同意加好友
@on_request('friend')
async def _(session: RequestSession):
    await session.bot.set_friend_add_request(flag=session.event.flag, approve=True, self_id=session.event.self_id,
                                             remark=session.event.comment)
