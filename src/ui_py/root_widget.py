from generated_py.ui_root_widget import Ui_root_widget
from PySide6.QtWidgets import QWidget, QFileDialog, QMessageBox
from utilities.document_converter import DocumentConverter
from utilities.document_format import DocumentFormat
from pathlib import Path
from ui_py.loading_widget import LoadingWidget


class RootWidget(QWidget, Ui_root_widget):
    doc_converter: DocumentConverter = DocumentConverter()

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.loading_widget = LoadingWidget()
        self.setup_slots()

    def setup_slots(self):
        self.input_doc_browse_btn.clicked.connect(self.select_input_file)
        self.output_doc_browse_btn.clicked.connect(self.set_output_file)
        self.input_doc_format_cb.currentIndexChanged.connect(
            self.set_input_file_format)
        self.output_doc_format_cb.currentIndexChanged.connect(
            self.set_output_file_format)
        self.convert_btn.clicked.connect(self.convert_btn_clicked_slot)
        self.doc_converter.succeeded.connect(self.show_success_msg)
        self.doc_converter.failed.connect(self.show_failure_msg)

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
        self.doc_converter.output, _ = QFileDialog.getSaveFileName(
            self, "Select One Input Document", str(Path.home()),
            f"Document ( *.{self.doc_converter.output_format.value})"
        )
        self.output_doc_lbl.setText(Path(self.doc_converter.output).name)

    def show_success_msg(self):
        self.loading_widget.hide()
        QMessageBox.information(
            self, 'Success', f'''Document was successfully converted from {self.doc_converter.input_format.value} to {self.doc_converter.output_format.value}''')

    def show_failure_msg(self):
        self.loading_widget.hide()
        QMessageBox.critical(
            self, 'Failure', 'Something went wrong please try again.')

    def convert_btn_clicked_slot(self):
        self.loading_widget.show()
        self.doc_converter.start()
