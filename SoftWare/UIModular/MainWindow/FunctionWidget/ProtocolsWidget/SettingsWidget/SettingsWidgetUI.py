# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'SettingsWidgetUI.ui'
#
# Created by: PyQt5 UI code generator 5.12.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_SettingsWidget(object):
    def setupUi(self, SettingsWidget):
        SettingsWidget.setObjectName("SettingsWidget")
        SettingsWidget.resize(1069, 808)
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(SettingsWidget)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.widgetInfo = QtWidgets.QWidget(SettingsWidget)
        self.widgetInfo.setObjectName("widgetInfo")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.widgetInfo)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.labelWelcome = QtWidgets.QLabel(self.widgetInfo)
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
        self.horizontalLayout.addWidget(self.labelWelcome)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.labelInfo = QtWidgets.QLabel(self.widgetInfo)
        self.labelInfo.setObjectName("labelInfo")
        self.verticalLayout.addWidget(self.labelInfo)
        self.horizontalLayout_2.addLayout(self.verticalLayout)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem1)
        self.pushButtonInfo = QtWidgets.QPushButton(self.widgetInfo)
        self.pushButtonInfo.setObjectName("pushButtonInfo")
        self.horizontalLayout_2.addWidget(self.pushButtonInfo)
        self.verticalLayout_6.addWidget(self.widgetInfo)
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.labelName = QtWidgets.QLabel(SettingsWidget)
        self.labelName.setObjectName("labelName")
        self.horizontalLayout_6.addWidget(self.labelName)
        self.lineEditName = QtWidgets.QLineEdit(SettingsWidget)
        self.lineEditName.setObjectName("lineEditName")
        self.horizontalLayout_6.addWidget(self.lineEditName)
        self.verticalLayout_2.addLayout(self.horizontalLayout_6)
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.labelVersion = QtWidgets.QLabel(SettingsWidget)
        self.labelVersion.setObjectName("labelVersion")
        self.horizontalLayout_5.addWidget(self.labelVersion)
        self.lineEditVersion = QtWidgets.QLineEdit(SettingsWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEditVersion.sizePolicy().hasHeightForWidth())
        self.lineEditVersion.setSizePolicy(sizePolicy)
        self.lineEditVersion.setObjectName("lineEditVersion")
        self.horizontalLayout_5.addWidget(self.lineEditVersion)
        self.horizontalLayout_7.addLayout(self.horizontalLayout_5)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.labelManufacturer = QtWidgets.QLabel(SettingsWidget)
        self.labelManufacturer.setObjectName("labelManufacturer")
        self.horizontalLayout_4.addWidget(self.labelManufacturer)
        self.lineEditManufacturer = QtWidgets.QLineEdit(SettingsWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEditManufacturer.sizePolicy().hasHeightForWidth())
        self.lineEditManufacturer.setSizePolicy(sizePolicy)
        self.lineEditManufacturer.setObjectName("lineEditManufacturer")
        self.horizontalLayout_4.addWidget(self.lineEditManufacturer)
        self.horizontalLayout_7.addLayout(self.horizontalLayout_4)
        self.verticalLayout_2.addLayout(self.horizontalLayout_7)
        self.horizontalLayout_8.addLayout(self.verticalLayout_2)
        self.plainTextEdit = QtWidgets.QPlainTextEdit(SettingsWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Ignored)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.plainTextEdit.sizePolicy().hasHeightForWidth())
        self.plainTextEdit.setSizePolicy(sizePolicy)
        self.plainTextEdit.setObjectName("plainTextEdit")
        self.horizontalLayout_8.addWidget(self.plainTextEdit)
        self.verticalLayout_6.addLayout(self.horizontalLayout_8)
        self.groupBoxAcquisitionSettings = QtWidgets.QGroupBox(SettingsWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBoxAcquisitionSettings.sizePolicy().hasHeightForWidth())
        self.groupBoxAcquisitionSettings.setSizePolicy(sizePolicy)
        self.groupBoxAcquisitionSettings.setObjectName("groupBoxAcquisitionSettings")
        self.horizontalLayout_13 = QtWidgets.QHBoxLayout(self.groupBoxAcquisitionSettings)
        self.horizontalLayout_13.setObjectName("horizontalLayout_13")
        self.gridLayout_2 = QtWidgets.QGridLayout()
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.label = QtWidgets.QLabel(self.groupBoxAcquisitionSettings)
        self.label.setObjectName("label")
        self.gridLayout_2.addWidget(self.label, 0, 0, 1, 1)
        self.comboBox = QtWidgets.QComboBox(self.groupBoxAcquisitionSettings)
        self.comboBox.setObjectName("comboBox")
        self.gridLayout_2.addWidget(self.comboBox, 0, 1, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.groupBoxAcquisitionSettings)
        self.label_2.setObjectName("label_2")
        self.gridLayout_2.addWidget(self.label_2, 1, 0, 1, 1)
        self.horizontalLayout_10 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")
        self.lineEdit = QtWidgets.QLineEdit(self.groupBoxAcquisitionSettings)
        self.lineEdit.setObjectName("lineEdit")
        self.horizontalLayout_10.addWidget(self.lineEdit)
        self.label_6 = QtWidgets.QLabel(self.groupBoxAcquisitionSettings)
        self.label_6.setObjectName("label_6")
        self.horizontalLayout_10.addWidget(self.label_6)
        self.gridLayout_2.addLayout(self.horizontalLayout_10, 1, 1, 1, 1)
        self.label_7 = QtWidgets.QLabel(self.groupBoxAcquisitionSettings)
        self.label_7.setObjectName("label_7")
        self.gridLayout_2.addWidget(self.label_7, 2, 0, 1, 1)
        self.horizontalLayout_11 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_11.setObjectName("horizontalLayout_11")
        self.checkBox = QtWidgets.QCheckBox(self.groupBoxAcquisitionSettings)
        self.checkBox.setObjectName("checkBox")
        self.horizontalLayout_11.addWidget(self.checkBox)
        self.lineEdit_4 = QtWidgets.QLineEdit(self.groupBoxAcquisitionSettings)
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.horizontalLayout_11.addWidget(self.lineEdit_4)
        self.label_9 = QtWidgets.QLabel(self.groupBoxAcquisitionSettings)
        self.label_9.setObjectName("label_9")
        self.horizontalLayout_11.addWidget(self.label_9)
        self.gridLayout_2.addLayout(self.horizontalLayout_11, 2, 1, 1, 1)
        self.label_8 = QtWidgets.QLabel(self.groupBoxAcquisitionSettings)
        self.label_8.setObjectName("label_8")
        self.gridLayout_2.addWidget(self.label_8, 3, 0, 1, 1)
        self.horizontalLayout_12 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_12.setObjectName("horizontalLayout_12")
        self.checkBox_2 = QtWidgets.QCheckBox(self.groupBoxAcquisitionSettings)
        self.checkBox_2.setObjectName("checkBox_2")
        self.horizontalLayout_12.addWidget(self.checkBox_2)
        self.lineEdit_5 = QtWidgets.QLineEdit(self.groupBoxAcquisitionSettings)
        self.lineEdit_5.setObjectName("lineEdit_5")
        self.horizontalLayout_12.addWidget(self.lineEdit_5)
        self.label_10 = QtWidgets.QLabel(self.groupBoxAcquisitionSettings)
        self.label_10.setObjectName("label_10")
        self.horizontalLayout_12.addWidget(self.label_10)
        self.gridLayout_2.addLayout(self.horizontalLayout_12, 3, 1, 1, 1)
        self.horizontalLayout_13.addLayout(self.gridLayout_2)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.label_4 = QtWidgets.QLabel(self.groupBoxAcquisitionSettings)
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 0, 0, 1, 1)
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.groupBoxAcquisitionSettings)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.horizontalLayout_9.addWidget(self.lineEdit_2)
        self.label_5 = QtWidgets.QLabel(self.groupBoxAcquisitionSettings)
        self.label_5.setObjectName("label_5")
        self.horizontalLayout_9.addWidget(self.label_5)
        self.lineEdit_3 = QtWidgets.QLineEdit(self.groupBoxAcquisitionSettings)
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.horizontalLayout_9.addWidget(self.lineEdit_3)
        self.gridLayout.addLayout(self.horizontalLayout_9, 0, 1, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.groupBoxAcquisitionSettings)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 1, 0, 1, 1)
        self.comboBox_2 = QtWidgets.QComboBox(self.groupBoxAcquisitionSettings)
        self.comboBox_2.setObjectName("comboBox_2")
        self.gridLayout.addWidget(self.comboBox_2, 1, 1, 1, 1)
        self.verticalLayout_3.addLayout(self.gridLayout)
        spacerItem2 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_3.addItem(spacerItem2)
        self.horizontalLayout_13.addLayout(self.verticalLayout_3)
        self.verticalLayout_6.addWidget(self.groupBoxAcquisitionSettings)
        self.groupBoxAnalysisSettings = QtWidgets.QGroupBox(SettingsWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBoxAnalysisSettings.sizePolicy().hasHeightForWidth())
        self.groupBoxAnalysisSettings.setSizePolicy(sizePolicy)
        self.groupBoxAnalysisSettings.setObjectName("groupBoxAnalysisSettings")
        self.horizontalLayout_19 = QtWidgets.QHBoxLayout(self.groupBoxAnalysisSettings)
        self.horizontalLayout_19.setObjectName("horizontalLayout_19")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout()
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.horizontalLayout_15 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_15.setObjectName("horizontalLayout_15")
        self.label_11 = QtWidgets.QLabel(self.groupBoxAnalysisSettings)
        self.label_11.setObjectName("label_11")
        self.horizontalLayout_15.addWidget(self.label_11)
        self.comboBox_3 = QtWidgets.QComboBox(self.groupBoxAnalysisSettings)
        self.comboBox_3.setObjectName("comboBox_3")
        self.horizontalLayout_15.addWidget(self.comboBox_3)
        self.checkBox_3 = QtWidgets.QCheckBox(self.groupBoxAnalysisSettings)
        self.checkBox_3.setObjectName("checkBox_3")
        self.horizontalLayout_15.addWidget(self.checkBox_3)
        self.lineEdit_6 = QtWidgets.QLineEdit(self.groupBoxAnalysisSettings)
        self.lineEdit_6.setObjectName("lineEdit_6")
        self.horizontalLayout_15.addWidget(self.lineEdit_6)
        self.verticalLayout_5.addLayout(self.horizontalLayout_15)
        self.horizontalLayout_16 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_16.setObjectName("horizontalLayout_16")
        self.label_13 = QtWidgets.QLabel(self.groupBoxAnalysisSettings)
        self.label_13.setObjectName("label_13")
        self.horizontalLayout_16.addWidget(self.label_13)
        self.lineEdit_8 = QtWidgets.QLineEdit(self.groupBoxAnalysisSettings)
        self.lineEdit_8.setObjectName("lineEdit_8")
        self.horizontalLayout_16.addWidget(self.lineEdit_8)
        self.verticalLayout_5.addLayout(self.horizontalLayout_16)
        self.horizontalLayout_17 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_17.setObjectName("horizontalLayout_17")
        self.label_14 = QtWidgets.QLabel(self.groupBoxAnalysisSettings)
        self.label_14.setObjectName("label_14")
        self.horizontalLayout_17.addWidget(self.label_14)
        self.lineEdit_7 = QtWidgets.QLineEdit(self.groupBoxAnalysisSettings)
        self.lineEdit_7.setObjectName("lineEdit_7")
        self.horizontalLayout_17.addWidget(self.lineEdit_7)
        self.verticalLayout_5.addLayout(self.horizontalLayout_17)
        self.horizontalLayout_18 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_18.setObjectName("horizontalLayout_18")
        self.radioButton = QtWidgets.QRadioButton(self.groupBoxAnalysisSettings)
        self.radioButton.setObjectName("radioButton")
        self.horizontalLayout_18.addWidget(self.radioButton)
        self.radioButton_2 = QtWidgets.QRadioButton(self.groupBoxAnalysisSettings)
        self.radioButton_2.setObjectName("radioButton_2")
        self.horizontalLayout_18.addWidget(self.radioButton_2)
        self.verticalLayout_5.addLayout(self.horizontalLayout_18)
        self.horizontalLayout_19.addLayout(self.verticalLayout_5)
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.checkBox_4 = QtWidgets.QCheckBox(self.groupBoxAnalysisSettings)
        self.checkBox_4.setObjectName("checkBox_4")
        self.verticalLayout_4.addWidget(self.checkBox_4)
        self.checkBox_5 = QtWidgets.QCheckBox(self.groupBoxAnalysisSettings)
        self.checkBox_5.setObjectName("checkBox_5")
        self.verticalLayout_4.addWidget(self.checkBox_5)
        self.horizontalLayout_14 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_14.setObjectName("horizontalLayout_14")
        self.label_12 = QtWidgets.QLabel(self.groupBoxAnalysisSettings)
        self.label_12.setObjectName("label_12")
        self.horizontalLayout_14.addWidget(self.label_12)
        self.comboBox_4 = QtWidgets.QComboBox(self.groupBoxAnalysisSettings)
        self.comboBox_4.setObjectName("comboBox_4")
        self.horizontalLayout_14.addWidget(self.comboBox_4)
        self.verticalLayout_4.addLayout(self.horizontalLayout_14)
        spacerItem3 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_4.addItem(spacerItem3)
        self.horizontalLayout_19.addLayout(self.verticalLayout_4)
        self.verticalLayout_6.addWidget(self.groupBoxAnalysisSettings)
        self.widget = QtWidgets.QWidget(SettingsWidget)
        self.widget.setObjectName("widget")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.widget)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem4)
        self.pushButtonCancel = QtWidgets.QPushButton(self.widget)
        self.pushButtonCancel.setObjectName("pushButtonCancel")
        self.horizontalLayout_3.addWidget(self.pushButtonCancel)
        self.pushButtonNext = QtWidgets.QPushButton(self.widget)
        self.pushButtonNext.setObjectName("pushButtonNext")
        self.horizontalLayout_3.addWidget(self.pushButtonNext)
        self.verticalLayout_6.addWidget(self.widget)

        self.retranslateUi(SettingsWidget)
        QtCore.QMetaObject.connectSlotsByName(SettingsWidget)

    def retranslateUi(self, SettingsWidget):
        _translate = QtCore.QCoreApplication.translate
        SettingsWidget.setWindowTitle(_translate("SettingsWidget", "Settings"))
        self.labelWelcome.setText(_translate("SettingsWidget", "Step 1: Protocol Setting for \"mTH1 2 9 17 22Treg 17 Plex\""))
        self.labelInfo.setText(_translate("SettingsWidget", "Instructions:  Name this protocol and select the acquisition settings. Press Next to continue."))
        self.pushButtonInfo.setText(_translate("SettingsWidget", "info"))
        self.labelName.setText(_translate("SettingsWidget", "Name"))
        self.labelVersion.setText(_translate("SettingsWidget", "Version"))
        self.labelManufacturer.setText(_translate("SettingsWidget", "Manufacturer"))
        self.groupBoxAcquisitionSettings.setTitle(_translate("SettingsWidget", "Acquisition Settings"))
        self.label.setText(_translate("SettingsWidget", "TextLabel"))
        self.label_2.setText(_translate("SettingsWidget", "TextLabel"))
        self.label_6.setText(_translate("SettingsWidget", "TextLabel"))
        self.label_7.setText(_translate("SettingsWidget", "TextLabel"))
        self.checkBox.setText(_translate("SettingsWidget", "CheckBox"))
        self.label_9.setText(_translate("SettingsWidget", "TextLabel"))
        self.label_8.setText(_translate("SettingsWidget", "TextLabel"))
        self.checkBox_2.setText(_translate("SettingsWidget", "CheckBox"))
        self.label_10.setText(_translate("SettingsWidget", "TextLabel"))
        self.label_4.setText(_translate("SettingsWidget", "TextLabel"))
        self.label_5.setText(_translate("SettingsWidget", "TextLabel"))
        self.label_3.setText(_translate("SettingsWidget", "TextLabel"))
        self.groupBoxAnalysisSettings.setTitle(_translate("SettingsWidget", "Analysis Settings"))
        self.label_11.setText(_translate("SettingsWidget", "TextLabel"))
        self.checkBox_3.setText(_translate("SettingsWidget", "CheckBox"))
        self.label_13.setText(_translate("SettingsWidget", "TextLabel"))
        self.label_14.setText(_translate("SettingsWidget", "TextLabel"))
        self.radioButton.setText(_translate("SettingsWidget", "RadioButton"))
        self.radioButton_2.setText(_translate("SettingsWidget", "RadioButton"))
        self.checkBox_4.setText(_translate("SettingsWidget", "CheckBox"))
        self.checkBox_5.setText(_translate("SettingsWidget", "CheckBox"))
        self.label_12.setText(_translate("SettingsWidget", "TextLabel"))
        self.pushButtonCancel.setText(_translate("SettingsWidget", "Cancel"))
        self.pushButtonNext.setText(_translate("SettingsWidget", "Next"))


