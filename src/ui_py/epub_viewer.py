from PySide6.QtWidgets import QWidget, QMessageBox
from PySide6.QtGui import QImage, QPixmap
from generated_py.ui_epub_viewer import Ui_epub_viewer
import fitz
from pathlib import Path


class EPubViewer(QWidget, Ui_epub_viewer):
    def __init__(self, doc_path: Path):
        super().__init__()
        self.setupUi(self)
        self.doc = fitz.open(doc_path)
        self.current_page = 0
        self.page_count = self.doc.page_count
        self.setup_slots()
        page = self.doc.load_page(self.current_page)
        qpix = self.get_qpix_from_page(page)
        self.display_image(qpix)
        self.current_page_lbl.setText(str(1))
        self.page_count_lbl.setText(str(self.page_count))

    def setup_slots(self):
        self.next_btn.clicked.connect(self.go_to_next_page)
        self.prev_btn.clicked.connect(self.go_to_prev_page)

    def display_image(self, qpix):
        self.img_lbl.setPixmap(qpix)

    def get_qpix_from_page(self, page):
        pix = page.get_pixmap()
        fmt = QImage.Format.Format_RGBA8888 if pix.alpha else QImage.Format.Format_RGB888
        qtimg = QImage(pix.samples, pix.width, pix.height, fmt)
        return QPixmap.fromImage(qtimg)

    def go_to_prev_page(self):
        if self.current_page == 0:
            return
        self.current_page -= 1
        page = self.doc.load_page(self.current_page)
        qpix = self.get_qpix_from_page(page)
        self.current_page_lbl.setText(str(self.current_page+1))
        self.display_image(qpix)

    def go_to_next_page(self):
        if self.current_page == self.page_count-1:
            self.show_page_end_message()
            return
        self.current_page += 1
        page = self.doc.load_page(self.current_page)
        qpix = self.get_qpix_from_page(page)
        self.current_page_lbl.setText(str(self.current_page+1))
        self.display_image(qpix)

    def show_page_end_message(self):
        QMessageBox.information(
            self, 'Page End', 'You have reached the end of the document')
