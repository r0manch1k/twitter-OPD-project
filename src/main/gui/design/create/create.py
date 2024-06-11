# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'create.ui'
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
    QHBoxLayout, QLabel, QLayout, QPlainTextEdit,
    QPushButton, QSizePolicy, QSpacerItem, QVBoxLayout,
    QWidget)

class Ui_frame_PostCreate(object):
    def setupUi(self, frame_PostCreate):
        if not frame_PostCreate.objectName():
            frame_PostCreate.setObjectName(u"frame_PostCreate")
        frame_PostCreate.resize(590, 110)
        frame_PostCreate.setMinimumSize(QSize(0, 50))
        frame_PostCreate.setMaximumSize(QSize(16777215, 120))
        frame_PostCreate.setStyleSheet(u"QFrame#frame_PostCreate {\n"
"	background: transponent;\n"
"	border-radius: 20px;\n"
"}\n"
"\n"
"QFrame {\n"
"	border: 0;\n"
"	background-color: white;\n"
"}\n"
"\n"
"QFrame#frame_HomeCreatePost {\n"
"	background: transponent;\n"
"}\n"
"\n"
"QFrame#frame_PostCreateMain {\n"
"	border-radius: 20px;\n"
"}\n"
"\n"
"QFrame#frame_PostCreateToolsSelected {\n"
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
"QPushButton#button_PostCreateAddImageSelected,\n"
"QPushButton#button_PostCreateAddImageUnselected,\n"
"QPushButton#button_PostCreateAddVideoSelected,\n"
"QPushButton#button_PostCreateAddVideoUnselected,\n"
"QPushButton#button_PostCreateAddMusicSelected,\n"
"QPushButton#button_Po"
                        "stCreateAddMusicUnselected {\n"
"	border-radius: 15px;\n"
"}\n"
"\n"
"QPushButton#button_PostCreate {\n"
"	color: white;\n"
"	background-color: rgb(0, 88, 155);\n"
"	border-radius: 15px;\n"
"}\n"
"\n"
"QPushButton#button_PostCreate:hover {\n"
"	background-color: rgb(0, 78, 145);\n"
"}\n"
"\n"
"QPushButton#button_PostCreate:pressed {\n"
"	background-color: rgb(0, 68, 135);\n"
"}\n"
"")
        frame_PostCreate.setFrameShape(QFrame.StyledPanel)
        frame_PostCreate.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(frame_PostCreate)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(20, 0, 10, 10)
        self.frame_PostCreateMain = QFrame(frame_PostCreate)
        self.frame_PostCreateMain.setObjectName(u"frame_PostCreateMain")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_PostCreateMain.sizePolicy().hasHeightForWidth())
        self.frame_PostCreateMain.setSizePolicy(sizePolicy)
        self.frame_PostCreateMain.setMinimumSize(QSize(0, 50))
        self.frame_PostCreateMain.setMaximumSize(QSize(16777215, 50))
        self.frame_PostCreateMain.setStyleSheet(u"")
        self.frame_PostCreateMain.setFrameShape(QFrame.StyledPanel)
        self.frame_PostCreateMain.setFrameShadow(QFrame.Raised)
        self.layout_PostCreateMain = QHBoxLayout(self.frame_PostCreateMain)
        self.layout_PostCreateMain.setSpacing(10)
        self.layout_PostCreateMain.setObjectName(u"layout_PostCreateMain")
        self.layout_PostCreateMain.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.layout_PostCreateMain.setContentsMargins(10, 10, 10, 10)
        self.frame_PostCreateImage = QFrame(self.frame_PostCreateMain)
        self.frame_PostCreateImage.setObjectName(u"frame_PostCreateImage")
        self.frame_PostCreateImage.setMinimumSize(QSize(0, 30))
        self.frame_PostCreateImage.setFrameShape(QFrame.StyledPanel)
        self.frame_PostCreateImage.setFrameShadow(QFrame.Raised)
        self.verticalLayout_11 = QVBoxLayout(self.frame_PostCreateImage)
        self.verticalLayout_11.setSpacing(0)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.verticalLayout_11.setContentsMargins(0, 0, 0, 0)
        self.label_PostCreateImage = QLabel(self.frame_PostCreateImage)
        self.label_PostCreateImage.setObjectName(u"label_PostCreateImage")
        self.label_PostCreateImage.setMinimumSize(QSize(30, 30))
        self.label_PostCreateImage.setMaximumSize(QSize(30, 30))

        self.verticalLayout_11.addWidget(self.label_PostCreateImage)

        self.verticalSpacer_7 = QSpacerItem(20, 12, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.MinimumExpanding)

        self.verticalLayout_11.addItem(self.verticalSpacer_7)


        self.layout_PostCreateMain.addWidget(self.frame_PostCreateImage)

        self.line_PostCreateText = QPlainTextEdit(self.frame_PostCreateMain)
        self.line_PostCreateText.setObjectName(u"line_PostCreateText")
        self.line_PostCreateText.setMinimumSize(QSize(0, 30))
        self.line_PostCreateText.setMaximumSize(QSize(16777215, 30))
        self.line_PostCreateText.setStyleSheet(u"padding-top: 3px;")
        self.line_PostCreateText.setFrameShadow(QFrame.Sunken)
        self.line_PostCreateText.setLineWidth(0)
        self.line_PostCreateText.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.line_PostCreateText.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.line_PostCreateText.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContents)
        self.line_PostCreateText.setBackgroundVisible(False)

        self.layout_PostCreateMain.addWidget(self.line_PostCreateText)

        self.frame_PostCreateToolsUnselected = QFrame(self.frame_PostCreateMain)
        self.frame_PostCreateToolsUnselected.setObjectName(u"frame_PostCreateToolsUnselected")
        self.frame_PostCreateToolsUnselected.setMinimumSize(QSize(0, 30))
        self.frame_PostCreateToolsUnselected.setFrameShape(QFrame.StyledPanel)
        self.frame_PostCreateToolsUnselected.setFrameShadow(QFrame.Raised)
        self.gridLayout_12 = QGridLayout(self.frame_PostCreateToolsUnselected)
        self.gridLayout_12.setObjectName(u"gridLayout_12")
        self.gridLayout_12.setHorizontalSpacing(5)
        self.gridLayout_12.setVerticalSpacing(0)
        self.gridLayout_12.setContentsMargins(0, 0, 0, 0)
        self.button_PostCreateAddVideoUnselected = QPushButton(self.frame_PostCreateToolsUnselected)
        self.button_PostCreateAddVideoUnselected.setObjectName(u"button_PostCreateAddVideoUnselected")
        self.button_PostCreateAddVideoUnselected.setMinimumSize(QSize(30, 30))
        self.button_PostCreateAddVideoUnselected.setMaximumSize(QSize(30, 30))

        self.gridLayout_12.addWidget(self.button_PostCreateAddVideoUnselected, 1, 2, 1, 1)

        self.button_PostCreateAddMusicUnselected = QPushButton(self.frame_PostCreateToolsUnselected)
        self.button_PostCreateAddMusicUnselected.setObjectName(u"button_PostCreateAddMusicUnselected")
        self.button_PostCreateAddMusicUnselected.setMinimumSize(QSize(30, 30))
        self.button_PostCreateAddMusicUnselected.setMaximumSize(QSize(30, 30))

        self.gridLayout_12.addWidget(self.button_PostCreateAddMusicUnselected, 1, 3, 1, 1)

        self.verticalSpacer_10 = QSpacerItem(20, 5, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Maximum)

        self.gridLayout_12.addItem(self.verticalSpacer_10, 0, 0, 1, 4)

        self.verticalSpacer_8 = QSpacerItem(78, 12, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.MinimumExpanding)

        self.gridLayout_12.addItem(self.verticalSpacer_8, 2, 0, 1, 4)

        self.button_PostCreateAddImageUnselected = QPushButton(self.frame_PostCreateToolsUnselected)
        self.button_PostCreateAddImageUnselected.setObjectName(u"button_PostCreateAddImageUnselected")
        self.button_PostCreateAddImageUnselected.setMinimumSize(QSize(30, 30))
        self.button_PostCreateAddImageUnselected.setMaximumSize(QSize(30, 30))

        self.gridLayout_12.addWidget(self.button_PostCreateAddImageUnselected, 1, 1, 1, 1)


        self.layout_PostCreateMain.addWidget(self.frame_PostCreateToolsUnselected)


        self.verticalLayout.addWidget(self.frame_PostCreateMain)

        self.frame_PostCreateToolsSelected = QFrame(frame_PostCreate)
        self.frame_PostCreateToolsSelected.setObjectName(u"frame_PostCreateToolsSelected")
        self.frame_PostCreateToolsSelected.setMinimumSize(QSize(0, 60))
        self.frame_PostCreateToolsSelected.setMaximumSize(QSize(16777215, 60))
        self.frame_PostCreateToolsSelected.setStyleSheet(u"")
        self.frame_PostCreateToolsSelected.setFrameShape(QFrame.StyledPanel)
        self.frame_PostCreateToolsSelected.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.frame_PostCreateToolsSelected)
        self.horizontalLayout_2.setSpacing(5)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(10, 10, 10, 10)
        self.button_PostCreateAddImageSelected = QPushButton(self.frame_PostCreateToolsSelected)
        self.button_PostCreateAddImageSelected.setObjectName(u"button_PostCreateAddImageSelected")
        self.button_PostCreateAddImageSelected.setMinimumSize(QSize(30, 30))
        self.button_PostCreateAddImageSelected.setMaximumSize(QSize(30, 30))

        self.horizontalLayout_2.addWidget(self.button_PostCreateAddImageSelected)

        self.button_PostCreateAddVideoSelected = QPushButton(self.frame_PostCreateToolsSelected)
        self.button_PostCreateAddVideoSelected.setObjectName(u"button_PostCreateAddVideoSelected")
        self.button_PostCreateAddVideoSelected.setMinimumSize(QSize(30, 30))
        self.button_PostCreateAddVideoSelected.setMaximumSize(QSize(30, 30))

        self.horizontalLayout_2.addWidget(self.button_PostCreateAddVideoSelected)

        self.button_PostCreateAddMusicSelected = QPushButton(self.frame_PostCreateToolsSelected)
        self.button_PostCreateAddMusicSelected.setObjectName(u"button_PostCreateAddMusicSelected")
        self.button_PostCreateAddMusicSelected.setMinimumSize(QSize(30, 30))
        self.button_PostCreateAddMusicSelected.setMaximumSize(QSize(30, 30))

        self.horizontalLayout_2.addWidget(self.button_PostCreateAddMusicSelected)

        self.horizontalSpacer_15 = QSpacerItem(377, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_15)

        self.button_PostCreate = QPushButton(self.frame_PostCreateToolsSelected)
        self.button_PostCreate.setObjectName(u"button_PostCreate")
        self.button_PostCreate.setMinimumSize(QSize(80, 40))
        self.button_PostCreate.setMaximumSize(QSize(80, 40))
        font = QFont()
        font.setBold(True)
        font.setItalic(False)
        self.button_PostCreate.setFont(font)
        self.button_PostCreate.setStyleSheet(u"")

        self.horizontalLayout_2.addWidget(self.button_PostCreate)


        self.verticalLayout.addWidget(self.frame_PostCreateToolsSelected)


        self.retranslateUi(frame_PostCreate)

        QMetaObject.connectSlotsByName(frame_PostCreate)
    # setupUi

    def retranslateUi(self, frame_PostCreate):
        frame_PostCreate.setWindowTitle(QCoreApplication.translate("frame_PostCreate", u"create", None))
