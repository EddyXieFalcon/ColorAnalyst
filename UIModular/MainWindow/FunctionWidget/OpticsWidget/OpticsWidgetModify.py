# coding=utf8

import os, sys
from PyQt5 import QtWidgets
from PyQt5.QtCore import pyqtSlot
from UIModular.MainWindow.FunctionWidget.OpticsWidget.OpticsWidgetUI import Ui_OpticsWidget
from ControllerModular.Device import Device


class OpticsWidgetModify(QtWidgets.QWidget, Ui_OpticsWidget):
    def __init__(self, parent=None):
        """构造方法"""

        # 父类方法
        QtWidgets.QWidget.__init__(self, parent)

        # 创建界面
        self.setupUi(self)  # 创建界面

        # 获取资源路径
        self.__resourcePath = os.path.dirname(os.path.realpath(__file__)).replace("UIModular", "UIResource")
