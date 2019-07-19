# coding=utf8

from SoftWare.UIModular.MainWindow.StatusBarWidget import StatusBarWidgetModify


class StatusBarWidget(StatusBarWidgetModify):
    def __init__(self, parent=None):
        """构造方法"""

        # 父类构造方法
        super(StatusBarWidget, self).__init__()