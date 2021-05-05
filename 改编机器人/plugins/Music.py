__plugin_name__ = '点歌'
__plugin_usage__ = r"""
分享网易云音乐链接
发送：点歌 [歌曲名/歌手名]
"""

from aiocqhttp import MessageSegment
from nonebot import on_command, CommandSession

from services.Music import get_music


@on_command('music', aliases=('点歌'))
async def music(session: CommandSession):
    song = session.get('song', prompt='你想听什么歌呢？')
    song_report = await get_music(song)
    res = MessageSegment.music(163, song_report, 1)
    await session.send(res)


@music.args_parser
async def _(session: CommandSession):
    stripped_arg = session.current_arg_text.strip()

    if session.is_first_run:
        if stripped_arg:
            session.state['song'] = stripped_arg
        return

    if not stripped_arg:
        session.pause('要查询的歌曲名不能为空哦！')
    session.state[session.current_key] = stripped_arg

