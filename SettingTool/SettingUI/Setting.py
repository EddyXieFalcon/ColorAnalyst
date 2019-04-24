# coding=utf8

from PyQt5 import QtWidgets
from PyQt5.QtCore import pyqtSlot
from SettingTool.SettingUI.SettingUI import Ui_Setting


class Setting(QtWidgets.QWidget, Ui_Setting):
    def __init__(self, parent=None):
        """构造方法"""

        # 父类方法
        QtWidgets.QWidget.__init__(self, parent)

        # 创建界面
        self.setupUi(self)  # 创建界面
