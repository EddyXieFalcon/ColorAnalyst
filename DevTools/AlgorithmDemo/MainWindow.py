# coding=utf8

import xlwt
import xlrd
import sys
import pims
import numpy as np
import pandas as pd
import trackpy as tp
import matplotlib as mpl
import matplotlib.pyplot as plt
from PyQt5 import QtWidgets, QtGui
from MainWindowUI import Ui_MainWindow
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

        # 按钮的执行
        self.btnLoad.clicked.connect(self.OnBtnLoadClickedSlot)

        self.btnImport.clicked.connect(self.OnBtnImportClickedSlot)
        self.btnExport.clicked.connect(self.OnBtnExportClickedSlot)
        self.btnAdd.clicked.connect(self.OnBtnAddClickedSlot)
        self.btnRemove.clicked.connect(self.OnBtnRemoveClickedSlot)
        self.btnAnalystOne.clicked.connect(self.OnBtnAnalystOneClickedSlot)
        self.btnAnalystAll.clicked.connect(self.OnBtnAnalystAllClickedSlot)

    def OnBtnLoadClickedSlot(self):
        """点击加载按钮"""

        # 获取打开的文件
        self.__pictrureName, type = QtWidgets.QFileDialog.getOpenFileName(self, u"打开文件", "./", "Image Files(*.png)")
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

    def OnBtnImportClickedSlot(self):
        """导入Excel表"""

        # 获取打开的文件
        ExcelName, type = QtWidgets.QFileDialog.getOpenFileName(self, u"打开文件", "./", "Excel Files(*.xlsx *.xls)")
        if len(ExcelName) == 0:
            return

        # 解析文件数据表
        file = xlrd.open_workbook(ExcelName)
        sheet_names = file.sheet_names()
        sheet = file.sheet_by_name(sheet_names[0])
        parameters = sheet.get_rows()

        # 将数据放入界面
        for row, values in enumerate(parameters):
            # 第一行标题数据舍弃
            if 0 == row:
                continue
            # 显示数据
            self.tableWidget.setRowCount(row)
            for col, value in enumerate(values):
                value = str(value).split(":")[-1]
                self.tableWidget.setItem(row - 1, col, QtWidgets.QTableWidgetItem(value))

    def OnBtnExportClickedSlot(self):
        """导出Excel"""

        # 获取文件保存路径
        (file_path, file_type) = QtWidgets.QFileDialog.getSaveFileName(self, u"保存文件", u"./", "Excel Files(*.xlsx *.xls)")

        # 容错判断
        if file_path is None:
            return

        # 获取每一行数据
        file = xlwt.Workbook()
        sheet = file.add_sheet('Sheet1')
        rowCount = self.tableWidget.rowCount()
        sheet.write(0, 0, 'diameter')
        sheet.write(0, 1, 'minmass')
        sheet.write(0, 2, 'maxsize')
        sheet.write(0, 3, 'separation')
        sheet.write(0, 4, 'noise_size')
        sheet.write(0, 5, 'smoothing_size')
        sheet.write(0, 6, 'threshold')
        sheet.write(0, 7, 'invert')
        sheet.write(0, 8, 'percentile')
        sheet.write(0, 9, 'topn')
        sheet.write(0, 10, 'preprocess')
        sheet.write(0, 11, 'max_iterations')
        sheet.write(0, 12, 'filter_before')
        sheet.write(0, 13, 'filter_after')
        sheet.write(0, 14, 'characterize')
        for row in range(rowCount):
            for col in range(15):
                sheet.write(row + 1, col, self.tableWidget.item(row, col).text())

        # 保存数据
        file.save(file_path)

    def OnBtnAddClickedSlot(self):
        """新加一行"""

        # 新加一行
        rowCount = self.tableWidget.rowCount()
        if rowCount <= 0:
            self.tableWidget.setRowCount(1)
        else:
            self.tableWidget.setRowCount(rowCount + 1)

        # 添加默认数据
        self.tableWidget.setItem(rowCount, 0, QtWidgets.QTableWidgetItem("11"))
        self.tableWidget.setItem(rowCount, 1, QtWidgets.QTableWidgetItem("1.0"))
        self.tableWidget.setItem(rowCount, 2, QtWidgets.QTableWidgetItem("1.0"))
        self.tableWidget.setItem(rowCount, 3, QtWidgets.QTableWidgetItem("1.0"))
        self.tableWidget.setItem(rowCount, 4, QtWidgets.QTableWidgetItem("1.0"))
        self.tableWidget.setItem(rowCount, 5, QtWidgets.QTableWidgetItem("1.0"))
        self.tableWidget.setItem(rowCount, 6, QtWidgets.QTableWidgetItem("1.0"))
        self.tableWidget.setItem(rowCount, 7, QtWidgets.QTableWidgetItem("False"))
        self.tableWidget.setItem(rowCount, 8, QtWidgets.QTableWidgetItem("64.0"))
        self.tableWidget.setItem(rowCount, 9, QtWidgets.QTableWidgetItem("1.0"))
        self.tableWidget.setItem(rowCount, 10, QtWidgets.QTableWidgetItem("True"))
        self.tableWidget.setItem(rowCount, 11, QtWidgets.QTableWidgetItem("10"))
        self.tableWidget.setItem(rowCount, 12, QtWidgets.QTableWidgetItem("False"))
        self.tableWidget.setItem(rowCount, 13, QtWidgets.QTableWidgetItem("False"))
        self.tableWidget.setItem(rowCount, 14, QtWidgets.QTableWidgetItem("True"))

    def OnBtnRemoveClickedSlot(self):
        """删除一行"""

        currentRow = self.tableWidget.currentRow()
        if currentRow < 0:
            return
        else:
            self.tableWidget.removeRow(currentRow)

    def OnBtnAnalystOneClickedSlot(self):
        """测试某一行参数"""

        # 获取当前行
        currentRow = self.tableWidget.currentRow()
        if currentRow < 0:
            return

        # 获取参数
        diameter = int(self.tableWidget.item(currentRow, 0).text()) \
            if self.tableWidget.item(currentRow, 0) is not None and len(self.tableWidget.item(currentRow, 0).text()) > 0 else 11
        minmass = float(self.tableWidget.item(currentRow, 1).text()) \
            if self.tableWidget.item(currentRow, 1) is not None and len(self.tableWidget.item(currentRow, 0).text()) > 0 else None
        maxsize = float(self.tableWidget.item(currentRow, 2).text()) \
            if self.tableWidget.item(currentRow, 2) is not None and len(self.tableWidget.item(currentRow, 0).text()) > 0 else None
        separation = float(self.tableWidget.item(currentRow, 3).text()) \
            if self.tableWidget.item(currentRow, 3) is not None and len(self.tableWidget.item(currentRow, 0).text()) > 0 else None
        noise_size = float(self.tableWidget.item(currentRow, 4).text()) \
            if self.tableWidget.item(currentRow, 4) is not None and len(self.tableWidget.item(currentRow, 0).text()) > 0 else None
        smoothing_size = float(self.tableWidget.item(currentRow, 5).text()) \
            if self.tableWidget.item(currentRow, 5) is not None and len(self.tableWidget.item(currentRow, 0).text()) > 0 else None
        threshold = float(self.tableWidget.item(currentRow, 6).text()) \
            if self.tableWidget.item(currentRow, 6) is not None and len(self.tableWidget.item(currentRow, 0).text()) > 0 else None
        invert = (self.tableWidget.item(currentRow, 7).text() == "True") \
            if self.tableWidget.item(currentRow, 17) is not None and len(self.tableWidget.item(currentRow, 0).text()) > 0 else False
        percentile = float(self.tableWidget.item(currentRow, 8).text()) \
            if self.tableWidget.item(currentRow, 8) is not None and len(self.tableWidget.item(currentRow, 0).text()) > 0 else 64
        topn = int(self.tableWidget.item(currentRow, 9).text()) \
            if self.tableWidget.item(currentRow, 9) is not None and len(self.tableWidget.item(currentRow, 0).text()) > 0 else None
        preprocess = (self.tableWidget.item(currentRow, 10).text() == "True") \
            if self.tableWidget.item(currentRow, 10) is not None and len(self.tableWidget.item(currentRow, 0).text()) > 0 else True
        max_iterations = int(self.tableWidget.item(currentRow, 11).text()) \
            if self.tableWidget.item(currentRow, 11) is not None and len(self.tableWidget.item(currentRow, 0).text()) > 0 else 10
        filter_before = (self.tableWidget.item(currentRow, 12).text() == "True") \
            if self.tableWidget.item(currentRow, 12) is not None and len(self.tableWidget.item(currentRow, 0).text()) > 0 else None
        filter_after = (self.tableWidget.item(currentRow, 13).text() == "True") \
            if self.tableWidget.item(currentRow, 13) is not None and len(self.tableWidget.item(currentRow, 0).text()) > 0 else None
        characterize = (self.tableWidget.item(currentRow, 14).text() == "True") \
            if self.tableWidget.item(currentRow, 14) is not None and len(self.tableWidget.item(currentRow, 0).text()) > 0 else True

        # 容错
        if self.__pictrureName is None or len(self.__pictrureName) == 0:
            return

        # 加载图片
        frames = pims.ImageSequence(self.__pictrureName, as_grey=True)
        plt.imshow(frames[0])

        # 查找特征点，返回一个DataFrame
        features = tp.locate(frames[0],
                             diameter=diameter,
                             minmass=minmass,
                             maxsize=maxsize,
                             separation=separation,
                             noise_size=noise_size,
                             smoothing_size=smoothing_size,
                             threshold=threshold,
                             invert=invert,
                             percentile=percentile,
                             topn=topn,
                             preprocess=preprocess,
                             max_iterations=max_iterations,
                             filter_before=filter_before,
                             filter_after=filter_after,
                             characterize=characterize
                             )
        features.head()

        # 分析显示
        plt.figure()  # make a new figure
        tp.annotate(features, frames[0])

    def OnBtnAnalystAllClickedSlot(self):
        """测试所有的参数"""

        # 获取行号
        rowCount = self.tableWidget.rowCount()
        if rowCount <= 0:
            return

        # 遍历循环
        for currentRow in range(rowCount):
            # 显示当前测试的参数
            self.tableWidget.setCurrentCell(currentRow, 0)

            # 获取参数
            diameter = int(self.tableWidget.item(currentRow, 0).text()) \
                if self.tableWidget.item(currentRow, 0) is not None and len(self.tableWidget.item(currentRow, 0).text()) > 0 else 11
            minmass = float(self.tableWidget.item(currentRow, 1).text()) \
                if self.tableWidget.item(currentRow, 1) is not None and len(self.tableWidget.item(currentRow, 0).text()) > 0 else None
            maxsize = float(self.tableWidget.item(currentRow, 2).text()) \
                if self.tableWidget.item(currentRow, 2) is not None and len(self.tableWidget.item(currentRow, 0).text()) > 0 else None
            separation = float(self.tableWidget.item(currentRow, 3).text()) \
                if self.tableWidget.item(currentRow, 3) is not None and len(self.tableWidget.item(currentRow, 0).text()) > 0 else None
            noise_size = float(self.tableWidget.item(currentRow, 4).text()) \
                if self.tableWidget.item(currentRow, 4) is not None and len(self.tableWidget.item(currentRow, 0).text()) > 0 else None
            smoothing_size = float(self.tableWidget.item(currentRow, 5).text()) \
                if self.tableWidget.item(currentRow, 5) is not None and len(self.tableWidget.item(currentRow, 0).text()) > 0 else None
            threshold = float(self.tableWidget.item(currentRow, 6).text()) \
                if self.tableWidget.item(currentRow, 6) is not None and len(self.tableWidget.item(currentRow, 0).text()) > 0 else None
            invert = (self.tableWidget.item(currentRow, 7).text() == "True") \
                if self.tableWidget.item(currentRow, 17) is not None and len(self.tableWidget.item(currentRow, 0).text()) > 0 else False
            percentile = float(self.tableWidget.item(currentRow, 8).text()) \
                if self.tableWidget.item(currentRow, 8) is not None and len(self.tableWidget.item(currentRow, 0).text()) > 0 else 64
            topn = int(self.tableWidget.item(currentRow, 9).text()) \
                if self.tableWidget.item(currentRow, 9) is not None and len(self.tableWidget.item(currentRow, 0).text()) > 0 else None
            preprocess = (self.tableWidget.item(currentRow, 10).text() == "True") \
                if self.tableWidget.item(currentRow, 10) is not None and len(self.tableWidget.item(currentRow, 0).text()) > 0 else True
            max_iterations = int(self.tableWidget.item(currentRow, 11).text()) \
                if self.tableWidget.item(currentRow, 11) is not None and len(self.tableWidget.item(currentRow, 0).text()) > 0 else 10
            filter_before = (self.tableWidget.item(currentRow, 12).text() == "True") \
                if self.tableWidget.item(currentRow, 12) is not None and len(self.tableWidget.item(currentRow, 0).text()) > 0 else None
            filter_after = (self.tableWidget.item(currentRow, 13).text() == "True") \
                if self.tableWidget.item(currentRow, 13) is not None and len(self.tableWidget.item(currentRow, 0).text()) > 0 else None
            characterize = (self.tableWidget.item(currentRow, 14).text() == "True") \
                if self.tableWidget.item(currentRow, 14) is not None and len(self.tableWidget.item(currentRow, 0).text()) > 0 else True

            # 容错
            if self.__pictrureName is None or len(self.__pictrureName) == 0:
                return

            # 加载图片
            frames = pims.ImageSequence(self.__pictrureName, as_grey=True)
            plt.imshow(frames[0])

            # 查找特征点，返回一个DataFrame
            features = tp.locate(frames[0], diameter=diameter, minmass=minmass, maxsize=maxsize, separation=separation,
                                 noise_size=noise_size, smoothing_size=smoothing_size, threshold=threshold, invert=invert,
                                 percentile=percentile, topn=topn, preprocess=preprocess, max_iterations=max_iterations,
                                 filter_before=filter_before, filter_after=filter_after, characterize=characterize)
            features.head()

            # 分析显示
            plt.figure()  # make a new figure
            tp.annotate(features, frames[0])

    def OnBtnAnalystClickedSlot(self):
        """点击加载按钮"""

        # 容错
        if self.__pictrureName is None or len(self.__pictrureName) == 0:
            return

        # 加载图片
        frames = pims.ImageSequence(self.__pictrureName, as_grey=True)
        plt.imshow(frames[0])

        # 查找特征点，返回一个DataFrame
        features = tp.locate(frames[0], 11, invert=True)
        features.head()

        # 分析显示
        plt.figure()  # make a new figure
        tp.annotate(features, frames[0])


def main():
    # 创建事件
    app = QtWidgets.QApplication(sys.argv)

    # 创建ui
    ui = MainWindow()

    # 显示ui界面
    ui.show()

    # 进入消息循环
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
