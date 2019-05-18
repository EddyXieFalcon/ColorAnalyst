# coding=utf8

import json
import serial
import serial.tools.list_ports
from PyQt5.QtWidgets import *
from UIModular.MainWindow.FunctionWidget.SamplingWidget.SamplingWidgetModify import SamplingWidgetModify
from UIModular.MainWindow.FunctionWidget.SamplingWidget.CommendDailog.CommendDailog import CommendDailog
from ControllerModular.InstructionsMgr.InstructionMgr import InstructionMgr


class SamplingWidget(SamplingWidgetModify):
    def __init__(self, parent=None):
        """构造方法"""

        # 父类构造方法
        super(SamplingWidget, self).__init__()

        # 准备对话框
        self.__commendDailog = CommendDailog()

        # 初始化状态
        self.InitStatus()

        # 串口连接的槽函数
        self.pushButton_connect.clicked.connect(self.on_pushbutton_connect_clicked_slot)

        # 五个安娜牛的槽函数
        self.pushButton_load.clicked.connect(self.on_pushbutton_load_clicked_slot)
        self.pushButton_export.clicked.connect(self.on_pushbutton_export_clicked_slot)
        self.pushButton_add.clicked.connect(self.on_pushbutton_add_clicked_slot)
        self.pushButton_remove.clicked.connect(self.on_pushbutton_remove_clicked_slot)
        self.pushButton_edit.clicked.connect(self.on_pushbutton_edit_clicked_slot)
        self.pushButton_DoIt.clicked.connect(self.on_pushbutton_Doit_clicked_slot)

    def InitStatus(self):
        """初始化状态，所有的按钮不可用"""

        self.pushButton_connect.setText("Connect")

        self.pushButton_connect.setEnabled(True)
        self.pushButton_scan.setEnabled(False)

        self.comboBox_connect.setEnabled(False)
        self.comboBox_scan.setEnabled(False)

        self.pushButton_load.setEnabled(False)
        self.pushButton_export.setEnabled(False)
        self.pushButton_add.setEnabled(False)
        self.pushButton_remove.setEnabled(False)
        self.pushButton_edit.setEnabled(False)
        self.pushButton_DoIt.setEnabled(False)

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
        print(port_list)

        if len(port_list) <= 0:
            print("The Serial port can't find!")
        else:
            port_list_0 = list(port_list[0])
            port_serial = port_list_0[0]
            ser = serial.Serial(port_serial, 9600, timeout=60)
            print("check which port was really used >", ser.name)

    def on_pushbutton_load_clicked_slot(self):
        """加载文件"""

        # 打开一个实验脚本
        (file_path, file_type) = QFileDialog.getOpenFileName(self, u"选择一个实验脚本", u"C:/", u"实验脚本(*.json)")

        # 容错判断
        if file_path is None or file_type != "json":
            return

        # 加载脚本
        self.load_experiment_script(file_path)

    def on_pushbutton_export_clicked_slot(self):
        """导出实验"""

        # 获取文件保存路径
        file_path = QFileDialog.getSaveFileName(self, u"保存文件", u"C:/", "实验脚本(*.json)")

        # 容错判断
        if file_path is None:
            return

        # 加载脚本
        self.export_experiment_script(file_path)

        # 创建实验数据结构
        script = []
        count = self.tableWidget.rowCount()
        for index in range(count):
            step = {}
            step["instructions"] = self.tableWidget.item(index, 0).text()
            step["parameter"] = self.tableWidget.item(index, 1).text()
            step["volume"] = self.tableWidget.item(index, 2).text()
            step["volume"] = self.tableWidget.item(index, 3).text()

        # 将数据转成文件
        with open(file_path, "w") as jsonFile:
            try:
                json.dump(script, jsonFile)
            except:
                QMessageBox.warning(self, u"加载实验文件", u"文件非法", QMessageBox.Ok)

    def on_pushbutton_add_clicked_slot(self):
        """添加命令"""

        # 弹出对话框，要求为配置输入一个名称
        self.__commendDailog.show()

        # 对话框按钮数据流方向
        self.__commendDailog.selectedInstruction.disconnect(self.editInstructionToTableWidget)
        self.__commendDailog.selectedInstruction.connect(self.addInstructionToTableWidget)

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
        self.__commendDailog.show()

        # 对话框按钮数据流方向
        self.__commendDailog.selectedInstruction.disconnect(self.addInstructionToTableWidget)
        self.__commendDailog.selectedInstruction.connect(self.editInstructionToTableWidget)

    def on_pushbutton_Doit_clicked_slot(self):
        """执行脚本"""
        
        # 获取表格中的行数
        rowCount = self.tableWidget.rowCount()
        if rowCount <= 0:
            return

        # 依次执行列表中的命令
        for index in range(rowCount):
            # 获取文本
            commend = self.tableWidget.item(index, 0).text()
            parameter1 = self.tableWidget.item(index, 1).text()
            parameter2 = self.tableWidget.item(index, 2).text()
            parameter3 = self.tableWidget.item(index, 3).text()

            # 合成指令
            instruction = commend % (parameter1, parameter2, parameter3)

            # 发送指令

            # 监听返回值
            returnMessage = ""

            # 选中当前行
            self.tableWidget.setCurrentRow(index)

            # 设置返回值到界面
            self.tableWidget.setItem(index, 4, QTableWidgetItem(returnMessage))

        # 取消选中
        self.tableWidget.setCurrentRow(-1)

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
            self.tableWidget.item(index, 0).setText(script[index]["instructions"])
            self.tableWidget.item(index, 1).setText(script[index]["parameter"])
            self.tableWidget.item(index, 2).setText(script[index]["volume"])
            self.tableWidget.item(index, 3).setText(script[index]["volume"])

    def addInstructionToTableWidget(self, instruction):
        """添加指令"""

        # 容错
        instructionlist = InstructionMgr().GetParameter()
        if instruction not in instructionlist:
            return

        # 添加指令到界面
        rowCount = self.tableWidget.rowCount()
        self.tableWidget.setRowCount(rowCount + 1)
        self.tableWidget.setItem(rowCount, 0, QTableWidgetItem(instruction))

    def editInstructionToTableWidget(self, instruction):
        """修改命令"""

        self.tableWidget.setItem(self.tableWidget.currentRow(), 0, QTableWidgetItem(instruction))
