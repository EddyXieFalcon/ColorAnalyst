# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'CommendDailogUI.ui'
#
# Created by: PyQt5 UI code generator 5.12.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_CommendDailog(object):
    def setupUi(self, CommendDailog):
        CommendDailog.setObjectName("CommendDailog")
        CommendDailog.resize(258, 69)
        self.verticalLayout = QtWidgets.QVBoxLayout(CommendDailog)
        self.verticalLayout.setObjectName("verticalLayout")
        self.comboBox = QtWidgets.QComboBox(CommendDailog)
        self.comboBox.setObjectName("comboBox")
        self.verticalLayout.addWidget(self.comboBox)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.pushButton_cancel = QtWidgets.QPushButton(CommendDailog)
        self.pushButton_cancel.setObjectName("pushButton_cancel")
        self.horizontalLayout.addWidget(self.pushButton_cancel)
        self.pushButton_ok = QtWidgets.QPushButton(CommendDailog)
        self.pushButton_ok.setObjectName("pushButton_ok")
        self.horizontalLayout.addWidget(self.pushButton_ok)
        self.verticalLayout.addLayout(self.horizontalLayout)

        self.retranslateUi(CommendDailog)
        QtCore.QMetaObject.connectSlotsByName(CommendDailog)

    def retranslateUi(self, CommendDailog):
        _translate = QtCore.QCoreApplication.translate
        CommendDailog.setWindowTitle(_translate("CommendDailog", "CommendDailog"))
        self.pushButton_cancel.setText(_translate("CommendDailog", "Cancel"))
        self.pushButton_ok.setText(_translate("CommendDailog", "OK"))


