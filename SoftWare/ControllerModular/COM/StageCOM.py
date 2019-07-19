# coding=utf8

from SoftWare.ControllerModular.COM import BaseCOM

"""
本类继承自串口设备基类，主要实现位移电机的控制
"""


class StageCOM(BaseCOM):
    def __init__(self, port, bps, timeout):
        """ 初始化方法，只需要调用父类的构造方法"""
        super(StageCOM,self).__init__(port, bps, timeout)

    def Move(self):
        """移动平台"""

        # 电机使能
        self.SendMsg(self.__InstructionList["on"][0])

        # 电机脱机
        self.SendMsg(self.__InstructionList["off"][0])
