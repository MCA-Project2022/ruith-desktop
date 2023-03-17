from generated_py.ui_root_widget import Ui_root_widget
from PySide6.QtWidgets import QWidget, QFileDialog
from utilities.document_converter import DocumentConverter
from utilities.document_format import DocumentFormat
from pathlib import Path


class RootWidget(QWidget, Ui_root_widget):
    doc_converter: DocumentConverter = DocumentConverter()

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setup_slots()

    def setup_slots(self):
        self.input_doc_browse_btn.clicked.connect(self.select_input_file)
        self.output_doc_browse_btn.clicked.connect(self.set_output_file)
        self.input_doc_format_cb.currentIndexChanged.connect(
            self.set_input_file_format)
        self.output_doc_format_cb.currentIndexChanged.connect(
            self.set_output_file_format)
        self.convert_btn.clicked.connect(self.doc_converter.start)

    def set_input_file_format(self):
        self.doc_converter.input_format = DocumentFormat.int_to_DocumentFormat(
            self.input_doc_format_cb.currentIndex()
        )

    def set_output_file_format(self):
        self.doc_converter.output_format = DocumentFormat.int_to_DocumentFormat(
            self.output_doc_format_cb.currentIndex()
        )

    def select_input_file(self):
        self.doc_converter.input, _ = QFileDialog.getOpenFileName(
            self, self.tr("Select One Input Document"), "/home/ajayk",
            self.tr(f"Document ( *.{self.doc_converter.input_format.value})")
        )
        self.input_doc_lbl.setText(Path(self.doc_converter.input).name)

    def set_output_file(self):
        self.doc_converter.output = QFileDialog.getSaveFileName(
            self, "Select One Input Document", str(Path.home()),
            f"Document ( *.{self.doc_converter.output_format.value})"
        )[0]+'.'+self.doc_converter.output_format.value
        self.output_doc_lbl.setText(Path(self.doc_converter.output).name)
