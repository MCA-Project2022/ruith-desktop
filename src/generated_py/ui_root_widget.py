# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'form.ui'
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
        root_widget.resize(508, 380)
        root_widget.setStyleSheet(u"")
        self.verticalLayout_3 = QVBoxLayout(root_widget)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.input_doc_sec = QGroupBox(root_widget)
        self.input_doc_sec.setObjectName(u"input_doc_sec")
        self.input_doc_sec.setStyleSheet(u"")
        self.verticalLayout = QVBoxLayout(self.input_doc_sec)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.input_format_lbl = QLabel(self.input_doc_sec)
        self.input_format_lbl.setObjectName(u"input_format_lbl")

        self.horizontalLayout.addWidget(self.input_format_lbl)

        self.input_doc_format_cb = QComboBox(self.input_doc_sec)
        self.input_doc_format_cb.addItem("")
        self.input_doc_format_cb.addItem("")
        self.input_doc_format_cb.addItem("")
        self.input_doc_format_cb.addItem("")
        self.input_doc_format_cb.addItem("")
        self.input_doc_format_cb.addItem("")
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
        self.output_doc_sec.setStyleSheet(u"")
        self.verticalLayout_2 = QVBoxLayout(self.output_doc_sec)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.output_format_lbl = QLabel(self.output_doc_sec)
        self.output_format_lbl.setObjectName(u"output_format_lbl")

        self.horizontalLayout_3.addWidget(self.output_format_lbl)

        self.output_doc_format_cb = QComboBox(self.output_doc_sec)
        self.output_doc_format_cb.addItem("")
        self.output_doc_format_cb.addItem("")
        self.output_doc_format_cb.addItem("")
        self.output_doc_format_cb.addItem("")
        self.output_doc_format_cb.addItem("")
        self.output_doc_format_cb.addItem("")
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


        self.verticalLayout_3.addWidget(self.output_doc_sec)

        self.convert_btn = QPushButton(root_widget)
        self.convert_btn.setObjectName(u"convert_btn")
        self.convert_btn.setStyleSheet(u"")

        self.verticalLayout_3.addWidget(self.convert_btn)


        self.retranslateUi(root_widget)

        self.output_doc_format_cb.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(root_widget)
    # setupUi

    def retranslateUi(self, root_widget):
        root_widget.setWindowTitle(QCoreApplication.translate("root_widget", u"Form", None))
#if QT_CONFIG(accessibility)
        self.input_doc_sec.setAccessibleName(QCoreApplication.translate("root_widget", u"Input Document's Widget Section", None))
#endif // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
        self.input_doc_sec.setAccessibleDescription(QCoreApplication.translate("root_widget", u"Input Document's widget contains all the widgets that's used to set the input document.", None))
#endif // QT_CONFIG(accessibility)
        self.input_doc_sec.setTitle(QCoreApplication.translate("root_widget", u"Input Document", None))
        self.input_format_lbl.setText(QCoreApplication.translate("root_widget", u"Format", None))
        self.input_doc_format_cb.setItemText(0, QCoreApplication.translate("root_widget", u"Microsoft Word(docx)", None))
        self.input_doc_format_cb.setItemText(1, QCoreApplication.translate("root_widget", u"Electronic Publication(epub)", None))
        self.input_doc_format_cb.setItemText(2, QCoreApplication.translate("root_widget", u"OpenOffice/LibreOffice(odt)", None))
        self.input_doc_format_cb.setItemText(3, QCoreApplication.translate("root_widget", u"Markdown(md)", None))
        self.input_doc_format_cb.setItemText(4, QCoreApplication.translate("root_widget", u"Rich Text Format(rtf)", None))
        self.input_doc_format_cb.setItemText(5, QCoreApplication.translate("root_widget", u"HTML(html)", None))

#if QT_CONFIG(accessibility)
        self.input_doc_format_cb.setAccessibleName(QCoreApplication.translate("root_widget", u"Input Document Format Dropdown List.", None))
