# coding=utf8

from SoftWare.UIModular.MainWindow.FunctionWidget.ProtocolsWidget import ProtocolsWidgetModify
from SoftWare.UIModular.MainWindow.FunctionWidget.ProtocolsWidget.SettingsWidget import SettingsWidget
from SoftWare.UIModular.MainWindow.FunctionWidget.ProtocolsWidget import AnalytesWidget
from SoftWare.UIModular.MainWindow.FunctionWidget.ProtocolsWidget import PlateLayoutWidget


class ProtocolsWidget(ProtocolsWidgetModify):
    def __init__(self, parent=None):
        """构造方法"""

        # 父类构造方法
        super(ProtocolsWidget, self).__init__()

        # 将所有的子界面放入MainWindow中，并用字典管理
        self.__functionWidgetDict = {}
        self.__settingsWidget = SettingsWidget(self.widgetFunction)
        self.gridLayout.addWidget(self.__settingsWidget, 0, 0, 1, 1)
        self.__functionWidgetDict[self.pushButtonSettings] = self.__settingsWidget

        self.__analytesWidget = AnalytesWidget(self.widgetFunction)
        self.gridLayout.addWidget(self.__analytesWidget, 0, 0, 1, 1)
        self.__functionWidgetDict[self.pushButtonAnalytes] = self.__analytesWidget

        self.__plateLayoutWidget = PlateLayoutWidget(self.widgetFunction)
        self.gridLayout.addWidget(self.__plateLayoutWidget, 0, 0, 1, 1)
        self.__functionWidgetDict[self.pushButtonPlateLayout] = self.__plateLayoutWidget

        # 将所有的子界面隐藏，默认显示第一个界面
        self.HideAllFunctionWidget()
        self.__settingsWidget.show()

        # 将按钮与子界面的关联
        for buttom in self.__functionWidgetDict:
            buttom.clicked.connect(self.ShowFunctionWidget)

    def HideAllFunctionWidget(self):
        """隐藏所有的子界面"""

        # 循环遍子界面管理字典
        for buttom in self.__functionWidgetDict:
            self.__functionWidgetDict[buttom].hide()

    def ShowFunctionWidget(self):
        """当按钮点击的时候，显示对应的子界面"""

        # 将所有的子界面隐藏
        self.HideAllFunctionWidget()

        # 显示电机的按钮对应的子界面
        self.__functionWidgetDict[self.sender()].show()