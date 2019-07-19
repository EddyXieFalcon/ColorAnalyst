# coding=utf8

import os
from PyQt5 import QtWidgets
from SoftWare.UIModular.MainWindow.FunctionWidget.ProtocolsWidget.PlateLayoutWidget.PlateLayoutWidgetUI import Ui_PlateLayoutWidget


class PlateLayoutWidgetModify(QtWidgets.QWidget, Ui_PlateLayoutWidget):
    def __init__(self, parent=None):
        """构造方法"""

        # 父类方法
        QtWidgets.QWidget.__init__(self, parent)

        # 创建界面
        self.setupUi(self)  # 创建界面

        # 获取资源路径
        self.__resourcePath = os.path.dirname(os.path.realpath(__file__)).replace("UIModular", "UIResource")
