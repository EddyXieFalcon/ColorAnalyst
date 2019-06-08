# coding=utf8

from ThirdParty.MVS.MvImport.MvCameraControl_class import *
from UIModular.MainWindow.FunctionWidget.ImagingWidget.ImagingWidgetModify import ImagingWidgetModify


class ImagingWidgetSettingMgr(ImagingWidgetModify):

    def __init__(self, parent=None):
        """构造方法"""

        # 父类构造方法
        super(ImagingWidgetSettingMgr, self).__init__()

        ######### 基本属性 #########
        # 帧率
        self.__fps = self.spinBoxFPS.value()
        self.spinBoxFPS.valueChanged.connect(self.OnSpinBoxFPSValueChangedSlot)
        # 曝光
        self.__autoExposureEnable = True
        self.__exposureTime = self.spinBoxExposureTime.value()
        self.btnAutoExposureOn.clicked.connect(self.OnBtnAutoExposureClickedSlot)
        self.btnAutoExposureOff.clicked.connect(self.OnBtnAutoExposureClickedSlot)
        self.spinBoxExposureTime.valueChanged.connect(self.OnSpinBoxExposureTimeValueChangedSlot)
        # 增益
        self.__gainEnable = True
        self.__gain = self.spinBoxGain.value()
        self.btnGainOn.clicked.connect(self.OnBtnGainClickedSlot)
        self.btnGainOff.clicked.connect(self.OnBtnGainClickedSlot)
        self.spinBoxGain.valueChanged.connect(self.OnSpinBoxGainValueChangedSlot)
        # 伽马
        self.__gamaEnable = True
        self.__gama = self.spinBoxGamma.value()
        self.btnGammaOn.clicked.connect(self.OnBtnGammaClickedSlot)
        self.btnGammaOff.clicked.connect(self.OnBtnGammaClickedSlot)
        self.spinBoxGamma.valueChanged.connect(self.OnSpinBoxGammaValueChangedSlot)
        # Black Level
        self.__blackLevelEnable = True
        self.__blackLevel = self.spinBoxBlackLevel.value()
        self.btnBlackLevelOn.clicked.connect(self.OnBtnBlackLevelClickedSlot)
        self.btnBlackLevelOff.clicked.connect(self.OnBtnBlackLevelClickedSlot)
        self.spinBoxBlackLevel.valueChanged.connect(self.OnSpinBoxBlackLevelValueChangedSlot)

        ######### 图像属性 #########
        # 宽度
        self.__width = self.spinBoxWidth.value()
        self.spinBoxWidth.valueChanged.connect(self.OnSpinBoxWidthValueChangedSlot)
        # 高度
        self.__height = self.spinBoxHeight.value()
        self.spinBoxHeight.valueChanged.connect(self.OnSpinBoxHeightValueChangedSlot)
        # Offset X
        self.__offsetX = self.spinBoxOffsetX.value()
        self.spinBoxOffsetX.valueChanged.connect(self.OnSpinBoxOffsetXValueChangedSlot)
        # Offset Y
        self.__offsetY = self.spinBoxOffsetY.value()
        self.spinBoxOffsetY.valueChanged.connect(self.OnSpinBoxOffsetYValueChangedSlot)
        # Reverse X
        self.__reverseX = True
        self.btnReverseXOn.clicked.connect(self.OnBtnReverseXClickedSlot)
        self.btnReverseXOff.clicked.connect(self.OnBtnReverseXClickedSlot)

        # 配置生效按钮的槽函数
        self.btnDoActivite.clicked.connect(self.SetSettingFileToDevice)

        # 读取配置文件
        self.GetSettingFileFormDevice()
        self.ReadSettingFromFile()

    def SetDoActiviteEnable(self, enable):
        """设置按钮是否能用"""
        self.btnDoActivite.setEnabled(enable)

    def OnSpinBoxFPSValueChangedSlot(self):
        """帧率"""
        # 写入文件
        self.WriteSettingToFile("AcquisitionFrameRate", str(self.__fps), str(self.spinBoxFPS.value()))
        # 新数据记录
        self.__fps = self.spinBoxFPS.value()

    def OnBtnAutoExposureClickedSlot(self):
        """自动曝光"""
        # 写入文件
        if self.__autoExposureEnable:
            self.WriteSettingToFile("ExposureAuto", "On", "Off")
        else:
            self.WriteSettingToFile("ExposureAuto", "Off", "On")
        # 新数据记录
        self.__autoExposureEnable = not self.__autoExposureEnable

    def OnSpinBoxExposureTimeValueChangedSlot(self):
        """曝光时间"""
        # 写入文件
        self.WriteSettingToFile("ExposureTime", str(self.__exposureTime), str(self.spinBoxExposureTime.value()))
        # 新数据记录
        self.__exposureTime = self.spinBoxExposureTime.value()

    def OnBtnGainClickedSlot(self):
        """是否打开增益"""
        # 写入文件
        if self.__gainEnable:
            self.WriteSettingToFile("GainAuto", "On", "Off")
        else:
            self.WriteSettingToFile("GainAuto", "Off", "On")
        # 新数据记录
        self.__gainEnable = not self.__gainEnable

    def OnSpinBoxGainValueChangedSlot(self):
        """增益大小"""
        # 写入文件
        self.WriteSettingToFile("Gain", str(self.__gain), str(self.spinBoxGain.value()))
        # 新数据记录
        self.__gain = self.spinBoxGain.value()

    def OnBtnGammaClickedSlot(self):
        """是否打开伽马"""
        # 写入文件
        if self.__gamaEnable:
            self.WriteSettingToFile("GammaEnable", "1", "0")
        else:
            self.WriteSettingToFile("GammaEnable", "0", "1")
        # 新数据记录
        self.__gamaEnable = not self.__gamaEnable

    def OnSpinBoxGammaValueChangedSlot(self):
        """伽马大小"""
        # 写入文件
        self.WriteSettingToFile("Gamma", str(self.__gama), str(self.spinBoxGamma.value()))
        # 新数据记录
        self.__gama = self.spinBoxGamma.value()

    def OnBtnBlackLevelClickedSlot(self):
        """是否打开Black Level"""
        # 写入文件
        if self.__blackLevelEnable:
            self.WriteSettingToFile("BlackLevelEnable", "1", "0")
        else:
            self.WriteSettingToFile("BlackLevelEnable", "0", "1")
        # 新数据记录
        self.__blackLevelEnable = not self.__blackLevelEnable

    def OnSpinBoxBlackLevelValueChangedSlot(self):
        """Black Level大小"""
        # 写入文件
        self.WriteSettingToFile("BlackLevel", str(self.__blackLevel), str(self.spinBoxBlackLevel.value()))
        # 新数据记录
        self.__blackLevel = self.spinBoxBlackLevel.value()

    def OnSpinBoxWidthValueChangedSlot(self):
        """宽度"""
        # 写入文件
        self.WriteSettingToFile("AutoFunctionAOIWidth", str(self.__width), str(self.spinBoxWidth.value()))
        # 新数据记录
        self.__width = self.spinBoxWidth.value()

    def OnSpinBoxHeightValueChangedSlot(self):
        """高度"""
        # 写入文件
        self.WriteSettingToFile("AutoFunctionAOIHeight", str(self.__height), str(self.spinBoxHeight.value()))
        # 新数据记录
        self.__height = self.spinBoxHeight.value()

    def OnSpinBoxOffsetXValueChangedSlot(self):
        """Offset X"""
        # 写入文件
        self.WriteSettingToFile("AutoFunctionAOIOffsetX", str(self.__offsetX), str(self.spinBoxOffsetX.value()))
        # 新数据记录
        self.__offsetX = self.spinBoxOffsetX.value()

    def OnSpinBoxOffsetYValueChangedSlot(self):
        """Offset X"""
        # 写入文件
        self.WriteSettingToFile("AutoFunctionAOIOffsetY", str(self.__offsetY), str(self.spinBoxOffsetY.value()))
        # 新数据记录
        self.__offsetY = self.spinBoxOffsetY.value()

    def OnBtnReverseXClickedSlot(self):
        """是否打开Reverse X"""
        # 写入文件
        if self.__reverseX:
            self.WriteSettingToFile("ReverseX", "1", "0")
        else:
            self.WriteSettingToFile("ReverseX", "0", "1")
        # 新数据记录
        self.__reverseX = not self.__reverseX

    def ReadSettingFromFile(self):
        """读取配置文件中的参数"""

        try:
            # 尝试打开ini文件
            with open("FeatureFile.ini", 'r') as featureFile:
                # 读取单行，一般第一行都是废话，无需处理
                line = featureFile.readline()

                # 对剩下的每一行循环遍历处理
                while line:
                    # 读取帧率
                    if "AcquisitionFrameRate\t" in line:
                        self.spinBoxFPS.setValue(float(line.split("\t")[-1]))
                        self.__fps = self.spinBoxFPS.value()
                    # 读取是否自动曝光
                    elif "ExposureAuto\t" in line:
                        # 如果是关闭
                        if line.split("\t")[-1] == "Off\n":
                            self.btnAutoExposureOff.setChecked(True)
                            self.__autoExposureEnable = False
                        # 如果是打开
                        elif line.split("\t")[-1] == "Off\n":
                            self.btnAutoExposureOn.setChecked(True)
                            self.__autoExposureEnable = True
                        self.spinBoxExposureTime.setDisabled(self.__autoExposureEnable)
                    # 读取曝光时间
                    elif "ExposureTime\t" in line:
                        self.spinBoxExposureTime.setValue(float(line.split("\t")[-1]))
                        self.__exposureTime = self.spinBoxExposureTime.value()
                    # 读取是否打开增益
                    elif "GainAuto\t" in line:
                        # 如果是关闭
                        if line.split("\t")[-1] == "Off\n":
                            self.btnGainOff.setChecked(True)
                            self.__gainEnable = False
                        # 如果是打开
                        elif line.split("\t")[-1] == "Off\n":
                            self.btnGainOn.setChecked(True)
                            self.__gainEnable = True
                        self.spinBoxGain.setDisabled(self.__gainEnable)
                    # 读取增益大小
                    elif "Gain\t" in line:
                        self.spinBoxGain.setValue(float(line.split("\t")[-1]))
                        self.__gain = self.spinBoxGain.value()
                    # 是否打开伽马
                    elif "GammaEnable" in line:
                        # 如果是关闭
                        if not line.split("\t")[-1]:
                            self.btnGammaOff.setChecked(True)
                            self.__gamaEnable = False
                        # 如果是打开
                        elif line.split("\t")[-1]:
                            self.btnGammaOn.setChecked(True)
                            self.__gamaEnable = True
                        self.spinBoxGamma.setDisabled(self.__gamaEnable)
                    # 读取伽马大小
                    elif "Gamma\t" in line:
                        self.spinBoxGamma.setValue(float(line.split("\t")[-1]))
                        self.__gama = self.spinBoxGamma.value()
                    # 是否打开BlackLevel
                    elif "BlackLevelEnable" in line:
                        # 如果是关闭
                        if not line.split("\t")[-1]:
                            self.btnBlackLevelOff.setChecked(True)
                            self.__blackLevelEnable = False
                        # 如果是打开
                        elif line.split("\t")[-1]:
                            self.btnBlackLevelOn.setChecked(True)
                            self.__blackLevelEnable = True
                        self.spinBoxBlackLevel.setDisabled(self.__blackLevelEnable)
                    # 读取BlackLevel大小
                    elif "BlackLevel\t" in line:
                        self.spinBoxBlackLevel.setValue(int(line.split("\t")[-1]))
                        self.__blackLevel = self.spinBoxBlackLevel.value()
                    # 读取宽度大小
                    elif "AutoFunctionAOIWidth\t" in line:
                        self.spinBoxWidth.setValue(int(line.split("\t")[-1]))
                        self.__width = self.spinBoxWidth.value()
                    # 读取高度大小
                    elif "AutoFunctionAOIHeight\t" in line:
                        self.spinBoxHeight.setValue(int(line.split("\t")[-1]))
                        self.__height = self.spinBoxHeight.value()
                    # 读取OffsetX大小
                    elif "AutoFunctionAOIOffsetX\t" in line:
                        self.spinBoxOffsetX.setValue(int(line.split("\t")[-1]))
                        self.__offsetX = self.spinBoxOffsetX.value()
                    # 读取OffsetY大小
                    elif "AutoFunctionAOIOffsetY\t" in line:
                        self.spinBoxOffsetY.setValue(int(line.split("\t")[-1]))
                        self.__offsetY = self.spinBoxOffsetY.value()
                    # 是否打开ReverseX
                    elif "ReverseX" in line:
                        # 如果是关闭
                        if not line.split("\t")[-1]:
                            self.btnReverseXOff.setChecked(True)
                            self.__reverseX = False
                        # 如果是打开
                        elif line.split("\t")[-1]:
                            self.btnReverseXOn.setChecked(True)
                            self.__reverseX = True
                    else:
                        pass

                    line = featureFile.readline()
        except:
            pass

    def WriteSettingToFile(self, parameterName, oldParameterValue, newParameterValue):
        """将参数写入配置文件"""

        try:
            # 准备新文件容器
            newFile = ""

            # 尝试打开ini文件，查询参数
            with open("FeatureFile.ini", 'r') as featureFile:

                # 新旧文本行
                oldLine = parameterName + "\t" + oldParameterValue
                newLine = parameterName + "\t" + newParameterValue

                # 读取单行，一般第一行都是废话，无需处理
                oldFile = featureFile.read()
                newFile += oldFile.replace(oldLine, newLine)

            # 将新数据写入文件
            with open("FeatureFile.ini", 'w') as featureFile:
                featureFile.write(newFile)
        except:
            pass

    def GetSettingFileFormDevice(self):
        """从硬件中将设置读取出来，然后保存至文件中"""

        deviceList = MV_CC_DEVICE_INFO_LIST()
        tlayerType = MV_GIGE_DEVICE | MV_USB_DEVICE

        # ch:枚举设备 | en:Enum device
        if MvCamera.MV_CC_EnumDevices(tlayerType, deviceList) != 0:
            return

        if deviceList.nDeviceNum == 0:
            return

        if 0 >= deviceList.nDeviceNum:
            return

        # ch:创建相机实例 | en:Creat Camera Object
        cam = MvCamera()

        # ch:选择设备并创建句柄 | en:Select device and create handle
        if cam.MV_CC_CreateHandle(cast(deviceList.pDeviceInfo[0], POINTER(MV_CC_DEVICE_INFO)).contents) != 0:
            return

        # ch:打开设备 | en:Open device
        if cam.MV_CC_OpenDevice(MV_ACCESS_Exclusive, 0) != 0:
            return

        # ch:打开设备 | en:Open device
        if cam.MV_CC_OpenDevice(MV_ACCESS_Exclusive, 0) != 0:
            return

        # ch:将相机属性导出到文件中 | en:Export the camera properties to the file
        if MV_OK != cam.MV_CC_FeatureSave("FeatureFile.ini"):
            return

        # ch:关闭设备 | Close device
        if cam.MV_CC_CloseDevice() != 0:
            return

        # ch:销毁句柄 | Destroy handle
        if cam.MV_CC_DestroyHandle() != 0:
            return

    def SetSettingFileToDevice(self):
        """将设置文件的配置写入硬件中"""

        deviceList = MV_CC_DEVICE_INFO_LIST()
        tlayerType = MV_GIGE_DEVICE | MV_USB_DEVICE

        # ch:枚举设备 | en:Enum device
        if MvCamera.MV_CC_EnumDevices(tlayerType, deviceList) != 0:
            return

        if deviceList.nDeviceNum == 0:
            return

        if 0 >= deviceList.nDeviceNum:
            return

        # ch:创建相机实例 | en:Creat Camera Object
        cam = MvCamera()

        # ch:选择设备并创建句柄 | en:Select device and create handle
        if cam.MV_CC_CreateHandle(cast(deviceList.pDeviceInfo[0], POINTER(MV_CC_DEVICE_INFO)).contents) != 0:
            return

        # ch:打开设备 | en:Open device
        if cam.MV_CC_OpenDevice(MV_ACCESS_Exclusive, 0) != 0:
            return

        # ch:将相机属性导出到文件中 | en:Export the camera properties to the file
        if MV_OK != cam.MV_CC_FeatureSave("FeatureFile.ini"):
            return

        # ch:关闭设备 | Close device
        if cam.MV_CC_CloseDevice() != 0:
            return

        # ch:销毁句柄 | Destroy handle
        if cam.MV_CC_DestroyHandle() != 0:
            return
