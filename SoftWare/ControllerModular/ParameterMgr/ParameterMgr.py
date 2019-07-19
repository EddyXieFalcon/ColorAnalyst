# coding=utf8

import json

"""
本类用于读取json文件，获取配置指令列表
"""


class ParameterMgr(object):
    def __init__(self):
        """初始化方法，加载配置参数"""
        self.__settingMap = {}

        # 尝试打开json文件
        try:
            with open("DeviceParameter.json", 'r') as jsonFile:
                self.__settingMap = json.load(jsonFile)
        except:
            pass
            # fp = open("DeviceParameter.json", "w")
            # fp.close()

    def GetParameter(self):
        return self.__settingMap


# 测试代码
if __name__ == '__main__':
    print(ParameterMgr().GetParameter())
    print(type(ParameterMgr().GetParameter()))
