from PySide6.QtCore import QSize, Qt, QEvent, Signal
from PySide6.QtGui import QIcon, QColor, QPainter, QCursor
from PySide6.QtWidgets import QFrame, QGraphicsDropShadowEffect, QPlainTextEdit, QStyleOptionButton, QStyle, \
    QApplication

from src.main.gui.design.create import Ui_frame_PostCreate
from src.main.objects.ImageTools import ImageTools
from src.main.gui.resources import resources


class CreatePost(Ui_frame_PostCreate, QFrame):

    postCreatedSignal = Signal(dict)
    userImagePressed = Signal()

    def __init__(self, userImagePath):
        super(Ui_frame_PostCreate, self).__init__()
        self.ui = Ui_frame_PostCreate()
        self.ui.setupUi(self)

        self.userImagePath = userImagePath

        self.__setIconsSVG()
        self.__initSetup()
        self.__setShadow()

    def __setIconsSVG(self):
        icon_AddImage = QIcon()
        icon_AddImage.addFile(":icons/icons/Image.svg", QSize(),
                              QIcon.Normal)
        self.ui.button_PostCreateAddImageUnselected.setIcon(icon_AddImage)
        self.ui.button_PostCreateAddImageUnselected.setIconSize(QSize(20, 20))
        self.ui.button_PostCreateAddImageSelected.setIcon(icon_AddImage)
        self.ui.button_PostCreateAddImageSelected.setIconSize(QSize(20, 20))

        icon_AddVideo = QIcon()
        icon_AddVideo.addFile(":icons/icons/Video.svg", QSize(),
                              QIcon.Normal)
        self.ui.button_PostCreateAddVideoUnselected.setIcon(icon_AddVideo)
        self.ui.button_PostCreateAddVideoUnselected.setIconSize(QSize(20, 20))
        self.ui.button_PostCreateAddVideoSelected.setIcon(icon_AddVideo)
        self.ui.button_PostCreateAddVideoSelected.setIconSize(QSize(20, 20))

        icon_AddMusic = QIcon()
        icon_AddMusic.addFile(":icons/icons/Music.svg", QSize(),
                              QIcon.Normal)
        self.ui.button_PostCreateAddMusicUnselected.setIcon(icon_AddMusic)
        self.ui.button_PostCreateAddMusicUnselected.setIconSize(QSize(20, 20))
        self.ui.button_PostCreateAddMusicSelected.setIcon(icon_AddMusic)
        self.ui.button_PostCreateAddMusicSelected.setIconSize(QSize(20, 20))

    def __initSetup(self):

        self.ui.frame_PostCreateToolsSelected.setVisible(False)
        self.ui.frame_PostCreateToolsUnselected.setHidden(False)

        self.setAttribute(Qt.WidgetAttribute.WA_Hover)

        self.ui.line_PostCreateText.installEventFilter(self)
        self.setAttribute(Qt.WidgetAttribute.WA_TranslucentBackground)

        self.setWindowFlags(Qt.Window | Qt.FramelessWindowHint | Qt.WindowMinMaxButtonsHint)
        shadow = QGraphicsDropShadowEffect(blurRadius=5, xOffset=3, yOffset=3)
        self.setGraphicsEffect(shadow)

        profilePixmap = ImageTools.getProfilePicturePixmap(self.userImagePath, self.ui.label_PostCreateImage.width(),
                                                           self.ui.label_PostCreateImage.height())
        self.ui.label_PostCreateImage.setPixmap(profilePixmap)

    def __setShadow(self):

        self.__shadowBlurRadius = 10.0
        self.__borderWidth = 1
        self.__shadowMargin = 0
        self.__borderRadius = 12.0

        self.__effect = QGraphicsDropShadowEffect()
        self.__effect.setBlurRadius(self.__shadowBlurRadius)
        self.__effect.setColor(QColor(0, 0, 0, 127))
        self.__effect.setOffset(5.0)
        self.setGraphicsEffect(self.__effect)

        self.repaint()

    def eventFilter(self, watched, event):

        if watched == self.ui.line_PostCreateText:

            if event.type() == QEvent.Type.FocusOut and self.underMouse():

                self.ui.line_PostCreateText.setFocus()
                return True

            if event.type() == QEvent.Type.FocusIn and self.underMouse():

                self.ui.frame_PostCreateToolsSelected.setVisible(True)
                self.ui.frame_PostCreateMain.setStyleSheet(
                    "QFrame#frame_PostCreateMain { border-bottom-left-radius: 0; border-bottom-right-radius: 0; }")
                self.ui.frame_PostCreateToolsUnselected.setHidden(True)
                self.ui.line_PostCreateText.setFixedHeight(80)
                self.ui.frame_PostCreateMain.setFixedHeight(100)
                self.setFixedHeight(160)
                QPlainTextEdit.focusInEvent(self.ui.line_PostCreateText, event)
                return True

            elif event.type() == QEvent.Type.FocusOut and not self.underMouse():

                self.ui.frame_PostCreateToolsSelected.setVisible(False)
                self.ui.frame_PostCreateMain.setStyleSheet(
                    "QFrame#frame_PostCreateMain { border-bottom-left-radius: 20px; "
                    "border-bottom-right-radius: 20px; }")
                self.ui.frame_PostCreateToolsUnselected.setHidden(False)
                self.ui.line_PostCreateText.setPlainText("")
                self.ui.line_PostCreateText.setFixedHeight(30)
                self.ui.frame_PostCreateMain.setFixedHeight(50)
                self.setFixedHeight(50)
                QPlainTextEdit.focusOutEvent(self.ui.line_PostCreateText, event)
                return True

        return False

    def openUserAccountPage(self):

        pass
