from PySide6.QtCore import Qt, QEvent, Signal
from PySide6.QtGui import QColor
from PySide6.QtWidgets import QFrame, QGraphicsDropShadowEffect, QPlainTextEdit, QFileDialog

from src.main.gui.design.createcom import Ui_frame_CommentCreate
from src.main.objects.ImageTools import ImageTools
from src.main.objects.server.PostTools import PostTools


class CreateComment(Ui_frame_CommentCreate, QFrame):
    openAccountPageSignal = Signal()

    errorSignal = Signal(dict)

    commentCreatedSignal = Signal(int)

    def __init__(self, userImagePath, postId: int, postTools: PostTools):
        super(Ui_frame_CommentCreate, self).__init__()
        self.ui = Ui_frame_CommentCreate()
        self.ui.setupUi(self)

        self.postId = postId
        self.__postTools = postTools

        self.userImagePath = userImagePath

        self.__setIconsSVG()
        self.__initSetup()
        self.__setShadow()

    def __setIconsSVG(self):

        pass

    def __initSetup(self):

        self.ui.frame_CommentCreateToolsSelected.setVisible(False)

        self.setAttribute(Qt.WidgetAttribute.WA_Hover)
        self.ui.button_CommentCreate.clicked.connect(self.createComment)

        self.installEventFilter(self)
        self.ui.line_CommentCreateText.installEventFilter(self)
        self.setAttribute(Qt.WidgetAttribute.WA_TranslucentBackground)

        self.setWindowFlags(Qt.Window | Qt.FramelessWindowHint | Qt.WindowMinMaxButtonsHint)
        shadow = QGraphicsDropShadowEffect(blurRadius=5, xOffset=3, yOffset=3)
        self.setGraphicsEffect(shadow)

        profilePixmap = ImageTools.getProfilePicturePixmap(self.userImagePath, self.ui.label_CommentCreateImage.width(),
                                                           self.ui.label_CommentCreateImage.height())
        self.ui.label_CommentCreateImage.setPixmap(profilePixmap)

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

        if event.type() == QEvent.Type.FocusOut and self.underMouse():
            self.ui.line_CommentCreateText.setFocus()
            return True

        if watched == self.ui.line_CommentCreateText:

            if event.type() == QEvent.Type.FocusIn and self.underMouse():

                self.ui.frame_CommentCreateToolsSelected.setVisible(True)
                self.ui.frame_CommentCreateMain.setStyleSheet(
                    "QFrame#frame_CommentCreateMain { border-bottom-left-radius: 0; border-bottom-right-radius: 0; }")
                self.ui.line_CommentCreateText.setFixedHeight(80)
                self.ui.frame_CommentCreateMain.setFixedHeight(100)
                self.setFixedHeight(160)
                QPlainTextEdit.focusInEvent(self.ui.line_CommentCreateText, event)

            elif event.type() == QEvent.Type.FocusOut and not self.underMouse():

                self.ui.frame_CommentCreateToolsSelected.setVisible(False)
                self.ui.frame_CommentCreateMain.setStyleSheet(
                    "QFrame#frame_CommentCreateMain { border-bottom-left-radius: 20px;"
                    "border-bottom-right-radius: 20px; }")
                self.ui.line_CommentCreateText.setPlainText("")
                self.ui.line_CommentCreateText.setFixedHeight(30)
                self.ui.frame_CommentCreateMain.setFixedHeight(50)
                self.setFixedHeight(50)
                QPlainTextEdit.focusOutEvent(self.ui.line_CommentCreateText, event)

        return False

    def isError(self, execute: dict) -> bool:
        if execute["error"]:
            self.errorSignal.emit(execute)
            return True
        return False

    def chooseFile(self, rootDir: str, nameFilter: str) -> str:

        fileName, ok = QFileDialog.getOpenFileName(self, "Select a File", rootDir, nameFilter)
        if ok:
            return fileName

    def createComment(self):

        text = self.ui.line_CommentCreateText.toPlainText()

        if not text:
            self.ui.line_CommentCreateText.setFocus()
            return

        execute = self.__postTools.createComment(comment_text=text, post_id=self.postId)
        if self.isError(execute):
            return
        self.commentCreatedSignal.emit(self.postId)

    def openUserAccountPage(self):

        self.openAccountPageSignal.emit()
