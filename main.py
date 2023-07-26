import sys
import os
from PySide6.QtWidgets import *
from PySide6.QtGui import *
from PySide6.QtCore import *
from myUi import Ui_MainWindow
from model import model


class Singnals(QThread):
    singnal_1 = Signal()

    def run(self):
        while True:
            self.singnal_1.emit()
            self.sleep(1)


class Main(QMainWindow):

    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.adjust_style()

        # 数据
        self.data = model()
        self.signals = Singnals()
        self.signals.singnal_1.connect(self.update_data)
        self.signals.start()

        # 初始化系统托盘相关的对象和菜单项
        self._quit_action = QAction("exit", self)
        self._quit_action.triggered.connect(
            QApplication.quit)  # "退出"菜单项触发退出应用程序的操作

        # 创建菜单
        self._tray_icon_menu = QMenu(self)
        self._tray_icon_menu.addAction(self._quit_action)

        # 创建系统托盘图标
        self.tray_icon = QSystemTrayIcon(self)
        self.tray_icon.setIcon(
            QIcon(os.path.join(os.getcwd(), "icon.png")))
        self.tray_icon.setToolTip("this tip can't show!")
        self.tray_icon.setContextMenu(self._tray_icon_menu)
        self.tray_icon.show()

    def adjust_style(self):
        self.setWindowFlag(Qt.WindowStaysOnTopHint)  # 置顶
        self.setWindowFlag(Qt.SplashScreen)   # 隐藏任务栏
        self.setWindowFlag(Qt.FramelessWindowHint)   # 无边框
        self.setAttribute(Qt.WA_TranslucentBackground)    # 透明
        screen = QGuiApplication.primaryScreen().size()
        size = self.geometry()
        self.move((screen.width() - size.width() / 2), 0)    # topRight

    def update_data(self):
        self.data.update()
        # self.ui.gpu.setText(str(time.localtime().tm_sec))
        # self.ui.cpu.setText(str(time.localtime().tm_sec+1))
        # self.ui.memory.setText(str(time.localtime().tm_sec+2))
        # self.ui.disk.setText(str(time.localtime().tm_sec+3))
        self.ui.gpu.setText(self.data.get_gpu_info())
        self.ui.cpu.setText(self.data.get_cpu_info())
        self.ui.memory.setText(self.data.get_memory_info())
        self.ui.disk.setText(self.data.get_disk_info())


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Main()
    window.show()
    sys.exit(app.exec())