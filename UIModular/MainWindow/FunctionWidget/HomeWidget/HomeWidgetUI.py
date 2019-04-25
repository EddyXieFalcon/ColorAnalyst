# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'HomeWidgetUI.ui'
#
# Created by: PyQt5 UI code generator 5.12.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_HomeWidget(object):
    def setupUi(self, HomeWidget):
        HomeWidget.setObjectName("HomeWidget")
        HomeWidget.resize(1200, 693)
        self.horizontalLayout = QtWidgets.QHBoxLayout(HomeWidget)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.widgetButton = QtWidgets.QWidget(HomeWidget)
        self.widgetButton.setObjectName("widgetButton")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.widgetButton)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.pushButtonHome = QtWidgets.QPushButton(self.widgetButton)
        self.pushButtonHome.setObjectName("pushButtonHome")
        self.verticalLayout.addWidget(self.pushButtonHome)
        spacerItem = QtWidgets.QSpacerItem(20, 649, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.horizontalLayout.addWidget(self.widgetButton)
        self.widgetFunction = QtWidgets.QWidget(HomeWidget)
        self.widgetFunction.setStyleSheet("")
        self.widgetFunction.setObjectName("widgetFunction")
        self.verticalLayout_9 = QtWidgets.QVBoxLayout(self.widgetFunction)
        self.verticalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_9.setSpacing(0)
        self.verticalLayout_9.setObjectName("verticalLayout_9")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.labelWelcome = QtWidgets.QLabel(self.widgetFunction)
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(0, 85, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 85, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        self.labelWelcome.setPalette(palette)
        self.labelWelcome.setObjectName("labelWelcome")
        self.horizontalLayout_2.addWidget(self.labelWelcome)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem1)
        self.verticalLayout_2.addLayout(self.horizontalLayout_2)
        self.labelInfo = QtWidgets.QLabel(self.widgetFunction)
        self.labelInfo.setObjectName("labelInfo")
        self.verticalLayout_2.addWidget(self.labelInfo)
        self.horizontalLayout_3.addLayout(self.verticalLayout_2)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem2)
        self.pushButtonInfo = QtWidgets.QPushButton(self.widgetFunction)
        self.pushButtonInfo.setObjectName("pushButtonInfo")
        self.horizontalLayout_3.addWidget(self.pushButtonInfo)
        self.verticalLayout_9.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.pushButtonNewBatch = QtWidgets.QPushButton(self.widgetFunction)
        self.pushButtonNewBatch.setText("")
        self.pushButtonNewBatch.setObjectName("pushButtonNewBatch")
        self.horizontalLayout_4.addWidget(self.pushButtonNewBatch)
        self.label_3 = QtWidgets.QLabel(self.widgetFunction)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_4.addWidget(self.label_3)
        self.horizontalLayout_6.addLayout(self.horizontalLayout_4)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_6.addItem(spacerItem3)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.pushButtonNewHighlightedBatch = QtWidgets.QPushButton(self.widgetFunction)
        self.pushButtonNewHighlightedBatch.setText("")
        self.pushButtonNewHighlightedBatch.setObjectName("pushButtonNewHighlightedBatch")
        self.horizontalLayout_5.addWidget(self.pushButtonNewHighlightedBatch)
        self.label_4 = QtWidgets.QLabel(self.widgetFunction)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_5.addWidget(self.label_4)
        self.horizontalLayout_6.addLayout(self.horizontalLayout_5)
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_6.addItem(spacerItem4)
        self.verticalLayout_3.addLayout(self.horizontalLayout_6)
        self.groupBoxInstalledProtocols = QtWidgets.QGroupBox(self.widgetFunction)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBoxInstalledProtocols.sizePolicy().hasHeightForWidth())
        self.groupBoxInstalledProtocols.setSizePolicy(sizePolicy)
        self.groupBoxInstalledProtocols.setObjectName("groupBoxInstalledProtocols")
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout(self.groupBoxInstalledProtocols)
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.tableWidget = QtWidgets.QTableWidget(self.groupBoxInstalledProtocols)
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
        self.horizontalLayout_7.addWidget(self.tableWidget)
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        spacerItem5 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_4.addItem(spacerItem5)
        self.labelScroll = QtWidgets.QLabel(self.groupBoxInstalledProtocols)
        self.labelScroll.setObjectName("labelScroll")
        self.verticalLayout_4.addWidget(self.labelScroll, 0, QtCore.Qt.AlignHCenter)
        self.pushButtonScrollUp = QtWidgets.QPushButton(self.groupBoxInstalledProtocols)
        self.pushButtonScrollUp.setObjectName("pushButtonScrollUp")
        self.verticalLayout_4.addWidget(self.pushButtonScrollUp)
        self.pushButtonScrollDown = QtWidgets.QPushButton(self.groupBoxInstalledProtocols)
        self.pushButtonScrollDown.setObjectName("pushButtonScrollDown")
        self.verticalLayout_4.addWidget(self.pushButtonScrollDown)
        spacerItem6 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_4.addItem(spacerItem6)
        self.labelView = QtWidgets.QLabel(self.groupBoxInstalledProtocols)
        self.labelView.setObjectName("labelView")
        self.verticalLayout_4.addWidget(self.labelView, 0, QtCore.Qt.AlignHCenter)
        self.pushButtonView = QtWidgets.QPushButton(self.groupBoxInstalledProtocols)
        self.pushButtonView.setObjectName("pushButtonView")
        self.verticalLayout_4.addWidget(self.pushButtonView)
        spacerItem7 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_4.addItem(spacerItem7)
        self.horizontalLayout_7.addLayout(self.verticalLayout_4)
        self.verticalLayout_3.addWidget(self.groupBoxInstalledProtocols)
        self.horizontalLayout_8.addLayout(self.verticalLayout_3)
        self.groupBoxDailyActivities = QtWidgets.QGroupBox(self.widgetFunction)
        self.groupBoxDailyActivities.setObjectName("groupBoxDailyActivities")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.groupBoxDailyActivities)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout()
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.pushButton_8 = QtWidgets.QPushButton(self.groupBoxDailyActivities)
        self.pushButton_8.setText("")
        self.pushButton_8.setObjectName("pushButton_8")
        self.horizontalLayout_9.addWidget(self.pushButton_8)
        self.label_7 = QtWidgets.QLabel(self.groupBoxDailyActivities)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_7.sizePolicy().hasHeightForWidth())
        self.label_7.setSizePolicy(sizePolicy)
        self.label_7.setObjectName("label_7")
        self.horizontalLayout_9.addWidget(self.label_7)
        self.verticalLayout_6.addLayout(self.horizontalLayout_9)
        self.labelSystemInitialization = QtWidgets.QLabel(self.groupBoxDailyActivities)
        self.labelSystemInitialization.setObjectName("labelSystemInitialization")
        self.verticalLayout_6.addWidget(self.labelSystemInitialization)
        self.verticalLayout_5.addLayout(self.verticalLayout_6)
        spacerItem8 = QtWidgets.QSpacerItem(20, 95, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_5.addItem(spacerItem8)
        self.verticalLayout_7 = QtWidgets.QVBoxLayout()
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.horizontalLayout_10 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")
        self.pushButton_9 = QtWidgets.QPushButton(self.groupBoxDailyActivities)
        self.pushButton_9.setText("")
        self.pushButton_9.setObjectName("pushButton_9")
        self.horizontalLayout_10.addWidget(self.pushButton_9)
        self.label_9 = QtWidgets.QLabel(self.groupBoxDailyActivities)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_9.sizePolicy().hasHeightForWidth())
        self.label_9.setSizePolicy(sizePolicy)
        self.label_9.setObjectName("label_9")
        self.horizontalLayout_10.addWidget(self.label_9)
        self.verticalLayout_7.addLayout(self.horizontalLayout_10)
        self.labelShutdown = QtWidgets.QLabel(self.groupBoxDailyActivities)
        self.labelShutdown.setObjectName("labelShutdown")
        self.verticalLayout_7.addWidget(self.labelShutdown)
        self.verticalLayout_5.addLayout(self.verticalLayout_7)
        spacerItem9 = QtWidgets.QSpacerItem(20, 96, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_5.addItem(spacerItem9)
        self.verticalLayout_8 = QtWidgets.QVBoxLayout()
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.horizontalLayout_11 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_11.setObjectName("horizontalLayout_11")
        self.pushButtonProbeAndHeater = QtWidgets.QPushButton(self.groupBoxDailyActivities)
        self.pushButtonProbeAndHeater.setText("")
        self.pushButtonProbeAndHeater.setObjectName("pushButtonProbeAndHeater")
        self.horizontalLayout_11.addWidget(self.pushButtonProbeAndHeater)
        self.label_11 = QtWidgets.QLabel(self.groupBoxDailyActivities)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_11.sizePolicy().hasHeightForWidth())
        self.label_11.setSizePolicy(sizePolicy)
        self.label_11.setObjectName("label_11")
        self.horizontalLayout_11.addWidget(self.label_11)
        self.verticalLayout_8.addLayout(self.horizontalLayout_11)
        self.labelProbeAndHeater = QtWidgets.QLabel(self.groupBoxDailyActivities)
        self.labelProbeAndHeater.setObjectName("labelProbeAndHeater")
        self.verticalLayout_8.addWidget(self.labelProbeAndHeater)
        self.verticalLayout_5.addLayout(self.verticalLayout_8)
        spacerItem10 = QtWidgets.QSpacerItem(20, 95, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_5.addItem(spacerItem10)
        self.horizontalLayout_8.addWidget(self.groupBoxDailyActivities)
        self.verticalLayout_9.addLayout(self.horizontalLayout_8)
        self.horizontalLayout_12 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_12.setObjectName("horizontalLayout_12")
        spacerItem11 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_12.addItem(spacerItem11)
        self.pushButtonSysInfo = QtWidgets.QPushButton(self.widgetFunction)
        self.pushButtonSysInfo.setObjectName("pushButtonSysInfo")
        self.horizontalLayout_12.addWidget(self.pushButtonSysInfo)
        self.pushButtonReports = QtWidgets.QPushButton(self.widgetFunction)
        self.pushButtonReports.setObjectName("pushButtonReports")
        self.horizontalLayout_12.addWidget(self.pushButtonReports)
        self.verticalLayout_9.addLayout(self.horizontalLayout_12)
        self.horizontalLayout.addWidget(self.widgetFunction)
        self.horizontalLayout.setStretch(0, 1)
        self.horizontalLayout.setStretch(1, 5)

        self.retranslateUi(HomeWidget)
        QtCore.QMetaObject.connectSlotsByName(HomeWidget)

    def retranslateUi(self, HomeWidget):
        _translate = QtCore.QCoreApplication.translate
        HomeWidget.setWindowTitle(_translate("HomeWidget", "Home"))
        self.pushButtonHome.setText(_translate("HomeWidget", "Home"))
        self.labelWelcome.setText(_translate("HomeWidget", "Welcome"))
        self.labelInfo.setText(_translate("HomeWidget", "Instructions:  Create a new batch, view installed protocols, perform a daily activity, or access system information and reports"))
        self.pushButtonInfo.setText(_translate("HomeWidget", "info"))
        self.label_3.setText(_translate("HomeWidget", "Click to Create a new Batch from a new Protocol"))
        self.label_4.setText(_translate("HomeWidget", "Click to Create a new Batch using the highlighted Protocol below"))
        self.groupBoxInstalledProtocols.setTitle(_translate("HomeWidget", "Installed Protocols"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("HomeWidget", "Name"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("HomeWidget", "Version"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("HomeWidget", "Manufacturer"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("HomeWidget", "Date"))
        self.labelScroll.setText(_translate("HomeWidget", "Scroll"))
        self.pushButtonScrollUp.setText(_translate("HomeWidget", "Up"))
        self.pushButtonScrollDown.setText(_translate("HomeWidget", "Down"))
        self.labelView.setText(_translate("HomeWidget", "View"))
        self.pushButtonView.setText(_translate("HomeWidget", "View"))
        self.groupBoxDailyActivities.setTitle(_translate("HomeWidget", "Daily Activities"))
        self.label_7.setText(_translate("HomeWidget", "System Initialization"))
        self.labelSystemInitialization.setText(_translate("HomeWidget", "<html><head/><body><p>Laser warm-up, fluidics, </p><p>calibration, performance </p><p>verification</p></body></html>"))
        self.label_9.setText(_translate("HomeWidget", "ShutDown"))
        self.labelShutdown.setText(_translate("HomeWidget", "Sanitize, wash, soak"))
        self.label_11.setText(_translate("HomeWidget", "Probe and Heater"))
        self.labelProbeAndHeater.setText(_translate("HomeWidget", "<html><head/><body><p>Adjust the probe, </p><p>set up the heater</p></body></html>"))
        self.pushButtonSysInfo.setText(_translate("HomeWidget", "Sys Info"))
        self.pushButtonReports.setText(_translate("HomeWidget", "Reports"))


