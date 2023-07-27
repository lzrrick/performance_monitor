import sys
import os
import atexit
import win32api
from PySide6.QtWidgets import *
from PySide6.QtGui import *
from PySide6.QtCore import *
from myUi import Ui_MainWindow
from model import model
import psutil


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
        self.ui.gpu.setText(self.data.get_gpu_info())
        self.ui.cpu.setText(self.data.get_cpu_info())
        self.ui.memory.setText(self.data.get_memory_info())
        self.ui.disk.setText(self.data.get_disk_info())


def remove_start():
    os.remove("start.pid")


if __name__ == "__main__":
    try:
        if os.path.exists("start.pid"):
            f = open("start.pid", "r")
            pid = int(f.read())
            f.close()
            if psutil.pid_exists(pid):
                win32api.MessageBox(0, "monitor is running!",
                                    "warning", 0x00000000 + 0x00000030)
                sys.exit()
            else:
                remove_start()

        atexit.register(remove_start)
        f = open("start.pid", "w")
        f.write(f"{os.getpid()}")
        f.close()
        win32api.SetFileAttributes("start.pid", 0x00000002)  # hide file
        app = QApplication(sys.argv)
        window = Main()
        window.show()
        sys.exit(app.exec())
    except Exception as e:
        print(e)
