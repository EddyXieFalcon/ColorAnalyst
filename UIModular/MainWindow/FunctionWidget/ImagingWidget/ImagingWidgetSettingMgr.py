# coding=utf8

from UIModular.MainWindow.FunctionWidget.ImagingWidget.ImagingWidgetModify import ImagingWidgetModify


class ImagingWidgetSettingMgr(ImagingWidgetModify):

    def __init__(self, parent=None):
        """构造方法"""

        # 父类构造方法
        super(ImagingWidgetSettingMgr, self).__init__()

        # 界面初始化的时候，所有的参数可用
        self.SetAllParameterEnable(True)

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

    def SetAllParameterEnable(self, enable):
        """设置所有的参数是否可用"""
        self.SetBaseParameterEnable(enable)
        self.SetImageParameterEnable(enable)
        self.SetDoActiviteEnable(enable)

    def SetBaseParameterEnable(self, enable):
        """设置基本参数是否可用"""

        # 所有的基本属性参数设置
        self.spinBoxFPS.setEnabled(enable)
        self.spinBoxGain.setEnabled(enable)
        self.spinBoxGamma.setEnabled(enable)
        self.spinBoxBlackLevel.setEnabled(enable)

        # 所有的基本属性开关
        self.btnAutoExposureOn.setEnabled(enable)
        self.btnAutoExposureOff.setEnabled(enable)
        self.btnGainOn.setEnabled(enable)
        self.btnGainOff.setEnabled(enable)
        self.btnGammaOn.setEnabled(enable)
        self.btnGammaOff.setEnabled(enable)
        self.btnBlackLevelOn.setEnabled(enable)
        self.btnBlackLevelOff.setEnabled(enable)

    def SetDoActiviteEnable(self, enable):
        """设置按钮是否能用"""

        self.progressBarForSetting.setEnabled(enable)
        self.btnDoActivite.setEnabled(enable)

    def SetImageParameterEnable(self, enable):
        """设置图片参数是否可用"""

        # 所有的图像属性参数设置
        self.spinBoxWidth.setEnabled(enable)
        self.spinBoxHeight.setEnabled(enable)
        self.spinBoxOffsetX.setEnabled(enable)
        self.spinBoxOffsetY.setEnabled(enable)
        self.spinBoxBinningX.setEnabled(enable)
        self.spinBoxBinningY.setEnabled(enable)

        # 所有的图像属性开关
        self.btnReverseXOn.setEnabled(enable)
        self.btnReverseXOff.setEnabled(enable)

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

