from generated_py.ui_root_widget import Ui_root_widget
from PySide6.QtWidgets import QWidget, QFileDialog, QMessageBox
from PySide6.QtGui import QKeySequence, QShortcut
from utilities.document_converter import DocumentConverter
from utilities.document_format import DocumentFormat
from pathlib import Path
from ui_py.loading_widget import LoadingWidget
from ui_py.epub_viewer import EPubViewer
from ui_py.conversion_result_widget import ConversionResultWidget


class RootWidget(QWidget, Ui_root_widget):
    doc_converter: DocumentConverter = DocumentConverter()

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.loading_widget = LoadingWidget()
        self.setup_slots()
        self.setup_key_shortcuts()

    def setup_slots(self):
        self.input_doc_browse_btn.clicked.connect(self.select_input_file)
        self.output_doc_browse_btn.clicked.connect(self.set_output_file)
        self.input_doc_format_cb.currentIndexChanged.connect(
            self.set_input_file_format)
        self.output_doc_format_cb.currentIndexChanged.connect(
            self.set_output_file_format)
        self.convert_btn.clicked.connect(self.start_conversion)
        self.doc_converter.succeeded.connect(self.show_success_msg)
        self.doc_converter.failed.connect(self.show_failure_msg)

    def setup_key_shortcuts(self):
        QShortcut(QKeySequence("Ctrl+i"),
                  self).activated.connect(self.input_doc_format_cb.showPopup)
        QShortcut(QKeySequence("Ctrl+o"),
                  self).activated.connect(self.output_doc_format_cb.showPopup)
        QShortcut(QKeySequence("i"),
                  self).activated.connect(self.select_input_file)
        QShortcut(QKeySequence("o"),
                  self).activated.connect(self.set_output_file)
        QShortcut(QKeySequence("c"),
                  self).activated.connect(self.start_conversion)

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
        self.conversion_result_widget = ConversionResultWidget(
            self.doc_converter.output_format,
            self.doc_converter.output
        )
        self.conversion_result_widget.message_lbl.setText(
            f'''Document was successfully converted from {
                self.doc_converter.input_format.value} to {
                    self.doc_converter.output_format.value}''')
        self.conversion_result_widget.show()

    def show_failure_msg(self):
        self.loading_widget.hide()
        QMessageBox.critical(
            self, 'Failure', 'Something went wrong please try again.')

    def start_conversion(self):
        self.loading_widget.show()
        self.doc_converter.start()
