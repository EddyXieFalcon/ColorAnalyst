# coding=utf-8

import threading
from ControllerModular.ParameterMgr.ParameterMgr import ParameterMgr
from ControllerModular.COM.StageCOM import StageCOM
from ControllerModular.COM.PumpCOM import PumpCOM
from ControllerModular.COM.FilterCOM import FilterCOM

"""
本类用以提供各种硬件的调用以及通讯，本程序所有的硬件访问，必须通过本类的接口来实现
考虑到对硬件的访问的，既有来自UI模块，又有来自数据分析模块的访问，故而，本类将被设计为单例模式
即在本程序中，将会只有一份对象实例存在

此外，本类管理的每一个硬件，都将被放入一个独立的线程进行管理，防止用户操作的时候，由于硬件通讯阻塞，发生软件的卡顿和奔溃
"""


class Device(object):
    # 线程锁，防止多线程调用的时候，单例模式失效
    _instance_lock = threading.Lock()

    def __init__(self):
        """初始化构造"""

        # 读取参数
        self.__Parameter = ParameterMgr().GetParameter()

        # 创建五个电机控制线程，传参为（端口号，波特率，超时判定）
        self.__MotorStageX = StageCOM(
            self.__Parameter["motor_stage_x_port"],
            self.__Parameter["baud_rate"],
            self.__Parameter["time_out"]
        )
        self.__MotorStageY = StageCOM(
            self.__Parameter["motor_stage_y_port"],
            self.__Parameter["baud_rate"],
            self.__Parameter["time_out"]
        )
        self.__MotorStageZ = StageCOM(
            self.__Parameter["motor_stage_z_port"],
            self.__Parameter["baud_rate"],
            self.__Parameter["time_out"]
        )
        self.__MotorPump = PumpCOM(
            self.__Parameter["motor_pump_port"],
            self.__Parameter["baud_rate"],
            self.__Parameter["time_out"])
        self.__MotorFilter = FilterCOM(
            self.__Parameter["motor_filter_port"],
            self.__Parameter["baud_rate"],
            self.__Parameter["time_out"]
        )

        # 创建CCD控制线程

    def __new__(cls, *args, **kwargs):
        """单例模式，如果对象没有被实例化，构造一个，如果已被构造，那么直接返回该对象"""
        if not hasattr(Device, "_instance"):
            with Device._instance_lock:
                if not hasattr(Device, "_instance"):
                    Device._instance = object.__new__(cls)
        return Device._instance

    def MotorX(self):
        """访问X方向电机"""
        return self.__MotorStageX

    def MotorY(self):
        """访问X方向电机"""
        return self.__MotorStageY

    def MotorZ(self):
        """访问X方向电机"""
        return self.__MotorStageZ

    def Pump(self):
        """访问泵电机"""
        return self.__MotorPump

    def MotorFilter(self):
        """访问滤光片电机"""
        return self.__MotorFilter
