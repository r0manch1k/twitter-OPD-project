import os
import configparser


thisFolder = os.path.dirname(os.path.abspath(__file__))
initFile = os.path.join(thisFolder, 'config.ini')
config = configparser.ConfigParser()
config.read(initFile)


def getConfigInfo(info_class, info_type):
    return config.get(info_class, info_type)


def setConfigInfo(info_class, info_type, info):
    config.set(info_class, info_type, info)
    with open(initFile, 'w') as configfile:
        config.write(configfile)