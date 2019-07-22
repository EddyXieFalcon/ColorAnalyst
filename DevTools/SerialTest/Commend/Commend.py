# coding=utf8

import os
import sys
import json


class Commend(object):
    def __init__(self):
        super(Commend, self).__init__()

        self.__CommendCodeFile = os.path.dirname(os.path.realpath(__file__)) + "\CommendCode.json"
        self.__FunctionCodeFile = os.path.dirname(os.path.realpath(__file__)) + "\FunctionCode.json"
        self.__ParameterFile = os.path.dirname(os.path.realpath(__file__)) + "\Parameter.json"

        self.__CommendCodeDict = {}
        self.__FunctionCodeDict = {}
        self.__ParameterDict = {}

        self.ReadFIle2Dict()

    def ReadFIle2Dict(self):
        """读取磁盘文件到内存"""

        try:
            with open(self.__CommendCodeFile, 'r') as jsonFile:
                self.__CommendCodeDict = json.load(jsonFile)
        except:
            pass

        try:
            with open(self.__FunctionCodeFile, 'r') as jsonFile:
                self.__FunctionCodeDict = json.load(jsonFile)
        except:
            pass

        try:
            with open(self.__ParameterFile, 'r') as jsonFile:
                self.__ParameterDict = json.load(jsonFile)
        except:
            pass

    def GetCommendDict(self):
        """获取命令字典"""

        return self.__CommendCodeDict, self.__FunctionCodeDict, self.__ParameterDict

    def SaveNewDict(self, CommendCodeDict, FunctionCodeDict, ParameterDict):
        """保存新的字典"""
        self.__CommendCodeDict = CommendCodeDict
        self.__FunctionCodeDict = FunctionCodeDict
        self.__ParameterDict = ParameterDict

        with open(self.__CommendCodeFile, "w") as jsonFile:
            try:
                json.dump(self.__CommendCodeDict, jsonFile)
            except:
                pass

        with open(self.__FunctionCodeFile, "w") as jsonFile:
            try:
                json.dump(self.__FunctionCodeDict, jsonFile)
            except:
                pass

        with open(self.__ParameterFile, "w") as jsonFile:
            try:
                json.dump(self.__ParameterDict, jsonFile)
            except:
                pass


if __name__ == '__main__':
    print(Commend().GetCommendDict())
