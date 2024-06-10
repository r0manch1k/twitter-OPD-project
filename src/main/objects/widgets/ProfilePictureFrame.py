from PySide6.QtCore import Qt, Signal, QEvent
from PySide6.QtGui import QPainter, QColor, QPen
from PySide6.QtWidgets import QLabel, QGraphicsDropShadowEffect

from src.main.objects.ImageTools import ImageTools


class ProfilePictureFrame(QLabel):

    hoverEnterSignal = Signal()
    hoverLeaveSignal = Signal()
    mousePressedSignal = Signal()

    def __init__(self, imagePath: str, width: int = 150, height: int = 150, radius: int = 75, frame: int = 2,
                 frameColor: tuple = (229, 235, 238), shadowOffset: int = 5,
                 parent=None):
        super(ProfilePictureFrame, self).__init__(parent)

        self.borderRadius = radius
        self.setFixedSize(width, height)

        self.frameColor = frameColor
        self.frame = frame
        self.shadowOffset = shadowOffset

        self.profileImage = ImageTools.getProfilePicturePixmap(imagePath, width, height)

        self.__initSetup()
        if shadowOffset:
            self.__setShadow()

    def __initSetup(self):
        self.setWindowFlags(Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_TranslucentBackground)
        self.setScaledContents(True)
        self.installEventFilter(self)
        self.setAttribute(Qt.WidgetAttribute.WA_Hover, True)

    def __setShadow(self):
        self.__shadowBlurRadius = 10.0
        self.__borderWidth = 1
        self.__shadowMargin = 0
        self.__borderRadius = 12.0

        self.__effect = QGraphicsDropShadowEffect()
        self.__effect.setBlurRadius(self.__shadowBlurRadius)
        self.__effect.setColor(QColor(0, 0, 0, 127))
        self.__effect.setOffset(self.shadowOffset)
        self.setGraphicsEffect(self.__effect)

        self.repaint()

    def eventFilter(self, watched, event):

        if watched == self:

            if event.type() == QEvent.Type.HoverEnter:

                self.hoverEnterSignal.emit()

                return True

            elif event.type() == QEvent.Type.HoverLeave:

                self.hoverLeaveSignal.emit()

                return True

            elif event.type() == QEvent.Type.MouseButtonPress:

                self.mousePressedSignal.emit()

                return

        return False

    def paintEvent(self, arg__1):
        size = self.size()
        painter = QPainter()
        painter.begin(self)
        painter.setRenderHint(QPainter.Antialiasing, True)
        painter.setPen(QPen(QColor(*self.frameColor), self.frame))
        painter.setBrush(self.profileImage)
        painter.drawRoundedRect(self.frame / 2, self.frame / 2, size.width() - self.frame,
                                size.height() - self.frame, self.borderRadius - self.frame / 2,
                                self.borderRadius - self.frame / 2)
        painter.end()
