# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'loading.ui'
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
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QLabel, QProgressBar,
    QSizePolicy, QVBoxLayout, QWidget)

class Ui_loading_widget(object):
    def setupUi(self, loading_widget):
        if not loading_widget.objectName():
            loading_widget.setObjectName(u"loading_widget")
        loading_widget.resize(242, 97)
        self.horizontalLayout = QHBoxLayout(loading_widget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label = QLabel(loading_widget)
        self.label.setObjectName(u"label")
        self.label.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.label)

        self.progressBar = QProgressBar(loading_widget)
        self.progressBar.setObjectName(u"progressBar")
        self.progressBar.setMaximum(0)
        self.progressBar.setValue(0)
        self.progressBar.setAlignment(Qt.AlignCenter)
        self.progressBar.setOrientation(Qt.Horizontal)

        self.verticalLayout.addWidget(self.progressBar)


        self.horizontalLayout.addLayout(self.verticalLayout)


        self.retranslateUi(loading_widget)

        QMetaObject.connectSlotsByName(loading_widget)
    # setupUi

    def retranslateUi(self, loading_widget):
        loading_widget.setWindowTitle(QCoreApplication.translate("loading_widget", u"Form", None))
        self.label.setText(QCoreApplication.translate("loading_widget", u"Converting Your document.\n"
"Please Wait...", None))
#if QT_CONFIG(accessibility)
        self.progressBar.setAccessibleName(QCoreApplication.translate("loading_widget", u"Indeterminate progressbar", None))
#endif // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
        self.progressBar.setAccessibleDescription(QCoreApplication.translate("loading_widget", u"Indeterminate progressbar signifiging the running process(document conversion)", None))
#endif // QT_CONFIG(accessibility)
    # retranslateUi

