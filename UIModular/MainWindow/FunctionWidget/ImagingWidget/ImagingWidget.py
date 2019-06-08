# coding=utf8

import msvcrt
import threading

from ctypes import *

from ThirdParty.MVS.MvImport.MvCameraControl_class import *
from ThirdParty.MVS.MvImport.MvCameraControl_header import *
from ThirdParty.MVS.MvImport.CameraParams_const import *

from PyQt5 import QtWidgets, QtGui, QtCore
from UIModular.MainWindow.FunctionWidget.ImagingWidget.ImagingWidgetSettingMgr import ImagingWidgetSettingMgr


class ImagingWidget(ImagingWidgetSettingMgr):
    LiveStreamingSccessSignal = QtCore.pyqtSignal()

    def __init__(self, parent=None):
        """构造方法"""

        # 父类构造方法
        super(ImagingWidget, self).__init__()

        # 界面初始化的时候，算法按钮不可用
        self.SetDoAlgorithmEnable(False)

        ######### 界面处理 #########
        self.__imageWidth = 0  # 图片宽度
        self.__imageHeight = 0  # 图片高度
        self.__image = QtGui.QImage()  # 图片对象
        self.__pixmap = QtGui.QPixmap()  # 图片像素集对象
        self.__pixmapItem = QtWidgets.QGraphicsPixmapItem()  # 图片图元
        self.__scene = QtWidgets.QGraphicsScene()  # 创建视口的场景
        self.graphicsView.setScene(self.__scene)  # 将视口与场景绑定

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

        ######### 激光控制 #########
        # 标识符，激光是否打开
        self.__isOpenLaser = False
        self.btnLaserMgr.clicked.connect(self.OnBtnLaserMgrClicked)

    def SetDoAlgorithmEnable(self, enable):
        """设置按钮是否能用"""

        self.btnDoAlgorithm.setEnabled(enable)

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
        # 先抓取一帧，用于初始化界面
        if cam.MV_CC_GetOneFrameTimeout(byref(data_buf), nPayloadSize, stDeviceList, 1000) == 0:
            # 初始化界面
            self.__scene.setSceneRect(0, 0, stDeviceList.nWidth / 8, stDeviceList.nHeight / 8)

            # 记录图片宽高
            self.__imageWidth = stDeviceList.nWidth
            self.__imageHeight = stDeviceList.nHeight

            # 将图片容器放入其中
            self.__scene.addItem(self.__pixmapItem)

            # 显示
            self.graphicsView.show()
            self.ShowStreamImageSlot()

            # 删除缓冲区
            del data_buf

        # 启动取流线程
        try:
            # 创建取流的线程
            hThreadHandle = threading.Thread(target=self.LiveStreamingThread, args=(cam, nPayloadSize))

            # 反转标识
            self.__isLiveStreaming = True

            # 禁用参数设置
            self.SetDoActiviteEnable(False)

            # 算法不可用
            self.SetDoAlgorithmEnable(False)

            # 启动线程，取流
            hThreadHandle.start()

        except:
            self.__isLiveStreaming = False
            self.SetDoActiviteEnable(True)

    def OnBtnCaptureClickedSlot(self):
        """抓取"""

        # 首先判断是否处于取流状态中，如果非取流状态，直接退出
        if not self.__isLiveStreaming:
            return

        # 先停止取流
        self.__lock.lock()
        self.__isLiveStreaming = False
        self.SetDoActiviteEnable(True)
        self.__lock.unlock()

        # 算法可用
        self.SetDoAlgorithmEnable(True)

    def OnBtnSaveAsClickedSlot(self):
        """保存"""

        # 如果还处在去留状态中，停止取流
        if self.__isLiveStreaming:
            self.__lock.lock()
            self.__isLiveStreaming = False
            self.SetDoActiviteEnable(True)
            self.__lock.unlock()

        # 弹出对话框，保存图片
        pictrureName, type = QtWidgets.QFileDialog.getSaveFileName(self, u"文件保存", "./", "Image Files(*.jpg)")

        # 保存图片
        self.__image.save(pictrureName, "JPG", 100)

        # 算法可用
        self.SetDoAlgorithmEnable(True)

    def OnBtnLoadClickedSlot(self):
        """载入"""

        # 如果在取流，退出
        if self.__isLiveStreaming:
            return

        # 获取打开的文件
        pictrureName, type = QtWidgets.QFileDialog.getOpenFileName(self, u"打开文件", "./", "Image Files(*.jpg)")

        # 加载文件
        self.__image = QtGui.QImage(pictrureName)

        # 显示图片
        self.__pixmap = QtGui.QPixmap.fromImage(self.__image.scaled(self.__image.width() / 8, self.__image.height() / 8))
        self.__pixmapItem.setPixmap(self.__pixmap)
        self.__scene.setSceneRect(0, 0, self.__image.width() / 8, self.__image.height() / 8)
        self.__scene.addItem(self.__pixmapItem)
        self.graphicsView.show()

        # 算法可用
        self.SetDoAlgorithmEnable(True)

    def LiveStreamingThread(self, cam=0, nPayloadSize=0):
        """取流的独立线程"""

        # 创建设备信息列表数据结构体
        stDeviceList = MV_FRAME_OUT_INFO_EX()
        # 为上述数据结构体填装数据
        memset(byref(stDeviceList), 0, sizeof(stDeviceList))
        # 创建数据缓冲区
        data_buf = (c_ubyte * nPayloadSize)()

        # 线程工作方式
        while True:
            # 停止取流
            if not self.__isLiveStreaming:
                break

            self.__lock.lock()
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

                # 转换格式，解析并填装
                img_buff = (c_ubyte * stConvertParam.nDstLen)()
                cdll.msvcrt.memcpy(byref(img_buff), stConvertParam.pDstBuffer, stConvertParam.nDstLen)
                img_byte_arry = bytearray(img_buff)
                self.__image = QtGui.QImage(img_byte_arry, self.__imageWidth, self.__imageHeight, QtGui.QImage.Format_RGB888)
                self.__pixmap = QtGui.QPixmap.fromImage(self.__image.scaled(self.__imageWidth / 8, self.__imageHeight / 8))

                # 放出信号，表示取流成功
                self.LiveStreamingSccessSignal.emit()
            else:
                continue
            self.__lock.unlock()

            # 停止取流
            if not self.__isLiveStreaming:
                # ch:停止取流 | en:Stop grab image
                if cam.MV_CC_StopGrabbing() != 0:
                    del img_buff
                    return

                # ch:关闭设备 | Close device
                if cam.MV_CC_CloseDevice() != 0:
                    del img_buff
                    return

                # ch:销毁句柄 | Destroy handle
                if cam.MV_CC_DestroyHandle() != 0:
                    return
                self.SetDoActiviteEnable(True)
                del img_buff

    def ShowStreamImageSlot(self):
        """将获取的图片流显示到UI"""

        self.__lock.lock()

        # 显示
        self.__pixmapItem.setPixmap(self.__pixmap)
        self.graphicsView.show()

        self.__lock.unlock()

    def OnBtnLaserMgrClicked(self):
        """激光控制按钮"""

        # 如果激光当前处于开启状态
        if self.__isOpenLaser:
            # 关闭激光
            pass
        # 如果激光当前处于关闭状态
        else:
            # 打开激光
            pass

        # 反转标识状态
        self.__isOpenLaser = not self.__isOpenLaser