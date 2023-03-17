import pypandoc
from utilities.document_format import DocumentFormat
from PySide6.QtCore import Signal, QObject


class DocumentConverter(QObject):
    succeeded = Signal()
    failed = Signal()

    def __init__(self):
        super().__init__()
        self.__input_format = DocumentFormat.DOCX
        self.__output_format = DocumentFormat.EPUB

    @property
    def input(self):
        return self.__input

    @input.setter
    def input(self, value):
        self.__input = value

    @property
    def input_format(self):
        return self.__input_format

    @input_format.setter
    def input_format(self, value: DocumentFormat):
        self.__input_format = value

    @property
    def output(self):
        return self.__output

    @output.setter
    def output(self, value):
        self.__output = value

    @property
    def output_format(self):
        return self.__output_format

    @output_format.setter
    def output_format(self, value: DocumentFormat):
        self.__output_format = value

    def start(self):
        try:
            pypandoc.convert_file(self.input, format=self.input_format.value,
                                  outputfile=self.output, to=self.output_format.value)
        except Exception:
            self.failed.emit()
        else:
            self.succeeded.emit()
