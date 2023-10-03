# coding:utf-8
import sys
import threading
import time

from PyQt5.QtCore import Qt, QSize
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QApplication, QFrame, QHBoxLayout
from qfluentwidgets import FluentIcon as FIF, SplashScreen
from qfluentwidgets import (NavigationItemPosition, FluentWindow,
                            SubtitleLabel, setFont, setThemeColor)

from gui.fragments.home import HomeFragment
from gui.fragments.process import ProcessFragment
from gui.fragments.scheduler import SchedulerFragment
from gui.fragments.settings import SettingsFragment

ICON_DIR = 'gui/assets/logo.png'


class Widget(QFrame):

    def __init__(self, text: str, parent=None):
        super().__init__(parent=parent)

        self.label = SubtitleLabel(text, self)
        self.hBoxLayout = QHBoxLayout(self)

        setFont(self.label, 24)
        self.label.setAlignment(Qt.AlignCenter)
        self.hBoxLayout.addWidget(self.label, 1, Qt.AlignCenter)
        self.setObjectName(text.replace(' ', '-'))


class Window(FluentWindow):

    def __init__(self):
        super().__init__()
        self.initWindow()
        self.splashScreen = SplashScreen(self.windowIcon(), self)
        self.splashScreen.setIconSize(QSize(102, 102))
        self.show()

        setThemeColor('#0078d4')
        # create sub interface
        self.homeInterface = HomeFragment()
        self.schedulerInterface = SchedulerFragment()
        self.processInterface = ProcessFragment()
        self.settingInterface = SettingsFragment()

        self.initNavigation()
        self.splashScreen.finish()

    def initNavigation(self):
        self.addSubInterface(self.homeInterface, FIF.HOME, '主页')

        self.navigationInterface.addSeparator()
        self.addSubInterface(self.schedulerInterface, FIF.CALENDAR, '调度器')
        self.addSubInterface(self.processInterface, FIF.CALORIES, '调度状态')

        # add custom widget to bottom
        self.addSubInterface(self.settingInterface, FIF.SETTING, '设置', NavigationItemPosition.BOTTOM)

    def worker(self):
        while True:
            print("hello")
            time.sleep(1)

    def initWindow(self):
        s=threading.Thread(target=self.worker,daemon=True)
        s.start()

        self.setFixedSize(900, 700)
        self.setWindowIcon(QIcon(ICON_DIR))
        self.setWindowTitle('BlueArchiveAutoScript')

        desktop = QApplication.desktop().availableGeometry()
        _w, _h = desktop.width(), desktop.height()
        self.move(_w // 2 - self.width() // 2, _h // 2 - self.height() // 2)

    def closeEvent(self, event):
        self.homeInterface.close()
        self.schedulerInterface.close()
        self.processInterface.close()
        self.settingInterface.close()
        super().closeEvent(event)
        exit(0)


if __name__ == '__main__':
    # pa=Main()
    # pa._init_emulator()
    # pa.solve("arena")
    QApplication.setHighDpiScaleFactorRoundingPolicy(Qt.HighDpiScaleFactorRoundingPolicy.PassThrough)
    QApplication.setAttribute(Qt.AA_EnableHighDpiScaling)
    QApplication.setAttribute(Qt.AA_UseHighDpiPixmaps)
    # setTheme(Theme.DARK)

    app = QApplication(sys.argv)
    w = Window()
    w.show()
    app.exec_()
