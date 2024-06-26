# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'post.ui'
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
    QTextEdit, QVBoxLayout, QWidget)

class Ui_form_Post(object):
    def setupUi(self, form_Post):
        if not form_Post.objectName():
            form_Post.setObjectName(u"form_Post")
        form_Post.resize(800, 300)
        form_Post.setMinimumSize(QSize(390, 0))
        form_Post.setMaximumSize(QSize(16777215, 16777215))
        form_Post.setStyleSheet(u"\n"
"QFrame , QWidget{\n"
"	border: 0;\n"
"	background-color: white;\n"
"}\n"
"\n"
"QWidget#widget_PostImage {\n"
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
"QPushButton#button_More::pressed {\n"
"	background-color:  rgb(235, 237, 239);\n"
"}\n"
"\n"
"\n"
"\n"
"\n"
"QComboBox {\n"
""
                        "	border: 0;\n"
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
        self.verticalLayout_3 = QVBoxLayout(form_Post)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.frame_Main = QFrame(form_Post)
        self.frame_Main.setObjectName(u"frame_Main")
        self.frame_Main.setStyleSheet(u"")
        self.frame_Main.setFrameShape(QFrame.StyledPanel)
        self.frame_Main.setFrameShadow(QFrame.Raised)
        self.layout_Main = QVBoxLayout(self.frame_Main)
        self.layout_Main.setSpacing(10)
        self.layout_Main.setObjectName(u"layout_Main")
        self.layout_Main.setContentsMargins(10, 10, 10, 10)
        self.frame_PostAuthor = QFrame(self.frame_Main)
        self.frame_PostAuthor.setObjectName(u"frame_PostAuthor")
        self.frame_PostAuthor.setMinimumSize(QSize(0, 50))
        self.frame_PostAuthor.setMaximumSize(QSize(16777215, 50))
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

        self.button_More = QPushButton(self.frame_PostAuthor)
        self.button_More.setObjectName(u"button_More")
        self.button_More.setMinimumSize(QSize(30, 30))
        self.button_More.setMaximumSize(QSize(30, 30))
        self.button_More.setCheckable(False)

        self.horizontalLayout.addWidget(self.button_More)


        self.layout_Main.addWidget(self.frame_PostAuthor)

        self.textBrowser_PostText = QTextBrowser(self.frame_Main)
        self.textBrowser_PostText.setObjectName(u"textBrowser_PostText")
        self.textBrowser_PostText.setMinimumSize(QSize(0, 20))
        self.textBrowser_PostText.setMaximumSize(QSize(16777215, 100))
        self.textBrowser_PostText.setOpenExternalLinks(True)

        self.layout_Main.addWidget(self.textBrowser_PostText)

        self.widget_PostImage = QWidget(self.frame_Main)
        self.widget_PostImage.setObjectName(u"widget_PostImage")
        self.widget_PostImage.setMaximumSize(QSize(570, 16777215))

        self.layout_Main.addWidget(self.widget_PostImage)

        self.label_PostData = QTextEdit(self.frame_Main)
        self.label_PostData.setObjectName(u"label_PostData")
        self.label_PostData.setMinimumSize(QSize(0, 30))
        self.label_PostData.setMaximumSize(QSize(16777215, 30))
        self.label_PostData.setReadOnly(True)

        self.layout_Main.addWidget(self.label_PostData)

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
        self.label_Likes.setTextInteractionFlags(Qt.LinksAccessibleByMouse|Qt.TextSelectableByMouse)

        self.horizontalLayout_3.addWidget(self.label_Likes)

        self.label_Dislikes = QLabel(self.frame_PostReactions)
        self.label_Dislikes.setObjectName(u"label_Dislikes")
        self.label_Dislikes.setMinimumSize(QSize(100, 25))
        self.label_Dislikes.setMaximumSize(QSize(16777215, 25))
        self.label_Dislikes.setStyleSheet(u"")
        self.label_Dislikes.setTextFormat(Qt.RichText)
        self.label_Dislikes.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.label_Dislikes.setTextInteractionFlags(Qt.LinksAccessibleByMouse|Qt.TextSelectableByMouse)

        self.horizontalLayout_3.addWidget(self.label_Dislikes)

        self.label_Comments = QLabel(self.frame_PostReactions)
        self.label_Comments.setObjectName(u"label_Comments")
        self.label_Comments.setMinimumSize(QSize(100, 25))
        self.label_Comments.setMaximumSize(QSize(16777215, 25))
        self.label_Comments.setStyleSheet(u"")
        self.label_Comments.setTextFormat(Qt.RichText)
        self.label_Comments.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.label_Comments.setTextInteractionFlags(Qt.LinksAccessibleByMouse|Qt.TextSelectableByMouse)

        self.horizontalLayout_3.addWidget(self.label_Comments)

        self.horizontalSpacer_3 = QSpacerItem(477, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_3)


        self.layout_Main.addWidget(self.frame_PostReactions)

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
        self.button_PostLike = QPushButton(self.frame_PostInfo)
        self.button_PostLike.setObjectName(u"button_PostLike")
        self.button_PostLike.setMinimumSize(QSize(40, 40))
        self.button_PostLike.setMaximumSize(QSize(40, 40))
        self.button_PostLike.setCheckable(True)

        self.horizontalLayout_2.addWidget(self.button_PostLike)

        self.button_PostDislike = QPushButton(self.frame_PostInfo)
        self.button_PostDislike.setObjectName(u"button_PostDislike")
        self.button_PostDislike.setMinimumSize(QSize(40, 40))
        self.button_PostDislike.setMaximumSize(QSize(40, 40))
        self.button_PostDislike.setCheckable(True)

        self.horizontalLayout_2.addWidget(self.button_PostDislike)

        self.button_PostComments = QPushButton(self.frame_PostInfo)
        self.button_PostComments.setObjectName(u"button_PostComments")
        self.button_PostComments.setMinimumSize(QSize(40, 40))
        self.button_PostComments.setMaximumSize(QSize(40, 40))
        self.button_PostComments.setCheckable(False)

        self.horizontalLayout_2.addWidget(self.button_PostComments)

        self.horizontalSpacer_2 = QSpacerItem(628, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_2)


        self.layout_Main.addWidget(self.frame_PostInfo)


        self.verticalLayout_3.addWidget(self.frame_Main)


        self.retranslateUi(form_Post)

        QMetaObject.connectSlotsByName(form_Post)
    # setupUi

    def retranslateUi(self, form_Post):
        form_Post.setWindowTitle(QCoreApplication.translate("form_Post", u"Form", None))
        self.button_More.setText("")
        self.textBrowser_PostText.setHtml(QCoreApplication.translate("form_Post", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'.AppleSystemUIFont'; font-size:13pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>", None))
        self.label_Likes.setText(QCoreApplication.translate("form_Post", u"Likes", None))
        self.label_Dislikes.setText(QCoreApplication.translate("form_Post", u"Dislikes", None))
        self.label_Comments.setText(QCoreApplication.translate("form_Post", u"Comments", None))
        self.button_PostLike.setText("")
        self.button_PostDislike.setText("")
        self.button_PostComments.setText("")
    # retranslateUi

