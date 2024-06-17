import io
import random
import string

from PIL import Image, ImageDraw, ImageOps, ImageQt
from PySide6.QtCore import QBuffer, QIODevice, QSize
from PySide6.QtGui import QPixmap, Qt, QImage, QBrush, QPainter, QWindow
from src.main.objects.server.Result import generateResult


class ImageTools:
    profilePictureWidth = 500
    profilePictureHeight = 500

    profileBackgroundPictureWidth = 1000
    profileBackgroundPictureHeight = 500

    nameStyle = ("font-size:14px;"
                 "font-weight:800;"
                 "text-align:center;")

    usernameStyle = ("color:rgb(184,191,195);"
                     "font-size:14px;"
                     "font-weight:350;"
                     "text-align:center;")

    aboutStyle = ("color:rgb(184,191,195);"
                  "font-size:13px;"
                  "font-weight:350;"
                  "text-align:center;")

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

    @classmethod
    def getPictureForPost(cls, widgetWidth: int, widgetHeight: int, filePath: str, pathToSave: str,
                          fileName: str = None) -> dict:

        if not filePath.endswith(".png"):
            return generateResult(error_type="format", error="File Name must contain '.png' extension!")

        if not fileName:
            fileName = cls.getRandomString() + ".png"

        image = Image.open(filePath)
        imageWidth, imageHeight = image.size

        pixelPatio = QWindow().devicePixelRatio()
        width = int(widgetWidth * pixelPatio)
        height = int(widgetHeight * pixelPatio)

        image = image.resize((width, int(imageHeight * width / imageWidth)))
        imageWidth, imageHeight = image.size

        if imageHeight > height:
            image = image.crop((0, 0, width, height))
            imageWidth, imageHeight = image.size

        image = image.resize((width, imageHeight))
        imageWidth, imageHeight = image.size

        image.save(pathToSave + fileName)

        execute = {"filePath": pathToSave + fileName, "widgetWidth": widgetWidth,
                   "widgetHeight": imageHeight / pixelPatio}

        return generateResult(data=execute)

    @classmethod
    def getProfileToolTip(cls, imagePath: str, name: str, username: str, about: str = None) -> dict:

        pixmap = cls.getProfilePicturePixmap(imagePath, 60, 60)
        buffer = QBuffer()
        buffer.open(QIODevice.WriteOnly)
        pixmap.save(buffer, "PNG", quality=100)
        image = bytes(buffer.data().toBase64()).decode()
        html = (
            f'<img src="data:image/png;base64,{image}" style="margin-left:auto;margin-right:auto;">'
            f'<p style="{cls.nameStyle}line-height:0.1;"><strong>{name}</strong><br>'
            f'<p style="{cls.usernameStyle}">@{username}</p><p style="{cls.aboutStyle}">{about}</p>')

        styleSheet = ("QToolTip { border: 0; border-radius: 20px; background-color: white; color: black; "
                      "opacity: 255; padding: 5px; }")
        execute = {"html": html, "styleSheet": styleSheet}

        return execute

    @classmethod
    def getPixmapFromImage(cls, filePath: str, widgetWidth: int, widgetHeight: int, offsetY: int) -> QPixmap:

        if not filePath.endswith(".png"):
            raise ValueError("File Name must contain '.png' extension!")

        image = Image.open(filePath)
        imageWidth, imageHeight = image.size

        pixelPatio = QWindow().devicePixelRatio()
        width = int(widgetWidth * pixelPatio)
        height = int(widgetHeight * pixelPatio)

        tempHeight = int((imageWidth / width) * height)

        if tempHeight + offsetY > imageHeight:
            raise ValueError("Please make picture bigger. I didn't wanna write how to handle it.")

        image = image.crop((0, offsetY, imageWidth, tempHeight + offsetY))
        image = image.resize((widgetWidth, widgetHeight))

        qImage = ImageQt.ImageQt(image)
        pixmap = QPixmap.fromImage(qImage)
        return pixmap

    @classmethod
    def concatenatePixmapH(cls, pixmapFirst: QPixmap, pixmapSecond: QPixmap):

        widthFirst = pixmapFirst.size().width()
        widthSecond = pixmapSecond.size().width()
        height = pixmapFirst.size().height()

        newImage = QImage(QSize(widthFirst + widthSecond, height), QImage.Format.Format_ARGB32)

        painter = QPainter(newImage)
        painter.drawPixmap(0, 0, pixmapFirst)
        painter.drawPixmap(widthFirst, 0, pixmapSecond)
        painter.end()

        newPixmap = QPixmap.fromImage(newImage)

        return newPixmap
