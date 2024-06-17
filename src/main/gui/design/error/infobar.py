# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'infobar.ui'
##
## Created by: Qt User Interface Compiler version 6.7.1
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
from PySide6.QtWidgets import (QApplication, QDialog, QLabel, QSizePolicy,
    QVBoxLayout, QWidget)

class Ui_dialog_Info(object):
    def setupUi(self, dialog_Info):
        if not dialog_Info.objectName():
            dialog_Info.setObjectName(u"dialog_Info")
        dialog_Info.resize(280, 40)
        dialog_Info.setMinimumSize(QSize(280, 40))
        dialog_Info.setMaximumSize(QSize(280, 40))
        dialog_Info.setLayoutDirection(Qt.LeftToRight)
        dialog_Info.setAutoFillBackground(True)
        dialog_Info.setStyleSheet(u"")
        self.verticalLayout = QVBoxLayout(dialog_Info)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label_Info = QLabel(dialog_Info)
        self.label_Info.setObjectName(u"label_Info")
        font = QFont()
        font.setBold(True)
        self.label_Info.setFont(font)
        self.label_Info.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.label_Info)


        self.retranslateUi(dialog_Info)

        QMetaObject.connectSlotsByName(dialog_Info)
    # setupUi

    def retranslateUi(self, dialog_Info):
        dialog_Info.setWindowTitle(QCoreApplication.translate("dialog_Info", u"Dialog", None))
        self.label_Info.setText(QCoreApplication.translate("dialog_Info", u"ERROR: Youski", None))
    # retranslateUi

