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
    QTextBrowser, QTextEdit, QVBoxLayout, QWidget)

class Ui_form_Post(object):
    def setupUi(self, form_Post):
        if not form_Post.objectName():
            form_Post.setObjectName(u"form_Post")
        form_Post.resize(800, 300)
        form_Post.setMinimumSize(QSize(390, 0))
        form_Post.setMaximumSize(QSize(16777215, 16777215))
        form_Post.setStyleSheet(u"QFrame , QWidget{\n"
"	border: 0;\n"
"	background-color: white;\n"
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
"QFrame#frame_PostReactions {\n"
"	border-bottom: 1px solid rgb(235, 237, 239);\n"
"}\n"
"\n"
"QTextEdit#label_PostData {\n"
"	border-bottom: 1px solid rgb(235, 237, 239);\n"
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
"}\n"
"\n"
"QPushButton#button_More {\n"
"	border-radius: 15px;\n"
"}\n"
"\n"
"\n"
"\n"
"QComboBox {\n"
"	border: 0;\n"
"	border-radius: 15px;	\n"
"}\n"
"\n"
"QComboBox::hover {\n"
"	background-color: rgb(235, 237, 239);\n"
"}\n"
"\n"
"QComboBox::pressed {\n"
"	background-c"
                        "olor:  rgb(184,191,195);\n"
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
        self.verticalLayout_3 = QVBoxLayout(form_Post)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.frame_Main = QFrame(form_Post)
        self.frame_Main.setObjectName(u"frame_Main")
        self.frame_Main.setStyleSheet(u"")
        self.frame_Main.setFrameShape(QFrame.StyledPanel)
        self.frame_Main.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(self.frame_Main)
        self.verticalLayout.setSpacing(10)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(10, 10, 10, 10)
        self.frame_PostAuthor = QFrame(self.frame_Main)
        self.frame_PostAuthor.setObjectName(u"frame_PostAuthor")
        self.frame_PostAuthor.setMinimumSize(QSize(0, 60))
        self.frame_PostAuthor.setMaximumSize(QSize(16777215, 60))
        self.frame_PostAuthor.setStyleSheet(u"")
        self.frame_PostAuthor.setFrameShape(QFrame.StyledPanel)
        self.frame_PostAuthor.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.frame_PostAuthor)
        self.horizontalLayout.setSpacing(10)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.frame_UserContainer = QFrame(self.frame_PostAuthor)
        self.frame_UserContainer.setObjectName(u"frame_UserContainer")
        self.frame_UserContainer.setMinimumSize(QSize(180, 50))
        self.frame_UserContainer.setMaximumSize(QSize(180, 50))
        self.frame_UserContainer.setFrameShape(QFrame.StyledPanel)
        self.frame_UserContainer.setFrameShadow(QFrame.Raised)
        self.layout_userName = QHBoxLayout(self.frame_UserContainer)
        self.layout_userName.setSpacing(5)
        self.layout_userName.setObjectName(u"layout_userName")
        self.layout_userName.setContentsMargins(0, 0, 0, 0)
        self.label_UserName = QTextBrowser(self.frame_UserContainer)
        self.label_UserName.setObjectName(u"label_UserName")
        self.label_UserName.setMinimumSize(QSize(0, 40))
        self.label_UserName.setMaximumSize(QSize(16777215, 50))
        self.label_UserName.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.label_UserName.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)

        self.layout_userName.addWidget(self.label_UserName)


        self.horizontalLayout.addWidget(self.frame_UserContainer)

        self.horizontalSpacer = QSpacerItem(636, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.button_More = QPushButton(self.frame_PostAuthor)
        self.button_More.setObjectName(u"button_More")
        self.button_More.setMinimumSize(QSize(30, 30))
        self.button_More.setMaximumSize(QSize(30, 30))
        self.button_More.setCheckable(False)

        self.horizontalLayout.addWidget(self.button_More)


        self.verticalLayout.addWidget(self.frame_PostAuthor)

        self.label_PostText = QTextBrowser(self.frame_Main)
        self.label_PostText.setObjectName(u"label_PostText")
        self.label_PostText.setMinimumSize(QSize(0, 30))
        self.label_PostText.setMaximumSize(QSize(16777215, 16777215))
        self.label_PostText.setOpenExternalLinks(True)

        self.verticalLayout.addWidget(self.label_PostText)

        self.label_PostData = QTextEdit(self.frame_Main)
        self.label_PostData.setObjectName(u"label_PostData")
        self.label_PostData.setMinimumSize(QSize(0, 30))
        self.label_PostData.setMaximumSize(QSize(16777215, 30))
        self.label_PostData.setReadOnly(True)

        self.verticalLayout.addWidget(self.label_PostData)

        self.frame_PostReactions = QFrame(self.frame_Main)
        self.frame_PostReactions.setObjectName(u"frame_PostReactions")
        self.frame_PostReactions.setMinimumSize(QSize(0, 30))
        self.frame_PostReactions.setMaximumSize(QSize(16777215, 30))
        self.frame_PostReactions.setFrameShape(QFrame.StyledPanel)
        self.frame_PostReactions.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.frame_PostReactions)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.label_Likes = QLabel(self.frame_PostReactions)
        self.label_Likes.setObjectName(u"label_Likes")
        self.label_Likes.setMinimumSize(QSize(100, 25))
        self.label_Likes.setMaximumSize(QSize(16777215, 25))
        self.label_Likes.setTextFormat(Qt.RichText)
        self.label_Likes.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.horizontalLayout_3.addWidget(self.label_Likes)

        self.label_Dislikes = QLabel(self.frame_PostReactions)
        self.label_Dislikes.setObjectName(u"label_Dislikes")
        self.label_Dislikes.setMinimumSize(QSize(100, 25))
        self.label_Dislikes.setMaximumSize(QSize(16777215, 25))
        self.label_Dislikes.setStyleSheet(u"")
        self.label_Dislikes.setTextFormat(Qt.RichText)
        self.label_Dislikes.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.horizontalLayout_3.addWidget(self.label_Dislikes)

        self.label_Comments = QLabel(self.frame_PostReactions)
        self.label_Comments.setObjectName(u"label_Comments")
        self.label_Comments.setMinimumSize(QSize(100, 25))
        self.label_Comments.setMaximumSize(QSize(16777215, 25))
        self.label_Comments.setStyleSheet(u"")
        self.label_Comments.setTextFormat(Qt.RichText)
        self.label_Comments.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.horizontalLayout_3.addWidget(self.label_Comments)

        self.horizontalSpacer_3 = QSpacerItem(477, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_3)


        self.verticalLayout.addWidget(self.frame_PostReactions)

        self.frame_PostInfo = QFrame(self.frame_Main)
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
        self.button_PostInfoLikes.setMinimumSize(QSize(40, 40))
        self.button_PostInfoLikes.setMaximumSize(QSize(40, 40))
        self.button_PostInfoLikes.setCheckable(True)

        self.horizontalLayout_2.addWidget(self.button_PostInfoLikes)

        self.button_PostInfoDislikes = QPushButton(self.frame_PostInfo)
        self.buttonGroup_PostReaction.addButton(self.button_PostInfoDislikes)
        self.button_PostInfoDislikes.setObjectName(u"button_PostInfoDislikes")
        self.button_PostInfoDislikes.setMinimumSize(QSize(40, 40))
        self.button_PostInfoDislikes.setMaximumSize(QSize(40, 40))
        self.button_PostInfoDislikes.setCheckable(True)

        self.horizontalLayout_2.addWidget(self.button_PostInfoDislikes)

        self.button_PostInfoComments = QPushButton(self.frame_PostInfo)
        self.button_PostInfoComments.setObjectName(u"button_PostInfoComments")
        self.button_PostInfoComments.setMinimumSize(QSize(40, 40))
        self.button_PostInfoComments.setMaximumSize(QSize(40, 40))
        self.button_PostInfoComments.setCheckable(False)

        self.horizontalLayout_2.addWidget(self.button_PostInfoComments)

        self.horizontalSpacer_2 = QSpacerItem(628, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_2)


        self.verticalLayout.addWidget(self.frame_PostInfo)


        self.verticalLayout_3.addWidget(self.frame_Main)


        self.retranslateUi(form_Post)

        QMetaObject.connectSlotsByName(form_Post)
    # setupUi

    def retranslateUi(self, form_Post):
        form_Post.setWindowTitle(QCoreApplication.translate("form_Post", u"Form", None))
        self.button_More.setText("")
        self.label_PostText.setHtml(QCoreApplication.translate("form_Post", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'.AppleSystemUIFont'; font-size:13pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">HUESOS</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>", None))
        self.label_Likes.setText(QCoreApplication.translate("form_Post", u"Likes", None))
        self.label_Dislikes.setText(QCoreApplication.translate("form_Post", u"Dislikes", None))
        self.label_Comments.setText(QCoreApplication.translate("form_Post", u"Comments", None))
        self.button_PostInfoLikes.setText("")
        self.button_PostInfoDislikes.setText("")
        self.button_PostInfoComments.setText("")
    # retranslateUi

