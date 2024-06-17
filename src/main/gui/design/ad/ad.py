# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ad.ui'
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
from PySide6.QtWidgets import (QApplication, QFrame, QHBoxLayout, QSizePolicy,
    QVBoxLayout, QWidget)

class Ui_form_Ad(object):
    def setupUi(self, form_Ad):
        if not form_Ad.objectName():
            form_Ad.setObjectName(u"form_Ad")
        form_Ad.resize(556, 120)
        form_Ad.setMinimumSize(QSize(0, 120))
        form_Ad.setMaximumSize(QSize(16777215, 120))
        form_Ad.setStyleSheet(u"QWidget {\n"
"	border: 0;\n"
"	border-radius: 20px;\n"
"	background: transponent;\n"
"}\n"
"\n"
"QLabel {\n"
"	background: transponent;\n"
"}")
        self.layout = QHBoxLayout(form_Ad)
        self.layout.setSpacing(0)
        self.layout.setObjectName(u"layout")
        self.layout.setContentsMargins(0, 0, 0, 0)
        self.frame_Ad = QFrame(form_Ad)
        self.frame_Ad.setObjectName(u"frame_Ad")
        self.frame_Ad.setFrameShape(QFrame.StyledPanel)
        self.frame_Ad.setFrameShadow(QFrame.Raised)
        self.layout_Main = QVBoxLayout(self.frame_Ad)
        self.layout_Main.setSpacing(0)
        self.layout_Main.setObjectName(u"layout_Main")
        self.layout_Main.setContentsMargins(0, 0, 0, 0)

        self.layout.addWidget(self.frame_Ad)


        self.retranslateUi(form_Ad)

        QMetaObject.connectSlotsByName(form_Ad)
    # setupUi

    def retranslateUi(self, form_Ad):
        form_Ad.setWindowTitle(QCoreApplication.translate("form_Ad", u"Form", None))
    # retranslateUi

