# coding=utf8

import sys
import threading
import msvcrt

from ctypes import *

from ThirdParty.MVS.MvImport.MvCameraControl_class import *
from ThirdParty.MVS.MvImport.CameraParams_const import *
from ThirdParty.MVS.MvImport.CameraParams_header import *

from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from UIModular.MainWindow.FunctionWidget.ImagingWidget.ImagingWidgetModify import ImagingWidgetModify


class ImagingWidget(ImagingWidgetModify):
    def __init__(self, parent=None):
        """构造方法"""

        # 父类构造方法
        super(ImagingWidget, self).__init__()

        ######### 界面处理 #########
        self.__scene = QGraphicsScene()#创建视口的场景
        self.graphicsView.setScene(self.__scene)#将视口与场景绑定

        ######### 图像处理 #########
        # 取流
        self.__isLiveStreaming = False
        self.btnLiveStreaming.clicked.connect(self.OnBtnLiveStreamingClickedSlot)
        # 抓取
        self.btnCapture.clicked.connect(self.OnBtnCaptureClickedSlot)
        # 保存
        self.btnSaveAs.clicked.connect(self.OnBtnSaveAsClickedSlot)
        # 载入
        self.btnLoad.clicked.connect(self.OnBtnLoadClickedSlot)

        ######### 基本属性 #########
        # 帧率
        self.__fps = self.spinBoxFPS.value()
        self.spinBoxFPS.valueChanged.connect(self.OnSpinBoxFPSValueChangedSlot)
        # 曝光
        self.__autoExposureEnable = False
        self.__exposureTime = self.spinBoxExposureTime.value()
        self.btnAutoExposureOn.clicked.connect(self.OnBtnAutoExposureClickedSlot)
        self.btnAutoExposureOff.clicked.connect(self.OnBtnAutoExposureClickedSlot)
        self.spinBoxExposureTime.valueChanged.connect(self.OnSpinBoxExposureTimeValueChangedSlot)
        # 增益
        self.__gainEnable = False
        self.__gain = self.spinBoxGain.value()
        self.btnGainOn.clicked.connect(self.OnBtnGainClickedSlot)
        self.btnGainOff.clicked.connect(self.OnBtnGainClickedSlot)
        self.spinBoxGain.valueChanged.connect(self.OnSpinBoxGainValueChangedSlot)
        # 伽马
        self.__gamaEnable = False
        self.__gama = self.spinBoxGamma.value()
        self.btnGammaOn.clicked.connect(self.OnBtnGammaClickedSlot)
        self.btnGammaOff.clicked.connect(self.OnBtnGammaClickedSlot)
        self.spinBoxGamma.valueChanged.connect(self.OnSpinBoxGammaValueChangedSlot)
        # Black Level
        self.__blackLevelEnable = False
        self.__blackLevel = self.spinBoxBlackLevel.value()
        self.btnBlackLevelOn.clicked.connect(self.OnBtnBlackLevelClickedSlot)
        self.btnBlackLevelOff.clicked.connect(self.OnBtnBlackLevelClickedSlot)
        self.spinBoxBlackLevel.valueChanged.connect(self.OnSpinBoxBlackLevelValueChangedSlot)

    def OnBtnLiveStreamingClickedSlot(self):
    	"""取流"""

    	# 判断状态，如果已经在取流，无需操作
    	if self.__isLiveStreaming:
    		return

    	# 获取CCD设备信息
    	deviceList = MV_CC_DEVICE_INFO_LIST()
    	tlayerType = MV_GIGE_DEVICE | MV_USB_DEVICE

    	# 如果没有查到设备，退出函数
    	if not MvCamera.MV_CC_EnumDevices(tlayerType, deviceList) or deviceList.nDeviceNum == 0:
	        QMessageBox.question(self, u"CCD连接", u"无法找到CCD", QMessageBox.Ok)
	        return

        # ch:创建相机实例 | en:Creat Camera Object
	    cam = MvCamera()

	    # ch:选择设备并创建句柄 | en:Select device and create handle
	    stDeviceList = cast(deviceList.pDeviceInfo[int(nConnectionNum)], POINTER(MV_CC_DEVICE_INFO)).contents

	    # 创建设备连接句柄
	    if not cam.MV_CC_CreateHandle(stDeviceList):
	        return

	    # ch:打开设备 | en:Open device
	    if not cam.MV_CC_OpenDevice(MV_ACCESS_Exclusive, 0):
	        return

	    # ch:设置触发模式为off | en:Set trigger mode as off
	    if not cam.MV_CC_SetEnumValue("TriggerMode", MV_TRIGGER_MODE_OFF):
	        return

	    # ch:获取数据包大小 | en:Get payload size
	    stParam = MVCC_INTVALUE()
	    memset(byref(stParam), 0, sizeof(MVCC_INTVALUE))

	    # ch:开始取流 | en:Start grab image

    	# 设置状态，是否正在取流
    	self.__isLiveStreaming = not self.__isLiveStreaming

    def OnBtnCaptureClickedSlot(self):
    	"""抓取"""
    	pass

    def OnBtnSaveAsClickedSlot(self):
    	"""保存"""
    	pass

    def OnBtnLoadClickedSlot(self):
    	"""载入"""
    	pass

    def OnSpinBoxFPSValueChangedSlot(self):
        """帧率"""
        self.__fps = self.spinBoxFPS.value()

    def OnBtnAutoExposureClickedSlot(self):
        """自动曝光"""
        self.__autoExposureEnable = not self.__autoExposureEnable

    def OnSpinBoxExposureTimeValueChangedSlot(self):
        """曝光时间"""
        self.__exposureTime = self.spinBoxExposureTime.value()

    def OnBtnGainClickedSlot(self):
        """是否打开增益"""
        self.__gainEnable = not self.__gainEnable

    def OnSpinBoxGainValueChangedSlot(self):
        """增益大小"""
        self.__gain = self.spinBoxGain.value()

    def OnBtnGammaClickedSlot(self):
        """是否打开伽马"""
        self.__gamaEnable = not self.__gamaEnable

    def OnSpinBoxGammaValueChangedSlot(self):
        """伽马大小"""
        self.__gama = self.spinBoxGamma.value()

    def OnBtnBlackLevelClickedSlot(self):
        """是否打开Black Level"""
        self.__blackLevelEnable = not self.__blackLevelEnable

    def OnSpinBoxBlackLevelValueChangedSlot(self):
        """Black Level大小"""
        self.__blackLevel = self.spinBoxBlackLevel.value()
