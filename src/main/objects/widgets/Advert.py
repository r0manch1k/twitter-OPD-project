import webbrowser

from PySide6.QtCore import QPropertyAnimation, QTimer, QEasingCurve, Qt, QPoint, Signal, QRect
from PySide6.QtGui import QColor, QPainter
from PySide6.QtWidgets import QWidget, QLabel, QGraphicsDropShadowEffect

from src.main.gui.design.ad import Ui_form_Ad
from src.main.objects.ImageTools import ImageTools


class Advert(Ui_form_Ad, QWidget):
    clickedSignal = Signal()

    amountTimeToHold = 15000

    def __init__(self, width: int):
        super(Ui_form_Ad, self).__init__()
        self.ui = Ui_form_Ad()
        self.ui.setupUi(self)

        self.width = width
        self._background = None
        self._scrollbar = QLabel()
        self._timer: QTimer = QTimer(self)
        self._animation: QPropertyAnimation = QPropertyAnimation()

        self._listAds = []

        self.__initSetup()
        # self.__setShadow()

    def __initSetup(self):

        self.setFixedWidth(self.width)
        self.setAttribute(Qt.WidgetAttribute.WA_TranslucentBackground)
        self._scrollbar.setAttribute(Qt.WidgetAttribute.WA_TranslucentBackground)
        self.ui.frame_Ad.setAttribute(Qt.WidgetAttribute.WA_TranslucentBackground)
        self._timer.timeout.connect(self.moveForward)
        self.ui.layout_Main.addWidget(self._scrollbar)

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

    def mouseReleaseEvent(self, event):

        if not self._listAds:
            return
        urlIndex = -self._scrollbar.pos().x() // self.size().width()
        webbrowser.open(self._listAds[urlIndex]["url"])
        self.start()

    def paintEvent(self, event):

        painter = QPainter()
        painter.begin(self)
        painter.setRenderHint(QPainter.Antialiasing, True)
        painter.setPen(Qt.PenStyle.NoPen)
        if self._background:
            pixmapCurrent = self._background.copy(
                QRect(-self._scrollbar.pos().x(), 0,
                      -self._scrollbar.pos().x() + self.size().width(), self.size().height()))
            painter.setBrush(pixmapCurrent)
        painter.drawRoundedRect(0, 0, self.size().width(), self.size().height(), 20, 20)
        painter.end()

    def setAdvert(self, pathImage: str, offsetY: int = 0, url: str = None):

        pixmapAd = ImageTools.getPixmapFromImage(pathImage, self.size().width(), self.size().height(), offsetY)
        infoAd = {"pixmap": pixmapAd, "url": url}
        self._listAds.append(infoAd)

    def moveForward(self):

        self._animation.setDuration(2500)
        self._animation.setStartValue(QPoint(self._scrollbar.pos().x(), 0))
        self._animation.setEndValue(QPoint(self._scrollbar.pos().x() - self.size().width(), 0))
        if self._scrollbar.pos().x() - self.size().width() + self._scrollbar.width() <= 0:
            self._animation.setEndValue(
                QPoint(self._scrollbar.pos().x() + self.size().width(), 0))
            self._timer.timeout.connect(self.moveBackward)
        self._animation.setEasingCurve(QEasingCurve.Type.Linear)
        self._animation.start()

    def moveBackward(self):

        self._animation.setDuration(2500)
        self._animation.setStartValue(QPoint(self._scrollbar.pos().x(), 0))
        self._animation.setEndValue(QPoint(self._scrollbar.pos().x() + self.size().width(), 0))
        if self._scrollbar.pos().x() >= 0:
            self._animation.setEndValue(
                self._animation.setEndValue(QPoint(self._scrollbar.pos().x() - self.size().width(), 0)))
            self._timer.timeout.connect(self.moveForward)
        self._animation.setEasingCurve(QEasingCurve.Type.Linear)
        self._animation.start()

    def start(self):

        if not self._listAds:
            return

        self._background = self._listAds[0]["pixmap"]
        for infoAd in self._listAds[1:]:
            self._background = ImageTools.concatenatePixmapH(self._background, infoAd["pixmap"])

        self._scrollbar.setFixedWidth(self._background.width())
        self._scrollbar.setFixedHeight(self.size().height())
        self.ui.layout_Main.addWidget(self._scrollbar)
        self._scrollbar.move(0, 0)
        self._animation = QPropertyAnimation(self._scrollbar, b"pos")

        self._timer.start(self.amountTimeToHold)
