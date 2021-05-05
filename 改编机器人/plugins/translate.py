from aiocqhttp import MessageSegment
from nonebot import on_command, CommandSession
from nonebot import on_natural_language, NLPSession, IntentCommand
from services.translate import get_translate

__plugin_name__ = '翻译'
__plugin_usage__ = r"""
翻译句子或单词，自动转换语言
发送：翻译 [句子或单词]
"""


@on_command('translate', aliases='翻译')
async def translate(session: CommandSession):
    words = session.get('words', prompt='你想翻译什么句子呢？')
    report = await get_translate(words)
    await session.send(MessageSegment.text(report))


# weather.args_parser 装饰器将函数声明为 weather 命令的参数解析器
# 命令解析器用于将用户输入的参数解析成命令真正需要的数据
@translate.args_parser
async def _(session: CommandSession):
    # 去掉消息首尾的空白符
    stripped_arg = session.current_arg_text.strip()

    if session.is_first_run:
        # 该命令第一次运行（第一次进入命令会话）
        if stripped_arg:
            session.state['words'] = stripped_arg
        return

    if not stripped_arg:
        session.pause('要翻译的句子不能为空哦！')

    session.state[session.current_key] = stripped_arg


# on_natural_language 装饰器将函数声明为一个自然语言处理器
# keywords 表示需要响应的关键词，类型为任意可迭代对象，元素类型为 str
# 如果不传入 keywords，则响应所有没有被当作命令处理的消息
@on_natural_language(keywords={'翻译'})
async def _(session: NLPSession):
    # 返回意图命令，前两个参数必填，分别表示置信度和意图命令名
    return IntentCommand(90.0, 'translate')
