import json
from nonebot.default_config import *


def getJson(name):
    text = open("C:\\Users\\mxcor\\Documents\\Code\\Project\\MxBot\\config\\config.json", "r", encoding='utf-8').read()
    deftext = open("C:\\Users\\mxcor\\Documents\\Code\\Project\\MxBot\\config\\config.default.json", "r", encoding='utf-8').read()
    configs = json.loads(text)
    defconfigs = json.loads(deftext)
    if configs.get(name, None) != None:
        return configs[name]
    else:
        return defconfigs.get(name, None)


SUPERUSERS = getJson("superusers")
COMMAND_START = getJson("command_start")
HOST = getJson("host")
PORT = getJson("port")
