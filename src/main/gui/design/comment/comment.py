# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'comment.ui'
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
from PySide6.QtWidgets import (QApplication, QFrame, QHBoxLayout, QLabel,
    QPushButton, QSizePolicy, QSpacerItem, QTextBrowser,
    QVBoxLayout, QWidget)

class Ui_form_Comment(object):
    def setupUi(self, form_Comment):
        if not form_Comment.objectName():
            form_Comment.setObjectName(u"form_Comment")
        form_Comment.resize(716, 170)
        form_Comment.setMinimumSize(QSize(390, 0))
        form_Comment.setMaximumSize(QSize(16777215, 16777215))
        form_Comment.setStyleSheet(u"QFrame , QWidget{\n"
"	border: 0;\n"
"	background-color: white;\n"
"}\n"
"\n"
"QWidget#widget_CommentImage {\n"
"	border-radius: 10px;\n"
"}\n"
"\n"
"QFrame#frame_Main {\n"
"	border-radius: 20px;\n"
"	border: 0px solid rgb(235, 237, 239);\n"
"}\n"
"\n"
"QFrame#frame_UserContainer {\n"
"	border-radius: 20px;\n"
"}\n"
"\n"
"QFrame#frame_CommentReactions {\n"
"	border-bottom: 1px solid rgb(235, 237, 239);\n"
"}\n"
"\n"
"QTextEdit#label_PostData {\n"
"	border-bottom: 1px solid rgb(235, 237, 239);\n"
"}\n"
"\n"
"QPushButton {\n"
"	padding: 0 5px 0 5px;\n"
"	color: black;\n"
"	margin: 0;\n"
"	border-radius: 15px;\n"
"	background-color:  white;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color:  rgb(235, 237, 239);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"	background-color: rgb(184,191,195);\n"
"}\n"
"\n"
"QPushButton#button_More {\n"
"	border-radius: 15px;\n"
"}\n"
"\n"
"QPushButton#button_More::pressed {\n"
"	background-color:  rgb(235, 237, 239);\n"
"}\n"
"\n"
"\n"
"\n"
"\n"
"QComboBox {\n"
"	border: 0;\n"
""
                        "	border-radius: 15px;	\n"
"}\n"
"\n"
"QComboBox::hover {\n"
"	background-color: rgb(235, 237, 239);\n"
"}\n"
"\n"
"QComboBox::pressed {\n"
"	background-color:  rgb(184,191,195);\n"
"}\n"
"\n"
"QComboBox::drop-down {\n"
"	border-radius: 15px;\n"
"	width: 100px;\n"
"}\n"
"\n"
"QComboBox::down-arrow {\n"
"	border-radius: 15px;\n"
"	width: 30px;\n"
"	height: 30px;\n"
"}\n"
"\n"
"QComboBox:on {\n"
"	border-radius: 15px;\n"
"	width: 100px;\n"
"} \n"
"\n"
"QComboBox QAbstractItemView {\n"
"	border-radius: 15px;\n"
"	color: red;\n"
"	width: 100px;\n"
"}\n"
"\n"
"\n"
"\n"
"QComboBox QListView:item {\n"
"\n"
"	color: black;\n"
"}\n"
"\n"
"QComboBox QAbstractItemView::item:hover {\n"
"	color: black;\n"
"	background-color: rgb(235, 237, 239);\n"
"}\n"
"\n"
"QComboBox QAbstractItemView::item:pressed {\n"
"	color: black;\n"
"	background-color:  rgb(184,191,195);\n"
"}\n"
"\n"
"QComboBox QAbstractItemView::item:pselected {\n"
"	color: black;\n"
"	background-color:  rgb(184,191,195);\n"
"}\n"
"\n"
"\n"
"")
        self.verticalLayout_3 = QVBoxLayout(form_Comment)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.frame_Main = QFrame(form_Comment)
        self.frame_Main.setObjectName(u"frame_Main")
        self.frame_Main.setStyleSheet(u"")
        self.frame_Main.setFrameShape(QFrame.StyledPanel)
        self.frame_Main.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(self.frame_Main)
        self.verticalLayout.setSpacing(10)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(10, 10, 10, 10)
        self.frame_CommentAuthor = QFrame(self.frame_Main)
        self.frame_CommentAuthor.setObjectName(u"frame_CommentAuthor")
        self.frame_CommentAuthor.setMinimumSize(QSize(0, 40))
        self.frame_CommentAuthor.setMaximumSize(QSize(16777215, 40))
        self.frame_CommentAuthor.setStyleSheet(u"")
        self.frame_CommentAuthor.setFrameShape(QFrame.StyledPanel)
        self.frame_CommentAuthor.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.frame_CommentAuthor)
        self.horizontalLayout.setSpacing(10)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.frame_UserContainer = QFrame(self.frame_CommentAuthor)
        self.frame_UserContainer.setObjectName(u"frame_UserContainer")
        self.frame_UserContainer.setMinimumSize(QSize(180, 40))
        self.frame_UserContainer.setMaximumSize(QSize(180, 40))
        self.frame_UserContainer.setFrameShape(QFrame.StyledPanel)
        self.frame_UserContainer.setFrameShadow(QFrame.Raised)
        self.layout_userName = QHBoxLayout(self.frame_UserContainer)
        self.layout_userName.setSpacing(5)
        self.layout_userName.setObjectName(u"layout_userName")
        self.layout_userName.setContentsMargins(0, 0, 0, 0)
        self.textBrowser_UserName = QTextBrowser(self.frame_UserContainer)
        self.textBrowser_UserName.setObjectName(u"textBrowser_UserName")
        self.textBrowser_UserName.setMinimumSize(QSize(0, 40))
        self.textBrowser_UserName.setMaximumSize(QSize(16777215, 40))
        self.textBrowser_UserName.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.textBrowser_UserName.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)

        self.layout_userName.addWidget(self.textBrowser_UserName)


        self.horizontalLayout.addWidget(self.frame_UserContainer)

        self.horizontalSpacer = QSpacerItem(636, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.button_More = QPushButton(self.frame_CommentAuthor)
        self.button_More.setObjectName(u"button_More")
        self.button_More.setMinimumSize(QSize(30, 30))
        self.button_More.setMaximumSize(QSize(30, 30))
        self.button_More.setCheckable(False)

        self.horizontalLayout.addWidget(self.button_More)


        self.verticalLayout.addWidget(self.frame_CommentAuthor)

        self.textBrowser_CommentText = QTextBrowser(self.frame_Main)
        self.textBrowser_CommentText.setObjectName(u"textBrowser_CommentText")
        self.textBrowser_CommentText.setMinimumSize(QSize(0, 20))
        self.textBrowser_CommentText.setMaximumSize(QSize(16777215, 100))
        self.textBrowser_CommentText.setOpenExternalLinks(True)

        self.verticalLayout.addWidget(self.textBrowser_CommentText)

        self.frame_CommentReactions = QFrame(self.frame_Main)
        self.frame_CommentReactions.setObjectName(u"frame_CommentReactions")
        self.frame_CommentReactions.setMinimumSize(QSize(0, 20))
        self.frame_CommentReactions.setMaximumSize(QSize(16777215, 15))
        self.frame_CommentReactions.setFrameShape(QFrame.StyledPanel)
        self.frame_CommentReactions.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.frame_CommentReactions)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.label_Likes = QLabel(self.frame_CommentReactions)
        self.label_Likes.setObjectName(u"label_Likes")
        self.label_Likes.setMinimumSize(QSize(100, 15))
        self.label_Likes.setMaximumSize(QSize(16777215, 15))
        self.label_Likes.setTextFormat(Qt.RichText)
        self.label_Likes.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.label_Likes.setTextInteractionFlags(Qt.LinksAccessibleByMouse|Qt.TextSelectableByMouse)

        self.horizontalLayout_3.addWidget(self.label_Likes)

        self.label_Dislikes = QLabel(self.frame_CommentReactions)
        self.label_Dislikes.setObjectName(u"label_Dislikes")
        self.label_Dislikes.setMinimumSize(QSize(100, 15))
        self.label_Dislikes.setMaximumSize(QSize(16777215, 15))
        self.label_Dislikes.setStyleSheet(u"")
        self.label_Dislikes.setTextFormat(Qt.RichText)
        self.label_Dislikes.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.label_Dislikes.setTextInteractionFlags(Qt.LinksAccessibleByMouse|Qt.TextSelectableByMouse)

        self.horizontalLayout_3.addWidget(self.label_Dislikes)

        self.label_CommentData = QLabel(self.frame_CommentReactions)
        self.label_CommentData.setObjectName(u"label_CommentData")
        self.label_CommentData.setMinimumSize(QSize(200, 0))
        self.label_CommentData.setMaximumSize(QSize(200, 16777215))
        self.label_CommentData.setTextFormat(Qt.RichText)

        self.horizontalLayout_3.addWidget(self.label_CommentData)

        self.horizontalSpacer_3 = QSpacerItem(477, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_3)


        self.verticalLayout.addWidget(self.frame_CommentReactions)

        self.frame_CommentInfo = QFrame(self.frame_Main)
        self.frame_CommentInfo.setObjectName(u"frame_CommentInfo")
        self.frame_CommentInfo.setMinimumSize(QSize(0, 30))
        self.frame_CommentInfo.setMaximumSize(QSize(16777215, 30))
        self.frame_CommentInfo.setStyleSheet(u"")
        self.frame_CommentInfo.setFrameShape(QFrame.StyledPanel)
        self.frame_CommentInfo.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.frame_CommentInfo)
        self.horizontalLayout_2.setSpacing(10)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.button_CommentLike = QPushButton(self.frame_CommentInfo)
        self.button_CommentLike.setObjectName(u"button_CommentLike")
        self.button_CommentLike.setMinimumSize(QSize(30, 30))
        self.button_CommentLike.setMaximumSize(QSize(30, 30))
        self.button_CommentLike.setCheckable(True)

        self.horizontalLayout_2.addWidget(self.button_CommentLike)

        self.button_CommentDislike = QPushButton(self.frame_CommentInfo)
        self.button_CommentDislike.setObjectName(u"button_CommentDislike")
        self.button_CommentDislike.setMinimumSize(QSize(30, 30))
        self.button_CommentDislike.setMaximumSize(QSize(30, 30))
        self.button_CommentDislike.setCheckable(True)

        self.horizontalLayout_2.addWidget(self.button_CommentDislike)

        self.horizontalSpacer_2 = QSpacerItem(628, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_2)


        self.verticalLayout.addWidget(self.frame_CommentInfo)


        self.verticalLayout_3.addWidget(self.frame_Main)


        self.retranslateUi(form_Comment)

        QMetaObject.connectSlotsByName(form_Comment)
    # setupUi

    def retranslateUi(self, form_Comment):
        form_Comment.setWindowTitle(QCoreApplication.translate("form_Comment", u"Form", None))
        self.button_More.setText("")
        self.textBrowser_CommentText.setHtml(QCoreApplication.translate("form_Comment", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'.AppleSystemUIFont'; font-size:13pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>", None))
        self.label_Likes.setText(QCoreApplication.translate("form_Comment", u"Likes", None))
        self.label_Dislikes.setText(QCoreApplication.translate("form_Comment", u"Dislikes", None))
        self.label_CommentData.setText(QCoreApplication.translate("form_Comment", u"Data", None))
        self.button_CommentLike.setText("")
        self.button_CommentDislike.setText("")
    # retranslateUi

