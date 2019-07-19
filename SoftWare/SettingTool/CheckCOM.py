# coding=utf-8

import serial
import serial.tools.list_ports

"""
本类用于提供一个检测串口设备的类
"""


class CheckCOM(object):
    def __int__(self):
        """初始化方法"""

        # 扫描当前系统连接的所有的串口设备号
        self.__port_list = list(serial.tools.list_ports.comports())

    def CheckOut(self):
        """判断当前的设备是否正常"""

        # 如果没有扫描到任何设备
        if len(self.__port_list) <= 0:
            print("The Serial port can't find!")
            return False
        # 如果扫描到的设备数量不对
        elif len(self.__port_list) < 6:
            print("Some Serial port can't find!")
            return False
        # 如果扫描到的设备正确
        else:
            port_list_0 = list(self.__port_list[0])
            port_serial = port_list_0[0]
            ser = serial.Serial(port_serial, 9600, timeout=60)
            print("check which port was really used >", ser.name)
            return True
