# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'MainWindowUI.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(954, 401)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.btnScan = QtWidgets.QPushButton(self.centralwidget)
        self.btnScan.setObjectName("btnScan")
        self.horizontalLayout.addWidget(self.btnScan)
        self.comboBox = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox.setObjectName("comboBox")
        self.horizontalLayout.addWidget(self.comboBox)
        self.btnConnect = QtWidgets.QPushButton(self.centralwidget)
        self.btnConnect.setObjectName("btnConnect")
        self.horizontalLayout.addWidget(self.btnConnect)
        self.verticalLayout.addLayout(self.horizontalLayout)
        spacerItem = QtWidgets.QSpacerItem(20, 44, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setObjectName("label")
        self.horizontalLayout_2.addWidget(self.label)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem1)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 0, 0, 1, 1)
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setObjectName("label_5")
        self.gridLayout.addWidget(self.label_5, 0, 1, 1, 1)
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setObjectName("label_6")
        self.gridLayout.addWidget(self.label_6, 0, 2, 1, 1)
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setObjectName("label_7")
        self.gridLayout.addWidget(self.label_7, 0, 3, 1, 1)
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setObjectName("label_8")
        self.gridLayout.addWidget(self.label_8, 0, 4, 1, 1)
        self.label_9 = QtWidgets.QLabel(self.centralwidget)
        self.label_9.setObjectName("label_9")
        self.gridLayout.addWidget(self.label_9, 0, 5, 1, 1)
        self.lineEditSendCtrlAddr = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEditSendCtrlAddr.setObjectName("lineEditSendCtrlAddr")
        self.gridLayout.addWidget(self.lineEditSendCtrlAddr, 1, 0, 1, 1)
        self.lineEditSendCmdType = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEditSendCmdType.setObjectName("lineEditSendCmdType")
        self.gridLayout.addWidget(self.lineEditSendCmdType, 1, 1, 1, 1)
        self.lineEditSendFunCode = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEditSendFunCode.setObjectName("lineEditSendFunCode")
        self.gridLayout.addWidget(self.lineEditSendFunCode, 1, 2, 1, 1)
        self.lineEditSendParam1 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEditSendParam1.setObjectName("lineEditSendParam1")
        self.gridLayout.addWidget(self.lineEditSendParam1, 1, 3, 1, 1)
        self.lineEditSendParam2 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEditSendParam2.setObjectName("lineEditSendParam2")
        self.gridLayout.addWidget(self.lineEditSendParam2, 1, 4, 1, 1)
        self.lineEditSendCeckCode = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEditSendCeckCode.setObjectName("lineEditSendCeckCode")
        self.gridLayout.addWidget(self.lineEditSendCeckCode, 1, 5, 1, 1)
        self.verticalLayout.addLayout(self.gridLayout)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem2)
        self.btnSend = QtWidgets.QPushButton(self.centralwidget)
        self.btnSend.setObjectName("btnSend")
        self.horizontalLayout_3.addWidget(self.btnSend)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        spacerItem3 = QtWidgets.QSpacerItem(20, 44, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem3)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_4.addWidget(self.label_2)
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem4)
        self.verticalLayout.addLayout(self.horizontalLayout_4)
        self.gridLayout_2 = QtWidgets.QGridLayout()
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setObjectName("label_4")
        self.gridLayout_2.addWidget(self.label_4, 0, 0, 1, 1)
        self.label_10 = QtWidgets.QLabel(self.centralwidget)
        self.label_10.setObjectName("label_10")
        self.gridLayout_2.addWidget(self.label_10, 0, 1, 1, 1)
        self.label_11 = QtWidgets.QLabel(self.centralwidget)
        self.label_11.setObjectName("label_11")
        self.gridLayout_2.addWidget(self.label_11, 0, 2, 1, 1)
        self.label_12 = QtWidgets.QLabel(self.centralwidget)
        self.label_12.setObjectName("label_12")
        self.gridLayout_2.addWidget(self.label_12, 0, 3, 1, 1)
        self.label_13 = QtWidgets.QLabel(self.centralwidget)
        self.label_13.setObjectName("label_13")
        self.gridLayout_2.addWidget(self.label_13, 0, 4, 1, 1)
        self.label_14 = QtWidgets.QLabel(self.centralwidget)
        self.label_14.setObjectName("label_14")
        self.gridLayout_2.addWidget(self.label_14, 0, 5, 1, 1)
        self.lineEditRecvCtrlAddr = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEditRecvCtrlAddr.setObjectName("lineEditRecvCtrlAddr")
        self.gridLayout_2.addWidget(self.lineEditRecvCtrlAddr, 1, 0, 1, 1)
        self.lineEditRecvCmdType = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEditRecvCmdType.setObjectName("lineEditRecvCmdType")
        self.gridLayout_2.addWidget(self.lineEditRecvCmdType, 1, 1, 1, 1)
        self.lineEditRecvFunCode = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEditRecvFunCode.setObjectName("lineEditRecvFunCode")
        self.gridLayout_2.addWidget(self.lineEditRecvFunCode, 1, 2, 1, 1)
        self.lineEditRecvParam1 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEditRecvParam1.setObjectName("lineEditRecvParam1")
        self.gridLayout_2.addWidget(self.lineEditRecvParam1, 1, 3, 1, 1)
        self.lineEditRecvParam2 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEditRecvParam2.setObjectName("lineEditRecvParam2")
        self.gridLayout_2.addWidget(self.lineEditRecvParam2, 1, 4, 1, 1)
        self.lineEditRecvCeckCode = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEditRecvCeckCode.setObjectName("lineEditRecvCeckCode")
        self.gridLayout_2.addWidget(self.lineEditRecvCeckCode, 1, 5, 1, 1)
        self.verticalLayout.addLayout(self.gridLayout_2)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.label_18 = QtWidgets.QLabel(self.centralwidget)
        self.label_18.setObjectName("label_18")
        self.horizontalLayout_5.addWidget(self.label_18)
        self.lineEditLimitTime = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEditLimitTime.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.lineEditLimitTime.setObjectName("lineEditLimitTime")
        self.horizontalLayout_5.addWidget(self.lineEditLimitTime)
        self.label_17 = QtWidgets.QLabel(self.centralwidget)
        self.label_17.setObjectName("label_17")
        self.horizontalLayout_5.addWidget(self.label_17)
        spacerItem5 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem5)
        self.label_15 = QtWidgets.QLabel(self.centralwidget)
        self.label_15.setObjectName("label_15")
        self.horizontalLayout_5.addWidget(self.label_15)
        self.lineEditTimeCount = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEditTimeCount.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.lineEditTimeCount.setObjectName("lineEditTimeCount")
        self.horizontalLayout_5.addWidget(self.lineEditTimeCount)
        self.label_16 = QtWidgets.QLabel(self.centralwidget)
        self.label_16.setObjectName("label_16")
        self.horizontalLayout_5.addWidget(self.label_16)
        self.verticalLayout.addLayout(self.horizontalLayout_5)
        self.horizontalLayout_7.addLayout(self.verticalLayout)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.btnShowCommendCode = QtWidgets.QPushButton(self.centralwidget)
        self.btnShowCommendCode.setObjectName("btnShowCommendCode")
        self.horizontalLayout_6.addWidget(self.btnShowCommendCode)
        self.brnShowFunctionCode = QtWidgets.QPushButton(self.centralwidget)
        self.brnShowFunctionCode.setObjectName("brnShowFunctionCode")
        self.horizontalLayout_6.addWidget(self.brnShowFunctionCode)
        self.btnShowParameter = QtWidgets.QPushButton(self.centralwidget)
        self.btnShowParameter.setObjectName("btnShowParameter")
        self.horizontalLayout_6.addWidget(self.btnShowParameter)
        self.verticalLayout_2.addLayout(self.horizontalLayout_6)
        self.textBrowser = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser.setObjectName("textBrowser")
        self.verticalLayout_2.addWidget(self.textBrowser)
        self.horizontalLayout_7.addLayout(self.verticalLayout_2)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 954, 23))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "彩科仪器串口通讯协议测试软件"))
        self.btnScan.setText(_translate("MainWindow", "扫描"))
        self.btnConnect.setText(_translate("MainWindow", "连接"))
        self.label.setText(_translate("MainWindow", "发送码："))
        self.label_3.setText(_translate("MainWindow", "控制器地址"))
        self.label_5.setText(_translate("MainWindow", "命令类型"))
        self.label_6.setText(_translate("MainWindow", "功能码"))
        self.label_7.setText(_translate("MainWindow", "参数1"))
        self.label_8.setText(_translate("MainWindow", "参数2"))
        self.label_9.setText(_translate("MainWindow", "校验码"))
        self.btnSend.setText(_translate("MainWindow", "发送"))
        self.label_2.setText(_translate("MainWindow", "返回码："))
        self.label_4.setText(_translate("MainWindow", "控制器地址"))
        self.label_10.setText(_translate("MainWindow", "命令类型"))
        self.label_11.setText(_translate("MainWindow", "功能码"))
        self.label_12.setText(_translate("MainWindow", "参数1"))
        self.label_13.setText(_translate("MainWindow", "参数2"))
        self.label_14.setText(_translate("MainWindow", "校验码"))
        self.label_18.setText(_translate("MainWindow", "设置超时："))
        self.lineEditLimitTime.setText(_translate("MainWindow", "5"))
        self.label_17.setText(_translate("MainWindow", "秒"))
        self.label_15.setText(_translate("MainWindow", "信号往返——共计用时："))
        self.label_16.setText(_translate("MainWindow", "秒"))
        self.btnShowCommendCode.setText(_translate("MainWindow", "显示命令码"))
        self.brnShowFunctionCode.setText(_translate("MainWindow", "显示功能码"))
        self.btnShowParameter.setText(_translate("MainWindow", "显示参数"))
