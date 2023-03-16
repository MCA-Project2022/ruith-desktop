from PySide6.QtWidgets import QApplication
from ui_py.main_window import MainWindow
import darkdetect


class RuithDesktop:
    def __init__(self):
        self.__qapp = QApplication()
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
        self.__main_window.show()
        self.__qapp.exec()
