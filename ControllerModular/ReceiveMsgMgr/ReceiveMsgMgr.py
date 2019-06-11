# coding=utf8

import json

"""
本类用于读取json文件，获取串口返回值列表
"""


class ReceiveMsgMgr(object):
    def __init__(self):
        """初始化方法，加载配置参数"""
        self.__settingMap = {}

        # 尝试打开json文件
        try:
            with open("ReceiveMsgList.json", 'r') as jsonFile:
                self.__settingMap = json.load(jsonFile)
        except:
            pass
            # fp = open("RS485_InstructionList.json", "w")
            # fp.close()

    def GetParameter(self):
        return self.__settingMap


# 测试代码
if __name__ == '__main__':
    print(ReceiveMsgMgr().GetParameter())
