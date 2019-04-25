# coding=utf8

from PyQt5 import QtWidgets
from UIModular.MainWindow.FunctionWidget.ProtocolsWidget.ProtocolsWidgetUI import Ui_ProtocolsWidget


class ProtocolsWidgetModify(QtWidgets.QWidget, Ui_ProtocolsWidget):
    def __init__(self, parent=None):
        """构造方法"""

        # 父类方法
        QtWidgets.QWidget.__init__(self, parent)

        # 创建界面
        self.setupUi(self)  # 创建界面
