# coding=utf8

import time
import json
import serial
import serial.tools.list_ports
from PyQt5.QtWidgets import *
from UIModular.MainWindow.FunctionWidget.SamplingWidget.SamplingWidgetModify import SamplingWidgetModify
from UIModular.MainWindow.FunctionWidget.SamplingWidget.CommendDailog.CommendDailog import CommendDailog
from ControllerModular.InstructionsMgr.InstructionMgr import RS485InstructionMgr


class SamplingWidget(SamplingWidgetModify):
    def __init__(self, parent=None):
        """构造方法"""

        # 父类构造方法
        super(SamplingWidget, self).__init__()

        # 当前控制的串口
        self.__serial = None

        # 准备对话框
        self.__commendDailogForAdd = CommendDailog()
        self.__commendDailogForEdit = CommendDailog()

        # 对话框按钮数据流方向
        self.__commendDailogForAdd.selectedInstruction.connect(self.addInstructionToTableWidget)
        self.__commendDailogForEdit.selectedInstruction.connect(self.editInstructionToTableWidget)

        # 初始化状态
        self.InitStatus()

        # 串口连接的槽函数
        self.pushButton_connect.clicked.connect(self.on_pushbutton_connect_clicked_slot)

        # “连接”下拉菜单的槽
        self.comboBox_connect.currentTextChanged.connect(self.on_comboBox_currentTextChanged_slot)

        # 串口扫描的槽函数
        self.pushButton_scan.clicked.connect(self.on_pushbutton_scan_clicked_slot)

        # 五个按钮的槽函数
        self.pushButton_load.clicked.connect(self.on_pushbutton_load_clicked_slot)
        self.pushButton_export.clicked.connect(self.on_pushbutton_export_clicked_slot)
        self.pushButton_add.clicked.connect(self.on_pushbutton_add_clicked_slot)
        self.pushButton_remove.clicked.connect(self.on_pushbutton_remove_clicked_slot)
        self.pushButton_edit.clicked.connect(self.on_pushbutton_edit_clicked_slot)
        self.pushButton_DoIt.clicked.connect(self.on_pushbutton_Doit_clicked_slot)

    def InitStatus(self):
        """初始化状态，所有的按钮不可用"""

        # 隐藏进度条
        self.progressBar.hide()

        # 设置“连接”按钮文本
        self.pushButton_connect.setText("Connect")

        # 关闭“连接”按钮
        self.comboBox_connect.setEnabled(False)
        self.comboBox_connect.clear()

        # 关闭“扫描”按钮
        self.comboBox_scan.setEnabled(False)
        self.comboBox_scan.clear()

        # 关闭控制按钮
        self.pushButton_load.setEnabled(False)
        self.pushButton_export.setEnabled(False)
        self.pushButton_add.setEnabled(False)
        self.pushButton_remove.setEnabled(False)
        self.pushButton_edit.setEnabled(False)
        self.pushButton_DoIt.setEnabled(False)

        # 断开串口链接
        if self.__serial is not None and self.__serial.isOpen():
            self.__serial.close()
            self.__serial = None

    def InitSerial(self):
        """串口通信初始化"""

        # 断开串口
        if self.__serial is not None and self.__serial.isOpen():
            self.__serial.close()

        # 隐藏进度条
        self.progressBar.hide()

        # 清空下拉菜单
        self.comboBox_scan.clear()

        # 禁用
        self.comboBox_scan.setEnabled(False)

    def on_pushbutton_connect_clicked_slot(self):
        """连接按钮，刷新串口列表"""

        # 如果处于初始状态，刷新
        if self.pushButton_connect.text() == "Connect":
            # 刷新列表
            self.ReflashComList()
        # 否则，回归初始化
        else:
            self.InitStatus()

    def ReflashComList(self):
        """扫描串口列表"""
        
        # 获取所有的串口设备号
        port_list = list(serial.tools.list_ports.comports())

        # 没有获取设备号
        if len(port_list) <= 0:
            QMessageBox.warning(self, "警告", "没有连接设备！！！", QMessageBox.Yes)
        # 判断有设备
        else:
            # 解析设备
            for port_info in port_list:
                # 获取单个串口的相关信息列表
                port_info_list = list(port_info)
                # 获取该串口的链接名称
                port_serial = port_info_list[0]
                # 将串口名称放入下拉菜单中
                self.comboBox_connect.addItem(port_serial)

            # 打开串口选择下拉菜单框
            self.comboBox_connect.setEnabled(True)

            # 连接按钮反转状态
            self.pushButton_connect.setText("Disconnect")

    def on_pushbutton_scan_clicked_slot(self):
        """扫描按钮，对选中的串口发起链接通讯"""

        # 串口通信初始化
        self.InitSerial()

        # 获取用户选择的串口名称
        port_serial = self.comboBox_connect.currentText()

        # 创建链接
        if not len(port_serial):
            return
        self.__serial = serial.Serial(port_serial, 115200, timeout=0.1)

        # 隐藏下拉菜单，显示进度条
        self.comboBox_scan.hide()
        self.progressBar.show()

        # 循环遍历1-32个
        for id in range(1, 33):
            # 发送握手
            msg = "%s hsk\n" % id
            self.__serial.write(msg.encode("utf-8"))

            # 读取反馈
            result = self.__serial.read(28)

            # 如果有反馈，将id加入下拉菜单
            if len(result) != 0:
                # 将id放入下拉菜单
                self.comboBox_scan.addItem(str(id))

            # 设置进度
            self.progressBar.setValue(100 * id / 32)

        # 隐藏进度条，显示下拉菜单
        self.progressBar.hide()
        self.comboBox_scan.show()

        # 如果扫描到设备，下拉菜单可用
        if self.comboBox_scan.count():
            # 下拉菜单可用
            self.comboBox_scan.setEnabled(True)

            # 打开所有的控制按钮
            self.pushButton_load.setEnabled(True)
            self.pushButton_export.setEnabled(True)
            self.pushButton_add.setEnabled(True)
            self.pushButton_remove.setEnabled(True)
            self.pushButton_edit.setEnabled(True)
            self.pushButton_DoIt.setEnabled(True)

    def on_pushbutton_load_clicked_slot(self):
        """加载文件"""

        # 打开一个实验脚本
        (file_path, file_type) = QFileDialog.getOpenFileName(self, u"选择一个实验脚本", u"C:/", u"实验脚本(*.json)")

        # 容错判断
        if file_path is None or "json" not in file_type:
            return

        # 加载脚本
        self.load_experiment_script(file_path)

    def on_pushbutton_export_clicked_slot(self):
        """导出实验"""

        # 获取文件保存路径
        (file_path, file_type) = QFileDialog.getSaveFileName(self, u"保存文件", u"C:/", "实验脚本(*.json)")

        # 容错判断
        if file_path is None:
            return

        # 创建实验数据结构
        script = {}
        count = self.tableWidget.rowCount()
        for index in range(count):
            # 单条指令
            instrction = []

            # 读取指令表格数据
            for i in range(4):
                if self.tableWidget.item(index, i) is not None:
                    instrction.append(self.tableWidget.item(index, i).text())
                else:
                    instrction.append("")

            # 放入指令
            script[index] = instrction

        # 将数据转成文件
        with open(file_path, "w") as jsonFile:
            try:
                json.dump(script, jsonFile)
            except:
                QMessageBox.warning(self, u"加载实验文件", u"文件非法", QMessageBox.Ok)

    def on_pushbutton_add_clicked_slot(self):
        """添加命令"""

        # 弹出对话框，要求为配置输入一个名称
        self.__commendDailogForAdd.show()

    def on_pushbutton_remove_clicked_slot(self):
        """删除命令"""

        # 判断当前是否有选中的行
        rowIndex = self.tableWidget.currentRow()
        if rowIndex < 0:
            return

        # 删除行
        self.tableWidget.removeRow(rowIndex)

    def on_pushbutton_edit_clicked_slot(self):
        """编辑命令"""

        # 判断当前是否有选中的行
        rowIndex = self.tableWidget.currentRow()
        if rowIndex < 0:
            return

        # 弹出对话框，要求为配置输入一个名称
        self.__commendDailogForEdit.show()

    def on_pushbutton_Doit_clicked_slot(self):
        """执行脚本"""
        
        # 获取表格中的行数
        rowCount = self.tableWidget.rowCount()
        if rowCount <= 0:
            return

        # 依次执行列表中的命令
        for index in range(rowCount):

            # 获取指令
            msg = self.tableWidget.item(index, 0).text()
            commend = RS485InstructionMgr().GetRS485InstructionsMap()[msg]

            # 解析指令
            instruction = commend[0]

            # 判断有几个参数
            paraNum = len(commend) - 1

            # 为指令添加参数
            paraList = []
            for num in range(paraNum):
                # 获取参数
                if self.tableWidget.item(index, num + 1) is not None:
                    parameter = self.tableWidget.item(index, num + 1).text()
                else:
                    parameter = '0'

                # 判断添加的参数是否合法，如果不合法，自动转换为最小值
                try:
                    value = float(parameter)
                    assert (value >= commend[num + 1][0] and value <= commend[num + 1][1])
                except:
                    parameter = str(commend[num + 1][0])
                    self.tableWidget.setItem(index, num + 1, QTableWidgetItem(parameter))

                # 放入参数
                paraList.append(parameter)

            # 合成指令
            if paraNum > 0:
                instruction = instruction % tuple(paraList)
            instruction = self.comboBox_scan.currentText() + " " + instruction

            # 发送指令
            self.__serial.write(instruction.encode("utf-8"))

            # 选中当前行
            self.tableWidget.setCurrentCell(index, 0)

            # 监听返回值
            returnMessage = self.__serial.read(128)

            # 设置返回值到界面
            self.tableWidget.setItem(index, 4, QTableWidgetItem(str(returnMessage)))

    def load_experiment_script(self, filePath):
        """加载已保存的1实验脚本"""

        # 准备数据容器
        script = []

        # 尝试打开实验脚本文件
        try:
            with open(filePath, 'r') as jsonFile:
                script = json.load(jsonFile)
        except:
            QMessageBox.warning(self, u"加载实验文件", u"文件非法", QMessageBox.Ok)

        # 加载数据
        self.tableWidget.clearContents()
        self.tableWidget.setRowCount(len(script))
        for index in range(len(script)):
            self.tableWidget.setItem(index, 0, QTableWidgetItem(script[str(index)][0]))
            self.tableWidget.setItem(index, 1, QTableWidgetItem(script[str(index)][1]))
            self.tableWidget.setItem(index, 2, QTableWidgetItem(script[str(index)][2]))
            self.tableWidget.setItem(index, 3, QTableWidgetItem(script[str(index)][3]))

    def addInstructionToTableWidget(self, instruction):
        """添加指令"""

        # 容错
        instructionlist = RS485InstructionMgr().GetRS485InstructionsMap()
        if instruction not in instructionlist:
            return

        # 添加指令到界面
        rowCount = self.tableWidget.rowCount()
        self.tableWidget.setRowCount(rowCount + 1)
        self.tableWidget.setItem(rowCount, 0, QTableWidgetItem(instruction))

    def editInstructionToTableWidget(self, instruction):
        """修改命令"""

        self.tableWidget.setItem(self.tableWidget.currentRow(), 0, QTableWidgetItem(instruction))

    def on_comboBox_currentTextChanged_slot(self):
        """连接下来菜单的槽函数"""

        # 关闭“扫描”按钮
        self.comboBox_scan.clear()

        # 关闭控制按钮
        self.pushButton_load.setEnabled(False)
        self.pushButton_export.setEnabled(False)
        self.pushButton_add.setEnabled(False)
        self.pushButton_remove.setEnabled(False)
        self.pushButton_edit.setEnabled(False)
        self.pushButton_DoIt.setEnabled(False)

        # 断开串口链接
        if self.__serial is not None and self.__serial.isOpen():
            self.__serial.close()
            self.__serial = None
