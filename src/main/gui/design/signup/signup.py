# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'signup.ui'
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
    QSpacerItem, QStackedWidget, QTextBrowser, QTextEdit,
    QVBoxLayout, QWidget)

class Ui_form_SignUp(object):
    def setupUi(self, form_SignUp):
        if not form_SignUp.objectName():
            form_SignUp.setObjectName(u"form_SignUp")
        form_SignUp.resize(1000, 550)
        form_SignUp.setMinimumSize(QSize(1000, 550))
        form_SignUp.setMaximumSize(QSize(1000, 550))
        form_SignUp.setStyleSheet(u"QFrame, QWidget {\n"
"	border: 0;		\n"
"	background-color: transparent;\n"
"}\n"
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
"/*-------------*/\n"
"\n"
"QPushButton#button_PasswordVisibility {\n"
"	padding-right: 10px;\n"
"}\n"
"\n"
"QLabel#label_FormatError,\n"
"QLabel#label_SubmitError {\n"
"	color: red;\n"
"}")
        self.gridLayout_2 = QGridLayout(form_SignUp)
        self.gridLayout_2.setSpacing(0)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.stacked_Main = QStackedWidget(form_SignUp)
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
"	background-color: rgb(235, 237, 239);\n"
"}\n"
"\n"
"QTextBrowser QScrollBar::sub-line:horizontal {\n"
"	width: 0px;\n"
"	height: 0px;\n"
"	border: none;\n"
"	background-color: rgb(235, 237, 239);\n"
"}")
        self.page_Main = QWidget()
        self.page_Main.setObjectName(u"page_Main")
        self.gridLayout_3 = QGridLayout(self.page_Main)
        self.gridLayout_3.setSpacing(0)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.gridLayout_3.setContentsMargins(0, 0, 0, 0)
        self.frame_Main = QFrame(self.page_Main)
        self.frame_Main.setObjectName(u"frame_Main")
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

        self.frame_SignUpMain_1 = QFrame(self.frame_Main)
        self.frame_SignUpMain_1.setObjectName(u"frame_SignUpMain_1")
        self.frame_SignUpMain_1.setMinimumSize(QSize(327, 0))
        self.frame_SignUpMain_1.setStyleSheet(u"")
        self.frame_SignUpMain_1.setFrameShape(QFrame.StyledPanel)
        self.frame_SignUpMain_1.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(self.frame_SignUpMain_1)
        self.verticalLayout.setSpacing(10)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalSpacer = QSpacerItem(20, 37, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)

        self.frame_SignUp_2 = QFrame(self.frame_SignUpMain_1)
        self.frame_SignUp_2.setObjectName(u"frame_SignUp_2")
        self.frame_SignUp_2.setMinimumSize(QSize(0, 450))
        self.frame_SignUp_2.setMaximumSize(QSize(16777215, 450))
        self.frame_SignUp_2.setStyleSheet(u"QFrame {\n"
"	background-color: white;\n"
"	border-radius: 30px;\n"
"}\n"
"\n"
"QLabel#label_FormatError {\n"
"	color: red;\n"
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
"QPushButton#button_PasswordVisibility {\n"
"	padding-right: 10px:\n"
"}")
        self.frame_SignUp_2.setFrameShape(QFrame.StyledPanel)
        self.frame_SignUp_2.setFrameShadow(QFrame.Raised)
        self.gridLayout = QGridLayout(self.frame_SignUp_2)
        self.gridLayout.setSpacing(0)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalSpacer_4 = QSpacerItem(20, 20, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Minimum)

        self.gridLayout.addItem(self.verticalSpacer_4, 0, 1, 1, 1)

        self.horizontalSpacer_2 = QSpacerItem(20, 20, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer_2, 1, 0, 1, 1)

        self.frame_SignUp_3 = QFrame(self.frame_SignUp_2)
        self.frame_SignUp_3.setObjectName(u"frame_SignUp_3")
        self.frame_SignUp_3.setMinimumSize(QSize(287, 410))
        self.frame_SignUp_3.setStyleSheet(u"")
        self.frame_SignUp_3.setFrameShape(QFrame.StyledPanel)
        self.frame_SignUp_3.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.frame_SignUp_3)
        self.verticalLayout_3.setSpacing(10)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.label_SignIn = QLabel(self.frame_SignUp_3)
        self.label_SignIn.setObjectName(u"label_SignIn")
        font = QFont()
        font.setPointSize(25)
        font.setBold(True)
        self.label_SignIn.setFont(font)
        self.label_SignIn.setIndent(0)

        self.verticalLayout_3.addWidget(self.label_SignIn)

        self.textBrowser_Rules = QTextBrowser(self.frame_SignUp_3)
        self.textBrowser_Rules.setObjectName(u"textBrowser_Rules")
        self.textBrowser_Rules.setMaximumSize(QSize(16777215, 100))

        self.verticalLayout_3.addWidget(self.textBrowser_Rules)

        self.line_Name = QLineEdit(self.frame_SignUp_3)
        self.line_Name.setObjectName(u"line_Name")
        self.line_Name.setMinimumSize(QSize(0, 40))
        self.line_Name.setMaximumSize(QSize(16777215, 40))
        font1 = QFont()
        font1.setPointSize(15)
        self.line_Name.setFont(font1)
        self.line_Name.setMaxLength(15)

        self.verticalLayout_3.addWidget(self.line_Name)

        self.frame_Username = QFrame(self.frame_SignUp_3)
        self.frame_Username.setObjectName(u"frame_Username")
        self.frame_Username.setMinimumSize(QSize(0, 40))
        self.frame_Username.setMaximumSize(QSize(16777215, 40))
        self.frame_Username.setStyleSheet(u"QFrame {\n"
"	height: 60px;\n"
"	color: black;\n"
"	border-radius: 20px;\n"
"	background-color:  rgb(235, 237, 239);\n"
"	padding-left: 10px;\n"
"}\n"
"\n"
"QLineEdit {\n"
"	border: 0;\n"
"	padding-left: 0;\n"
"	background-color: rgb(235, 237, 239);\n"
"}\n"
"\n"
"QLineEdit#line_Snail {\n"
"	border-top-left-radius: 20px;\n"
"	border-bottom-left-radius: 20px;\n"
"	border-top-right-radius: 0;\n"
"	border-bottom-right-radius: 0;\n"
"}")
        self.frame_Username.setFrameShape(QFrame.StyledPanel)
        self.frame_Username.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.frame_Username)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.line_Snail = QLineEdit(self.frame_Username)
        self.line_Snail.setObjectName(u"line_Snail")
        self.line_Snail.setMinimumSize(QSize(20, 40))
        self.line_Snail.setMaximumSize(QSize(20, 40))
        font2 = QFont()
        font2.setPointSize(16)
        self.line_Snail.setFont(font2)
        self.line_Snail.setReadOnly(True)

        self.horizontalLayout_4.addWidget(self.line_Snail)

        self.line_Username = QLineEdit(self.frame_Username)
        self.line_Username.setObjectName(u"line_Username")
        self.line_Username.setFont(font1)
        self.line_Username.setMaxLength(32)
        self.line_Username.setEchoMode(QLineEdit.Normal)

        self.horizontalLayout_4.addWidget(self.line_Username)


        self.verticalLayout_3.addWidget(self.frame_Username)

        self.line_Email = QLineEdit(self.frame_SignUp_3)
        self.line_Email.setObjectName(u"line_Email")
        self.line_Email.setMinimumSize(QSize(0, 40))
        self.line_Email.setMaximumSize(QSize(16777215, 40))
        self.line_Email.setFont(font1)
        self.line_Email.setReadOnly(False)

        self.verticalLayout_3.addWidget(self.line_Email)

        self.frame_PasswordInput = QFrame(self.frame_SignUp_3)
        self.frame_PasswordInput.setObjectName(u"frame_PasswordInput")
        self.frame_PasswordInput.setMinimumSize(QSize(0, 40))
        self.frame_PasswordInput.setMaximumSize(QSize(16777215, 40))
        self.frame_PasswordInput.setStyleSheet(u"QFrame {\n"
"	height: 60px;\n"
"	color: black;\n"
"	border-radius: 20px;\n"
"	background-color:  rgb(235, 237, 239);\n"
"	padding-left: 10px;\n"
"}\n"
"\n"
"\n"
"QLineEdit {\n"
"	border: 0;\n"
"	padding-left: 0;\n"
"	background-color: rgb(235, 237, 239);\n"
"	border-top-right-radius: 0;\n"
"	border-bottom-right-radius: 0;\n"
"}\n"
"\n"
"QPushButton {\n"
"	height: 60px;\n"
"	border: 20px;\n"
"	background-color: rgb(235, 237, 239);\n"
"	border-top-left-radius: 0;\n"
"	border-bottom-left-radius: 0;\n"
"}")
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


        self.verticalLayout_3.addWidget(self.frame_PasswordInput)

        self.label_SignUpError = QLabel(self.frame_SignUp_3)
        self.label_SignUpError.setObjectName(u"label_SignUpError")
        self.label_SignUpError.setMinimumSize(QSize(287, 20))
        self.label_SignUpError.setMaximumSize(QSize(287, 20))

        self.verticalLayout_3.addWidget(self.label_SignUpError)

        self.textBrowser_toLogIn = QTextBrowser(self.frame_SignUp_3)
        self.textBrowser_toLogIn.setObjectName(u"textBrowser_toLogIn")
        self.textBrowser_toLogIn.setMinimumSize(QSize(0, 20))
        self.textBrowser_toLogIn.setMaximumSize(QSize(16777215, 20))
        self.textBrowser_toLogIn.setLineWrapMode(QTextEdit.WidgetWidth)

        self.verticalLayout_3.addWidget(self.textBrowser_toLogIn)

        self.button_CheckEmail = QPushButton(self.frame_SignUp_3)
        self.button_CheckEmail.setObjectName(u"button_CheckEmail")
        self.button_CheckEmail.setMinimumSize(QSize(0, 50))
        self.button_CheckEmail.setMaximumSize(QSize(16777215, 50))
        font3 = QFont()
        font3.setBold(True)
        self.button_CheckEmail.setFont(font3)

        self.verticalLayout_3.addWidget(self.button_CheckEmail)


        self.gridLayout.addWidget(self.frame_SignUp_3, 1, 1, 1, 1)

        self.horizontalSpacer_4 = QSpacerItem(20, 20, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer_4, 1, 2, 1, 1)

        self.verticalSpacer_5 = QSpacerItem(20, 20, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Minimum)

        self.gridLayout.addItem(self.verticalSpacer_5, 2, 1, 1, 1)


        self.verticalLayout.addWidget(self.frame_SignUp_2)

        self.verticalSpacer_2 = QSpacerItem(20, 37, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer_2)


        self.horizontalLayout.addWidget(self.frame_SignUpMain_1)

        self.horizontalSpacer = QSpacerItem(320, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)


        self.gridLayout_3.addWidget(self.frame_Main, 0, 0, 1, 1)

        self.stacked_Main.addWidget(self.page_Main)
        self.page_Submit = QWidget()
        self.page_Submit.setObjectName(u"page_Submit")
        self.page_Submit.setStyleSheet(u"")
        self.gridLayout_5 = QGridLayout(self.page_Submit)
        self.gridLayout_5.setSpacing(0)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.gridLayout_5.setContentsMargins(0, 0, 0, 0)
        self.frame_Submit = QFrame(self.page_Submit)
        self.frame_Submit.setObjectName(u"frame_Submit")
        self.frame_Submit.setStyleSheet(u"")
        self.frame_Submit.setFrameShape(QFrame.StyledPanel)
        self.frame_Submit.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_5 = QHBoxLayout(self.frame_Submit)
        self.horizontalLayout_5.setSpacing(10)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.frame_ControlSubmitContainer = QFrame(self.frame_Submit)
        self.frame_ControlSubmitContainer.setObjectName(u"frame_ControlSubmitContainer")
        self.frame_ControlSubmitContainer.setMinimumSize(QSize(325, 0))
        self.frame_ControlSubmitContainer.setFrameShape(QFrame.StyledPanel)
        self.frame_ControlSubmitContainer.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.frame_ControlSubmitContainer)
        self.verticalLayout_4.setSpacing(10)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.verticalSpacer_6 = QSpacerItem(20, 477, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_4.addItem(self.verticalSpacer_6)


        self.horizontalLayout_5.addWidget(self.frame_ControlSubmitContainer)

        self.frame_Submit_1 = QFrame(self.frame_Submit)
        self.frame_Submit_1.setObjectName(u"frame_Submit_1")
        self.frame_Submit_1.setMinimumSize(QSize(327, 0))
        self.frame_Submit_1.setStyleSheet(u"")
        self.frame_Submit_1.setFrameShape(QFrame.StyledPanel)
        self.frame_Submit_1.setFrameShadow(QFrame.Raised)
        self.verticalLayout_5 = QVBoxLayout(self.frame_Submit_1)
        self.verticalLayout_5.setSpacing(10)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.verticalSpacer_7 = QSpacerItem(20, 37, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_5.addItem(self.verticalSpacer_7)

        self.frame_Submit_2 = QFrame(self.frame_Submit_1)
        self.frame_Submit_2.setObjectName(u"frame_Submit_2")
        self.frame_Submit_2.setMinimumSize(QSize(0, 450))
        self.frame_Submit_2.setMaximumSize(QSize(16777215, 450))
        self.frame_Submit_2.setStyleSheet(u"QFrame {\n"
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
        self.frame_Submit_2.setFrameShape(QFrame.StyledPanel)
        self.frame_Submit_2.setFrameShadow(QFrame.Raised)
        self.gridLayout_4 = QGridLayout(self.frame_Submit_2)
        self.gridLayout_4.setSpacing(0)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.gridLayout_4.setContentsMargins(0, 0, 0, 0)
        self.verticalSpacer_8 = QSpacerItem(20, 20, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Minimum)

        self.gridLayout_4.addItem(self.verticalSpacer_8, 0, 1, 1, 1)

        self.horizontalSpacer_6 = QSpacerItem(20, 20, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Minimum)

        self.gridLayout_4.addItem(self.horizontalSpacer_6, 1, 0, 1, 1)

        self.frame_Submit_3 = QFrame(self.frame_Submit_2)
        self.frame_Submit_3.setObjectName(u"frame_Submit_3")
        self.frame_Submit_3.setMinimumSize(QSize(287, 410))
        self.frame_Submit_3.setStyleSheet(u"")
        self.frame_Submit_3.setFrameShape(QFrame.StyledPanel)
        self.frame_Submit_3.setFrameShadow(QFrame.Raised)
        self.verticalLayout_6 = QVBoxLayout(self.frame_Submit_3)
        self.verticalLayout_6.setSpacing(10)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.label_SubmitEmail = QLabel(self.frame_Submit_3)
        self.label_SubmitEmail.setObjectName(u"label_SubmitEmail")
        self.label_SubmitEmail.setFont(font)
        self.label_SubmitEmail.setIndent(0)

        self.verticalLayout_6.addWidget(self.label_SubmitEmail)

        self.textBrowser_SubmitAbout = QTextBrowser(self.frame_Submit_3)
        self.textBrowser_SubmitAbout.setObjectName(u"textBrowser_SubmitAbout")
        self.textBrowser_SubmitAbout.setMaximumSize(QSize(16777215, 100))
        self.textBrowser_SubmitAbout.setOpenLinks(False)

        self.verticalLayout_6.addWidget(self.textBrowser_SubmitAbout)

        self.verticalSpacer_11 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_6.addItem(self.verticalSpacer_11)

        self.line_SubmitCode = QLineEdit(self.frame_Submit_3)
        self.line_SubmitCode.setObjectName(u"line_SubmitCode")
        self.line_SubmitCode.setMinimumSize(QSize(0, 50))
        self.line_SubmitCode.setMaximumSize(QSize(16777215, 50))
        self.line_SubmitCode.setFont(font1)
        self.line_SubmitCode.setMaxLength(6)
        self.line_SubmitCode.setReadOnly(False)

        self.verticalLayout_6.addWidget(self.line_SubmitCode)

        self.label_SubmitError = QLabel(self.frame_Submit_3)
        self.label_SubmitError.setObjectName(u"label_SubmitError")
        self.label_SubmitError.setMinimumSize(QSize(287, 20))
        self.label_SubmitError.setMaximumSize(QSize(287, 20))
        self.label_SubmitError.setStyleSheet(u"")

        self.verticalLayout_6.addWidget(self.label_SubmitError)

        self.textBrowser_SubmitTimer = QTextBrowser(self.frame_Submit_3)
        self.textBrowser_SubmitTimer.setObjectName(u"textBrowser_SubmitTimer")
        self.textBrowser_SubmitTimer.setMinimumSize(QSize(0, 20))
        self.textBrowser_SubmitTimer.setMaximumSize(QSize(16777215, 20))

        self.verticalLayout_6.addWidget(self.textBrowser_SubmitTimer)

        self.textBrowser_SubmitBack = QTextBrowser(self.frame_Submit_3)
        self.textBrowser_SubmitBack.setObjectName(u"textBrowser_SubmitBack")
        self.textBrowser_SubmitBack.setMinimumSize(QSize(0, 20))
        self.textBrowser_SubmitBack.setMaximumSize(QSize(16777215, 20))

        self.verticalLayout_6.addWidget(self.textBrowser_SubmitBack)

        self.button_SignUp = QPushButton(self.frame_Submit_3)
        self.button_SignUp.setObjectName(u"button_SignUp")
        self.button_SignUp.setFont(font3)

        self.verticalLayout_6.addWidget(self.button_SignUp)


        self.gridLayout_4.addWidget(self.frame_Submit_3, 1, 1, 1, 1)

        self.horizontalSpacer_7 = QSpacerItem(20, 20, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Minimum)

        self.gridLayout_4.addItem(self.horizontalSpacer_7, 1, 2, 1, 1)

        self.verticalSpacer_9 = QSpacerItem(20, 20, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Minimum)

        self.gridLayout_4.addItem(self.verticalSpacer_9, 2, 1, 1, 1)


        self.verticalLayout_5.addWidget(self.frame_Submit_2)

        self.verticalSpacer_10 = QSpacerItem(20, 37, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_5.addItem(self.verticalSpacer_10)


        self.horizontalLayout_5.addWidget(self.frame_Submit_1)

        self.horizontalSpacer_8 = QSpacerItem(320, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_5.addItem(self.horizontalSpacer_8)


        self.gridLayout_5.addWidget(self.frame_Submit, 0, 0, 1, 1)

        self.stacked_Main.addWidget(self.page_Submit)

        self.gridLayout_2.addWidget(self.stacked_Main, 0, 0, 1, 1)


        self.retranslateUi(form_SignUp)

        self.stacked_Main.setCurrentIndex(1)


        QMetaObject.connectSlotsByName(form_SignUp)
    # setupUi

    def retranslateUi(self, form_SignUp):
        form_SignUp.setWindowTitle(QCoreApplication.translate("form_SignUp", u"R&R", None))
        self.button_ControlBack.setText("")
        self.label_SignIn.setText(QCoreApplication.translate("form_SignUp", u"Sign Up", None))
        self.line_Name.setPlaceholderText(QCoreApplication.translate("form_SignUp", u"Name", None))
        self.line_Snail.setPlaceholderText(QCoreApplication.translate("form_SignUp", u"@", None))
        self.line_Username.setPlaceholderText(QCoreApplication.translate("form_SignUp", u"Username", None))
        self.line_Email.setText("")
        self.line_Email.setPlaceholderText(QCoreApplication.translate("form_SignUp", u"Email", None))
        self.line_Password.setPlaceholderText(QCoreApplication.translate("form_SignUp", u"Password", None))
        self.button_PasswordVisibility.setText("")
        self.label_SignUpError.setText(QCoreApplication.translate("form_SignUp", u"Invalid suka", None))
        self.button_CheckEmail.setText(QCoreApplication.translate("form_SignUp", u"Check Email", None))
        self.label_SubmitEmail.setText(QCoreApplication.translate("form_SignUp", u"Submit Email", None))
        self.textBrowser_SubmitAbout.setHtml(QCoreApplication.translate("form_SignUp", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'.AppleSystemUIFont'; font-size:13pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>", None))
        self.line_SubmitCode.setText("")
        self.line_SubmitCode.setPlaceholderText(QCoreApplication.translate("form_SignUp", u"Verification Code", None))
        self.label_SubmitError.setText(QCoreApplication.translate("form_SignUp", u"Invalid suka", None))
        self.button_SignUp.setText(QCoreApplication.translate("form_SignUp", u"Sign Up", None))
    # retranslateUi

