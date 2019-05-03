# coding=utf8

from UIModular.MainWindow.FunctionWidget.SamplingWidget.SamplingWidgetModify import SamplingWidgetModify


class SamplingWidget(SamplingWidgetModify):
    def __init__(self, parent=None):
        """构造方法"""

        # 父类构造方法
        super(SamplingWidget, self).__init__()

        # 五个安娜牛的槽函数
        self.pushButton_load.clicked.connect(self.on_pushbutton_load_clicked_slot)
        self.pushButton_export.clicked.connect(self.on_pushbutton_export_clicked_slot)
        self.pushButton_add.clicked.connect(self.on_pushbutton_add_clicked_slot)
        self.pushButton_remove.clicked.connect(self.on_pushbutton_remove_clicked_slot)
        self.pushButton_edit.clicked.connect(self.on_pushbutton_edit_clicked_slot)
        self.pushButton_DoIt.clicked.connect(self.on_pushbutton_Doit_clicked_slot)

    def on_pushbutton_load_clicked_slot(self):
        """加载文件"""
        pass

    def on_pushbutton_export_clicked_slot(self):
        """导出实验"""
        pass

    def on_pushbutton_add_clicked_slot(self):
        """添加命令"""
        pass

    def on_pushbutton_remove_clicked_slot(self):
        """删除命令"""
        pass

    def on_pushbutton_edit_clicked_slot(self):
        """编辑命令"""
        pass

    def on_pushbutton_Doit_clicked_slot(self):
        """执行脚本"""
        pass