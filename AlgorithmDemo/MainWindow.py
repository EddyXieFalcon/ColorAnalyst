# coding=utf8

import sys
import pims
import numpy as np
import pandas as pd
import trackpy as tp
from PyQt5 import QtWidgets, QtGui
from AlgorithmDemo.MainWindowUI import Ui_MainWindow
from pandas import DataFrame, Series  # for convenience


class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        """构造方法"""

        # 父类构造方法
        super(MainWindow, self).__init__()

        # 创建界面
        self.setupUi(self)  # 创建界面

        # 前置工作
        self.__pictrureName = None  # jpg图片
        self.__image = QtGui.QImage()  # 图片对象
        self.__pixmap = QtGui.QPixmap()  # 图片像素集对象
        self.__pixmapItem = QtWidgets.QGraphicsPixmapItem()  # 图片图元
        self.__scene = QtWidgets.QGraphicsScene()  # 创建视口的场景
        self.graphicsView.setScene(self.__scene)  # 将视口与场景绑定

        # 两个按钮的执行
        self.btnLoad.clicked.connect(self.OnBtnLoadClickedSlot)
        self.btnAnalyst.clicked.connect(self.OnBtnAnalystClickedSlot)

    def OnBtnLoadClickedSlot(self):
        """点击加载按钮"""

        # 获取打开的文件
        self.__pictrureName, type = QtWidgets.QFileDialog.getOpenFileName(self, u"打开文件", "./", "Image Files(*.jpg)")
        if len(self.__pictrureName) == 0:
            return

        # 加载文件
        self.__image = QtGui.QImage(self.__pictrureName)

        # 显示图片
        self.__pixmap = QtGui.QPixmap.fromImage(self.__image)
        self.__pixmapItem.setPixmap(self.__pixmap)
        self.__scene.setSceneRect(0, 0, self.__image.width(), self.__image.height())
        self.__scene.addItem(self.__pixmapItem)
        self.graphicsView.show()

    def OnBtnAnalystClickedSlot(self):
        """点击加载按钮"""

        # 容错
        if self.__pictrureName is None or len(self.__pictrureName) == 0:
            return

        # 加载图片
        frames = pims.ImageSequence('../sample_data/bulk_water/*.png', as_grey=True)

        #

def main():
    # 创建事件
    app = QtWidgets.QApplication(sys.argv)

    # 创建ui
    ui = MainWindow()

    # 显示ui界面
    ui.showMaximized()
    # ui.show()

    # 进入消息循环
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
