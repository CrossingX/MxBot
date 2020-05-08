import json
import os
from platform import platform
from shutil import rmtree
from nonebot.default_config import *


def getJson(name):
    text = open("config/config.json", "r", encoding='utf-8').read()
    deftext = open("config/config.default.json", "r", encoding='utf-8').read()
    configs = json.loads(text)
    defconfigs = json.loads(deftext)
    if configs.get(name, None) != None:
        return configs[name]
    else:
        return defconfigs.get(name, [])

def enable_plugins():
    plugList = getJson("enable_plugins")
    copy_com = "cp" if "Linux" in platform() else "copy"
    if os.path.exists("enabled"):
        rmtree("enabled")
    os.makedirs("enabled/plugins")
    fileNames = os.listdir("plugins") 
    for file in fileNames:
        newDir = ".\\plugins\\" + file
        if os.path.isfile(newDir) and file in plugList:
            newFile = ".\\enabled\\plugins\\" + file
            os.system(copy_com + " " + newDir + " " + newFile)


SUPERUSERS = getJson("superusers")
COMMAND_START = getJson("command_start")
HOST = getJson("host")
PORT = getJson("port")
DEBUG = eval(getJson("debug"))
SESSION_CANCEL_EXPRESSION = getJson("session_cancel_expression")
