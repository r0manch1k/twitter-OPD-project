from PySide6.QtCore import QPropertyAnimation, QTimer, QEasingCurve, Qt, QPoint
from PySide6.QtGui import QColor
from PySide6.QtWidgets import QDialog, QWidget, QGraphicsDropShadowEffect

from src.main.gui.design.error import Ui_dialog_Info


class InfoBar(Ui_dialog_Info, QDialog):

    red = "rgba(255,0,0,255)"
    blue = "rgba(5,168,22,255)"

    def __init__(self, parent: QWidget, text: str, error: bool = False, duration: int = 5000):
        super(Ui_dialog_Info, self).__init__()
        self.ui = Ui_dialog_Info()
        self.ui.setupUi(self)

        self.setParent(parent)
        self.text = text
        self.duration = duration
        self.startPos = QPoint(parent.size().width() + self.size().width() + 10,
                               parent.size().height() - self.size().height() - 10)
        self.endPos = QPoint(parent.size().width() - self.size().width() - 10,
                             parent.size().height() - self.size().height() - 10)

        if not error:
            self.color = self.blue
        else:
            self.color = self.red

        self.posAnimation = QPropertyAnimation(self, b"pos")

        self.__initSetup()
        self.__setShadow()

    def __initSetup(self):
        self.setAttribute(Qt.WidgetAttribute.WA_MacAlwaysShowToolWindow)
        self.setWindowFlag(Qt.WindowType.FramelessWindowHint)
        self.ui.label_Info.setText(self.text)
        self.setStyleSheet(f"QDialog "
                           f"{{border-radius: 20px; background-color: {self.color}; }} "
                           f"QLabel {{ color: white; }}")

    def __setShadow(self):

        self.__shadowBlurRadius = 10.0
        self.__borderWidth = 1
        self.__shadowMargin = 0
        self.__borderRadius = 12.0

        self.__effectSideBar = QGraphicsDropShadowEffect()
        self.__effectSideBar.setBlurRadius(self.__shadowBlurRadius)
        self.__effectSideBar.setColor(QColor(0, 0, 0, 127))
        self.__effectSideBar.setOffset(3.0)
        self.setGraphicsEffect(self.__effectSideBar)
        self.repaint()

    def __slideIn(self):
        self.posAnimation.setDuration(1500)
        self.posAnimation.setStartValue(self.startPos)
        self.posAnimation.setEndValue(self.endPos)
        self.posAnimation.setEasingCurve(QEasingCurve.Type.OutBack)
        self.posAnimation.start()

    def __slideOut(self):
        self.posAnimation.setDuration(500)
        self.posAnimation.setStartValue(self.endPos)
        self.posAnimation.setEndValue(self.startPos)
        self.posAnimation.setEasingCurve(QEasingCurve.Type.Linear)
        self.posAnimation.finished.connect(self.close)
        self.posAnimation.start()

    def showEvent(self, arg__1):
        super().showEvent(arg__1)

        self.__slideIn()
        if self.duration >= 0:
            QTimer.singleShot(self.duration, self.__slideOut)

    def close(self):
        self.hide()
        super().close()
