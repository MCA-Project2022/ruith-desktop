from generated_py.ui_loading_widget import Ui_loading_widget
from PySide6.QtWidgets import QWidget
from PySide6.QtCore import Qt

class LoadingWidget(QWidget,Ui_loading_widget):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowFlags(Qt.FramelessWindowHint)
        self.setWindowModality(Qt.ApplicationModal)