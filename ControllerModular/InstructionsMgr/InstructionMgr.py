# coding=utf8

import json

"""
本类用于读取json文件，获取配置参数列表
"""


class InstructionMgr(object):
    def __init__(self):
        """初始化方法，加载配置参数"""
        self.__rs485InstructionMap = {}
        self.__stm32InstructionMap = {}

        # 尝试打开json文件
        try:
            with open("RS485_InstructionList.json", 'r') as jsonFile:
                self.__rs485InstructionMap = json.load(jsonFile)
        except:
            pass

        # 尝试打开json文件
        try:
            with open("STM32_InstructionList.json", 'r') as jsonFile:
                self.__stm32InstructionMap = json.load(jsonFile)
        except:
            pass

    def GetRS485InstructionsMap(self):
        return self.__rs485InstructionMap

    def GetSTM32InstructionsMap(self):
        return self.__stm32InstructionMap


# 测试代码
if __name__ == '__main__':
    print(InstructionMgr().GetRS485InstructionsMap())