#endif // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
        self.input_doc_format_cb.setAccessibleDescription(QCoreApplication.translate("root_widget", u"This dropdown list can be used to select the format of the input document. Key shortcut is 'Ctrl+i'.", None))
#endif // QT_CONFIG(accessibility)
        self.input_loc_lbl.setText(QCoreApplication.translate("root_widget", u"Location", None))
#if QT_CONFIG(accessibility)
        self.input_doc_browse_btn.setAccessibleName(QCoreApplication.translate("root_widget", u"Input Document selector button.", None))
#endif // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
        self.input_doc_browse_btn.setAccessibleDescription(QCoreApplication.translate("root_widget", u"This button can be used to open the file explorer and select the input document of the format selected in the drop down list. Key shortcut is 'i'.", None))
#endif // QT_CONFIG(accessibility)
        self.input_doc_browse_btn.setText(QCoreApplication.translate("root_widget", u"Browse...", None))
        self.input_doc_lbl.setText("")
#if QT_CONFIG(accessibility)
        self.output_doc_sec.setAccessibleName(QCoreApplication.translate("root_widget", u"Output Document's Widget Section", None))
#endif // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
        self.output_doc_sec.setAccessibleDescription(QCoreApplication.translate("root_widget", u"Output Document's widget contains all the widgets that's used to set the output document.", None))
#endif // QT_CONFIG(accessibility)
        self.output_doc_sec.setTitle(QCoreApplication.translate("root_widget", u"Output Document", None))
        self.output_format_lbl.setText(QCoreApplication.translate("root_widget", u"Format", None))
        self.output_doc_format_cb.setItemText(0, QCoreApplication.translate("root_widget", u"Microsoft Word(docx)", None))
        self.output_doc_format_cb.setItemText(1, QCoreApplication.translate("root_widget", u"Electronic Publication(epub)", None))
        self.output_doc_format_cb.setItemText(2, QCoreApplication.translate("root_widget", u"OpenOffice/LibreOffice(odt)", None))
        self.output_doc_format_cb.setItemText(3, QCoreApplication.translate("root_widget", u"Markdown(md)", None))
        self.output_doc_format_cb.setItemText(4, QCoreApplication.translate("root_widget", u"Rich Text Format(rtf)", None))
        self.output_doc_format_cb.setItemText(5, QCoreApplication.translate("root_widget", u"HTML(html)", None))

#if QT_CONFIG(accessibility)
        self.output_doc_format_cb.setAccessibleName(QCoreApplication.translate("root_widget", u"Output Document Format Dropdown List.", None))
#endif // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
        self.output_doc_format_cb.setAccessibleDescription(QCoreApplication.translate("root_widget", u"This dropdown list can be used to select the format of the output document. Key shortcut is 'Ctrl+o'.", None))
#endif // QT_CONFIG(accessibility)
        self.output_loc_lbl.setText(QCoreApplication.translate("root_widget", u"Location", None))
#if QT_CONFIG(accessibility)
        self.output_doc_browse_btn.setAccessibleName(QCoreApplication.translate("root_widget", u"Output Document setter button.", None))
#endif // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
        self.output_doc_browse_btn.setAccessibleDescription(QCoreApplication.translate("root_widget", u"This button can be used to open the file explorer and set the output document of the format selected in the drop down list. The user'll have to navigate to the desired location and give a name for the resulting document. Key shortcut is 'o'.", None))
#endif // QT_CONFIG(accessibility)
        self.output_doc_browse_btn.setText(QCoreApplication.translate("root_widget", u"Browse...", None))
        self.output_doc_lbl.setText("")
#if QT_CONFIG(accessibility)
        self.convert_btn.setAccessibleName(QCoreApplication.translate("root_widget", u"Convert button", None))
#endif // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
        self.convert_btn.setAccessibleDescription(QCoreApplication.translate("root_widget", u"Clicking this button will start converting the selected document and create the output document specified by the user. Key shortcut is 'c'.", None))
#endif // QT_CONFIG(accessibility)
        self.convert_btn.setText(QCoreApplication.translate("root_widget", u"Convert", None))
    # retranslateUi