#if QT_CONFIG(tooltip)
        self.label_PostCreateImage.setToolTip(QCoreApplication.translate("frame_PostCreate", u"Your Profile", None))
#endif // QT_CONFIG(tooltip)
        self.label_PostCreateImage.setText("")
        self.line_PostCreateText.setPlaceholderText(QCoreApplication.translate("frame_PostCreate", u"What's new?", None))
#if QT_CONFIG(tooltip)
        self.button_PostCreateAddVideoUnselected.setToolTip(QCoreApplication.translate("frame_PostCreate", u"Choose Video", None))
#endif // QT_CONFIG(tooltip)
        self.button_PostCreateAddVideoUnselected.setText("")
#if QT_CONFIG(tooltip)
        self.button_PostCreateAddMusicUnselected.setToolTip(QCoreApplication.translate("frame_PostCreate", u"Choose Music", None))
#endif // QT_CONFIG(tooltip)
        self.button_PostCreateAddMusicUnselected.setText("")
#if QT_CONFIG(tooltip)
        self.button_PostCreateAddImageUnselected.setToolTip(QCoreApplication.translate("frame_PostCreate", u"Choose Image", None))
#endif // QT_CONFIG(tooltip)
        self.button_PostCreateAddImageUnselected.setText("")
#if QT_CONFIG(tooltip)
        self.button_PostCreateAddImageSelected.setToolTip(QCoreApplication.translate("frame_PostCreate", u"Choose Image", None))
#endif // QT_CONFIG(tooltip)
        self.button_PostCreateAddImageSelected.setText("")
#if QT_CONFIG(tooltip)
        self.button_PostCreateAddVideoSelected.setToolTip(QCoreApplication.translate("frame_PostCreate", u"Choose Video", None))
#endif // QT_CONFIG(tooltip)
        self.button_PostCreateAddVideoSelected.setText("")
#if QT_CONFIG(tooltip)
        self.button_PostCreateAddMusicSelected.setToolTip(QCoreApplication.translate("frame_PostCreate", u"Choose Music", None))
#endif // QT_CONFIG(tooltip)
        self.button_PostCreateAddMusicSelected.setText("")
#if QT_CONFIG(tooltip)
        self.button_PostCreate.setToolTip(QCoreApplication.translate("frame_PostCreate", u"Create Post", None))
#endif // QT_CONFIG(tooltip)
        self.button_PostCreate.setText(QCoreApplication.translate("frame_PostCreate", u"Post", None))
    # retranslateUi

