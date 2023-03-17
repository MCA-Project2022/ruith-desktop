from PySide6.QtWidgets import QWidget
from PySide6.QtCore import Qt, Signal
from generated_py.ui_splash import Ui_splash_screen
from utility.downloader import Downloader
from etc.pandoc_helper import get_pandoc_url, get_pandoc_archive_file_path, setup_pandoc


class SplashScreen(QWidget, Ui_splash_screen):
    finished = Signal()

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowFlags(Qt.FramelessWindowHint)

    def show_progress(self):
        PANDOC_URL = get_pandoc_url()
        PANDOC_ARCHIVE_FILE_PATH = get_pandoc_archive_file_path()
        self.downloader = Downloader(
            PANDOC_URL, PANDOC_ARCHIVE_FILE_PATH)
        self.downloader.got_total_progress.connect(
            self.progress_bar.setMaximum)
        self.downloader.got_current_progress.connect(
            self.progress_bar.setValue)
        self.downloader.succeeded.connect(self.loading_done)
        self.downloader.start()

    def loading_done(self):
        self.label.setText('Setting up Pandoc')
        setup_pandoc()
        del self.downloader
        self.close()
        self.finished.emit()
