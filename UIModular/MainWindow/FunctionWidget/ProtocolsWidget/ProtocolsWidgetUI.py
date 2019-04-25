# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ProtocolsWidgetUI.ui'
#
# Created by: PyQt5 UI code generator 5.12.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_ProtocolsWidget(object):
    def setupUi(self, ProtocolsWidget):
        ProtocolsWidget.setObjectName("ProtocolsWidget")
        ProtocolsWidget.resize(1060, 766)
        self.horizontalLayout = QtWidgets.QHBoxLayout(ProtocolsWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.widgetButton = QtWidgets.QWidget(ProtocolsWidget)
        self.widgetButton.setObjectName("widgetButton")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.widgetButton)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.pushButtonProtocols = QtWidgets.QPushButton(self.widgetButton)
        self.pushButtonProtocols.setObjectName("pushButtonProtocols")
        self.verticalLayout.addWidget(self.pushButtonProtocols)
        self.pushButtonSettings = QtWidgets.QPushButton(self.widgetButton)
        self.pushButtonSettings.setObjectName("pushButtonSettings")
        self.buttonGroup = QtWidgets.QButtonGroup(ProtocolsWidget)
        self.buttonGroup.setObjectName("buttonGroup")
        self.buttonGroup.addButton(self.pushButtonSettings)
        self.verticalLayout.addWidget(self.pushButtonSettings)
        self.pushButtonAnalytes = QtWidgets.QPushButton(self.widgetButton)
        self.pushButtonAnalytes.setObjectName("pushButtonAnalytes")
        self.buttonGroup.addButton(self.pushButtonAnalytes)
        self.verticalLayout.addWidget(self.pushButtonAnalytes)
        self.pushButtonPlateLayout = QtWidgets.QPushButton(self.widgetButton)
        self.pushButtonPlateLayout.setObjectName("pushButtonPlateLayout")
        self.buttonGroup.addButton(self.pushButtonPlateLayout)
        self.verticalLayout.addWidget(self.pushButtonPlateLayout)
        self.pushButtonStdAndCtrls = QtWidgets.QPushButton(self.widgetButton)
        self.pushButtonStdAndCtrls.setObjectName("pushButtonStdAndCtrls")
        self.verticalLayout.addWidget(self.pushButtonStdAndCtrls)
        spacerItem = QtWidgets.QSpacerItem(20, 649, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.horizontalLayout.addWidget(self.widgetButton)
        self.widgetFunction = QtWidgets.QWidget(ProtocolsWidget)
        self.widgetFunction.setObjectName("widgetFunction")
        self.gridLayout = QtWidgets.QGridLayout(self.widgetFunction)
        self.gridLayout.setObjectName("gridLayout")
        self.horizontalLayout.addWidget(self.widgetFunction)
        self.horizontalLayout.setStretch(0, 1)
        self.horizontalLayout.setStretch(1, 5)

        self.retranslateUi(ProtocolsWidget)
        QtCore.QMetaObject.connectSlotsByName(ProtocolsWidget)

    def retranslateUi(self, ProtocolsWidget):
        _translate = QtCore.QCoreApplication.translate
        ProtocolsWidget.setWindowTitle(_translate("ProtocolsWidget", "Protocols"))
        self.pushButtonProtocols.setText(_translate("ProtocolsWidget", "Protocols"))
        self.pushButtonSettings.setText(_translate("ProtocolsWidget", "Settings"))
        self.pushButtonAnalytes.setText(_translate("ProtocolsWidget", "Analytes"))
        self.pushButtonPlateLayout.setText(_translate("ProtocolsWidget", "Plate Layout"))
        self.pushButtonStdAndCtrls.setText(_translate("ProtocolsWidget", "Std and Ctrls"))


