# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'post.ui'
##
## Created by: Qt User Interface Compiler version 6.6.2
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
from PySide6.QtWidgets import (QApplication, QButtonGroup, QFrame, QHBoxLayout,
    QLabel, QPushButton, QSizePolicy, QSpacerItem,
    QVBoxLayout, QWidget)

class Ui_form_Post(object):
    def setupUi(self, form_Post):
        if not form_Post.objectName():
            form_Post.setObjectName(u"form_Post")
        form_Post.resize(788, 250)
        form_Post.setMinimumSize(QSize(390, 250))
        form_Post.setMaximumSize(QSize(16777215, 300))
        form_Post.setStyleSheet(u"QFrame , QWidget{\n"
"	border: 0;\n"
"	background-color: white;\n"
"}\n"
"\n"
"QFrame#frame {\n"
"	border-radius: 20px;\n"
"	border: 1px solid rgb(235, 237, 239);\n"
"}\n"
"\n"
"QPushButton {\n"
"	height: 40px;\n"
"	padding: 0 5px 0 5px;\n"
"	color: black;\n"
"	margin: 0;\n"
"	border-radius: 20px;\n"
"	background-color:  white;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color:  rgb(235, 237, 239);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"	background-color: rgb(184,191,195);\n"
"}")
        self.verticalLayout_3 = QVBoxLayout(form_Post)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.frame = QFrame(form_Post)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(self.frame)
        self.verticalLayout.setSpacing(10)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(10, 10, 10, 10)
        self.frame_PostAuthor = QFrame(self.frame)
        self.frame_PostAuthor.setObjectName(u"frame_PostAuthor")
        self.frame_PostAuthor.setMinimumSize(QSize(0, 40))
        self.frame_PostAuthor.setMaximumSize(QSize(16777215, 40))
        self.frame_PostAuthor.setStyleSheet(u"QPush")
        self.frame_PostAuthor.setFrameShape(QFrame.StyledPanel)
        self.frame_PostAuthor.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.frame_PostAuthor)
        self.horizontalLayout.setSpacing(10)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.button_PostAuthorAccount = QPushButton(self.frame_PostAuthor)
        self.button_PostAuthorAccount.setObjectName(u"button_PostAuthorAccount")

        self.horizontalLayout.addWidget(self.button_PostAuthorAccount)

        self.label_PostAuthorDate = QLabel(self.frame_PostAuthor)
        self.label_PostAuthorDate.setObjectName(u"label_PostAuthorDate")

        self.horizontalLayout.addWidget(self.label_PostAuthorDate)

        self.horizontalSpacer = QSpacerItem(636, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)


        self.verticalLayout.addWidget(self.frame_PostAuthor)

        self.frame_PostContent = QFrame(self.frame)
        self.frame_PostContent.setObjectName(u"frame_PostContent")
        self.frame_PostContent.setFrameShape(QFrame.StyledPanel)
        self.frame_PostContent.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame_PostContent)
        self.verticalLayout_2.setSpacing(10)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.label_PostContentHeader = QLabel(self.frame_PostContent)
        self.label_PostContentHeader.setObjectName(u"label_PostContentHeader")

        self.verticalLayout_2.addWidget(self.label_PostContentHeader)

        self.label_PostContentImage = QLabel(self.frame_PostContent)
        self.label_PostContentImage.setObjectName(u"label_PostContentImage")

        self.verticalLayout_2.addWidget(self.label_PostContentImage)


        self.verticalLayout.addWidget(self.frame_PostContent)

        self.frame_PostInfo = QFrame(self.frame)
        self.frame_PostInfo.setObjectName(u"frame_PostInfo")
        self.frame_PostInfo.setMinimumSize(QSize(0, 40))
        self.frame_PostInfo.setMaximumSize(QSize(16777215, 40))
        self.frame_PostInfo.setStyleSheet(u"")
        self.frame_PostInfo.setFrameShape(QFrame.StyledPanel)
        self.frame_PostInfo.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.frame_PostInfo)
        self.horizontalLayout_2.setSpacing(10)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.button_PostInfoLikes = QPushButton(self.frame_PostInfo)
        self.buttonGroup_PostReaction = QButtonGroup(form_Post)
        self.buttonGroup_PostReaction.setObjectName(u"buttonGroup_PostReaction")
        self.buttonGroup_PostReaction.addButton(self.button_PostInfoLikes)
        self.button_PostInfoLikes.setObjectName(u"button_PostInfoLikes")
        self.button_PostInfoLikes.setCheckable(True)

        self.horizontalLayout_2.addWidget(self.button_PostInfoLikes)

        self.button_PostInfoDislikes = QPushButton(self.frame_PostInfo)
        self.buttonGroup_PostReaction.addButton(self.button_PostInfoDislikes)
        self.button_PostInfoDislikes.setObjectName(u"button_PostInfoDislikes")
        self.button_PostInfoDislikes.setCheckable(True)

        self.horizontalLayout_2.addWidget(self.button_PostInfoDislikes)

        self.button_PostInfoComments = QPushButton(self.frame_PostInfo)
        self.button_PostInfoComments.setObjectName(u"button_PostInfoComments")
        self.button_PostInfoComments.setCheckable(False)

        self.horizontalLayout_2.addWidget(self.button_PostInfoComments)

        self.horizontalSpacer_2 = QSpacerItem(628, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_2)


        self.verticalLayout.addWidget(self.frame_PostInfo)


        self.verticalLayout_3.addWidget(self.frame)


        self.retranslateUi(form_Post)

        QMetaObject.connectSlotsByName(form_Post)
    # setupUi

    def retranslateUi(self, form_Post):
        form_Post.setWindowTitle(QCoreApplication.translate("form_Post", u"Form", None))
        self.button_PostAuthorAccount.setText(QCoreApplication.translate("form_Post", u"Admin", None))
        self.label_PostAuthorDate.setText(QCoreApplication.translate("form_Post", u"12.05.1925", None))
        self.label_PostContentHeader.setText("")
        self.label_PostContentImage.setText("")
        self.button_PostInfoLikes.setText("")
        self.button_PostInfoDislikes.setText("")
        self.button_PostInfoComments.setText("")
    # retranslateUi

