from aiocqhttp import MessageSegment
from jieba import posseg
from nonebot import on_command, CommandSession, on_natural_language, NLPSession, IntentCommand
from services.common import ServiceException
from services.weather import  get_current_weather_short

__plugin_name__ = '天气'
__plugin_usage__ = (
    '用法：\n'
    '对我说 “天气 香港” 获取天气简要\n'
    '“天气 香港 详细” 获取当前天气的详细报告'
)

weather_permission = lambda sender: (not sender.is_privatechat) or sender.is_superuser


@on_command('weather', aliases=('气温', '天气'))
async def _(session: CommandSession):
    # 若用户对机器人说“天气”，则此变量为 `['']`
    # 若用户对机器人说“天气 香港”，则此变量为 `['香港']`
    # 若用户对机器人说“天气 香港 详细”，则此变量为 `['香港', '详细']`
    args = session.current_arg_text.strip().split(' ', 1)
    if not args[0]:
        city = await session.aget(key='city', prompt='请问是什么城市呢？', at_sender=True)
    else:
        city = args[0]
    func = get_current_weather_short
    result = await func(city)
    if result['msg'] == 'success':
        data = result['data']
        cityname=data['cityname']
        temp=data['temp']
        weather=data['weather']
        pm25=data['pm25']
        time=data['time']
        msg='天气数据最后更新时间：'+time+'\n'+'城市：'+cityname+'\n'+\
        '天气：'+weather+' '+temp+'℃\n'+'PM2.5：'+pm25+'μg/m3\n'
        await session.send(MessageSegment.text(msg))
    else:
        await session.send(MessageSegment.text(result['msg']))


# 只要消息包含“天气”，就执行此处理器
@on_natural_language(keywords={'天气'})
async def _(session: NLPSession):
    # 使用 jieba 将消息句子分词
    words = posseg.lcut(session.msg_text.strip())
    args = {}
    for word in words:
        if word.flag == 'ns': # ns 表示该词为地名
            args['city'] = word.word

    # 置信度为 90，意为将此会话当作 'weather' 命令处理
    return IntentCommand(90, 'weather', args=args)
