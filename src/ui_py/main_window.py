from PySide6.QtWidgets import QMainWindow
from ui_py.root_widget import RootWidget
from PySide6.QtWidgets import QMessageBox


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.root_widget = RootWidget()
        self.setWindowTitle('Ruith')
        self.populate_menu_bar()
        self.setCentralWidget(self.root_widget)

    def populate_menu_bar(self):
        help_menu = self.menuBar().addMenu('&Help')
        about_action = help_menu.addAction('About')
        about_action.triggered.connect(self.show_about)

    def show_about(self):
        QMessageBox.information(
            self, 'About',
            'This application was made by:\nAjay Karthikesan\nRohan Rathod\nHrishikesh Yenure'
        )
