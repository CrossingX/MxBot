import os
import sys

import nonebot

import init


nonebot.init(init)
init.enable_plugins()
nonebot.load_plugins(
    os.path.join(os.path.dirname(__file__), 'enabled', 'plugins'),
    'enabled.plugins'
)
enable_groups = init.getJson("enable_groups")
ban_users = init.getJson("ban_users")
bot = nonebot.get_bot()
app = bot.asgi

if __name__ == '__main__':
    bot.run()


# pm2 start main.py -x --interpreter python --name mxbot
