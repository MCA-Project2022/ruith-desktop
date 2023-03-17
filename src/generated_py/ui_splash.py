# -*- coding: utf-8 -*-

################################################################################
# Form generated from reading UI file 'splash.ui'
##
# Created by: Qt User Interface Compiler version 6.4.2
##
# WARNING! All changes made in this file will be lost when recompiling UI file!
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
import generated_py.resource_rc


class Ui_splash_screen(object):
    def setupUi(self, splash_screen):
        if not splash_screen.objectName():
            splash_screen.setObjectName(u"splash_screen")
        splash_screen.resize(632, 334)
        splash_screen.setStyleSheet(u"QWidget{\n"
                                    "background-color:#e4edef;\n"
                                    "}")
        self.verticalLayout = QVBoxLayout(splash_screen)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.root_layout = QVBoxLayout()
        self.root_layout.setObjectName(u"root_layout")
        self.icon_root_layout = QHBoxLayout()
        self.icon_root_layout.setObjectName(u"icon_root_layout")
        self.icon_lbl = QLabel(splash_screen)
        self.icon_lbl.setObjectName(u"icon_lbl")
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.icon_lbl.sizePolicy().hasHeightForWidth())
        self.icon_lbl.setSizePolicy(sizePolicy)
        self.icon_lbl.setMaximumSize(QSize(60, 55))
        self.icon_lbl.setBaseSize(QSize(0, 15))
        self.icon_lbl.setStyleSheet(u"QLabel{\n"
                                    "color:#2a484c;\n"
                                    "}")
        self.icon_lbl.setPixmap(QPixmap(u":/assets/images/eye.png"))
        self.icon_lbl.setScaledContents(True)
        self.icon_lbl.setAlignment(Qt.AlignCenter)

        self.icon_root_layout.addWidget(self.icon_lbl)

        self.root_layout.addLayout(self.icon_root_layout)

        self.welcome_lbl = QLabel(splash_screen)
        self.welcome_lbl.setObjectName(u"welcome_lbl")
        self.welcome_lbl.setMinimumSize(QSize(10, 13))
        font = QFont()
        font.setFamilies([u"Poppins Thin"])
        font.setPointSize(30)
        font.setBold(True)
        font.setItalic(False)
        self.welcome_lbl.setFont(font)
        self.welcome_lbl.setStyleSheet(u"QLabel{\n"
                                       "	font-size:30pt;\n"
                                       "	font-weight:700;\n"
                                       "	color:#633936;\n"
                                       "}\n"
                                       "")
        self.welcome_lbl.setAlignment(Qt.AlignCenter)

        self.root_layout.addWidget(self.welcome_lbl)

        self.label = QLabel(splash_screen)
        self.label.setObjectName(u"label")
        self.label.setStyleSheet(u"QLabel{\n"
                                 "color:#633936;\n"
                                 "font-style:italic;\n"
                                 "}")
        self.label.setAlignment(Qt.AlignCenter)

        self.root_layout.addWidget(self.label)

        self.progress_bar_root_layout = QHBoxLayout()
        self.progress_bar_root_layout.setObjectName(
            u"progress_bar_root_layout")
        self.progress_bar = QProgressBar(splash_screen)
        self.progress_bar.setObjectName(u"progress_bar")
        sizePolicy.setHeightForWidth(
            self.progress_bar.sizePolicy().hasHeightForWidth())
        self.progress_bar.setSizePolicy(sizePolicy)
        self.progress_bar.setMaximumSize(QSize(500, 16777215))
        self.progress_bar.setStyleSheet(u"QProgressBar{\n"
                                        "border-radius:6px;\n"
                                        "background-color:#b8c4dd;\n"
                                        "color:#633936;\n"
                                        "font-weight:bold;\n"
                                        "}\n"
                                        "QProgressBar::chunk{\n"
                                        "border-radius:6px;\n"
                                        "background-color:#c6f68d;\n"
                                        "}")
        self.progress_bar.setValue(0)
        self.progress_bar.setAlignment(Qt.AlignCenter)
        self.progress_bar.setInvertedAppearance(False)

        self.progress_bar_root_layout.addWidget(self.progress_bar)

        self.root_layout.addLayout(self.progress_bar_root_layout)

        self.verticalLayout.addLayout(self.root_layout)

        self.retranslateUi(splash_screen)

        QMetaObject.connectSlotsByName(splash_screen)
    # setupUi

    def retranslateUi(self, splash_screen):
        splash_screen.setWindowTitle(
            QCoreApplication.translate("splash_screen", u"Form", None))
        self.icon_lbl.setText("")
        self.welcome_lbl.setText(QCoreApplication.translate(
            "splash_screen", u"Welcome To Ruith", None))
        self.label.setText(QCoreApplication.translate("splash_screen", u"Please wait while dependencies are being installed...\n"
                                                      "[This will happen only once]", None))
    # retranslateUi
