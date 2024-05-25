# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'reg.ui'
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
from PySide6.QtWidgets import (QApplication, QFrame, QGridLayout, QHBoxLayout,
    QLabel, QLineEdit, QPushButton, QSizePolicy,
    QSpacerItem, QTextBrowser, QVBoxLayout, QWidget)

class Ui_form_Registration(object):
    def setupUi(self, form_Registration):
        if not form_Registration.objectName():
            form_Registration.setObjectName(u"form_Registration")
        form_Registration.resize(1000, 550)
        form_Registration.setMinimumSize(QSize(1000, 550))
        form_Registration.setMaximumSize(QSize(1000, 550))
        form_Registration.setStyleSheet(u"QFrame, QWidget {\n"
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
"QTextBrowser QScrollBar:vertical {\n"
"	background-color: rgb(235, 237, 239);\n"
"	width: 8px;\n"
"}\n"
"\n"
"QTextBrowser QScrollBar::handle:vertical {\n"
"        background-color: rgb(184,191,195);\n"
"        min-height: 5px;\n"
"        border-radius: 4px;\n"
"}\n"
"\n"
"QTextBrowser QScrollBar::up-arrow:vertical, QScrollBar::down-arrow:vertical {\n"
"        background: none;\n"
"}\n"
"\n"
"QTextBrowserQScrollBar::add-page:vertical, QScrollBar::sub-page"
                        ":vertical {\n"
"        background: none;\n"
"}")
        self.gridLayout_2 = QGridLayout(form_Registration)
        self.gridLayout_2.setSpacing(0)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.frame_Main = QFrame(form_Registration)
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

        self.frame_RegistrationMain = QFrame(self.frame_Main)
        self.frame_RegistrationMain.setObjectName(u"frame_RegistrationMain")
        self.frame_RegistrationMain.setMinimumSize(QSize(327, 0))
        self.frame_RegistrationMain.setStyleSheet(u"")
        self.frame_RegistrationMain.setFrameShape(QFrame.StyledPanel)
        self.frame_RegistrationMain.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(self.frame_RegistrationMain)
        self.verticalLayout.setSpacing(10)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalSpacer = QSpacerItem(20, 37, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)

        self.frame_RegistrationWindow = QFrame(self.frame_RegistrationMain)
        self.frame_RegistrationWindow.setObjectName(u"frame_RegistrationWindow")
        self.frame_RegistrationWindow.setMinimumSize(QSize(0, 450))
        self.frame_RegistrationWindow.setMaximumSize(QSize(16777215, 450))
        self.frame_RegistrationWindow.setStyleSheet(u"QFrame {\n"
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
        self.frame_RegistrationWindow.setFrameShape(QFrame.StyledPanel)
        self.frame_RegistrationWindow.setFrameShadow(QFrame.Raised)
        self.gridLayout = QGridLayout(self.frame_RegistrationWindow)
        self.gridLayout.setSpacing(0)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalSpacer_4 = QSpacerItem(20, 20, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Minimum)

        self.gridLayout.addItem(self.verticalSpacer_4, 0, 1, 1, 1)

        self.horizontalSpacer_2 = QSpacerItem(20, 20, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer_2, 1, 0, 1, 1)

        self.frame_RegistrationWindowSub = QFrame(self.frame_RegistrationWindow)
        self.frame_RegistrationWindowSub.setObjectName(u"frame_RegistrationWindowSub")
        self.frame_RegistrationWindowSub.setMinimumSize(QSize(287, 410))
        self.frame_RegistrationWindowSub.setFrameShape(QFrame.StyledPanel)
        self.frame_RegistrationWindowSub.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.frame_RegistrationWindowSub)
        self.verticalLayout_3.setSpacing(10)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.label_SignIn = QLabel(self.frame_RegistrationWindowSub)
        self.label_SignIn.setObjectName(u"label_SignIn")
        font = QFont()
        font.setPointSize(25)
        font.setBold(True)
        self.label_SignIn.setFont(font)
        self.label_SignIn.setIndent(0)

        self.verticalLayout_3.addWidget(self.label_SignIn)

        self.textBrowser_Rules = QTextBrowser(self.frame_RegistrationWindowSub)
        self.textBrowser_Rules.setObjectName(u"textBrowser_Rules")
        self.textBrowser_Rules.setMaximumSize(QSize(16777215, 100))

        self.verticalLayout_3.addWidget(self.textBrowser_Rules)

        self.line_Login_2 = QLineEdit(self.frame_RegistrationWindowSub)
        self.line_Login_2.setObjectName(u"line_Login_2")
        font1 = QFont()
        font1.setPointSize(15)
        self.line_Login_2.setFont(font1)

        self.verticalLayout_3.addWidget(self.line_Login_2)

        self.line_Login = QLineEdit(self.frame_RegistrationWindowSub)
        self.line_Login.setObjectName(u"line_Login")
        self.line_Login.setFont(font1)

        self.verticalLayout_3.addWidget(self.line_Login)

        self.frame_PasswordInput = QFrame(self.frame_RegistrationWindowSub)
        self.frame_PasswordInput.setObjectName(u"frame_PasswordInput")
        self.frame_PasswordInput.setMinimumSize(QSize(0, 50))
        self.frame_PasswordInput.setMaximumSize(QSize(16777215, 50))
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
        self.line_Password.setEchoMode(QLineEdit.Password)

        self.horizontalLayout_3.addWidget(self.line_Password)

        self.button_PasswordVisibility = QPushButton(self.frame_PasswordInput)
        self.button_PasswordVisibility.setObjectName(u"button_PasswordVisibility")
        self.button_PasswordVisibility.setCheckable(True)

        self.horizontalLayout_3.addWidget(self.button_PasswordVisibility)


        self.verticalLayout_3.addWidget(self.frame_PasswordInput)

        self.label_FormatError = QLabel(self.frame_RegistrationWindowSub)
        self.label_FormatError.setObjectName(u"label_FormatError")
        self.label_FormatError.setMinimumSize(QSize(0, 20))
        self.label_FormatError.setMaximumSize(QSize(16777215, 20))

        self.verticalLayout_3.addWidget(self.label_FormatError)

        self.textBrowser_LogIn = QTextBrowser(self.frame_RegistrationWindowSub)
        self.textBrowser_LogIn.setObjectName(u"textBrowser_LogIn")
        self.textBrowser_LogIn.setMinimumSize(QSize(0, 30))
        self.textBrowser_LogIn.setMaximumSize(QSize(16777215, 20))

        self.verticalLayout_3.addWidget(self.textBrowser_LogIn)

        self.button_SignIn = QPushButton(self.frame_RegistrationWindowSub)
        self.button_SignIn.setObjectName(u"button_SignIn")
        font2 = QFont()
        font2.setBold(True)
        self.button_SignIn.setFont(font2)

        self.verticalLayout_3.addWidget(self.button_SignIn)


        self.gridLayout.addWidget(self.frame_RegistrationWindowSub, 1, 1, 1, 1)

        self.horizontalSpacer_4 = QSpacerItem(20, 20, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer_4, 1, 2, 1, 1)

        self.verticalSpacer_5 = QSpacerItem(20, 20, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Minimum)

        self.gridLayout.addItem(self.verticalSpacer_5, 2, 1, 1, 1)


        self.verticalLayout.addWidget(self.frame_RegistrationWindow)

        self.verticalSpacer_2 = QSpacerItem(20, 37, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer_2)


        self.horizontalLayout.addWidget(self.frame_RegistrationMain)

        self.horizontalSpacer = QSpacerItem(320, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)


        self.gridLayout_2.addWidget(self.frame_Main, 0, 0, 1, 1)


        self.retranslateUi(form_Registration)

        QMetaObject.connectSlotsByName(form_Registration)
    # setupUi

    def retranslateUi(self, form_Registration):
        form_Registration.setWindowTitle(QCoreApplication.translate("form_Registration", u"Form", None))
        self.button_ControlBack.setText("")
        self.label_SignIn.setText(QCoreApplication.translate("form_Registration", u"Sign Up", None))
        self.line_Login_2.setPlaceholderText(QCoreApplication.translate("form_Registration", u"Name", None))
        self.line_Login.setPlaceholderText(QCoreApplication.translate("form_Registration", u"Login", None))
        self.line_Password.setPlaceholderText(QCoreApplication.translate("form_Registration", u"Password", None))
        self.button_PasswordVisibility.setText("")
        self.label_FormatError.setText(QCoreApplication.translate("form_Registration", u"Invalid suka", None))
        self.button_SignIn.setText(QCoreApplication.translate("form_Registration", u"Sign Up", None))
    # retranslateUi

