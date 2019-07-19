# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ImagingWidgetUI.ui'
#
# Created by: PyQt5 UI code generator 5.12.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_ImagingWidget(object):
    def setupUi(self, ImagingWidget):
        ImagingWidget.setObjectName("ImagingWidget")
        ImagingWidget.resize(939, 555)
        self.horizontalLayout_20 = QtWidgets.QHBoxLayout(ImagingWidget)
        self.horizontalLayout_20.setObjectName("horizontalLayout_20")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.btnLiveStreaming = QtWidgets.QPushButton(ImagingWidget)
        self.btnLiveStreaming.setObjectName("btnLiveStreaming")
        self.horizontalLayout.addWidget(self.btnLiveStreaming)
        self.btnCapture = QtWidgets.QPushButton(ImagingWidget)
        self.btnCapture.setObjectName("btnCapture")
        self.horizontalLayout.addWidget(self.btnCapture)
        self.btnSaveAs = QtWidgets.QPushButton(ImagingWidget)
        self.btnSaveAs.setObjectName("btnSaveAs")
        self.horizontalLayout.addWidget(self.btnSaveAs)
        self.btnLoad = QtWidgets.QPushButton(ImagingWidget)
        self.btnLoad.setObjectName("btnLoad")
        self.horizontalLayout.addWidget(self.btnLoad)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.graphicsView = QtWidgets.QGraphicsView(ImagingWidget)
        self.graphicsView.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.graphicsView.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.graphicsView.setObjectName("graphicsView")
        self.verticalLayout.addWidget(self.graphicsView)
        self.verticalLayout_3.addLayout(self.verticalLayout)
        self.horizontalLayout_16 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_16.setObjectName("horizontalLayout_16")
        self.btnDoAlgorithm = QtWidgets.QPushButton(ImagingWidget)
        self.btnDoAlgorithm.setObjectName("btnDoAlgorithm")
        self.horizontalLayout_16.addWidget(self.btnDoAlgorithm)
        self.verticalLayout_3.addLayout(self.horizontalLayout_16)
        self.horizontalLayout_20.addLayout(self.verticalLayout_3)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout_12 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_12.setObjectName("horizontalLayout_12")
        self.groupBoxBaseFeature = QtWidgets.QGroupBox(ImagingWidget)
        self.groupBoxBaseFeature.setObjectName("groupBoxBaseFeature")
        self.gridLayout = QtWidgets.QGridLayout(self.groupBoxBaseFeature)
        self.gridLayout.setObjectName("gridLayout")
        self.labelFPSName = QtWidgets.QLabel(self.groupBoxBaseFeature)
        self.labelFPSName.setObjectName("labelFPSName")
        self.gridLayout.addWidget(self.labelFPSName, 0, 0, 1, 1)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.spinBoxFPS = QtWidgets.QDoubleSpinBox(self.groupBoxBaseFeature)
        self.spinBoxFPS.setEnabled(True)
        self.spinBoxFPS.setMaximum(100000.0)
        self.spinBoxFPS.setObjectName("spinBoxFPS")
        self.horizontalLayout_4.addWidget(self.spinBoxFPS)
        self.labelFPSUnit = QtWidgets.QLabel(self.groupBoxBaseFeature)
        self.labelFPSUnit.setObjectName("labelFPSUnit")
        self.horizontalLayout_4.addWidget(self.labelFPSUnit)
        self.gridLayout.addLayout(self.horizontalLayout_4, 0, 1, 1, 1)
        self.labelAutoExposureName = QtWidgets.QLabel(self.groupBoxBaseFeature)
        self.labelAutoExposureName.setObjectName("labelAutoExposureName")
        self.gridLayout.addWidget(self.labelAutoExposureName, 1, 0, 1, 1)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.btnAutoExposureOn = QtWidgets.QPushButton(self.groupBoxBaseFeature)
        self.btnAutoExposureOn.setCheckable(True)
        self.btnAutoExposureOn.setChecked(True)
        self.btnAutoExposureOn.setObjectName("btnAutoExposureOn")
        self.buttonGroup = QtWidgets.QButtonGroup(ImagingWidget)
        self.buttonGroup.setObjectName("buttonGroup")
        self.buttonGroup.addButton(self.btnAutoExposureOn)
        self.horizontalLayout_2.addWidget(self.btnAutoExposureOn)
        self.btnAutoExposureOff = QtWidgets.QPushButton(self.groupBoxBaseFeature)
        self.btnAutoExposureOff.setCheckable(True)
        self.btnAutoExposureOff.setChecked(False)
        self.btnAutoExposureOff.setObjectName("btnAutoExposureOff")
        self.buttonGroup.addButton(self.btnAutoExposureOff)
        self.horizontalLayout_2.addWidget(self.btnAutoExposureOff)
        self.gridLayout.addLayout(self.horizontalLayout_2, 1, 1, 1, 1)
        self.labelExposureTimeName = QtWidgets.QLabel(self.groupBoxBaseFeature)
        self.labelExposureTimeName.setObjectName("labelExposureTimeName")
        self.gridLayout.addWidget(self.labelExposureTimeName, 2, 0, 1, 1)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.spinBoxExposureTime = QtWidgets.QSpinBox(self.groupBoxBaseFeature)
        self.spinBoxExposureTime.setEnabled(False)
        self.spinBoxExposureTime.setMaximum(999999999)
        self.spinBoxExposureTime.setObjectName("spinBoxExposureTime")
        self.horizontalLayout_3.addWidget(self.spinBoxExposureTime)
        self.labelExposureTimeUnit = QtWidgets.QLabel(self.groupBoxBaseFeature)
        self.labelExposureTimeUnit.setObjectName("labelExposureTimeUnit")
        self.horizontalLayout_3.addWidget(self.labelExposureTimeUnit)
        self.gridLayout.addLayout(self.horizontalLayout_3, 2, 1, 1, 1)
        self.labelAutoGainName = QtWidgets.QLabel(self.groupBoxBaseFeature)
        self.labelAutoGainName.setObjectName("labelAutoGainName")
        self.gridLayout.addWidget(self.labelAutoGainName, 3, 0, 1, 1)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setSpacing(0)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.btnGainOn = QtWidgets.QPushButton(self.groupBoxBaseFeature)
        self.btnGainOn.setCheckable(True)
        self.btnGainOn.setChecked(True)
        self.btnGainOn.setObjectName("btnGainOn")
        self.buttonGroup_2 = QtWidgets.QButtonGroup(ImagingWidget)
        self.buttonGroup_2.setObjectName("buttonGroup_2")
        self.buttonGroup_2.addButton(self.btnGainOn)
        self.horizontalLayout_5.addWidget(self.btnGainOn)
        self.btnGainOff = QtWidgets.QPushButton(self.groupBoxBaseFeature)
        self.btnGainOff.setCheckable(True)
        self.btnGainOff.setChecked(False)
        self.btnGainOff.setObjectName("btnGainOff")
        self.buttonGroup_2.addButton(self.btnGainOff)
        self.horizontalLayout_5.addWidget(self.btnGainOff)
        self.gridLayout.addLayout(self.horizontalLayout_5, 3, 1, 1, 1)
        self.labelGainName = QtWidgets.QLabel(self.groupBoxBaseFeature)
        self.labelGainName.setObjectName("labelGainName")
        self.gridLayout.addWidget(self.labelGainName, 4, 0, 1, 1)
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.spinBoxGain = QtWidgets.QSpinBox(self.groupBoxBaseFeature)
        self.spinBoxGain.setEnabled(False)
        self.spinBoxGain.setObjectName("spinBoxGain")
        self.horizontalLayout_8.addWidget(self.spinBoxGain)
        self.label_12 = QtWidgets.QLabel(self.groupBoxBaseFeature)
        self.label_12.setText("")
        self.label_12.setObjectName("label_12")
        self.horizontalLayout_8.addWidget(self.label_12)
        self.gridLayout.addLayout(self.horizontalLayout_8, 4, 1, 1, 1)
        self.labelAutoGammaName = QtWidgets.QLabel(self.groupBoxBaseFeature)
        self.labelAutoGammaName.setObjectName("labelAutoGammaName")
        self.gridLayout.addWidget(self.labelAutoGammaName, 5, 0, 1, 1)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setSpacing(0)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.btnGammaOn = QtWidgets.QPushButton(self.groupBoxBaseFeature)
        self.btnGammaOn.setCheckable(True)
        self.btnGammaOn.setChecked(True)
        self.btnGammaOn.setObjectName("btnGammaOn")
        self.buttonGroup_3 = QtWidgets.QButtonGroup(ImagingWidget)
        self.buttonGroup_3.setObjectName("buttonGroup_3")
        self.buttonGroup_3.addButton(self.btnGammaOn)
        self.horizontalLayout_6.addWidget(self.btnGammaOn)
        self.btnGammaOff = QtWidgets.QPushButton(self.groupBoxBaseFeature)
        self.btnGammaOff.setCheckable(True)
        self.btnGammaOff.setChecked(False)
        self.btnGammaOff.setObjectName("btnGammaOff")
        self.buttonGroup_3.addButton(self.btnGammaOff)
        self.horizontalLayout_6.addWidget(self.btnGammaOff)
        self.gridLayout.addLayout(self.horizontalLayout_6, 5, 1, 1, 1)
        self.labelGammaName = QtWidgets.QLabel(self.groupBoxBaseFeature)
        self.labelGammaName.setObjectName("labelGammaName")
        self.gridLayout.addWidget(self.labelGammaName, 6, 0, 1, 1)
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.spinBoxGamma = QtWidgets.QDoubleSpinBox(self.groupBoxBaseFeature)
        self.spinBoxGamma.setEnabled(False)
        self.spinBoxGamma.setMaximum(4.0)
        self.spinBoxGamma.setObjectName("spinBoxGamma")
        self.horizontalLayout_9.addWidget(self.spinBoxGamma)
        self.label_13 = QtWidgets.QLabel(self.groupBoxBaseFeature)
        self.label_13.setText("")
        self.label_13.setObjectName("label_13")
        self.horizontalLayout_9.addWidget(self.label_13)
        self.gridLayout.addLayout(self.horizontalLayout_9, 6, 1, 1, 1)
        self.labelAutoBlackLevelName = QtWidgets.QLabel(self.groupBoxBaseFeature)
        self.labelAutoBlackLevelName.setObjectName("labelAutoBlackLevelName")
        self.gridLayout.addWidget(self.labelAutoBlackLevelName, 7, 0, 1, 1)
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setSpacing(0)
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.btnBlackLevelOn = QtWidgets.QPushButton(self.groupBoxBaseFeature)
        self.btnBlackLevelOn.setCheckable(True)
        self.btnBlackLevelOn.setChecked(True)
        self.btnBlackLevelOn.setObjectName("btnBlackLevelOn")
        self.buttonGroup_4 = QtWidgets.QButtonGroup(ImagingWidget)
        self.buttonGroup_4.setObjectName("buttonGroup_4")
        self.buttonGroup_4.addButton(self.btnBlackLevelOn)
        self.horizontalLayout_7.addWidget(self.btnBlackLevelOn)
        self.btnBlackLevelOff = QtWidgets.QPushButton(self.groupBoxBaseFeature)
        self.btnBlackLevelOff.setCheckable(True)
        self.btnBlackLevelOff.setChecked(False)
        self.btnBlackLevelOff.setObjectName("btnBlackLevelOff")
        self.buttonGroup_4.addButton(self.btnBlackLevelOff)
        self.horizontalLayout_7.addWidget(self.btnBlackLevelOff)
        self.gridLayout.addLayout(self.horizontalLayout_7, 7, 1, 1, 1)
        self.labelBlackLevelName = QtWidgets.QLabel(self.groupBoxBaseFeature)
        self.labelBlackLevelName.setObjectName("labelBlackLevelName")
        self.gridLayout.addWidget(self.labelBlackLevelName, 8, 0, 1, 1)
        self.horizontalLayout_10 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")
        self.spinBoxBlackLevel = QtWidgets.QSpinBox(self.groupBoxBaseFeature)
        self.spinBoxBlackLevel.setEnabled(False)
        self.spinBoxBlackLevel.setMaximum(999999999)
        self.spinBoxBlackLevel.setObjectName("spinBoxBlackLevel")
        self.horizontalLayout_10.addWidget(self.spinBoxBlackLevel)
        self.label_14 = QtWidgets.QLabel(self.groupBoxBaseFeature)
        self.label_14.setText("")
        self.label_14.setObjectName("label_14")
        self.horizontalLayout_10.addWidget(self.label_14)
        self.gridLayout.addLayout(self.horizontalLayout_10, 8, 1, 1, 1)
        self.horizontalLayout_12.addWidget(self.groupBoxBaseFeature)
        self.groupBoxImageFeature = QtWidgets.QGroupBox(ImagingWidget)
        self.groupBoxImageFeature.setObjectName("groupBoxImageFeature")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.groupBoxImageFeature)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.labelWidthName = QtWidgets.QLabel(self.groupBoxImageFeature)
        self.labelWidthName.setObjectName("labelWidthName")
        self.gridLayout_2.addWidget(self.labelWidthName, 0, 0, 1, 1)
        self.horizontalLayout_11 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_11.setObjectName("horizontalLayout_11")
        self.spinBoxWidth = QtWidgets.QSpinBox(self.groupBoxImageFeature)
        self.spinBoxWidth.setMaximum(999999999)
        self.spinBoxWidth.setObjectName("spinBoxWidth")
        self.horizontalLayout_11.addWidget(self.spinBoxWidth)
        self.gridLayout_2.addLayout(self.horizontalLayout_11, 0, 1, 1, 1)
        self.labelHeightName = QtWidgets.QLabel(self.groupBoxImageFeature)
        self.labelHeightName.setObjectName("labelHeightName")
        self.gridLayout_2.addWidget(self.labelHeightName, 1, 0, 1, 1)
        self.horizontalLayout_13 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_13.setObjectName("horizontalLayout_13")
        self.spinBoxHeight = QtWidgets.QSpinBox(self.groupBoxImageFeature)
        self.spinBoxHeight.setMaximum(999999999)
        self.spinBoxHeight.setObjectName("spinBoxHeight")
        self.horizontalLayout_13.addWidget(self.spinBoxHeight)
        self.gridLayout_2.addLayout(self.horizontalLayout_13, 1, 1, 1, 1)
        self.labelOffsetXName = QtWidgets.QLabel(self.groupBoxImageFeature)
        self.labelOffsetXName.setObjectName("labelOffsetXName")
        self.gridLayout_2.addWidget(self.labelOffsetXName, 2, 0, 1, 1)
        self.horizontalLayout_15 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_15.setObjectName("horizontalLayout_15")
        self.spinBoxOffsetX = QtWidgets.QSpinBox(self.groupBoxImageFeature)
        self.spinBoxOffsetX.setMinimum(-999999999)
        self.spinBoxOffsetX.setMaximum(999999999)
        self.spinBoxOffsetX.setObjectName("spinBoxOffsetX")
        self.horizontalLayout_15.addWidget(self.spinBoxOffsetX)
        self.gridLayout_2.addLayout(self.horizontalLayout_15, 2, 1, 1, 1)
        self.labelOffsetYName = QtWidgets.QLabel(self.groupBoxImageFeature)
        self.labelOffsetYName.setObjectName("labelOffsetYName")
        self.gridLayout_2.addWidget(self.labelOffsetYName, 3, 0, 1, 1)
        self.spinBoxOffsetY = QtWidgets.QSpinBox(self.groupBoxImageFeature)
        self.spinBoxOffsetY.setMaximum(999999999)
        self.spinBoxOffsetY.setObjectName("spinBoxOffsetY")
        self.gridLayout_2.addWidget(self.spinBoxOffsetY, 3, 1, 1, 1)
        self.labelReverseXName = QtWidgets.QLabel(self.groupBoxImageFeature)
        self.labelReverseXName.setObjectName("labelReverseXName")
        self.gridLayout_2.addWidget(self.labelReverseXName, 4, 0, 1, 1)
        self.horizontalLayout_17 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_17.setObjectName("horizontalLayout_17")
        self.horizontalLayout_18 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_18.setSpacing(0)
        self.horizontalLayout_18.setObjectName("horizontalLayout_18")
        self.btnReverseXOn = QtWidgets.QPushButton(self.groupBoxImageFeature)
        self.btnReverseXOn.setCheckable(True)
        self.btnReverseXOn.setChecked(True)
        self.btnReverseXOn.setObjectName("btnReverseXOn")
        self.buttonGroup_5 = QtWidgets.QButtonGroup(ImagingWidget)
        self.buttonGroup_5.setObjectName("buttonGroup_5")
        self.buttonGroup_5.addButton(self.btnReverseXOn)
        self.horizontalLayout_18.addWidget(self.btnReverseXOn)
        self.btnReverseXOff = QtWidgets.QPushButton(self.groupBoxImageFeature)
        self.btnReverseXOff.setCheckable(True)
        self.btnReverseXOff.setChecked(False)
        self.btnReverseXOff.setObjectName("btnReverseXOff")
        self.buttonGroup_5.addButton(self.btnReverseXOff)
        self.horizontalLayout_18.addWidget(self.btnReverseXOff)
        self.horizontalLayout_17.addLayout(self.horizontalLayout_18)
        self.gridLayout_2.addLayout(self.horizontalLayout_17, 4, 1, 1, 1)
        self.labelBinningXName = QtWidgets.QLabel(self.groupBoxImageFeature)
        self.labelBinningXName.setObjectName("labelBinningXName")
        self.gridLayout_2.addWidget(self.labelBinningXName, 5, 0, 1, 1)
        self.spinBoxBinningX = QtWidgets.QSpinBox(self.groupBoxImageFeature)
        self.spinBoxBinningX.setObjectName("spinBoxBinningX")
        self.gridLayout_2.addWidget(self.spinBoxBinningX, 5, 1, 1, 1)
        self.labelBinningYName = QtWidgets.QLabel(self.groupBoxImageFeature)
        self.labelBinningYName.setObjectName("labelBinningYName")
        self.gridLayout_2.addWidget(self.labelBinningYName, 6, 0, 1, 1)
        self.horizontalLayout_19 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_19.setObjectName("horizontalLayout_19")
        self.spinBoxBinningY = QtWidgets.QSpinBox(self.groupBoxImageFeature)
        self.spinBoxBinningY.setObjectName("spinBoxBinningY")
        self.horizontalLayout_19.addWidget(self.spinBoxBinningY)
        self.gridLayout_2.addLayout(self.horizontalLayout_19, 6, 1, 1, 1)
        self.horizontalLayout_12.addWidget(self.groupBoxImageFeature)
        self.verticalLayout_2.addLayout(self.horizontalLayout_12)
        self.horizontalLayout_14 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_14.setObjectName("horizontalLayout_14")
        self.btnDoActivite = QtWidgets.QPushButton(ImagingWidget)
        self.btnDoActivite.setObjectName("btnDoActivite")
        self.horizontalLayout_14.addWidget(self.btnDoActivite)
        self.verticalLayout_2.addLayout(self.horizontalLayout_14)
        self.verticalLayout_2.setStretch(0, 1)
        self.horizontalLayout_20.addLayout(self.verticalLayout_2)

        self.retranslateUi(ImagingWidget)
        self.btnBlackLevelOn.clicked['bool'].connect(self.spinBoxBlackLevel.setDisabled)
        self.btnBlackLevelOff.clicked['bool'].connect(self.spinBoxBlackLevel.setEnabled)
        self.btnGammaOn.clicked['bool'].connect(self.spinBoxGamma.setDisabled)
        self.btnGammaOff.clicked['bool'].connect(self.spinBoxGamma.setEnabled)
        QtCore.QMetaObject.connectSlotsByName(ImagingWidget)

    def retranslateUi(self, ImagingWidget):
        _translate = QtCore.QCoreApplication.translate
        ImagingWidget.setWindowTitle(_translate("ImagingWidget", "Form"))
        self.btnLiveStreaming.setText(_translate("ImagingWidget", "Live streaming"))
        self.btnCapture.setText(_translate("ImagingWidget", "Capture"))
        self.btnSaveAs.setText(_translate("ImagingWidget", "Save as"))
        self.btnLoad.setText(_translate("ImagingWidget", "Load"))
        self.btnDoAlgorithm.setText(_translate("ImagingWidget", "执行算法"))
        self.groupBoxBaseFeature.setTitle(_translate("ImagingWidget", "基本属性"))
        self.labelFPSName.setText(_translate("ImagingWidget", "帧率"))
        self.labelFPSUnit.setText(_translate("ImagingWidget", "fps"))
        self.labelAutoExposureName.setText(_translate("ImagingWidget", "自动曝光"))
        self.btnAutoExposureOn.setText(_translate("ImagingWidget", "On"))
        self.btnAutoExposureOff.setText(_translate("ImagingWidget", "Off"))
        self.labelExposureTimeName.setText(_translate("ImagingWidget", "曝光时间"))
        self.labelExposureTimeUnit.setText(_translate("ImagingWidget", "s"))
        self.labelAutoGainName.setText(_translate("ImagingWidget", "自动增益"))
        self.btnGainOn.setText(_translate("ImagingWidget", "On"))
        self.btnGainOff.setText(_translate("ImagingWidget", "Off"))
        self.labelGainName.setText(_translate("ImagingWidget", "增益"))
        self.labelAutoGammaName.setText(_translate("ImagingWidget", "伽马"))
        self.btnGammaOn.setText(_translate("ImagingWidget", "On"))
        self.btnGammaOff.setText(_translate("ImagingWidget", "Off"))
        self.labelGammaName.setText(_translate("ImagingWidget", "伽马"))
        self.labelAutoBlackLevelName.setText(_translate("ImagingWidget", "Black Level"))
        self.btnBlackLevelOn.setText(_translate("ImagingWidget", "On"))
        self.btnBlackLevelOff.setText(_translate("ImagingWidget", "Off"))
        self.labelBlackLevelName.setText(_translate("ImagingWidget", "Black Level"))
        self.groupBoxImageFeature.setTitle(_translate("ImagingWidget", "图像属性"))
        self.labelWidthName.setText(_translate("ImagingWidget", "宽度"))
        self.labelHeightName.setText(_translate("ImagingWidget", "高度"))
        self.labelOffsetXName.setText(_translate("ImagingWidget", "Offset X"))
        self.labelOffsetYName.setText(_translate("ImagingWidget", "Offset Y"))
        self.labelReverseXName.setText(_translate("ImagingWidget", "Reverse X"))
        self.btnReverseXOn.setText(_translate("ImagingWidget", "On"))
        self.btnReverseXOff.setText(_translate("ImagingWidget", "Off"))
        self.labelBinningXName.setText(_translate("ImagingWidget", "Binning X"))
        self.labelBinningYName.setText(_translate("ImagingWidget", "Binning Y"))
        self.btnDoActivite.setText(_translate("ImagingWidget", "配置生效"))


