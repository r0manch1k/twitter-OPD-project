import os

from PySide6.QtCore import QSize, Qt, QEvent, Signal
from PySide6.QtGui import QIcon, QColor
from PySide6.QtWidgets import QFrame, QGraphicsDropShadowEffect, QPlainTextEdit, QFileDialog

from src.main.gui.design.create import Ui_frame_PostCreate
from src.main.objects.ImageTools import ImageTools
from src.main.objects.server.FileManager import FileManager
from src.main.objects.server.PostTools import PostTools
from src.main.gui.resources import resources
from src.main.objects.server.Result import generateResult


class CreatePost(Ui_frame_PostCreate, QFrame):
    openAccountPageSignal = Signal()

    errorSignal = Signal(dict)

    postCreatedSignal = Signal()

    amountMaxFileNameSymbols = 40

    def __init__(self, userImagePath, postTools: PostTools, fileManager: FileManager):
        super(Ui_frame_PostCreate, self).__init__()
        self.ui = Ui_frame_PostCreate()
        self.ui.setupUi(self)

        self.__postTools = postTools
        self.__fileManager = fileManager

        self.userImagePath = userImagePath
        self.pathPostFile = None

        self.dictButtonsFileIcons = {}

        self.__setIconsSVG()
        self.__initSetup()
        self.__setShadow()

    def __setIconsSVG(self):

        icon_AddImage = QIcon()
        icon_AddImage.addFile(":icons/icons/Image.svg", QSize(), QIcon.Normal)
        icon_AddImageGrey = QIcon()
        icon_AddImageGrey.addFile(":icons/icons/ImageGrey.svg", QSize(), QIcon.Normal)
        self.ui.button_PostCreateAddImageUnselected.setIcon(icon_AddImageGrey)
        self.ui.button_PostCreateAddImageUnselected.setIconSize(QSize(20, 20))
        self.ui.button_PostCreateAddImageSelected.setIcon(icon_AddImageGrey)
        self.ui.button_PostCreateAddImageSelected.setIconSize(QSize(20, 20))

        icon_AddVideo = QIcon()
        icon_AddVideo.addFile(":icons/icons/Video.svg", QSize(), QIcon.Normal)
        icon_AddVideoGrey = QIcon()
        icon_AddVideoGrey.addFile(":icons/icons/VideoGrey.svg", QSize(), QIcon.Normal)
        self.ui.button_PostCreateAddVideoUnselected.setIcon(icon_AddVideoGrey)
        self.ui.button_PostCreateAddVideoUnselected.setIconSize(QSize(20, 20))
        self.ui.button_PostCreateAddVideoSelected.setIcon(icon_AddVideoGrey)
        self.ui.button_PostCreateAddVideoSelected.setIconSize(QSize(20, 20))

        icon_AddMusic = QIcon()
        icon_AddMusic.addFile(":icons/icons/Music.svg", QSize(), QIcon.Normal)
        icon_AddMusicGrey = QIcon()
        icon_AddMusicGrey.addFile(":icons/icons/MusicGrey.svg", QSize(), QIcon.Normal)
        self.ui.button_PostCreateAddMusicUnselected.setIcon(icon_AddMusicGrey)
        self.ui.button_PostCreateAddMusicUnselected.setIconSize(QSize(20, 20))
        self.ui.button_PostCreateAddMusicSelected.setIcon(icon_AddMusicGrey)
        self.ui.button_PostCreateAddMusicSelected.setIconSize(QSize(20, 20))

        self.dictButtonsFileIcons = {"image": {True: icon_AddImage, False: icon_AddImageGrey},
                                     "video": {True: icon_AddVideo, False: icon_AddVideoGrey},
                                     "music": {True: icon_AddMusic, False: icon_AddMusicGrey}}
        icon_RemoveFile = QIcon()
        icon_RemoveFile.addFile(":icons/icons/CloseRed.svg", QSize(), QIcon.Normal)
        self.ui.button_RemoveFile.setIcon(icon_RemoveFile)
        self.ui.button_RemoveFile.setIconSize(QSize(10, 10))

    def __initSetup(self):

        self.ui.frame_PostCreateToolsSelected.setVisible(False)
        self.ui.frame_PostCreateToolsUnselected.setHidden(False)
        self.ui.frame_Hint.setHidden(True)

        self.setAttribute(Qt.WidgetAttribute.WA_Hover)

        self.ui.button_PostCreateAddImageUnselected.clicked.connect(self.loadFile)
        self.ui.button_PostCreateAddImageSelected.clicked.connect(self.loadFile)
        self.ui.button_PostCreateAddVideoUnselected.clicked.connect(self.loadFile)
        self.ui.button_PostCreateAddVideoSelected.clicked.connect(self.loadFile)
        self.ui.button_PostCreateAddMusicUnselected.clicked.connect(self.loadFile)
        self.ui.button_PostCreateAddMusicSelected.clicked.connect(self.loadFile)
        self.ui.button_RemoveFile.clicked.connect(self.removeFile)
        self.ui.button_PostCreate.clicked.connect(self.createPost)

        self.installEventFilter(self)
        self.ui.line_PostCreateText.installEventFilter(self)
        self.ui.button_PostCreateAddImageSelected.installEventFilter(self)
        self.ui.button_PostCreateAddImageUnselected.installEventFilter(self)
        self.ui.button_PostCreateAddVideoSelected.installEventFilter(self)
        self.ui.button_PostCreateAddVideoUnselected.installEventFilter(self)
        self.ui.button_PostCreateAddMusicSelected.installEventFilter(self)
        self.ui.button_PostCreateAddMusicUnselected.installEventFilter(self)
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

        if (event.type() == QEvent.Type.FocusOut and self.underMouse()
                and not self.ui.button_RemoveFile.underMouse()
                and not self.ui.button_PostCreateAddImageSelected.underMouse()
                and not self.ui.button_PostCreateAddImageUnselected.underMouse()
                and not self.ui.button_PostCreateAddVideoSelected.underMouse()
                and not self.ui.button_PostCreateAddVideoUnselected.underMouse()
                and not self.ui.button_PostCreateAddMusicSelected.underMouse()
                and not self.ui.button_PostCreateAddMusicUnselected.underMouse()):

            self.ui.line_PostCreateText.setFocus()
            return True

        if watched == self.ui.line_PostCreateText:

            if event.type() == QEvent.Type.FocusIn and self.underMouse():

                self.ui.frame_PostCreateToolsSelected.setVisible(True)
                self.ui.frame_PostCreateMain.setStyleSheet(
                    "QFrame#frame_PostCreateMain { border-bottom-left-radius: 0; border-bottom-right-radius: 0; }")
                self.ui.frame_PostCreateToolsUnselected.setHidden(True)
                self.ui.line_PostCreateText.setFixedHeight(80)
                if self.ui.frame_Hint.isVisible():
                    self.ui.frame_PostCreateMain.setFixedHeight(100 + self.ui.frame_Hint.size().height())
                    self.setFixedHeight(160 + self.ui.frame_Hint.size().height())
                else:
                    self.ui.frame_PostCreateMain.setFixedHeight(100)
                    self.setFixedHeight(160)
                QPlainTextEdit.focusInEvent(self.ui.line_PostCreateText, event)

            elif event.type() == QEvent.Type.FocusOut and not self.underMouse():

                self.ui.frame_PostCreateToolsSelected.setVisible(False)
                self.ui.frame_PostCreateMain.setStyleSheet(
                    "QFrame#frame_PostCreateMain { border-bottom-left-radius: 20px;border-bottom-right-radius: 20px; }")
                self.ui.frame_PostCreateToolsUnselected.setHidden(False)
                self.ui.line_PostCreateText.setPlainText("")
                self.removeFile()
                self.ui.line_PostCreateText.setFixedHeight(30)
                self.ui.frame_PostCreateMain.setFixedHeight(50)
                self.setFixedHeight(50)
                QPlainTextEdit.focusOutEvent(self.ui.line_PostCreateText, event)

        elif watched == self.ui.button_PostCreateAddImageSelected:

            if event.type() == QEvent.Type.HoverEnter:
                self.ui.button_PostCreateAddImageSelected.setIcon(self.dictButtonsFileIcons["image"][True])
            elif event.type() == QEvent.Type.HoverLeave:
                self.ui.button_PostCreateAddImageSelected.setIcon(self.dictButtonsFileIcons["image"][False])

        elif watched == self.ui.button_PostCreateAddImageUnselected:

            if event.type() == QEvent.Type.HoverEnter:
                self.ui.button_PostCreateAddImageUnselected.setIcon(self.dictButtonsFileIcons["image"][True])
            elif event.type() == QEvent.Type.HoverLeave:
                self.ui.button_PostCreateAddImageUnselected.setIcon(self.dictButtonsFileIcons["image"][False])

        elif watched == self.ui.button_PostCreateAddVideoSelected:

            if event.type() == QEvent.Type.HoverEnter:
                self.ui.button_PostCreateAddVideoSelected.setIcon(self.dictButtonsFileIcons["video"][True])
            elif event.type() == QEvent.Type.HoverLeave:
                self.ui.button_PostCreateAddVideoSelected.setIcon(self.dictButtonsFileIcons["video"][False])

        elif watched == self.ui.button_PostCreateAddVideoUnselected:

            if event.type() == QEvent.Type.HoverEnter:
                self.ui.button_PostCreateAddVideoUnselected.setIcon(self.dictButtonsFileIcons["video"][True])
            elif event.type() == QEvent.Type.HoverLeave:
                self.ui.button_PostCreateAddVideoUnselected.setIcon(self.dictButtonsFileIcons["video"][False])

        elif watched == self.ui.button_PostCreateAddMusicSelected:

            if event.type() == QEvent.Type.HoverEnter:
                self.ui.button_PostCreateAddMusicSelected.setIcon(self.dictButtonsFileIcons["music"][True])
            elif event.type() == QEvent.Type.HoverLeave:
                self.ui.button_PostCreateAddMusicSelected.setIcon(self.dictButtonsFileIcons["music"][False])

        elif watched == self.ui.button_PostCreateAddMusicUnselected:

            if event.type() == QEvent.Type.HoverEnter:
                self.ui.button_PostCreateAddMusicUnselected.setIcon(self.dictButtonsFileIcons["music"][True])
            elif event.type() == QEvent.Type.HoverLeave:
                self.ui.button_PostCreateAddMusicUnselected.setIcon(self.dictButtonsFileIcons["music"][False])

        return False

    def isError(self, execute: dict) -> bool:
        if execute["error"]:
            self.errorSignal.emit(execute)
            return True
        return False

    @classmethod
    def formatFileName(cls, filename: str):
        lengthFileName = len(filename)
        if lengthFileName > cls.amountMaxFileNameSymbols:
            startIndex = lengthFileName // 2 - (lengthFileName - cls.amountMaxFileNameSymbols) // 2
            endIndex = lengthFileName // 2 + (lengthFileName - cls.amountMaxFileNameSymbols) // 2
            filename = filename[:startIndex] + "..." + filename[endIndex:]
        return filename

    def chooseFile(self, rootDir: str, nameFilter: str) -> str:

        fileName, ok = QFileDialog.getOpenFileName(self, "Select a File", rootDir, nameFilter)
        if ok:
            return fileName

    def loadFile(self):

        if (self.sender() == self.ui.button_PostCreateAddImageSelected
                or self.sender() == self.ui.button_PostCreateAddImageUnselected):

            self.pathPostFile = self.chooseFile(os.path.expanduser("~/Desktop"), "Images (*.png)")

        elif (self.sender() == self.ui.button_PostCreateAddVideoSelected
              or self.sender() == self.ui.button_PostCreateAddVideoUnselected):

            self.pathPostFile = self.chooseFile(os.path.expanduser("~/Desktop"), "Video (*.mp4)")

        elif (self.sender() == self.ui.button_PostCreateAddMusicSelected
              or self.sender() == self.ui.button_PostCreateAddMusicUnselected):

            self.pathPostFile = self.chooseFile(os.path.expanduser("~/Desktop"), "Music (*.mp3)")

        if self.pathPostFile:
            self.showHint(text=self.formatFileName(self.pathPostFile.split("/")[-1]), removeButton=True)

    def removeFile(self):

        self.hideHint()
        self.pathPostFile = None

    def createPost(self):

        text = self.ui.line_PostCreateText.toPlainText()

        if not text:
            self.ui.line_PostCreateText.setFocus()
            return

        imageId = videoId = None
        if self.pathPostFile and os.path.exists(self.pathPostFile):
            if self.pathPostFile.endswith(".png"):
                execute = self.__fileManager.loadFile(self.pathPostFile, imageId=1)
                if self.isError(execute):
                    return
                imageId = execute["data"]
            elif self.pathPostFile.endswith(".mp4"):
                execute = self.__fileManager.loadFile(self.pathPostFile, videoId=1)
                if self.isError(execute):
                    return
                videoId = execute["data"]
            else:
                execute = generateResult(error_type="format", error="Wrong file extension. Image must be PNG.")
                if self.isError(execute):
                    return

        execute = self.__postTools.createPost(post_text=text, image_id=imageId, video_id=videoId)
        if self.isError(execute):
            return
        self.postCreatedSignal.emit()

    def openUserAccountPage(self):

        self.openAccountPageSignal.emit()

    def showHint(self, text: str, removeButton: bool = False):

        if self.ui.frame_Hint.isHidden():
            self.ui.frame_PostCreateMain.setFixedHeight(
                self.ui.frame_PostCreateMain.size().height() + self.ui.frame_Hint.minimumHeight())
            self.setFixedHeight(self.size().height() + self.ui.frame_Hint.minimumHeight())

        self.ui.line_PostCreateText.setFocus()
        self.ui.button_RemoveFile.setVisible(removeButton)
        self.ui.label_Hint.setText(text)

        self.ui.frame_Hint.setVisible(True)

    def hideHint(self):

        if self.ui.line_PostCreateText.toPlainText() or self.ui.frame_PostCreateToolsSelected.isVisible():
            self.ui.line_PostCreateText.setFocus()
        self.ui.frame_Hint.setHidden(True)
        self.ui.frame_PostCreateMain.setFixedHeight(
            self.ui.frame_PostCreateMain.size().height() - self.ui.frame_Hint.minimumHeight())
        self.setFixedHeight(self.size().height() - self.ui.frame_Hint.minimumHeight())
