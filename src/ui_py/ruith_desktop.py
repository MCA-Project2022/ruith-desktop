from PySide6.QtWidgets import QApplication
from ui_py.main_window import MainWindow

class RuithDesktop:
    def __init__(self):
        self.__qapp = QApplication()
        self.__main_window = MainWindow()

    def start(self):
        self.__main_window.show()
        self.__qapp.exec()
    