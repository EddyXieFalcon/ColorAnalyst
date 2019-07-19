# coding=utf8

import sys
from PyQt5.QtWidgets import QApplication
from PyQt5 import QtWidgets
from SoftWare.SettingTool.SettingUI import Ui_Setting


class Setting(QtWidgets.QWidget, Ui_Setting):
    def __init__(self, parent=None):
        """构造方法"""

        # 父类方法
        QtWidgets.QWidget.__init__(self, parent)

        # 创建界面
        self.setupUi(self)  # 创建界面


if __name__ == '__main__':
    # 创建事件
    app = QApplication(sys.argv)

    # 创建ui
    ui = Setting()

    # 显示ui界面
    # ui.showMaximized()
    ui.show()

    # 进入消息循环
    sys.exit(app.exec_())