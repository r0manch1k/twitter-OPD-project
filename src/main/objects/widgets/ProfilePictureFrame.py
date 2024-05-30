from PySide6.QtCore import Qt, QSize
from PySide6.QtGui import QPixmap, QPainter, QColor, QPen
from PySide6.QtWidgets import QLabel


class ProfilePictureFrame(QLabel):

    frameSize = 2

    def __init__(self, imagePath: str, width: int = 150, height: int = 150, radius: int = 75, parent=None):
        super(ProfilePictureFrame, self).__init__(parent)

        self.setWindowFlags(Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_TranslucentBackground)
        self.setScaledContents(True)

        self.borderRadius = radius
        self.setFixedSize(width, height)

        self.profileImage = QPixmap(imagePath)
        self.profileImage = self.profileImage.scaled(QSize(width, height), Qt.AspectRatioMode.IgnoreAspectRatio,
                                                     Qt.TransformationMode.SmoothTransformation)

        # self.profileImage = QImage(imagePath)
        # self.profileImage = self.profileImage.scaled(QSize(width, height), Qt.AspectRatioMode.KeepAspectRatio,
        #                                              Qt.TransformationMode.SmoothTransformation)

    def paintEvent(self, arg__1):
        size = self.size()
        painter = QPainter()
        painter.begin(self)
        painter.setRenderHint(QPainter.Antialiasing, True)
        # painter.drawPixmap(self.rect(), self.profileImage, self.profileImage.rect())
        # painter.setPen(QPen(QColor(229, 235, 238), self.frameSize))
        painter.setPen(QPen(QColor(255, 255, 255), self.frameSize))
        painter.setBrush(self.profileImage)
        painter.drawRoundedRect(self.frameSize / 2, self.frameSize / 2, size.width() - self.frameSize,
                                size.height() - self.frameSize, self.borderRadius - self.frameSize / 2,
                                self.borderRadius - self.frameSize / 2)
        painter.end()
