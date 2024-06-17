# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'createcom.ui'
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
from PySide6.QtWidgets import (QAbstractScrollArea, QApplication, QFrame, QGridLayout,
    QHBoxLayout, QLabel, QPlainTextEdit, QPushButton,
    QSizePolicy, QSpacerItem, QVBoxLayout, QWidget)

class Ui_frame_CommentCreate(object):
    def setupUi(self, frame_CommentCreate):
        if not frame_CommentCreate.objectName():
            frame_CommentCreate.setObjectName(u"frame_CommentCreate")
        frame_CommentCreate.resize(575, 110)
        frame_CommentCreate.setMinimumSize(QSize(0, 50))
        frame_CommentCreate.setMaximumSize(QSize(16777215, 110))
        frame_CommentCreate.setStyleSheet(u"QFrame#frame_CommentCreate {\n"
"	background: transponent;\n"
"	border-radius: 20px;\n"
"}\n"
"\n"
"QFrame {\n"
"	border: 0;\n"
"	background-color: white;\n"
"}\n"
"\n"
"QFrame#frame_HomeCreateComment {\n"
"	background: transponent;\n"
"}\n"
"\n"
"QFrame#frame_CommentCreateMain {\n"
"	border-radius: 20px;\n"
"}\n"
"\n"
"QFrame#frame_CommentCreateToolsSelected {\n"
"	border-top: 1px solid rgb(190, 194, 196);\n"
"	border-bottom-left-radius: 20px;\n"
"	border-bottom-right-radius: 20px;\n"
"}\n"
"\n"
"QPushButton {\n"
"	color: black;\n"
"	margin: 0;\n"
"	background-color:  white;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color:  rgb(235, 237, 239);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"	background-color: rgb(190, 194, 196);\n"
"}\n"
"\n"
"QPushButton#button_CommentCreate {\n"
"	color: white;\n"
"	background-color: rgb(0, 88, 155);\n"
"	border-radius: 15px;\n"
"}\n"
"\n"
"QPushButton#button_CommentCreate:hover {\n"
"	background-color: rgb(0, 78, 145);\n"
"}\n"
"\n"
"QPushButton#button_CommentCreate:pres"
                        "sed {\n"
"	background-color: rgb(0, 68, 135);\n"
"}\n"
"")
        frame_CommentCreate.setFrameShape(QFrame.StyledPanel)
        frame_CommentCreate.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(frame_CommentCreate)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.frame_CommentCreateMain = QFrame(frame_CommentCreate)
        self.frame_CommentCreateMain.setObjectName(u"frame_CommentCreateMain")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_CommentCreateMain.sizePolicy().hasHeightForWidth())
        self.frame_CommentCreateMain.setSizePolicy(sizePolicy)
        self.frame_CommentCreateMain.setMinimumSize(QSize(0, 50))
        self.frame_CommentCreateMain.setMaximumSize(QSize(16777215, 50))
        self.frame_CommentCreateMain.setStyleSheet(u"")
        self.frame_CommentCreateMain.setFrameShape(QFrame.StyledPanel)
        self.frame_CommentCreateMain.setFrameShadow(QFrame.Raised)
        self.gridLayout = QGridLayout(self.frame_CommentCreateMain)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setHorizontalSpacing(10)
        self.gridLayout.setVerticalSpacing(0)
        self.gridLayout.setContentsMargins(10, 10, 10, 10)
        self.line_CommentCreateText = QPlainTextEdit(self.frame_CommentCreateMain)
        self.line_CommentCreateText.setObjectName(u"line_CommentCreateText")
        self.line_CommentCreateText.setMinimumSize(QSize(0, 30))
        self.line_CommentCreateText.setMaximumSize(QSize(16777215, 30))
        self.line_CommentCreateText.setStyleSheet(u"padding-top: 3px;")
        self.line_CommentCreateText.setFrameShadow(QFrame.Sunken)
        self.line_CommentCreateText.setLineWidth(0)
        self.line_CommentCreateText.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.line_CommentCreateText.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.line_CommentCreateText.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContents)
        self.line_CommentCreateText.setBackgroundVisible(False)

        self.gridLayout.addWidget(self.line_CommentCreateText, 0, 1, 1, 1)

        self.frame_CommentCreateImage = QFrame(self.frame_CommentCreateMain)
        self.frame_CommentCreateImage.setObjectName(u"frame_CommentCreateImage")
        self.frame_CommentCreateImage.setMinimumSize(QSize(0, 30))
        self.frame_CommentCreateImage.setStyleSheet(u"")
        self.frame_CommentCreateImage.setFrameShape(QFrame.StyledPanel)
        self.frame_CommentCreateImage.setFrameShadow(QFrame.Raised)
        self.verticalLayout_11 = QVBoxLayout(self.frame_CommentCreateImage)
        self.verticalLayout_11.setSpacing(0)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.verticalLayout_11.setContentsMargins(0, 0, 0, 0)
        self.label_CommentCreateImage = QLabel(self.frame_CommentCreateImage)
        self.label_CommentCreateImage.setObjectName(u"label_CommentCreateImage")
        self.label_CommentCreateImage.setMinimumSize(QSize(30, 30))
        self.label_CommentCreateImage.setMaximumSize(QSize(30, 30))

        self.verticalLayout_11.addWidget(self.label_CommentCreateImage)

        self.verticalSpacer_7 = QSpacerItem(20, 12, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.MinimumExpanding)

        self.verticalLayout_11.addItem(self.verticalSpacer_7)


        self.gridLayout.addWidget(self.frame_CommentCreateImage, 0, 0, 1, 1)


        self.verticalLayout.addWidget(self.frame_CommentCreateMain)

        self.frame_CommentCreateToolsSelected = QFrame(frame_CommentCreate)
        self.frame_CommentCreateToolsSelected.setObjectName(u"frame_CommentCreateToolsSelected")
        self.frame_CommentCreateToolsSelected.setMinimumSize(QSize(0, 60))
        self.frame_CommentCreateToolsSelected.setMaximumSize(QSize(16777215, 60))
        self.frame_CommentCreateToolsSelected.setStyleSheet(u"")
        self.frame_CommentCreateToolsSelected.setFrameShape(QFrame.StyledPanel)
        self.frame_CommentCreateToolsSelected.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.frame_CommentCreateToolsSelected)
        self.horizontalLayout_2.setSpacing(5)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(10, 10, 10, 10)
        self.horizontalSpacer_15 = QSpacerItem(377, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_15)

        self.button_CommentCreate = QPushButton(self.frame_CommentCreateToolsSelected)
        self.button_CommentCreate.setObjectName(u"button_CommentCreate")
        self.button_CommentCreate.setMinimumSize(QSize(100, 40))
        self.button_CommentCreate.setMaximumSize(QSize(100, 40))
        font = QFont()
        font.setBold(True)
        font.setItalic(False)
        self.button_CommentCreate.setFont(font)
        self.button_CommentCreate.setStyleSheet(u"")

        self.horizontalLayout_2.addWidget(self.button_CommentCreate)


        self.verticalLayout.addWidget(self.frame_CommentCreateToolsSelected)


        self.retranslateUi(frame_CommentCreate)

        QMetaObject.connectSlotsByName(frame_CommentCreate)
    # setupUi

    def retranslateUi(self, frame_CommentCreate):
        frame_CommentCreate.setWindowTitle(QCoreApplication.translate("frame_CommentCreate", u"create", None))
        self.line_CommentCreateText.setPlaceholderText(QCoreApplication.translate("frame_CommentCreate", u"What're you thinking?", None))
#if QT_CONFIG(tooltip)
        self.label_CommentCreateImage.setToolTip(QCoreApplication.translate("frame_CommentCreate", u"Your Profile", None))
#endif // QT_CONFIG(tooltip)
        self.label_CommentCreateImage.setText("")
#if QT_CONFIG(tooltip)
        self.button_CommentCreate.setToolTip(QCoreApplication.translate("frame_CommentCreate", u"Create Post", None))
#endif // QT_CONFIG(tooltip)
        self.button_CommentCreate.setText(QCoreApplication.translate("frame_CommentCreate", u"Comment", None))
    # retranslateUi

