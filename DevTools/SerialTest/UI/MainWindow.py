# coding=utf8

import serial
import serial.tools.list_ports

from PyQt5 import QtWidgets
from PyQt5.QtCore import pyqtSlot
from DevTools.SerialTest.UI.MainWindowUI import Ui_MainWindow
from DevTools.SerialTest.Commend.Commend import Commend


class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        """构造方法"""

        # 父类构造方法
        super(MainWindow, self).__init__()

        # 串口通讯对象
        self.__serial = None
        # 串口命令对象
        self.__commend = Commend()
        # 创建界面
        self.setupUi(self)  # 创建界面
        # 初始化动作
        # self.InitStatus()

        # 扫描按钮
        self.btnScan.clicked.connect(self.OnBtnScanClickedSlot)
        # 连接按钮
        self.btnConnect.clicked.connect(self.OnBtnConnectClickedSlot)
        # 发送按钮
        self.btnSend.clicked.connect(self.OnBtnSendClickedSlot)

    def InitStatus(self):
        """界面启动初始化动作"""
        self.btnConnect.setEnabled(False)
        self.SetSendFunctionEnable(False)
        self.SetRecvFunctionEnable(False)

    def InitSerial(self):
        """串口通信初始化"""
        # 断开串口
        if self.__serial is None:
            return
        if self.__serial.isOpen():
            self.__serial.close()
            self.__serial = None

    def ConnectSerial(self):
        """连接串口"""
        if self.comboBox.count() == 0:
            self.statusbar.showMessage("串口连接失败！！！")
            self.__serial = None
            return
        serial = self.comboBox.currentText()
        self.__serial = serial.Serial(serial, 115200, timeout=0.1)

    def SetSendFunctionEnable(self, isEnabled):
        """设置发送功能是否能够使用"""
        self.lineEditSendCtrlAddr.setEnabled(isEnabled)
        self.lineEditSendCmdType.setEnabled(isEnabled)
        self.lineEditSendFunCode.setEnabled(isEnabled)
        self.lineEditSendParam1.setEnabled(isEnabled)
        self.lineEditSendParam2.setEnabled(isEnabled)
        self.lineEditSendCeckCode.setEnabled(isEnabled)
        self.btnSend.setEnabled(isEnabled)

    def SetRecvFunctionEnable(self, isEnabled):
        """设置发送功能是否能够使用"""
        self.lineEditRecvCtrlAddr.setEnabled(isEnabled)
        self.lineEditRecvCmdType.setEnabled(isEnabled)
        self.lineEditRecvFunCode.setEnabled(isEnabled)
        self.lineEditRecvParam1.setEnabled(isEnabled)
        self.lineEditRecvParam2.setEnabled(isEnabled)
        self.lineEditRecvCeckCode.setEnabled(isEnabled)
        self.lineEditErrorCode.setEnabled(isEnabled)
        self.lineEditLimitTime.setEnabled(isEnabled)
        self.lineEditTimeCount.setEnabled(isEnabled)

    @pyqtSlot()
    def OnBtnScanClickedSlot(self):
        """扫描所有的串口，并放入下拉菜单"""
        # 清空下拉菜单
        self.comboBox.clear()

        # 清空状态栏消息
        self.statusbar.showMessage("")

        # 获取所有的串口设备号
        port_list = list(serial.tools.list_ports.comports())

        # 容错，并提示
        if len(port_list) == 0:
            self.statusbar.showMessage("搜索不到任何串口设备！！！")
            return

        # 解析设备，在下拉菜单中显示
        for port_info in port_list:
            # 获取单个串口的相关信息列表
            port_info_list = list(port_info)
            # 获取该串口的链接名称
            port_serial = port_info_list[0]
            # 将串口名称放入下拉菜单中
            self.comboBox.addItem(port_serial)

        # 连接按钮功能可用
        self.btnConnect.setEnabled(True)

        # 禁用功能，等待连接
        self.SetSendFunctionEnable(False)
        self.SetRecvFunctionEnable(False)

    @pyqtSlot()
    def OnBtnConnectClickedSlot(self):
        """连接按钮点击槽函数"""
        # 如果当前处于断开状态
        if self.btnConnect.text() == "连接":
            # 断开串口
            self.InitSerial()
            # 连接串口
            self.ConnectSerial()
            # 判断是否连接成功
            if self.__serial is not None and self.__serial.isOpen():
                # 反转状态
                self.btnConnect.setText("断开")
                self.SetSendFunctionEnable(True)
                self.SetRecvFunctionEnable(True)
        # 如果当前处于连接状态
        else:
            # 关闭串口
            self.InitSerial()
            # 反转状态
            self.btnConnect.setText("连接")
            self.SetSendFunctionEnable(False)
            self.SetRecvFunctionEnable(False)

    @pyqtSlot()
    def OnBtnSendClickedSlot(self):
        """发送信息按钮"""
        # 容错
        if self.__serial is None or not self.__serial.isOpen():
            self.statusbar.showMessage("请重新连接串口！！！")
            return

        # 获取发送码, todo


