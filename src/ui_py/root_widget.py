from ui_py.root_widget_ui import Ui_root_widget
from PySide6.QtWidgets import QWidget


class RootWidget(QWidget,Ui_root_widget):
    def __init__(self):
        super().__init__()
        self.setupUi(self)


