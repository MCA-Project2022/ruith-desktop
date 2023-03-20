# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'conversion_result.ui'
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

class Ui_conversion_result_widget(object):
    def setupUi(self, conversion_result_widget):
        if not conversion_result_widget.objectName():
            conversion_result_widget.setObjectName(u"conversion_result_widget")
        conversion_result_widget.resize(400, 300)
        self.verticalLayout = QVBoxLayout(conversion_result_widget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.message_lbl = QLabel(conversion_result_widget)
        self.message_lbl.setObjectName(u"message_lbl")
        self.message_lbl.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.message_lbl)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.close_btn = QPushButton(conversion_result_widget)
        self.close_btn.setObjectName(u"close_btn")

        self.horizontalLayout.addWidget(self.close_btn)

        self.view_doc_btn = QPushButton(conversion_result_widget)
        self.view_doc_btn.setObjectName(u"view_doc_btn")

        self.horizontalLayout.addWidget(self.view_doc_btn)


        self.verticalLayout.addLayout(self.horizontalLayout)


        self.retranslateUi(conversion_result_widget)

        QMetaObject.connectSlotsByName(conversion_result_widget)
    # setupUi

    def retranslateUi(self, conversion_result_widget):
        conversion_result_widget.setWindowTitle(QCoreApplication.translate("conversion_result_widget", u"Form", None))
        self.message_lbl.setText("")
        self.close_btn.setText(QCoreApplication.translate("conversion_result_widget", u"Close", None))
        self.view_doc_btn.setText(QCoreApplication.translate("conversion_result_widget", u"View", None))
    # retranslateUi

