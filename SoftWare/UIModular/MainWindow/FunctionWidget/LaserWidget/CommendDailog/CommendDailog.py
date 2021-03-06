# coding=utf8

from PyQt5.QtCore import pyqtSignal
from SoftWare.UIModular.MainWindow.FunctionWidget.LaserWidget.CommendDailog.CommendDailogModify import CommendDailogModify
from SoftWare.ControllerModular.InstructionsMgr.InstructionMgr import LaserInstructionMgr


class CommendDailog(CommendDailogModify):
    selectedInstruction = pyqtSignal(str)

    def __init__(self, parent=None):
        """构造方法"""

        # 父类构造方法
        super(CommendDailog, self).__init__()

        # 将所有的选项放入列表中
        self.__instructionDict = LaserInstructionMgr().GetLaserInstructionsMap()
        for instruction in self.__instructionDict:
            self.comboBox.addItem(instruction)

        # 取消按钮
        self.pushButton_cancel.clicked.connect(self.onPushButtonCancelClickedSlot)

        # 确定按钮
        self.pushButton_ok.clicked.connect(self.onPushButtonOKClickedSlot)

    def onPushButtonCancelClickedSlot(self):
        """点击取消按钮的时候，关闭窗口"""
        self.close()

    def onPushButtonOKClickedSlot(self):
        """点击确定按钮的时候，返回数据"""
        self.selectedInstruction.emit(self.comboBox.currentText())
        self.close()
