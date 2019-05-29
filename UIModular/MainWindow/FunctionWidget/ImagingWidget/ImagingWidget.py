# coding=utf8

from UIModular.MainWindow.FunctionWidget.ImagingWidget.ImagingWidgetModify import ImagingWidgetModify


class ImagingWidget(ImagingWidgetModify):
    def __init__(self, parent=None):
        """构造方法"""

        # 父类构造方法
        super(ImagingWidget, self).__init__()

        ######### 基本属性 #########
        # 帧率
        self.spinBoxFPS.valueChanged.connect(self.OnSpinBoxFPSValueChangedSlot)
        # 自动曝光
        self.btnAutoExposureOn.clicked.connect(self.OnBtnAutoExposureClickedSlot)
        self.btnAutoExposureOff.clicked.connect(self.OnBtnAutoExposureClickedSlot)

    def OnSpinBoxFPSValueChangedSlot(self):
        """帧率"""

        pass

    def OnBtnAutoExposureClickedSlot(self):
        """自动曝光"""

        print(self.btnAutoExposureOn.isChecked(), self.btnAutoExposureOff.isChecked())