# /usr/bin/python3
# coding=utf8

import sys
from PyQt5.QtWidgets import QApplication
from SoftWare.UIModular.MainWindow.MainWindow import MainWindow


def main():
    # 创建事件
    app = QApplication(sys.argv)

    # 创建ui
    ui = MainWindow()

    # 显示ui界面
    ui.showMaximized()
    # ui.show()

    # 进入消息循环
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()


