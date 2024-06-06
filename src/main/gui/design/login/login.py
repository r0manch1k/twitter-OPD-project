# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'login.ui'
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
from PySide6.QtWidgets import (QApplication, QFrame, QGridLayout, QHBoxLayout,
    QLabel, QLineEdit, QPushButton, QSizePolicy,
    QSpacerItem, QStackedWidget, QTextBrowser, QVBoxLayout,
    QWidget)

class Ui_form_LogIn(object):
    def setupUi(self, form_LogIn):
        if not form_LogIn.objectName():
            form_LogIn.setObjectName(u"form_LogIn")
        form_LogIn.resize(1000, 550)
        form_LogIn.setMinimumSize(QSize(1000, 550))
        form_LogIn.setMaximumSize(QSize(1000, 550))
        form_LogIn.setStyleSheet(u"QFrame, QWidget {\n"
"	border: 0;		\n"
"	background-color: transparent;\n"
"}\n"
"\n"
"\n"
"QPushButton {\n"
"	width: 40px;\n"
"	height: 40px;\n"
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
"QLineEdit {\n"
"	height: 50px;\n"
"	color: black;\n"
"	border-radius: 20px;\n"
"	background-color:  rgb(235, 237, 239);\n"
"	padding-left: 10px;\n"
"}\n"
"\n"
"/*------*/\n"
"\n"
"QLabel#label_FormatError,\n"
"QLabel#label_RecoverError,\n"
"QLabel#label_NewError {\n"
"	color: red;\n"
"}\n"
"\n"
"QPushButton#button_PasswordVisibility {\n"
"	padding-right: 10px:\n"
"}\n"
"\n"
"/*------SCROLL BAR------*/\n"
"\n"
"QTextBrowser QScrollBar:vertical {\n"
"	background-color: rgb(235, 237, 239);\n"
"	width: 8px;\n"
"	border-radius: 4px;\n"
"}\n"
"\n"
"QTextBrowser QScrollBar::handle:vertical {\n"
"        background-col"
                        "or: rgb(184,191,195);\n"
"        min-height: 5px;\n"
"        border-radius: 4px;\n"
"}\n"
"\n"
"QTextBrowser QScrollBar::add-line:horizontal {\n"
"      border: none;\n"
"      background: none;\n"
"}\n"
"\n"
"QTextBrowser QScrollBar::sub-line:horizontal {\n"
"      border: none;\n"
"      background: none;\n"
"}")
        self.gridLayout_2 = QGridLayout(form_LogIn)
        self.gridLayout_2.setSpacing(0)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.stacked_Main = QStackedWidget(form_LogIn)
        self.stacked_Main.setObjectName(u"stacked_Main")
        self.stacked_Main.setStyleSheet(u"QTextBrowser QScrollBar:vertical {\n"
"	background-color: rgb(235, 237, 239);\n"
"	width: 8px;\n"
"	border-radius: 4px;\n"
"}\n"
"\n"
"QTextBrowser QScrollBar::handle:vertical {\n"
"	background-color: rgb(184,191,195);\n"
"	min-height: 5px;\n"
"	border-radius: 4px;\n"
"}\n"
"\n"
"QTextBrowser QScrollBar::add-line:horizontal {\n"
"	width: 0px;\n"
"	height: 0px;\n"
"	border: none;\n"
"	background: none;\n"
"}\n"
"\n"
"QTextBrowser QScrollBar::sub-line:horizontal {\n"
"	width: 0px;\n"
"	height: 0px;\n"
"	border: none;\n"
"	background: none;\n"
"}")
        self.page_Main = QWidget()
        self.page_Main.setObjectName(u"page_Main")
        self.page_Main.setStyleSheet(u"")
        self.gridLayout_3 = QGridLayout(self.page_Main)
        self.gridLayout_3.setSpacing(0)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.gridLayout_3.setContentsMargins(0, 0, 0, 0)
        self.frame_Main = QFrame(self.page_Main)
        self.frame_Main.setObjectName(u"frame_Main")
        self.frame_Main.setStyleSheet(u"")
        self.frame_Main.setFrameShape(QFrame.StyledPanel)
        self.frame_Main.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.frame_Main)
        self.horizontalLayout.setSpacing(10)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.frame_ControlMain = QFrame(self.frame_Main)
        self.frame_ControlMain.setObjectName(u"frame_ControlMain")
        self.frame_ControlMain.setMinimumSize(QSize(325, 0))
        self.frame_ControlMain.setMaximumSize(QSize(325, 16777215))
        self.frame_ControlMain.setFrameShape(QFrame.StyledPanel)
        self.frame_ControlMain.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame_ControlMain)
        self.verticalLayout_2.setSpacing(10)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.frame_Control = QFrame(self.frame_ControlMain)
        self.frame_Control.setObjectName(u"frame_Control")
        self.frame_Control.setMinimumSize(QSize(0, 60))
        self.frame_Control.setMaximumSize(QSize(16777215, 60))
        self.frame_Control.setFrameShape(QFrame.StyledPanel)
        self.frame_Control.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.frame_Control)
        self.horizontalLayout_2.setSpacing(10)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(10, 10, 10, 10)
        self.button_ControlBack = QPushButton(self.frame_Control)
        self.button_ControlBack.setObjectName(u"button_ControlBack")

        self.horizontalLayout_2.addWidget(self.button_ControlBack)

        self.horizontalSpacer_3 = QSpacerItem(252, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_3)


        self.verticalLayout_2.addWidget(self.frame_Control)

        self.verticalSpacer_3 = QSpacerItem(20, 477, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer_3)


        self.horizontalLayout.addWidget(self.frame_ControlMain)

        self.frame_LogIn_1 = QFrame(self.frame_Main)
        self.frame_LogIn_1.setObjectName(u"frame_LogIn_1")
        self.frame_LogIn_1.setMinimumSize(QSize(327, 0))
        self.frame_LogIn_1.setStyleSheet(u"")
        self.frame_LogIn_1.setFrameShape(QFrame.StyledPanel)
        self.frame_LogIn_1.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(self.frame_LogIn_1)
        self.verticalLayout.setSpacing(10)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalSpacer = QSpacerItem(20, 37, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)

        self.frame_LogIn_2 = QFrame(self.frame_LogIn_1)
        self.frame_LogIn_2.setObjectName(u"frame_LogIn_2")
        self.frame_LogIn_2.setMinimumSize(QSize(0, 450))
        self.frame_LogIn_2.setMaximumSize(QSize(16777215, 450))
        self.frame_LogIn_2.setStyleSheet(u"QFrame {\n"
"	background-color: white;\n"
"	border-radius: 30px;\n"
"}\n"
"\n"
"QPushButton {\n"
"	height: 60px;\n"
"	background-color: black;\n"
"	color: white;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"	background-color: rgb(30,30,30);\n"
"}")
        self.frame_LogIn_2.setFrameShape(QFrame.StyledPanel)
        self.frame_LogIn_2.setFrameShadow(QFrame.Raised)
        self.gridLayout = QGridLayout(self.frame_LogIn_2)
        self.gridLayout.setSpacing(0)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalSpacer_4 = QSpacerItem(20, 20, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Minimum)

        self.gridLayout.addItem(self.verticalSpacer_4, 0, 1, 1, 1)

        self.horizontalSpacer_2 = QSpacerItem(20, 20, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer_2, 1, 0, 1, 1)

        self.frame_LogIn_3 = QFrame(self.frame_LogIn_2)
        self.frame_LogIn_3.setObjectName(u"frame_LogIn_3")
        self.frame_LogIn_3.setMinimumSize(QSize(287, 410))
        self.frame_LogIn_3.setStyleSheet(u"QFrame#frame_PasswordInput {\n"
"	height: 60px;\n"
"	color: black;\n"
"	border-radius: 20px;\n"
"	background-color:  rgb(235, 237, 239);\n"
"	padding-left: 10px;\n"
"}\n"
"\n"
"\n"
"QLineEdit#line_Password {\n"
"	border: 0;\n"
"	padding-left: 0;\n"
"	background-color: rgb(235, 237, 239);\n"
"	border-top-right-radius: 0;\n"
"	border-bottom-right-radius: 0;\n"
"}\n"
"\n"
"QPushButton#button_PasswordVisibility {\n"
"	height: 60px;\n"
"	border: 20px;\n"
"	background-color: rgb(235, 237, 239);\n"
"	border-top-left-radius: 0;\n"
"	border-bottom-left-radius: 0;\n"
"}")
        self.frame_LogIn_3.setFrameShape(QFrame.StyledPanel)
        self.frame_LogIn_3.setFrameShadow(QFrame.Raised)
        self.verticalLayout_12 = QVBoxLayout(self.frame_LogIn_3)
        self.verticalLayout_12.setSpacing(10)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.verticalLayout_12.setContentsMargins(0, 0, 0, 0)
        self.label_SignIn = QLabel(self.frame_LogIn_3)
        self.label_SignIn.setObjectName(u"label_SignIn")
        font = QFont()
        font.setPointSize(25)
        font.setBold(True)
        self.label_SignIn.setFont(font)
        self.label_SignIn.setIndent(0)

        self.verticalLayout_12.addWidget(self.label_SignIn)

        self.textBrowser_Rules = QTextBrowser(self.frame_LogIn_3)
        self.textBrowser_Rules.setObjectName(u"textBrowser_Rules")
        self.textBrowser_Rules.setMaximumSize(QSize(16777215, 100))
        self.textBrowser_Rules.setStyleSheet(u"")

        self.verticalLayout_12.addWidget(self.textBrowser_Rules)

        self.verticalSpacer_7 = QSpacerItem(20, 20, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Minimum)

        self.verticalLayout_12.addItem(self.verticalSpacer_7)

        self.line_Email = QLineEdit(self.frame_LogIn_3)
        self.line_Email.setObjectName(u"line_Email")
        font1 = QFont()
        font1.setPointSize(15)
        self.line_Email.setFont(font1)
        self.line_Email.setStyleSheet(u"")

        self.verticalLayout_12.addWidget(self.line_Email)

        self.frame_PasswordInput = QFrame(self.frame_LogIn_3)
        self.frame_PasswordInput.setObjectName(u"frame_PasswordInput")
        self.frame_PasswordInput.setMinimumSize(QSize(0, 50))
        self.frame_PasswordInput.setMaximumSize(QSize(16777215, 50))
        self.frame_PasswordInput.setStyleSheet(u"x")
        self.frame_PasswordInput.setFrameShape(QFrame.StyledPanel)
        self.frame_PasswordInput.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.frame_PasswordInput)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.line_Password = QLineEdit(self.frame_PasswordInput)
        self.line_Password.setObjectName(u"line_Password")
        self.line_Password.setFont(font1)
        self.line_Password.setMaxLength(16)
        self.line_Password.setEchoMode(QLineEdit.Password)

        self.horizontalLayout_3.addWidget(self.line_Password)

        self.button_PasswordVisibility = QPushButton(self.frame_PasswordInput)
        self.button_PasswordVisibility.setObjectName(u"button_PasswordVisibility")
        self.button_PasswordVisibility.setCheckable(True)

        self.horizontalLayout_3.addWidget(self.button_PasswordVisibility)


        self.verticalLayout_12.addWidget(self.frame_PasswordInput)

        self.frame_SignsLogIn = QFrame(self.frame_LogIn_3)
        self.frame_SignsLogIn.setObjectName(u"frame_SignsLogIn")
        self.frame_SignsLogIn.setFrameShape(QFrame.StyledPanel)
        self.frame_SignsLogIn.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.frame_SignsLogIn)
        self.verticalLayout_3.setSpacing(5)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.label_LogInError = QLabel(self.frame_SignsLogIn)
        self.label_LogInError.setObjectName(u"label_LogInError")
        self.label_LogInError.setMinimumSize(QSize(287, 20))
        self.label_LogInError.setMaximumSize(QSize(287, 20))

        self.verticalLayout_3.addWidget(self.label_LogInError)

        self.textBrowser_toSignUp = QTextBrowser(self.frame_SignsLogIn)
        self.textBrowser_toSignUp.setObjectName(u"textBrowser_toSignUp")
        self.textBrowser_toSignUp.setMinimumSize(QSize(0, 20))
        self.textBrowser_toSignUp.setMaximumSize(QSize(16777215, 20))

        self.verticalLayout_3.addWidget(self.textBrowser_toSignUp)

        self.textBrowser_Reset = QTextBrowser(self.frame_SignsLogIn)
        self.textBrowser_Reset.setObjectName(u"textBrowser_Reset")
        self.textBrowser_Reset.setMinimumSize(QSize(0, 20))
        self.textBrowser_Reset.setMaximumSize(QSize(16777215, 20))

        self.verticalLayout_3.addWidget(self.textBrowser_Reset)


        self.verticalLayout_12.addWidget(self.frame_SignsLogIn)

        self.button_LogIn = QPushButton(self.frame_LogIn_3)
        self.button_LogIn.setObjectName(u"button_LogIn")
        font2 = QFont()
        font2.setBold(True)
        self.button_LogIn.setFont(font2)

        self.verticalLayout_12.addWidget(self.button_LogIn)


        self.gridLayout.addWidget(self.frame_LogIn_3, 1, 1, 1, 1)

        self.horizontalSpacer_4 = QSpacerItem(20, 20, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer_4, 1, 2, 1, 1)

        self.verticalSpacer_5 = QSpacerItem(20, 20, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Minimum)

        self.gridLayout.addItem(self.verticalSpacer_5, 2, 1, 1, 1)


        self.verticalLayout.addWidget(self.frame_LogIn_2)

        self.verticalSpacer_2 = QSpacerItem(20, 37, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer_2)


        self.horizontalLayout.addWidget(self.frame_LogIn_1)

        self.horizontalSpacer = QSpacerItem(320, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)


        self.gridLayout_3.addWidget(self.frame_Main, 0, 0, 1, 1)

        self.stacked_Main.addWidget(self.page_Main)
        self.page_Reset = QWidget()
        self.page_Reset.setObjectName(u"page_Reset")
        self.gridLayout_5 = QGridLayout(self.page_Reset)
        self.gridLayout_5.setSpacing(0)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.gridLayout_5.setContentsMargins(0, 0, 0, 0)
        self.frame_Reset = QFrame(self.page_Reset)
        self.frame_Reset.setObjectName(u"frame_Reset")
        self.frame_Reset.setFrameShape(QFrame.StyledPanel)
        self.frame_Reset.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.frame_Reset)
        self.horizontalLayout_4.setSpacing(10)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.frame_Reset_1 = QFrame(self.frame_Reset)
        self.frame_Reset_1.setObjectName(u"frame_Reset_1")
        self.frame_Reset_1.setMinimumSize(QSize(325, 0))
        self.frame_Reset_1.setFrameShape(QFrame.StyledPanel)
        self.frame_Reset_1.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.frame_Reset_1)
        self.verticalLayout_4.setSpacing(10)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.verticalSpacer_8 = QSpacerItem(20, 477, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_4.addItem(self.verticalSpacer_8)


        self.horizontalLayout_4.addWidget(self.frame_Reset_1)

        self.frame_Reset_2 = QFrame(self.frame_Reset)
        self.frame_Reset_2.setObjectName(u"frame_Reset_2")
        self.frame_Reset_2.setMinimumSize(QSize(327, 0))
        self.frame_Reset_2.setStyleSheet(u"")
        self.frame_Reset_2.setFrameShape(QFrame.StyledPanel)
        self.frame_Reset_2.setFrameShadow(QFrame.Raised)
        self.verticalLayout_5 = QVBoxLayout(self.frame_Reset_2)
        self.verticalLayout_5.setSpacing(10)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.verticalSpacer_9 = QSpacerItem(20, 37, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_5.addItem(self.verticalSpacer_9)

        self.frame_Reset_3 = QFrame(self.frame_Reset_2)
        self.frame_Reset_3.setObjectName(u"frame_Reset_3")
        self.frame_Reset_3.setMinimumSize(QSize(0, 450))
        self.frame_Reset_3.setMaximumSize(QSize(16777215, 450))
        self.frame_Reset_3.setStyleSheet(u"QFrame {\n"
"	background-color: white;\n"
"	border-radius: 30px;\n"
"}\n"
"\n"
"QPushButton {\n"
"	height: 60px;\n"
"	background-color: black;\n"
"	color: white;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"	background-color: rgb(30,30,30);\n"
"}")
        self.frame_Reset_3.setFrameShape(QFrame.StyledPanel)
        self.frame_Reset_3.setFrameShadow(QFrame.Raised)
        self.gridLayout_4 = QGridLayout(self.frame_Reset_3)
        self.gridLayout_4.setSpacing(0)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.gridLayout_4.setContentsMargins(0, 0, 0, 0)
        self.verticalSpacer_10 = QSpacerItem(20, 20, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Minimum)

        self.gridLayout_4.addItem(self.verticalSpacer_10, 0, 1, 1, 1)

        self.horizontalSpacer_6 = QSpacerItem(20, 20, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Minimum)

        self.gridLayout_4.addItem(self.horizontalSpacer_6, 1, 0, 1, 1)

        self.frame_Reset_4 = QFrame(self.frame_Reset_3)
        self.frame_Reset_4.setObjectName(u"frame_Reset_4")
        self.frame_Reset_4.setMinimumSize(QSize(287, 410))
        self.frame_Reset_4.setStyleSheet(u"QFrame#frame_EmailToReset {\n"
"	height: 60px;\n"
"	color: black;\n"
"	border-radius: 20px;\n"
"	background-color:  rgb(235, 237, 239);\n"
"	padding-left: 10px;\n"
"}\n"
"\n"
"\n"
"QLineEdit#line_EmailToReset {\n"
"	border: 0;\n"
"	padding-left: 0;\n"
"	background-color: rgb(235, 237, 239);\n"
"	border-top-right-radius: 0;\n"
"	border-bottom-right-radius: 0;\n"
"}\n"
"\n"
"QPushButton#button_CodeSend {\n"
"	height: 60px;\n"
"	border: 20px;\n"
"	background-color: rgb(235, 237, 239);\n"
"	border-top-left-radius: 0;\n"
"	border-bottom-left-radius: 0;\n"
"}")
        self.frame_Reset_4.setFrameShape(QFrame.StyledPanel)
        self.frame_Reset_4.setFrameShadow(QFrame.Raised)
        self.verticalLayout_10 = QVBoxLayout(self.frame_Reset_4)
        self.verticalLayout_10.setSpacing(10)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.verticalLayout_10.setContentsMargins(0, 0, 0, 0)
        self.label_Forgot = QLabel(self.frame_Reset_4)
        self.label_Forgot.setObjectName(u"label_Forgot")
        self.label_Forgot.setFont(font)
        self.label_Forgot.setIndent(0)

        self.verticalLayout_10.addWidget(self.label_Forgot)

        self.textBrowser_ResetAbout = QTextBrowser(self.frame_Reset_4)
        self.textBrowser_ResetAbout.setObjectName(u"textBrowser_ResetAbout")
        self.textBrowser_ResetAbout.setMaximumSize(QSize(16777215, 100))

        self.verticalLayout_10.addWidget(self.textBrowser_ResetAbout)

        self.verticalSpacer_12 = QSpacerItem(20, 0, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_10.addItem(self.verticalSpacer_12)

        self.frame_EmailToReset = QFrame(self.frame_Reset_4)
        self.frame_EmailToReset.setObjectName(u"frame_EmailToReset")
        self.frame_EmailToReset.setMinimumSize(QSize(0, 50))
        self.frame_EmailToReset.setMaximumSize(QSize(16777215, 50))
        self.frame_EmailToReset.setStyleSheet(u"")
        self.frame_EmailToReset.setFrameShape(QFrame.StyledPanel)
        self.frame_EmailToReset.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_10 = QHBoxLayout(self.frame_EmailToReset)
        self.horizontalLayout_10.setSpacing(0)
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.horizontalLayout_10.setContentsMargins(0, 0, 0, 0)
        self.line_EmailToReset = QLineEdit(self.frame_EmailToReset)
        self.line_EmailToReset.setObjectName(u"line_EmailToReset")
        self.line_EmailToReset.setFont(font1)
        self.line_EmailToReset.setEchoMode(QLineEdit.Normal)

        self.horizontalLayout_10.addWidget(self.line_EmailToReset)

        self.button_CodeSend = QPushButton(self.frame_EmailToReset)
        self.button_CodeSend.setObjectName(u"button_CodeSend")
        self.button_CodeSend.setCheckable(True)

        self.horizontalLayout_10.addWidget(self.button_CodeSend)


        self.verticalLayout_10.addWidget(self.frame_EmailToReset)

        self.line_Code = QLineEdit(self.frame_Reset_4)
        self.line_Code.setObjectName(u"line_Code")
        self.line_Code.setFont(font1)
        self.line_Code.setMaxLength(6)

        self.verticalLayout_10.addWidget(self.line_Code)

        self.frame_SignsResend = QFrame(self.frame_Reset_4)
        self.frame_SignsResend.setObjectName(u"frame_SignsResend")
        self.frame_SignsResend.setMinimumSize(QSize(0, 0))
        self.frame_SignsResend.setFrameShape(QFrame.StyledPanel)
        self.frame_SignsResend.setFrameShadow(QFrame.Raised)
        self.verticalLayout_6 = QVBoxLayout(self.frame_SignsResend)
        self.verticalLayout_6.setSpacing(5)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.label_ResetError = QLabel(self.frame_SignsResend)
        self.label_ResetError.setObjectName(u"label_ResetError")
        self.label_ResetError.setMinimumSize(QSize(287, 20))
        self.label_ResetError.setMaximumSize(QSize(287, 20))

        self.verticalLayout_6.addWidget(self.label_ResetError)

        self.textBrowser_ResendTimer = QTextBrowser(self.frame_SignsResend)
        self.textBrowser_ResendTimer.setObjectName(u"textBrowser_ResendTimer")
        self.textBrowser_ResendTimer.setMinimumSize(QSize(0, 20))
        self.textBrowser_ResendTimer.setMaximumSize(QSize(16777215, 20))

        self.verticalLayout_6.addWidget(self.textBrowser_ResendTimer)

        self.textBrowser_BackFromReset = QTextBrowser(self.frame_SignsResend)
        self.textBrowser_BackFromReset.setObjectName(u"textBrowser_BackFromReset")
        self.textBrowser_BackFromReset.setMinimumSize(QSize(0, 20))
        self.textBrowser_BackFromReset.setMaximumSize(QSize(16777215, 20))

        self.verticalLayout_6.addWidget(self.textBrowser_BackFromReset)


        self.verticalLayout_10.addWidget(self.frame_SignsResend)

        self.button_VerifyCode = QPushButton(self.frame_Reset_4)
        self.button_VerifyCode.setObjectName(u"button_VerifyCode")
        self.button_VerifyCode.setFont(font2)

        self.verticalLayout_10.addWidget(self.button_VerifyCode)


        self.gridLayout_4.addWidget(self.frame_Reset_4, 1, 1, 1, 1)

        self.horizontalSpacer_7 = QSpacerItem(20, 20, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Minimum)

        self.gridLayout_4.addItem(self.horizontalSpacer_7, 1, 2, 1, 1)

        self.verticalSpacer_13 = QSpacerItem(20, 20, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Minimum)

        self.gridLayout_4.addItem(self.verticalSpacer_13, 2, 1, 1, 1)


        self.verticalLayout_5.addWidget(self.frame_Reset_3)

        self.verticalSpacer_14 = QSpacerItem(20, 37, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_5.addItem(self.verticalSpacer_14)


        self.horizontalLayout_4.addWidget(self.frame_Reset_2)

        self.horizontalSpacer_8 = QSpacerItem(320, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer_8)


        self.gridLayout_5.addWidget(self.frame_Reset, 0, 0, 1, 1)

        self.stacked_Main.addWidget(self.page_Reset)
        self.page_New = QWidget()
        self.page_New.setObjectName(u"page_New")
        self.gridLayout_7 = QGridLayout(self.page_New)
        self.gridLayout_7.setSpacing(0)
        self.gridLayout_7.setObjectName(u"gridLayout_7")
        self.gridLayout_7.setContentsMargins(0, 0, 0, 0)
        self.frame_New = QFrame(self.page_New)
        self.frame_New.setObjectName(u"frame_New")
        self.frame_New.setStyleSheet(u"")
        self.frame_New.setFrameShape(QFrame.StyledPanel)
        self.frame_New.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_5 = QHBoxLayout(self.frame_New)
        self.horizontalLayout_5.setSpacing(10)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.frame_New_1 = QFrame(self.frame_New)
        self.frame_New_1.setObjectName(u"frame_New_1")
        self.frame_New_1.setMinimumSize(QSize(325, 0))
        self.frame_New_1.setFrameShape(QFrame.StyledPanel)
        self.frame_New_1.setFrameShadow(QFrame.Raised)
        self.verticalLayout_7 = QVBoxLayout(self.frame_New_1)
        self.verticalLayout_7.setSpacing(10)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.verticalSpacer_11 = QSpacerItem(20, 477, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_7.addItem(self.verticalSpacer_11)


        self.horizontalLayout_5.addWidget(self.frame_New_1)

        self.frame_New_2 = QFrame(self.frame_New)
        self.frame_New_2.setObjectName(u"frame_New_2")
        self.frame_New_2.setMinimumSize(QSize(327, 0))
        self.frame_New_2.setStyleSheet(u"")
        self.frame_New_2.setFrameShape(QFrame.StyledPanel)
        self.frame_New_2.setFrameShadow(QFrame.Raised)
        self.verticalLayout_8 = QVBoxLayout(self.frame_New_2)
        self.verticalLayout_8.setSpacing(10)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.verticalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.verticalSpacer_15 = QSpacerItem(20, 37, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_8.addItem(self.verticalSpacer_15)

        self.frame_New_3 = QFrame(self.frame_New_2)
        self.frame_New_3.setObjectName(u"frame_New_3")
        self.frame_New_3.setMinimumSize(QSize(0, 450))
        self.frame_New_3.setMaximumSize(QSize(16777215, 450))
        self.frame_New_3.setStyleSheet(u"QFrame {\n"
"	background-color: white;\n"
"	border-radius: 30px;\n"
"}\n"
"\n"
"QPushButton {\n"
"	height: 60px;\n"
"	background-color: black;\n"
"	color: white;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"	background-color: rgb(30,30,30);\n"
"}\n"
"\n"
"")
        self.frame_New_3.setFrameShape(QFrame.StyledPanel)
        self.frame_New_3.setFrameShadow(QFrame.Raised)
        self.gridLayout_6 = QGridLayout(self.frame_New_3)
        self.gridLayout_6.setSpacing(0)
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.gridLayout_6.setContentsMargins(0, 0, 0, 0)
        self.horizontalSpacer_9 = QSpacerItem(20, 20, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Minimum)

        self.gridLayout_6.addItem(self.horizontalSpacer_9, 1, 0, 1, 1)

        self.verticalSpacer_16 = QSpacerItem(20, 20, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Minimum)

        self.gridLayout_6.addItem(self.verticalSpacer_16, 0, 1, 1, 1)

        self.horizontalSpacer_10 = QSpacerItem(20, 20, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Minimum)

        self.gridLayout_6.addItem(self.horizontalSpacer_10, 1, 2, 1, 1)

        self.verticalSpacer_18 = QSpacerItem(20, 20, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Minimum)

        self.gridLayout_6.addItem(self.verticalSpacer_18, 2, 1, 1, 1)

        self.frame_New_4 = QFrame(self.frame_New_3)
        self.frame_New_4.setObjectName(u"frame_New_4")
        self.frame_New_4.setMinimumSize(QSize(287, 410))
        self.frame_New_4.setStyleSheet(u"QFrame#frame_PwdFirst {\n"
"	height: 60px;\n"
"	color: black;\n"
"	border-radius: 20px;\n"
"	background-color:  rgb(235, 237, 239);\n"
"	padding-left: 10px;\n"
"}\n"
"\n"
"\n"
"QLineEdit#line_PwdFirst {\n"
"	border: 0;\n"
"	padding-left: 0;\n"
"	background-color: rgb(235, 237, 239);\n"
"	border-top-right-radius: 0;\n"
"	border-bottom-right-radius: 0;\n"
"}\n"
"\n"
"QPushButton#button_PwdVis {\n"
"	height: 60px;\n"
"	border: 20px;\n"
"	background-color: rgb(235, 237, 239);\n"
"	border-top-left-radius: 0;\n"
"	border-bottom-left-radius: 0;\n"
"}")
        self.frame_New_4.setFrameShape(QFrame.StyledPanel)
        self.frame_New_4.setFrameShadow(QFrame.Raised)
        self.verticalLayout_11 = QVBoxLayout(self.frame_New_4)
        self.verticalLayout_11.setSpacing(10)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.verticalLayout_11.setContentsMargins(0, 0, 0, 0)
        self.label_Forgot_2 = QLabel(self.frame_New_4)
        self.label_Forgot_2.setObjectName(u"label_Forgot_2")
        self.label_Forgot_2.setFont(font)
        self.label_Forgot_2.setIndent(0)

        self.verticalLayout_11.addWidget(self.label_Forgot_2)

        self.textBrowser_NewAbout = QTextBrowser(self.frame_New_4)
        self.textBrowser_NewAbout.setObjectName(u"textBrowser_NewAbout")
        self.textBrowser_NewAbout.setMaximumSize(QSize(16777215, 100))

        self.verticalLayout_11.addWidget(self.textBrowser_NewAbout)

        self.verticalSpacer_17 = QSpacerItem(20, 0, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_11.addItem(self.verticalSpacer_17)

        self.frame_PwdFirst = QFrame(self.frame_New_4)
        self.frame_PwdFirst.setObjectName(u"frame_PwdFirst")
        self.frame_PwdFirst.setMinimumSize(QSize(0, 50))
        self.frame_PwdFirst.setMaximumSize(QSize(16777215, 50))
        self.frame_PwdFirst.setStyleSheet(u"")
        self.frame_PwdFirst.setFrameShape(QFrame.StyledPanel)
        self.frame_PwdFirst.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_8 = QHBoxLayout(self.frame_PwdFirst)
        self.horizontalLayout_8.setSpacing(0)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.horizontalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.line_PwdFirst = QLineEdit(self.frame_PwdFirst)
        self.line_PwdFirst.setObjectName(u"line_PwdFirst")
        self.line_PwdFirst.setFont(font1)
        self.line_PwdFirst.setMaxLength(16)
        self.line_PwdFirst.setEchoMode(QLineEdit.Password)

        self.horizontalLayout_8.addWidget(self.line_PwdFirst)

        self.button_PwdVis = QPushButton(self.frame_PwdFirst)
        self.button_PwdVis.setObjectName(u"button_PwdVis")
        self.button_PwdVis.setCheckable(True)

        self.horizontalLayout_8.addWidget(self.button_PwdVis)


        self.verticalLayout_11.addWidget(self.frame_PwdFirst)

        self.line_PwdSecond = QLineEdit(self.frame_New_4)
        self.line_PwdSecond.setObjectName(u"line_PwdSecond")
        self.line_PwdSecond.setFont(font1)
        self.line_PwdSecond.setStyleSheet(u"")
        self.line_PwdSecond.setMaxLength(16)
        self.line_PwdSecond.setEchoMode(QLineEdit.Password)

        self.verticalLayout_11.addWidget(self.line_PwdSecond)

        self.frame_SignsNew = QFrame(self.frame_New_4)
        self.frame_SignsNew.setObjectName(u"frame_SignsNew")
        self.frame_SignsNew.setFrameShape(QFrame.StyledPanel)
        self.frame_SignsNew.setFrameShadow(QFrame.Raised)
        self.verticalLayout_9 = QVBoxLayout(self.frame_SignsNew)
        self.verticalLayout_9.setSpacing(5)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.verticalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.label_NewError = QLabel(self.frame_SignsNew)
        self.label_NewError.setObjectName(u"label_NewError")
        self.label_NewError.setMinimumSize(QSize(287, 20))
        self.label_NewError.setMaximumSize(QSize(287, 20))

        self.verticalLayout_9.addWidget(self.label_NewError)

        self.textBrowser_BackFromNew = QTextBrowser(self.frame_SignsNew)
        self.textBrowser_BackFromNew.setObjectName(u"textBrowser_BackFromNew")
        self.textBrowser_BackFromNew.setMinimumSize(QSize(0, 20))
        self.textBrowser_BackFromNew.setMaximumSize(QSize(16777215, 20))

        self.verticalLayout_9.addWidget(self.textBrowser_BackFromNew)


        self.verticalLayout_11.addWidget(self.frame_SignsNew)

        self.button_Submit = QPushButton(self.frame_New_4)
        self.button_Submit.setObjectName(u"button_Submit")
        self.button_Submit.setFont(font2)

        self.verticalLayout_11.addWidget(self.button_Submit)


        self.gridLayout_6.addWidget(self.frame_New_4, 1, 1, 1, 1)


        self.verticalLayout_8.addWidget(self.frame_New_3)

        self.verticalSpacer_19 = QSpacerItem(20, 37, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_8.addItem(self.verticalSpacer_19)


        self.horizontalLayout_5.addWidget(self.frame_New_2)

        self.horizontalSpacer_11 = QSpacerItem(320, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_5.addItem(self.horizontalSpacer_11)


        self.gridLayout_7.addWidget(self.frame_New, 0, 0, 1, 1)

        self.stacked_Main.addWidget(self.page_New)

        self.gridLayout_2.addWidget(self.stacked_Main, 0, 0, 1, 1)


        self.retranslateUi(form_LogIn)

        self.stacked_Main.setCurrentIndex(1)


        QMetaObject.connectSlotsByName(form_LogIn)
    # setupUi

    def retranslateUi(self, form_LogIn):
        form_LogIn.setWindowTitle(QCoreApplication.translate("form_LogIn", u"R&R", None))
        self.button_ControlBack.setText("")
        self.label_SignIn.setText(QCoreApplication.translate("form_LogIn", u"Log In", None))
        self.textBrowser_Rules.setHtml(QCoreApplication.translate("form_LogIn", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'.AppleSystemUIFont'; font-size:13pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>", None))
        self.line_Email.setText("")
        self.line_Email.setPlaceholderText(QCoreApplication.translate("form_LogIn", u"Email", None))
        self.line_Password.setPlaceholderText(QCoreApplication.translate("form_LogIn", u"Password", None))
        self.button_PasswordVisibility.setText("")
        self.label_LogInError.setText(QCoreApplication.translate("form_LogIn", u"Invalidsuka\u043e\u0430\u043b\u0432\u044b\u043e\u0430\u043b\u043e\u0432\u044b\u043b\u0434\u0430\u043e\u043b\u0432\u044b\u0430\u043b\u043e\u043b\u0432\u044b\u043e\u0430\u0430f", None))
        self.button_LogIn.setText(QCoreApplication.translate("form_LogIn", u"Log In", None))
        self.label_Forgot.setText(QCoreApplication.translate("form_LogIn", u"Forgot Password", None))
        self.line_EmailToReset.setPlaceholderText(QCoreApplication.translate("form_LogIn", u"Email", None))
        self.button_CodeSend.setText("")
        self.line_Code.setText("")
        self.line_Code.setPlaceholderText(QCoreApplication.translate("form_LogIn", u"Verification Code", None))
        self.label_ResetError.setText(QCoreApplication.translate("form_LogIn", u"Invalid suka", None))
        self.textBrowser_ResendTimer.setHtml(QCoreApplication.translate("form_LogIn", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'.AppleSystemUIFont'; font-size:13pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>", None))
        self.textBrowser_BackFromReset.setHtml(QCoreApplication.translate("form_LogIn", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'.AppleSystemUIFont'; font-size:13pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>", None))
        self.button_VerifyCode.setText(QCoreApplication.translate("form_LogIn", u"Verify Code", None))
        self.label_Forgot_2.setText(QCoreApplication.translate("form_LogIn", u"Forgot Password", None))
        self.textBrowser_NewAbout.setHtml(QCoreApplication.translate("form_LogIn", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'.AppleSystemUIFont'; font-size:13pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>", None))
        self.line_PwdFirst.setPlaceholderText(QCoreApplication.translate("form_LogIn", u"Password", None))
        self.button_PwdVis.setText("")
        self.line_PwdSecond.setText("")
        self.line_PwdSecond.setPlaceholderText(QCoreApplication.translate("form_LogIn", u"Confirm Password", None))
        self.label_NewError.setText(QCoreApplication.translate("form_LogIn", u"Invalid suka", None))
        self.button_Submit.setText(QCoreApplication.translate("form_LogIn", u"Submit", None))
    # retranslateUi

