# coding=utf8

from PyQt5 import QtWidgets
from UIModular.MainWindow.StatusBarWidget.StatusBarWidgetUI import Ui_StatusBarWidget


class StatusBarWidgetModify(QtWidgets.QWidget, Ui_StatusBarWidget):
    def __init__(self, parent=None):
        """构造方法"""

        # 父类方法
        QtWidgets.QWidget.__init__(self, parent)

        # 创建界面
        self.setupUi(self)  # 创建界面