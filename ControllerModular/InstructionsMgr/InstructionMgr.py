# coding=utf8

import json

"""
本类用于读取json文件，获取配置参数列表
"""


class RS485InstructionMgr(object):
    def __init__(self):
        """初始化方法，加载配置参数"""
        self.__rs485InstructionMap = {}

        # 尝试打开json文件
        try:
            with open("RS485_InstructionList.json", 'r') as jsonFileRS485:
                self.__rs485InstructionMap = json.load(jsonFileRS485)
        except:
            pass

    def GetRS485InstructionsMap(self):
        return self.__rs485InstructionMap


class STM32InstructionMgr(object):
    def __init__(self):
        """初始化方法，加载配置参数"""
        self.__stm32InstructionMap = {}

        # 尝试打开json文件
        try:
            with open("STM32_InstructionList.json", 'r') as jsonFileSTM32:
                self.__stm32InstructionMap = json.load(jsonFileSTM32)
        except:
            pass

    def GetSTM32InstructionsMap(self):
        return self.__stm32InstructionMap


class LaserInstructionMgr(object):
    def __init__(self):
        """初始化方法，加载配置参数"""
        self.__laserInstructionMap = {}

        # 尝试打开json文件
        try:
            with open("Laser_InstructionList.json", 'r') as jsonFileLaser:
                self.__laserInstructionMap = json.load(jsonFileLaser)
        except:
            pass

    def GetLaserInstructionsMap(self):
        return self.__laserInstructionMap

# 测试代码
