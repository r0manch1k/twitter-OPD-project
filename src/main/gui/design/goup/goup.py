# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'goup.ui'
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
from PySide6.QtWidgets import (QApplication, QDialog, QHBoxLayout, QPushButton,
    QSizePolicy, QSpacerItem, QWidget)

class Ui_dialog_GoUp(object):
    def setupUi(self, dialog_GoUp):
        if not dialog_GoUp.objectName():
            dialog_GoUp.setObjectName(u"dialog_GoUp")
        dialog_GoUp.resize(95, 30)
        dialog_GoUp.setMinimumSize(QSize(40, 30))
        dialog_GoUp.setMaximumSize(QSize(95, 30))
        dialog_GoUp.setStyleSheet(u"QDialog {\n"
"	background: transponent;\n"
"}\n"
"QPushButton {\n"
"	width: 50px;\n"
"	height: 30px;\n"
"	color: black;\n"
"	margin: 0;\n"
"	border-radius: 15px;\n"
"	background-color:  rgb(0,88,155);\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color:  rgb(0,78,145);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"	background-color: rgb(0,68,135);\n"
"}\n"
"")
        self.horizontalLayout = QHBoxLayout(dialog_GoUp)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalSpacer = QSpacerItem(20, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.button_GoUp = QPushButton(dialog_GoUp)
        self.button_GoUp.setObjectName(u"button_GoUp")
        self.button_GoUp.setMaximumSize(QSize(50, 30))

        self.horizontalLayout.addWidget(self.button_GoUp)

        self.horizontalSpacer_2 = QSpacerItem(19, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_2)


        self.retranslateUi(dialog_GoUp)

        QMetaObject.connectSlotsByName(dialog_GoUp)
    # setupUi

    def retranslateUi(self, dialog_GoUp):
        dialog_GoUp.setWindowTitle(QCoreApplication.translate("dialog_GoUp", u"Dialog", None))
        self.button_GoUp.setText("")
    # retranslateUi

