# coding=utf8

import numpy as np
import cv2
import msvcrt
import threading

from ctypes import *

from ThirdParty.MVS.MvImport.MvCameraControl_class import *
from ThirdParty.MVS.MvImport.MvCameraControl_header import *
from ThirdParty.MVS.MvImport.CameraParams_const import *

from PyQt5 import QtWidgets, QtGui, QtCore
from UIModular.MainWindow.FunctionWidget.ImagingWidget.ImagingWidgetModify import ImagingWidgetModify


class ImagingWidget(ImagingWidgetModify):
    LiveStreamingSccessSignal = QtCore.pyqtSignal()

    def __init__(self, parent=None):
        """构造方法"""

        # 父类构造方法
        super(ImagingWidget, self).__init__()

        ######### 界面处理 #########
        self.__dataBuff = None  # 取流数据缓冲
        self.__scene = QtWidgets.QGraphicsScene()  # 创建视口的场景
        self.graphicsView.setScene(self.__scene)  # 将视口与场景绑定
        self.__pixmapItem = QtWidgets.QGraphicsPixmapItem()  # 图片图元
        self.__imageWidth = 0  # 图片宽度
        self.__imageHeight = 0  # 图片高度

        ######### 图像处理 #########
        # 取流
        self.__isLiveStreaming = False
        self.__lock = QtCore.QMutex()
        self.btnLiveStreaming.clicked.connect(self.OnBtnLiveStreamingClickedSlot)
        self.LiveStreamingSccessSignal.connect(self.ShowStreamImageSlot)
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

        # 摄像头信息
        deviceList = MV_CC_DEVICE_INFO_LIST()
        tlayerType = MV_GIGE_DEVICE | MV_USB_DEVICE

        # ch:枚举设备 | en:Enum device
        if MvCamera.MV_CC_EnumDevices(tlayerType, deviceList) != 0:
            return

        # 容错，检索不到设备信息
        if deviceList.nDeviceNum == 0:
            return

        # ch:创建相机实例 | en:Creat Camera Object
        cam = MvCamera()

        # ch:选择设备并创建句柄 | en:Select device and create handle
        stDeviceList = cast(deviceList.pDeviceInfo[0], POINTER(MV_CC_DEVICE_INFO)).contents

        # 创建设备连接句柄
        if cam.MV_CC_CreateHandle(stDeviceList) != 0:
            return

        # ch:打开设备 | en:Open device
        if cam.MV_CC_OpenDevice(MV_ACCESS_Exclusive, 0) != 0:
            return

        # ch:设置触发模式为off | en:Set trigger mode as off
        if cam.MV_CC_SetEnumValue("TriggerMode", MV_TRIGGER_MODE_OFF) != 0:
            return

        # ch:获取数据包大小 | en:Get payload size
        stParam = MVCC_INTVALUE()
        memset(byref(stParam), 0, sizeof(MVCC_INTVALUE))

        # 获取Integer型属性值
        if cam.MV_CC_GetIntValue("PayloadSize", stParam) != 0:
            return
        nPayloadSize = stParam.nCurValue

        # ch:开始取流 | en:Start grab image
        if cam.MV_CC_StartGrabbing() != 0:
            return

        # 创建设备信息列表数据结构体
        stDeviceList = MV_FRAME_OUT_INFO_EX()
        # 为上述数据结构体填装数据
        memset(byref(stDeviceList), 0, sizeof(stDeviceList))
        # 创建数据缓冲区
        data_buf = (c_ubyte * nPayloadSize)()

        # 先抓一帧数据
        if cam.MV_CC_GetOneFrameTimeout(byref(data_buf), nPayloadSize, stDeviceList, 1000) == 0:

            # 解析数据
            nRGBSize = stDeviceList.nWidth * stDeviceList.nHeight * 3
            stConvertParam = MV_CC_PIXEL_CONVERT_PARAM()
            memset(byref(stConvertParam), 0, sizeof(stConvertParam))
            stConvertParam.nWidth = stDeviceList.nWidth
            stConvertParam.nHeight = stDeviceList.nHeight
            stConvertParam.pSrcData = data_buf
            stConvertParam.nSrcDataLen = stDeviceList.nFrameLen
            stConvertParam.enSrcPixelType = stDeviceList.enPixelType
            stConvertParam.enDstPixelType = PixelType_Gvsp_RGB8_Packed
            stConvertParam.pDstBuffer = (c_ubyte * nRGBSize)()
            stConvertParam.nDstBufferSize = nRGBSize

            # 进行数据类型转换
            if cam.MV_CC_ConvertPixelType(stConvertParam) != 0:
                del data_buf

            self.__dataBuff = (c_ubyte * stConvertParam.nDstLen)()
            cdll.msvcrt.memcpy(byref(self.__dataBuff), stConvertParam.pDstBuffer, stConvertParam.nDstLen)

            # 如果这区成功，初始化界面
            self.__scene.setSceneRect(0, 0, stDeviceList.nWidth, stDeviceList.nHeight)
            # 记录图片宽高
            self.__imageWidth = stDeviceList.nWidth
            self.__imageHeight = stDeviceList.nHeight
            # 将图片容器放入其中
            self.__scene.addItem(self.__pixmapItem)
            # 显示
            self.graphicsView.show()

            # test
            self.ShowStreamImageSlot()

        else:
            return

        # 启动取流线程
        try:
            # hThreadHandle = threading.Thread(target=self.LiveStreamingThread,
            #                                  args=(cam, byref(self.__dataBuff), nPayloadSize))

            # 反转标识
            self.__isLiveStreaming = True

            # hThreadHandle.start()
        except:
            self.__isLiveStreaming = False

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

    def LiveStreamingThread(self, cam=0, pData=0, nDataSize=0):
        """取流的独立工作线程"""

        # 流信息容器
        stFrameInfo = MV_FRAME_OUT_INFO_EX()
        # 内存拷贝
        memset(byref(stFrameInfo), 0, sizeof(stFrameInfo))
        # 线程工作方式
        while True:
            self.__lock.lock()
            if cam.MV_CC_GetOneFrameTimeout(pData, nDataSize, stFrameInfo, 1000) == 0:
                # 解析图片流
                data = list(self.__dataBuff).copy()

                # 解析并填装
                count = 0
                for line in range(0, self.__imageHeight, 8):
                    for point in range(0, self.__imageWidth, 8):
                        pixel = int(255 - (data[count] + data[count + 2] + data[count + 4] + data[count + 8]) / 4)
                        # print("pixel = ", pixel)
                        color = QtGui.QColor(pixel, pixel, pixel)
                        count = line * point + point
                        print(point / 8, line / 8)
                        self.__img.setPixel(point / 8, line / 8, color.rgb())

                # 放出信号，表示取流成功
                print("0" * 10)
                self.LiveStreamingSccessSignal.emit()
            else:
                continue
            self.__lock.unlock()

            if self.__isLiveStreaming == False:
                break

    def ShowStreamImageSlot(self):
        """将获取的图片流显示到UI"""

        self.__lock.lock()

        # 转换格式
        img_byte_arry = bytearray(self.__dataBuff)
        image = QtGui.QImage(img_byte_arry, self.__imageHeight, self.__imageWidth, QtGui.QImage.Format_RGB888)

        # 显示
        pixmap = QtGui.QPixmap.fromImage(image)
        self.__pixmapItem.setPixmap(pixmap)
        self.graphicsView.show()

        self.__lock.unlock()
