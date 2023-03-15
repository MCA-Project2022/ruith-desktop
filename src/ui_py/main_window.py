from PySide6.QtWidgets import QMainWindow
from ui_py.root_widget import RootWidget

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.__root_widget = RootWidget()
        self.setCentralWidget(self.__root_widget)
