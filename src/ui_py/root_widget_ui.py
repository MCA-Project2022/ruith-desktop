# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'root_widget.ui'
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
from PySide6.QtWidgets import (QApplication, QComboBox, QGroupBox, QHBoxLayout,
    QLabel, QPushButton, QSizePolicy, QVBoxLayout,
    QWidget)

class Ui_root_widget(object):
    def setupUi(self, root_widget):
        if not root_widget.objectName():
            root_widget.setObjectName(u"root_widget")
        root_widget.resize(697, 483)
        self.verticalLayout_3 = QVBoxLayout(root_widget)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.input_doc_sec = QGroupBox(root_widget)
        self.input_doc_sec.setObjectName(u"input_doc_sec")
        self.verticalLayout = QVBoxLayout(self.input_doc_sec)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.input_format_lbl = QLabel(self.input_doc_sec)
        self.input_format_lbl.setObjectName(u"input_format_lbl")

        self.horizontalLayout.addWidget(self.input_format_lbl)

        self.input_doc_format_cb = QComboBox(self.input_doc_sec)
        self.input_doc_format_cb.setObjectName(u"input_doc_format_cb")

        self.horizontalLayout.addWidget(self.input_doc_format_cb)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.input_loc_lbl = QLabel(self.input_doc_sec)
        self.input_loc_lbl.setObjectName(u"input_loc_lbl")

        self.horizontalLayout_2.addWidget(self.input_loc_lbl)

        self.input_doc_browse_btn = QPushButton(self.input_doc_sec)
        self.input_doc_browse_btn.setObjectName(u"input_doc_browse_btn")

        self.horizontalLayout_2.addWidget(self.input_doc_browse_btn)

        self.input_doc_lbl = QLabel(self.input_doc_sec)
        self.input_doc_lbl.setObjectName(u"input_doc_lbl")

        self.horizontalLayout_2.addWidget(self.input_doc_lbl)


        self.verticalLayout.addLayout(self.horizontalLayout_2)


        self.verticalLayout_3.addWidget(self.input_doc_sec)

        self.output_doc_sec = QGroupBox(root_widget)
        self.output_doc_sec.setObjectName(u"output_doc_sec")
        self.verticalLayout_2 = QVBoxLayout(self.output_doc_sec)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.output_format_lbl = QLabel(self.output_doc_sec)
        self.output_format_lbl.setObjectName(u"output_format_lbl")

        self.horizontalLayout_3.addWidget(self.output_format_lbl)

        self.output_doc_format_cb = QComboBox(self.output_doc_sec)
        self.output_doc_format_cb.setObjectName(u"output_doc_format_cb")

        self.horizontalLayout_3.addWidget(self.output_doc_format_cb)


        self.verticalLayout_2.addLayout(self.horizontalLayout_3)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.output_loc_lbl = QLabel(self.output_doc_sec)
        self.output_loc_lbl.setObjectName(u"output_loc_lbl")

        self.horizontalLayout_4.addWidget(self.output_loc_lbl)

        self.output_doc_browse_btn = QPushButton(self.output_doc_sec)
        self.output_doc_browse_btn.setObjectName(u"output_doc_browse_btn")

        self.horizontalLayout_4.addWidget(self.output_doc_browse_btn)

        self.output_doc_lbl = QLabel(self.output_doc_sec)
        self.output_doc_lbl.setObjectName(u"output_doc_lbl")

        self.horizontalLayout_4.addWidget(self.output_doc_lbl)


        self.verticalLayout_2.addLayout(self.horizontalLayout_4)

        self.pushButton_2 = QPushButton(self.output_doc_sec)
        self.pushButton_2.setObjectName(u"pushButton_2")

        self.verticalLayout_2.addWidget(self.pushButton_2)


        self.verticalLayout_3.addWidget(self.output_doc_sec)


        self.retranslateUi(root_widget)

        QMetaObject.connectSlotsByName(root_widget)
    # setupUi

    def retranslateUi(self, root_widget):
        root_widget.setWindowTitle(QCoreApplication.translate("root_widget", u"Form", None))
        self.input_doc_sec.setTitle(QCoreApplication.translate("root_widget", u"Input Document", None))
        self.input_format_lbl.setText(QCoreApplication.translate("root_widget", u"Format", None))
        self.input_loc_lbl.setText(QCoreApplication.translate("root_widget", u"Location", None))
        self.input_doc_browse_btn.setText(QCoreApplication.translate("root_widget", u"Browse...", None))
        self.input_doc_lbl.setText("")
        self.output_doc_sec.setTitle(QCoreApplication.translate("root_widget", u"Output Document", None))
        self.output_format_lbl.setText(QCoreApplication.translate("root_widget", u"Format", None))
        self.output_loc_lbl.setText(QCoreApplication.translate("root_widget", u"Location", None))
        self.output_doc_browse_btn.setText(QCoreApplication.translate("root_widget", u"Browse...", None))
        self.output_doc_lbl.setText("")
        self.pushButton_2.setText(QCoreApplication.translate("root_widget", u"Convert", None))
    # retranslateUi

