import nonebot
import config
from config import getJson
from os import path


if __name__ == '__main__':
    nonebot.init(config)
    nonebot.load_plugins(
        path.join(path.dirname(__file__), 'enabled', 'plugins'),
        'enabled.plugins'
    )
    nonebot.run()
