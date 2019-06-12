# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'LaserWidgetUI.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_LaserWidget(object):
    def setupUi(self, LaserWidget):
        LaserWidget.setObjectName("LaserWidget")
        LaserWidget.resize(721, 437)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(LaserWidget)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.pushButton_connect = QtWidgets.QPushButton(LaserWidget)
        self.pushButton_connect.setObjectName("pushButton_connect")
        self.horizontalLayout_3.addWidget(self.pushButton_connect)
        self.comboBox_connect = QtWidgets.QComboBox(LaserWidget)
        self.comboBox_connect.setObjectName("comboBox_connect")
        self.horizontalLayout_3.addWidget(self.comboBox_connect)
        self.verticalLayout_2.addLayout(self.horizontalLayout_3)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.tableWidget = QtWidgets.QTableWidget(LaserWidget)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(3)
        self.tableWidget.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        self.tableWidget.horizontalHeader().setStretchLastSection(True)
        self.horizontalLayout.addWidget(self.tableWidget)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.pushButton_load = QtWidgets.QPushButton(LaserWidget)
        self.pushButton_load.setObjectName("pushButton_load")
        self.verticalLayout.addWidget(self.pushButton_load)
        self.pushButton_export = QtWidgets.QPushButton(LaserWidget)
        self.pushButton_export.setObjectName("pushButton_export")
        self.verticalLayout.addWidget(self.pushButton_export)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.pushButton_add = QtWidgets.QPushButton(LaserWidget)
        self.pushButton_add.setObjectName("pushButton_add")
        self.verticalLayout.addWidget(self.pushButton_add)
        self.pushButton_remove = QtWidgets.QPushButton(LaserWidget)
        self.pushButton_remove.setObjectName("pushButton_remove")
        self.verticalLayout.addWidget(self.pushButton_remove)
        self.pushButton_edit = QtWidgets.QPushButton(LaserWidget)
        self.pushButton_edit.setObjectName("pushButton_edit")
        self.verticalLayout.addWidget(self.pushButton_edit)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem1)
        self.pushButton_DoIt = QtWidgets.QPushButton(LaserWidget)
        self.pushButton_DoIt.setObjectName("pushButton_DoIt")
        self.verticalLayout.addWidget(self.pushButton_DoIt)
        self.horizontalLayout.addLayout(self.verticalLayout)
        self.verticalLayout_2.addLayout(self.horizontalLayout)

        self.retranslateUi(LaserWidget)
        QtCore.QMetaObject.connectSlotsByName(LaserWidget)

    def retranslateUi(self, LaserWidget):
        _translate = QtCore.QCoreApplication.translate
        LaserWidget.setWindowTitle(_translate("LaserWidget", "Sampling"))
        self.pushButton_connect.setText(_translate("LaserWidget", "Connect"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("LaserWidget", "instructions "))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("LaserWidget", "voltage(mV)"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("LaserWidget", "return message"))
        self.pushButton_load.setText(_translate("LaserWidget", "load"))
        self.pushButton_export.setText(_translate("LaserWidget", "export"))
        self.pushButton_add.setText(_translate("LaserWidget", "add"))
        self.pushButton_remove.setText(_translate("LaserWidget", "remove"))
        self.pushButton_edit.setText(_translate("LaserWidget", "edit"))
        self.pushButton_DoIt.setText(_translate("LaserWidget", "Do it"))

