from os import path
import nonebot
import config

if __name__ == '__main__':
    nonebot.init(config)
    nonebot.load_plugins(
        path.join(path.dirname(__file__), '', 'plugins'),
        'plugins'
    )
    bot = nonebot.get_bot()
    app = bot.asgi
    nonebot.run()
