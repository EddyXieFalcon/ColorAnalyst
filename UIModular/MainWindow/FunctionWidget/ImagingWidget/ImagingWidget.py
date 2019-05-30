# coding=utf8

from PyQt5 import QtWidgets
from UIModular.MainWindow.FunctionWidget.ImagingWidget.ImagingWidgetModify import ImagingWidgetModify


class ImagingWidget(ImagingWidgetModify):
    def __init__(self, parent=None):
        """构造方法"""

        # 父类构造方法
        super(ImagingWidget, self).__init__()

        ######### 界面处理 #########
        self.__scene = QtWidgets.QGraphicsScene()#创建视口的场景
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
