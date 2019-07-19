# coding=utf8

from PyQt5 import QtWidgets
from DevTools.SerialTest.UI.MainWindowUI import Ui_MainWindow


class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        """构造方法"""

        # 父类构造方法
        super(MainWindow, self).__init__()

        # 创建界面
        self.setupUi(self)  # 创建界面

