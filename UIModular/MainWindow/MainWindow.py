# coding=utf8

from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QFileDialog, QInputDialog, QLineEdit, QTableWidgetItem
from PyQt5.QtCore import pyqtSlot
from UIModular.MainWindow.MainWindowUI import Ui_MainWindow


class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        """构造方法"""

        # 父类方法
        QtWidgets.QWidget.__init__(self, parent)

        # 创建界面
        self.setupUi(self)  # 创建界面
