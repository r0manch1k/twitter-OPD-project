import random
import string

from PIL import Image, ImageDraw, ImageOps
from PySide6.QtCore import QRect
from PySide6.QtGui import QPixmap, Qt, QImage, QBrush, QPainter, QWindow


class ImageTools:
    profilePictureWidth = 500
    profilePictureHeight = 500

    profileBackgroundPictureWidth = 1000
    profileBackgroundPictureHeight = 500

    @staticmethod
    def getRandomString(length: int = 8) -> str:

        all_symbols = string.ascii_uppercase + string.digits
        result = ''.join(random.choice(all_symbols) for _ in range(length))
        return result

    @classmethod
    def getProfilePicture(cls, filePath: str, pathToSave: str, fileName: str = None) -> str:

        if not fileName:
            fileName = cls.getRandomString() + ".png"

        if not fileName.endswith(".png"):
            raise ValueError("File Name must contain '.png' extension!")

        image = Image.open(filePath)
        imageWidth, imageHeight = image.size

        if image.mode != "RGBA":
            raise ValueError("Image must be PNG!")

        if imageWidth < cls.profilePictureWidth:
            image = image.resize((cls.profilePictureWidth, int(imageHeight * cls.profilePictureWidth / imageWidth)))
            imageWidth, imageHeight = image.size

        if imageHeight < cls.profilePictureHeight:
            image = image.resize((int(imageWidth * cls.profilePictureHeight / imageHeight), cls.profilePictureHeight))
            imageWidth, imageHeight = image.size

        image = image.crop((int((imageWidth - cls.profilePictureWidth) / 2),
                            int((imageHeight - cls.profilePictureHeight) / 2),
                            int(imageWidth - (imageWidth - cls.profilePictureWidth) / 2),
                            int(imageHeight - (imageHeight - cls.profilePictureHeight) / 2)))
        image = image.resize(
            (cls.profilePictureWidth, cls.profilePictureHeight))  # Resizing 'cause crop doesn't work perfectly

        image.save(pathToSave + "Just" + fileName)

        imageFrame = Image.new("L", (cls.profilePictureWidth, cls.profilePictureHeight), 0)
        drawFrame_1 = ImageDraw.Draw(imageFrame)
        drawFrame_1.ellipse((0, 0, cls.profilePictureWidth, cls.profilePictureHeight), fill=255)

        image.putalpha(imageFrame)

        drawFrame_2 = ImageDraw.Draw(image)
        drawFrame_2.ellipse((0, 0, cls.profilePictureWidth, cls.profilePictureHeight),
                            outline=(235, 237, 239), width=15)

        image.save(pathToSave + fileName)

        return pathToSave + fileName

    @classmethod
    def getProfilePicturePixmap(cls, filePath: str, width: int, height: int) -> QPixmap:

        if not filePath.endswith(".png"):
            raise TypeError("File Name must contain '.png' extension!")

        with open(filePath, "rb") as imageData:
            image = QImage.fromData(imageData.read(), ".png")
        image.convertToFormat(QImage.Format_ARGB32)

        outImage = QImage(image.width(), image.height(), QImage.Format_ARGB32)
        outImage.fill(Qt.GlobalColor.transparent)

        brush = QBrush(image)
        painter = QPainter(outImage)
        painter.setBrush(brush)
        painter.setPen(Qt.PenStyle.NoPen)
        painter.setRenderHint(QPainter.Antialiasing, True)
        painter.drawEllipse(0, 0, image.width(), image.height())
        painter.end()

        pixelRatio = QWindow().devicePixelRatio()
        pixMap = QPixmap.fromImage(outImage)
        pixMap.setDevicePixelRatio(pixelRatio)
        width *= pixelRatio
        height *= pixelRatio

        pixMap = pixMap.scaled(width, height, Qt.AspectRatioMode.KeepAspectRatio,
                               Qt.TransformationMode.SmoothTransformation)

        return pixMap

    @classmethod
    def getPictureForWidget(cls, widgetWidth: int, widgetHeight: int, offsetY: int, filePath: str, pathToSave: str,
                            fileName: str = None) -> str:

        if not filePath.endswith(".png"):
            raise ValueError("File Name must contain '.png' extension!")

        if not fileName:
            fileName = cls.getRandomString() + ".png"

        image = Image.open(filePath)
        imageWidth, imageHeight = image.size

        pixelPatio = QWindow().devicePixelRatio()
        width = int(widgetWidth * pixelPatio)
        height = int(widgetHeight * pixelPatio)

        if imageWidth < width:
            image = image.resize((width, int(imageHeight * width / imageWidth)))
            imageWidth, imageHeight = image.size

        while imageHeight < height + offsetY:
            concatenatedImageV = Image.new("RGBA", (imageWidth, imageHeight + imageHeight))
            concatenatedImageV.paste(image, (0, 0))
            concatenatedImageV.paste(ImageOps.flip(image), (0, imageHeight))
            image = concatenatedImageV
            imageWidth, imageHeight = image.size

        image = image.crop((int((imageWidth - width) / 2),
                            offsetY,
                            int(imageWidth - (imageWidth - width) / 2),
                            offsetY + height))

        image = image.resize((width, height))

        image.save(pathToSave + fileName)

        return pathToSave + fileName
