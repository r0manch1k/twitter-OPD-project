import io
from urllib.request import Request, urlopen

import PIL
from PIL import Image
from PySide6.QtCore import QIODevice, QBuffer, Signal
from PySide6.QtGui import QImage
from PySide6.QtWidgets import QFrame, QWidget

from src.main.gui.design.drag import Ui_DragNDrop
from src.main.objects.ImageTools import ImageTools


class DragNDrop(Ui_DragNDrop, QFrame):
    imageDropped = Signal(bool)

    def __init__(self, parent: QWidget, pathToSave: str, fileName: str = None):
        super(Ui_DragNDrop, self).__init__()

        self.ui = Ui_DragNDrop()
        self.ui.setupUi(self)

        self.parent = parent
        self.pathToSave = pathToSave
        self.fileName = fileName

        self.initSetup()

    def initSetup(self):

        self.setAcceptDrops(True)
        self.ui.label_StateInfo.setText("Drag and Drop Profile Image")

    def setUnHovered(self):

        self.setStyleSheet("QFrame { background-color: rgb(235, 237, 239);"
                           "border-radius: 30px;"
                           "border: 2px dashed rgb(184,191,195); }"
                           "QLabel {"
                           "border: 0;"
                           "color: rgb(184,191,195); }")

    def setHovered(self):

        self.setStyleSheet("QFrame { background-color: rgb(219,228,233);"
                           "border-radius: 30px;"
                           "border: 2px dashed rgb(184,191,195); }"
                           "QLabel {"
                           "border: 0;"
                           "color: rgb(184,191,195); }")

    def dragEnterEvent(self, e):

        e.accept()
        self.setHovered()
        self.ui.label_StateInfo.setText("Drag and Drop Profile Image")

    def dragLeaveEvent(self, event):

        self.setUnHovered()

    def dropEvent(self, e):

        if e.mimeData().hasImage():

            try:
                qImage = QImage(e.mimeData().imageData())
                bIO = io.BytesIO()
                buffer = QBuffer()
                buffer.open(QIODevice.ReadWrite)
                qImage.save(buffer, "PNG")
                byteArray = buffer.data()
                bIO.write(byteArray.data())
                buffer.close()
                bIO.seek(0)
                image = Image.open(bIO)

            except Exception as exc:
                raise exc
                # self.setUnHovered()
                # self.ui.label_StateInfo.setText("Something went wrong...")
                # return

        elif e.mimeData().hasUrls():
            url = e.mimeData().urls()[0]

            if url.isLocalFile():

                try:
                    image = Image.open(url.toLocalFile())
                except PIL.UnidentifiedImageError:
                    self.ui.label_StateInfo.setText("Is it a picture?")
                    self.setUnHovered()
                    self.imageDropped.emit(False)
                    return

            else:
                try:
                    request = Request(url.toString())
                    image = Image.open(urlopen(request))

                except PIL.UnidentifiedImageError:
                    self.ui.label_StateInfo.setText("Is it a picture?")
                    self.setUnHovered()
                    self.imageDropped.emit(False)
                    return

        else:
            self.ui.label_StateInfo.setText("Something went wrong...")
            self.setUnHovered()
            self.imageDropped.emit(False)
            return

        if not image:
            self.ui.label_StateInfo.setText("Something went wrong...")
            self.setUnHovered()
            self.imageDropped.emit(False)
            return

        self.ui.label_StateInfo.setText("Uploaded!")

        if not self.fileName:
            filePath = self.pathToSave + ImageTools.getRandomString() + ".png"
        else:
            filePath = self.pathToSave + self.fileName
        image.save(filePath)

        try:
            imagePath = ImageTools.getProfilePicture(filePath, self.pathToSave, self.fileName)
        except ValueError:
            self.ui.label_StateInfo.setText("Only URLs or PNG!")
            self.setUnHovered()
            self.imageDropped.emit(False)
            return

        self.parent.setStyleSheet(f"""QFrame {{ border-image:  url({imagePath}) 0 0 0 0}}""")
        self.setUnHovered()
        self.imageDropped.emit(True)
