# coding=utf8

from PyQt5 import QtWidgets
from UIModular.MainWindow.FunctionWidget.ProtocolsWidget.AnalytesWidget.AnalytesWidgetUI import Ui_AnalytesWidget


class AnalytesWidgetModify(QtWidgets.QWidget, Ui_AnalytesWidget):
    def __init__(self, parent=None):
        """构造方法"""

        # 父类方法
        QtWidgets.QWidget.__init__(self, parent)

        # 创建界面
        self.setupUi(self)  # 创建界面
