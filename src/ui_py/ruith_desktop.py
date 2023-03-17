from PySide6.QtWidgets import QApplication
from ui_py.main_window import MainWindow
from ui_py.splash import SplashScreen
import darkdetect
import os
from etc.pandoc_helper import PANDOC_PATH, add_pandoc_to_path


class RuithDesktop:
    def __init__(self):
        self.__qapp = QApplication()
        self.splash_sc = SplashScreen()
        self.__main_window = MainWindow()
        self.__set_style()

    def __set_style(self):
        style = ''
        if darkdetect.isDark():
            style = 'dark'
        else:
            style = 'light'
        with open(f'src/ui/root_widget/style/{style}.qss') as style_file:
            self.__qapp.setStyleSheet(style_file.read())

    def start(self):
        if os.path.exists(PANDOC_PATH):
            add_pandoc_to_path()
            self.__main_window.show()
        else:
            self.splash_sc.show()
            self.splash_sc.show_progress()
            self.splash_sc.finished.connect(self.__main_window.show)
        self.__qapp.exec()
