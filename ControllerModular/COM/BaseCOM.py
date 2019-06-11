# coding=utf8

import serial
import time
import serial.tools.list_ports
import threading
import binascii
from ControllerModular.InstructionsMgr.InstructionMgr import *
from ControllerModular.ReceiveMsgMgr.ReceiveMsgMgr import ReceiveMsgMgr

"""
本类为所有串口设备的控制基类，
主要实现：
    消息队列
    线程锁
    指令发送与监听机制等
"""


class BaseCOM(threading.Thread):
    # 安全锁
    __msg_lock = threading.Lock()

    def __init__(self, port, bps, timeout):
        """
            初始化方法, 用于指定本条线程管理哪一个串口
            参数：
                port：串口设备号
                bps：波特兰
                timeout：超时等待时间，单位为秒
        """

        # 调用父类初始化方法
        threading.Thread.__init__(self)

        # 初始化串口参数
        self.__serial_port = serial.Serial(port, bps, timeout=timeout)

        # 创建消息队列
        self.__msg_queue = []

        # 串口指令表
        self.__InstructionList = InstructionMgr().GetRS485InstructionsMap()

        # 串口返回值列表
        self.__ReceiveMsgList = ReceiveMsgMgr().GetParameter()

    def CreatInstruction(self, msg, parameters=[]):
        """解析串口指令"""

        # 获取指令格式
        if msg not in self.__InstructionList:
            return None
        InstructionTemplate = self.__InstructionList[msg][0]

        # 获取参数数量
        ParameterCount = len(self.__InstructionList[msg]) - 1
        if ParameterCount != len(parameters):
            return None

        # 循环遍历所有的参数
        for index, param in enumerate(parameters):
            # 获取该参数的合法值
            rangeList = self.__InstructionList[msg][index + 1]
            if param < rangeList[0] or param > rangeList[1]:
                return None

        # 生成指令
        Instruction = InstructionTemplate % tuple(parameters)

        return Instruction

    def SendMsg(self, msg, parameters=[]):
        """发送消息"""

        # 解析指令
        instruction = self.CreatInstruction(msg, parameters)

        # 容错，指令非法
        if instruction is None:
            return

        # 当需要发送数据的时候，先要判断消息队列是否在被操作（即是否有在发送数据）
        if BaseCOM.__msg_lock.acquire():
            # 将传来的消息转义，然后放入待发送的消息队列中
            self.__msg_queue.append(instruction)

            # 完成工作，将锁释放
            BaseCOM.__msg_lock.release()

    def ReceiveMsg(self):
        """监听串口，抓取返回值"""

        # 创建一个零时数据容器
        serialData = ""

        # 创建一个计数器
        count = 0

        # 循环监听，防止消息不全
        while True:
            # 读取串口数据
            serialData = serialData + str(binascii.b2a_hex(self.__serial_port.read_all()))

            # 如果读到数据尾了，或者超时退出
            if self.__ReceiveMsgList["tail"] in serialData or count > 60:
                break

            # 暂停0.1秒，并计数
            time.sleep(0.1)
            count = count + 1

        # 返回串口数据
        return serialData

    def ReceiveLongMsg(self):
        """监听串口，抓取长返回值"""

        # 创建一个零时数据容器
        serialData = ""

        # 创建一个计数器
        count = 0

        # 循环监听，防止消息不全
        while True:
            # 读取串口数据
            serialData = serialData + str(binascii.b2a_hex(self.__serial_port.read_all()))

            # 如果读到数据尾了，或者超时退出
            if self.__ReceiveMsgList["end"] in serialData:
                break

            # 超时控制
            if count > 600 and len(serialData) == 0:
                break

            # 暂停0.1秒，并计数
            time.sleep(0.1)
            count = count + 1

        # 返回串口数据
        return serialData

    def run(self):
        """线程将会循环执行本函数，可视为一个while True循环"""

        # 如果安全锁没有被打开，表示其他模块正在添加数据，阻塞，暂不执行动作
        if BaseCOM.__msg_lock.acquire():
            # 发送消息
            for instruction in self.__msg_queue:
                self.__serial_port.write(instruction)

            # 发送完消息之后，监听端口，抓取返回值
            self.ReceiveMsg()

            # 完成工作，将锁释放，并暂停0.1秒，防止线程冲突
            BaseCOM.__msg_lock.release()
            time.sleep(0.1)
