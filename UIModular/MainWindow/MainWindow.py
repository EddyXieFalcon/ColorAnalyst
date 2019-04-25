# coding=utf8

from UIModular.MainWindow.MainWindowModify import MainWindowModify
from UIModular.MainWindow.FunctionWidget.HomeWidget.HomeWidget import HomeWidget
from UIModular.MainWindow.FunctionWidget.ProtocolsWidget.ProtocolsWidget import ProtocolsWidget


class MainWindow(MainWindowModify):
    def __init__(self, parent=None):
        """构造方法"""

        # 父类构造方法
        super(MainWindow, self).__init__()

        # 将所有的子界面放入MainWindow中，并用字典管理
        self.__functionWidgetDict = {}
        self.__homeWidget = HomeWidget(self.widgetFunction)
        self.gridLayout_3.addWidget(self.__homeWidget, 0, 0, 1, 1)
        self.__functionWidgetDict[self.pushButtonHome] = self.__homeWidget
        self.__protocolsWidget = ProtocolsWidget(self.widgetFunction)
        self.gridLayout_3.addWidget(self.__protocolsWidget, 0, 0, 1, 1)
        self.__functionWidgetDict[self.pushButtonProtocols] = self.__protocolsWidget

        # 将所有的子界面隐藏，默认显示第一个界面
        self.HideAllFunctionWidget()
        self.__homeWidget.show()

        # 将按钮与子界面的关联
        for buttom in self.__functionWidgetDict:
            buttom.clicked.connect(self.ShowFunctionWidget)

        # 创建硬件管理类
        # self.__device = Device()

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
