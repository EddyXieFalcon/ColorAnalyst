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

        # 配置生效按钮
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
        self.WriteSettingToFile("AcquisitionFrameRate", self.__fps, self.spinBoxFPS.value())
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
        self.WriteSettingToFile("ExposureTime", self.__exposureTime, self.spinBoxExposureTime.value())
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
        self.WriteSettingToFile("Gain", self.__gain, self.spinBoxGain.value())
        # 新数据记录
        self.__gain = self.spinBoxGain.value()

    def OnBtnGammaClickedSlot(self):
        """是否打开伽马"""
        # 写入文件
        if self.__gamaEnable:
            self.WriteSettingToFile("GammaEnable", "1", "0")
        else:
            self.WriteSettingToFile("GammaEnable", "0", "1")
        self.__gamaEnable = not self.__gamaEnable

    def OnSpinBoxGammaValueChangedSlot(self):
        """伽马大小"""
        # 写入文件
        self.WriteSettingToFile("Gamma", self.__gama, self.spinBoxGamma.value())
        # 新数据记录
        self.__gama = self.spinBoxGamma.value()

    def OnBtnBlackLevelClickedSlot(self):
        """是否打开Black Level"""
        self.__blackLevelEnable = not self.__blackLevelEnable

    def OnSpinBoxBlackLevelValueChangedSlot(self):
        """Black Level大小"""
        self.__blackLevel = self.spinBoxBlackLevel.value()

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
                    # 读取伽马大小
                    elif "Gamma\t" in line:
                        self.spinBoxGamma.setValue(float(line.split("\t")[-1]))
                        self.__gama = self.spinBoxGamma.value()
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

                # 读取单行，一般第一行都是废话，无需处理
                line = featureFile.readline()
                newFile += line

                # 对剩下的每一行循环遍历处理
                while line:
                    if (parameterName + "\t") in line:
                        line = line.replace(oldParameterValue, newParameterValue)
                    newFile += line
                    line = featureFile.readline()
                newFile += line

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

        # ch:从文件中导入相机属性 | en:Import the camera properties from the file
        if MV_OK != cam.MV_CC_FeatureLoad("FeatureFile.ini"):
            return

        # ch:关闭设备 | Close device
        if cam.MV_CC_CloseDevice() != 0:
            return

        # ch:销毁句柄 | Destroy handle
        if cam.MV_CC_DestroyHandle() != 0:
            return