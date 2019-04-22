# coding=utf8

import serial
import serial.tools.list_ports
import threading
import time
import binascii, re


class COM(object):
    def __init__(self):
        """初始化方法"""

        # 调用父类初始化方法
        super().__init__()

        # 初始化所有的变量
        self.__isOccupy = False  # 全局锁，判断是否有别的对象再进行串口调用
        self.__isDetectSerialPort = False   # 是否已经查找过COM口
        self.__msgQueue = []  # 消息队列

        # 执行初始化行为
        self.detectSerialPort()  # 查找串口

    def detectSerialPort(self):
        """检测串口"""

        # 如果没有检测到串口，为串口控制创建一条线程，并将串口连接标识设置为true
        if not self.__isDetectSerialPort:
            # 已经查找过串口
            self.__isDetectSerialPort = True

            # 查找连接串口，将查找方法放入一个线程
            t = threading.Thread(target=self.detectSerialPortProcess)
            t.setDaemon(True)
            t.start()

    def detectSerialPortProcess(self):
        """连接串口"""

        pass
        # # 循环握手连接
        # while True:
        #
        #     # 查询所有的串口信息，汇成列表
        #     portList = self.findSerialPort()
        #
        #     # 如果列表有内容，才进行判断
        #     if len(portList) > 0:
        #         # 从下拉列表菜单中获取一个串口名
        #         currText = self.serialPortCombobox.currentText()
        #         # 清空下拉列表
        #         self.serialPortCombobox.clear()
        #         # 遍历列表内从容
        #         for i in portList:
        #             # 拼接列表内容
        #             showStr = str(i[0]) + " " + str(i[1])
        #             self.serialPortCombobox.addItem(showStr)
        #         index = self.serialPortCombobox.findText(currText)
        #         if index >= 0:
        #             self.serialPortCombobox.setCurrentIndex(index)
        #         else:
        #             self.serialPortCombobox.setCurrentIndex(0)
        #         break
        #     time.sleep(1)
        # self.showSerialComboboxSignal.emit()
        # self.isDetectSerialPort = False


SingletonCOM = COM()
