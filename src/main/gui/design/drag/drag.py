# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'drag.ui'
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
from PySide6.QtWidgets import (QApplication, QFrame, QGridLayout, QLabel,
    QSizePolicy, QSpacerItem, QWidget)

class Ui_DragNDrop(object):
    def setupUi(self, DragNDrop):
        if not DragNDrop.objectName():
            DragNDrop.setObjectName(u"DragNDrop")
        DragNDrop.resize(300, 150)
        DragNDrop.setMinimumSize(QSize(300, 150))
        DragNDrop.setMaximumSize(QSize(300, 150))
        DragNDrop.setStyleSheet(u"QFrame {\n"
"	border-radius: 30px;\n"
"	border: 2px dashed rgb(184,191,195);\n"
"	background-color: rgb(235, 237, 239);\n"
"}\n"
"\n"
"QLabel {\n"
"	border: 0;\n"
"	color: rgb(184,191,195);\n"
"}")
        DragNDrop.setFrameShape(QFrame.StyledPanel)
        DragNDrop.setFrameShadow(QFrame.Raised)
        self.gridLayout = QGridLayout(DragNDrop)
        self.gridLayout.setSpacing(0)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalSpacer = QSpacerItem(20, 54, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Maximum)

        self.gridLayout.addItem(self.verticalSpacer, 0, 1, 1, 1)

        self.horizontalSpacer = QSpacerItem(50, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer, 1, 0, 1, 1)

        self.label_StateInfo = QLabel(DragNDrop)
        self.label_StateInfo.setObjectName(u"label_StateInfo")
        self.label_StateInfo.setMinimumSize(QSize(190, 20))
        self.label_StateInfo.setMaximumSize(QSize(190, 20))
        font = QFont()
        font.setBold(True)
        self.label_StateInfo.setFont(font)
        self.label_StateInfo.setAlignment(Qt.AlignCenter)
        self.label_StateInfo.setIndent(0)

        self.gridLayout.addWidget(self.label_StateInfo, 1, 1, 1, 1)

        self.horizontalSpacer_2 = QSpacerItem(50, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer_2, 1, 2, 1, 1)

        self.verticalSpacer_2 = QSpacerItem(20, 57, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Maximum)

        self.gridLayout.addItem(self.verticalSpacer_2, 2, 1, 1, 1)


        self.retranslateUi(DragNDrop)

        QMetaObject.connectSlotsByName(DragNDrop)
    # setupUi

    def retranslateUi(self, DragNDrop):
        DragNDrop.setWindowTitle(QCoreApplication.translate("DragNDrop", u"Frame", None))
        self.label_StateInfo.setText(QCoreApplication.translate("DragNDrop", u"Drag and Drop Profile Picture", None))
    # retranslateUi

