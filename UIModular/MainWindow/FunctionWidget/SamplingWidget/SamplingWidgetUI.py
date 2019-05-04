# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'SamplingWidgetUI.ui'
#
# Created by: PyQt5 UI code generator 5.12.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_SamplingWidget(object):
    def setupUi(self, SamplingWidget):
        SamplingWidget.setObjectName("SamplingWidget")
        SamplingWidget.resize(1033, 842)
        self.horizontalLayout = QtWidgets.QHBoxLayout(SamplingWidget)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.tableWidget = QtWidgets.QTableWidget(SamplingWidget)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(4)
        self.tableWidget.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, item)
        self.tableWidget.horizontalHeader().setStretchLastSection(True)
        self.horizontalLayout.addWidget(self.tableWidget)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.pushButton_load = QtWidgets.QPushButton(SamplingWidget)
        self.pushButton_load.setObjectName("pushButton_load")
        self.verticalLayout.addWidget(self.pushButton_load)
        self.pushButton_export = QtWidgets.QPushButton(SamplingWidget)
        self.pushButton_export.setObjectName("pushButton_export")
        self.verticalLayout.addWidget(self.pushButton_export)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.pushButton_add = QtWidgets.QPushButton(SamplingWidget)
        self.pushButton_add.setObjectName("pushButton_add")
        self.verticalLayout.addWidget(self.pushButton_add)
        self.pushButton_remove = QtWidgets.QPushButton(SamplingWidget)
        self.pushButton_remove.setObjectName("pushButton_remove")
        self.verticalLayout.addWidget(self.pushButton_remove)
        self.pushButton_edit = QtWidgets.QPushButton(SamplingWidget)
        self.pushButton_edit.setObjectName("pushButton_edit")
        self.verticalLayout.addWidget(self.pushButton_edit)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem1)
        self.pushButton_DoIt = QtWidgets.QPushButton(SamplingWidget)
        self.pushButton_DoIt.setObjectName("pushButton_DoIt")
        self.verticalLayout.addWidget(self.pushButton_DoIt)
        self.horizontalLayout.addLayout(self.verticalLayout)

        self.retranslateUi(SamplingWidget)
        QtCore.QMetaObject.connectSlotsByName(SamplingWidget)

    def retranslateUi(self, SamplingWidget):
        _translate = QtCore.QCoreApplication.translate
        SamplingWidget.setWindowTitle(_translate("SamplingWidget", "Sampling"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("SamplingWidget", "instructions "))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("SamplingWidget", "parameter"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("SamplingWidget", "volume(ml)"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("SamplingWidget", "describe"))
        self.pushButton_load.setText(_translate("SamplingWidget", "load"))
        self.pushButton_export.setText(_translate("SamplingWidget", "export"))
        self.pushButton_add.setText(_translate("SamplingWidget", "add"))
        self.pushButton_remove.setText(_translate("SamplingWidget", "remove"))
        self.pushButton_edit.setText(_translate("SamplingWidget", "edit"))
        self.pushButton_DoIt.setText(_translate("SamplingWidget", "Do it"))


