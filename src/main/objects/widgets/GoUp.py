from PySide6.QtCore import QPropertyAnimation, QTimer, QEasingCurve, Qt, QPoint, Signal, QSize, QEvent
from PySide6.QtGui import QIcon
from PySide6.QtWidgets import QDialog, QWidget

from src.main.gui.design.goup import Ui_dialog_GoUp
from src.main.gui.resources import resources


class GoUp(Ui_dialog_GoUp, QDialog):

    clickedSignal = Signal()

    def __init__(self, parent: QWidget):
        super(Ui_dialog_GoUp, self).__init__()
        self.ui = Ui_dialog_GoUp()
        self.ui.setupUi(self)

        self.setParent(parent)

        self.__setIconsSVG()
        self.__initSetup()

    def __setIconsSVG(self):

        icon_Up = QIcon()
        icon_Up.addFile(":icons/icons/Up.svg", QSize(), QIcon.Normal)
        self.ui.button_GoUp.setIcon(icon_Up)
        self.ui.button_GoUp.setIconSize(QSize(20, 20))

    def __initSetup(self):

        self.setWindowFlag(Qt.WindowType.FramelessWindowHint)
        self.setAttribute(Qt.WidgetAttribute.WA_TranslucentBackground)
        self.ui.button_GoUp.clicked.connect(self.clicked)

    def clicked(self):

        self.clickedSignal.emit()


