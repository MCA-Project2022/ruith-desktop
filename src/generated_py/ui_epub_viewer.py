# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'epub_viewer.ui'
##
## Created by: Qt User Interface Compiler version 6.4.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QLabel, QPushButton,
    QSizePolicy, QVBoxLayout, QWidget)

class Ui_epub_viewer(object):
    def setupUi(self, epub_viewer):
        if not epub_viewer.objectName():
            epub_viewer.setObjectName(u"epub_viewer")
        epub_viewer.resize(396, 494)
        self.verticalLayout = QVBoxLayout(epub_viewer)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.img_lbl = QLabel(epub_viewer)
        self.img_lbl.setObjectName(u"img_lbl")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.img_lbl.sizePolicy().hasHeightForWidth())
        self.img_lbl.setSizePolicy(sizePolicy)
        self.img_lbl.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.img_lbl)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.prev_btn = QPushButton(epub_viewer)
        self.prev_btn.setObjectName(u"prev_btn")
        sizePolicy1 = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.prev_btn.sizePolicy().hasHeightForWidth())
        self.prev_btn.setSizePolicy(sizePolicy1)

        self.horizontalLayout.addWidget(self.prev_btn)

        self.current_page_lbl = QLabel(epub_viewer)
        self.current_page_lbl.setObjectName(u"current_page_lbl")
        self.current_page_lbl.setAlignment(Qt.AlignCenter)

        self.horizontalLayout.addWidget(self.current_page_lbl)

        self.slash_lbl = QLabel(epub_viewer)
        self.slash_lbl.setObjectName(u"slash_lbl")
        sizePolicy2 = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Preferred)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.slash_lbl.sizePolicy().hasHeightForWidth())
        self.slash_lbl.setSizePolicy(sizePolicy2)

        self.horizontalLayout.addWidget(self.slash_lbl)

        self.page_count_lbl = QLabel(epub_viewer)
        self.page_count_lbl.setObjectName(u"page_count_lbl")
        self.page_count_lbl.setAlignment(Qt.AlignCenter)

        self.horizontalLayout.addWidget(self.page_count_lbl)

        self.next_btn = QPushButton(epub_viewer)
        self.next_btn.setObjectName(u"next_btn")
        sizePolicy1.setHeightForWidth(self.next_btn.sizePolicy().hasHeightForWidth())
        self.next_btn.setSizePolicy(sizePolicy1)

        self.horizontalLayout.addWidget(self.next_btn)


        self.verticalLayout.addLayout(self.horizontalLayout)


        self.retranslateUi(epub_viewer)

        QMetaObject.connectSlotsByName(epub_viewer)
    # setupUi

    def retranslateUi(self, epub_viewer):
        epub_viewer.setWindowTitle(QCoreApplication.translate("epub_viewer", u"Form", None))
        self.img_lbl.setText("")
        self.prev_btn.setText(QCoreApplication.translate("epub_viewer", u"Previous", None))
        self.current_page_lbl.setText("")
        self.slash_lbl.setText(QCoreApplication.translate("epub_viewer", u"/", None))
        self.page_count_lbl.setText("")
        self.next_btn.setText(QCoreApplication.translate("epub_viewer", u"Next", None))
    # retranslateUi

