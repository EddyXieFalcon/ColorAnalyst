# coding=utf8

import json
import serial
import serial.tools.list_ports
import threading
import time
import binascii, re


class BaseCOM(object):
    def __init__(self):
        """初始化方法"""

        # 调用父类初始化方法
        super().__init__()

        # 初始化参数
        self.__defaultSettingMap = None    # 所有的硬件配置参数
        self.__userSettingMap = None    # 所有的硬件配置参数

    def loadConfig(self):
        """加载本地的一个config文件，解析参数"""

        # 尝试打开json文件
        try:
            # 成功打开json文件
            with open("setting.json", 'r') as jsonFile:
                self.__userSettingMap = json.load(jsonFile)
            return True
        except:
            # 如果打开失败，那么为程序创建一个json
            fp = open("setting.json", "w")
            fp.close()
            return False

    def loadParameter(self):
        """由导入的json文件，加载本地参数"""

        # 解析参数

