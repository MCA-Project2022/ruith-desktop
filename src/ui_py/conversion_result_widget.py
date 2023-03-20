from PySide6.QtWidgets import QWidget
from generated_py.ui_conversion_result_widget import Ui_conversion_result_widget
from utilities.document_format import DocumentFormat
from ui_py.epub_viewer import EPubViewer
from pathlib import Path


class ConversionResultWidget(QWidget, Ui_conversion_result_widget):
    def __init__(self, doc_format: DocumentFormat, doc_path: Path):
        super().__init__()
        self.setupUi(self)
        self.doc_format = doc_format
        self.doc_path = doc_path
        self.setup_slots()

    def set_doc_format(self, doc_format: DocumentFormat):
        self.doc_format = doc_format

    def set_doc_path(self, doc_path: Path):
        self.doc_path = doc_path

    def setup_slots(self):
        self.view_doc_btn.clicked.connect(self.show_epub)
        self.close_btn.clicked.connect(self.close)

    def show_epub(self):
        if self.doc_format != DocumentFormat.EPUB:
            return
        self.epub_viewer = EPubViewer(self.doc_path)
        self.epub_viewer.show()
