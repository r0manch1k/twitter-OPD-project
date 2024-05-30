import random
import string
import os

from PIL import Image, ImageQt, ImageDraw
from PySide6.QtGui import QPixmap, QPen, Qt, QPainterPath, QRegion, QImage, QBrush, QPainter, QWindow
from PySide6.QtCore import QObject, QRect


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
        image = image.resize((cls.profilePictureWidth, cls.profilePictureHeight))

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
    def getProfileBackgroundPicture(cls, filePath: str, pathToSave: str, fileName: str = None) -> str:

        if not fileName:
            fileName = cls.getRandomString() + ".png"

        if not fileName.endswith(".png"):
            raise ValueError("File Name must contain '.png' extension!")

        gradient = Image.linear_gradient("L")
        gradient = gradient.resize((cls.profileBackgroundPictureWidth, cls.profileBackgroundPictureHeight))

        alpha = Image.new("L", (cls.profileBackgroundPictureWidth, cls.profileBackgroundPictureHeight), "white")
        alpha.paste(gradient)
        alpha = alpha.transpose(Image.Transpose.FLIP_TOP_BOTTOM)
        alpha.paste(gradient)

        image = Image.open(filePath)
        imageWidth, imageHeight = image.size

        if imageWidth < cls.profileBackgroundPictureWidth:
            image = image.resize(
                (cls.profileBackgroundPictureWidth, int(imageHeight * cls.profileBackgroundPictureWidth / imageWidth)))
            imageWidth, imageHeight = image.size

        if imageHeight < cls.profileBackgroundPictureHeight:
            image = image.resize((int(imageWidth * cls.profileBackgroundPictureHeight / imageHeight),
                                  cls.profileBackgroundPictureHeight))
            imageWidth, imageHeight = image.size

        image = image.crop((int((imageWidth - cls.profileBackgroundPictureWidth) / 2),
                            int((imageHeight - cls.profileBackgroundPictureHeight) / 2),
                            imageWidth - int((imageWidth - cls.profileBackgroundPictureWidth) / 2),
                            imageHeight - int((imageHeight - cls.profileBackgroundPictureHeight) / 2)))

        frame = Image.open("gui/resources/images/frame.png")
        frame = frame.crop((0, 0, cls.profileBackgroundPictureWidth, cls.profileBackgroundPictureHeight))

        image_rgba = Image.new("RGBA", (cls.profileBackgroundPictureWidth, cls.profileBackgroundPictureHeight), 'white')
        image_rgba.paste(image, (0, 0), image)
        image_rgba.paste(frame, (0, 0), frame)

        # image_rgba.putalpha(alpha)

        image_rgba.save(pathToSave + fileName)

        return pathToSave + fileName

    @classmethod
    def getRoundedMask(cls, imgdata, imgtype="png", size=150):

        image = QImage.fromData(imgdata, imgtype)
        image.convertToFormat(QImage.Format_ARGB32)

        # Crop image to a square:
        imgsize = min(image.width(), image.height())
        rect = QRect(
            (image.width() - imgsize) / 2,
            (image.height() - imgsize) / 2,
            imgsize,
            imgsize,
        )
        image = image.copy(rect)

        # Create the output image with the same dimensions and an alpha channel
        # and make it completely transparent:
        out_img = QImage(imgsize, imgsize, QImage.Format_ARGB32)
        out_img.fill(Qt.GlobalColor.transparent)

        # Create a texture brush and paint a circle with the original image onto
        # the output image:
        brush = QBrush(image)  # Create texture brush
        painter = QPainter(out_img)  # Paint the output image
        painter.setBrush(brush)  # Use the image texture brush
        painter.setPen(Qt.PenStyle.NoPen)  # Don't draw an outline
        painter.setRenderHint(QPainter.Antialiasing, True)  # Use AA
        painter.drawEllipse(0, 0, imgsize, imgsize)  # Actually draw the circle
        painter.end()  # We are done (segfault if you forget this)

        # Convert the image to a pixmap and rescale it.  Take pixel ratio into
        # account to get a sharp image on retina displays:
        pr = QWindow().devicePixelRatio()
        pm = QPixmap.fromImage(out_img)
        pm.setDevicePixelRatio(pr)
        size *= pr
        pm = pm.scaled(size, size, Qt.AspectRatioMode.KeepAspectRatio, Qt.TransformationMode.SmoothTransformation)

        return pm


def getPicture(fp):
    frame_width = 500
    frame_height = 500
    background = Image.open(fp)
    b_width, b_height = background.size

    background = background.crop((int((b_width - frame_width) / 2),
                                  int((b_height - frame_height) / 2),
                                  int(b_width - (b_width - frame_width) / 2),
                                  int(b_height - (b_height - frame_height) / 2)))

    img_frame = Image.new("L", (frame_width, frame_height), 0)
    draw = ImageDraw.Draw(img_frame)
    draw.ellipse((50, 50, frame_width - 50, frame_height - 50), fill=255)

    background.putalpha(img_frame)

    draw_frame = ImageDraw.Draw(background)
    draw_frame.ellipse((30, 30, frame_width - 30, frame_height - 30), outline=(235, 237, 239), width=10)

    background.save("gui/resources/images/rendered/image.png")

    imgQT = ImageQt.ImageQt(background)
    imgQT = QPixmap.fromImage(imgQT)
    return imgQT


def getPicture_1(fp: str, name: str):
    frame_width = 500
    frame_height = 500
    background = Image.open(fp)
    b_width, b_height = background.size

    background = background.crop((int((b_width - frame_width) / 2),
                                  int((b_height - frame_height) / 2),
                                  int(b_width - (b_width - frame_width) / 2),
                                  int(b_height - (b_height - frame_height) / 2)))

    img_frame = Image.new("L", (frame_width, frame_height), 0)
    draw = ImageDraw.Draw(img_frame)
    draw.ellipse((0, 0, frame_width, frame_height), fill=255)

    background.putalpha(img_frame)

    draw_frame = ImageDraw.Draw(background)
    draw_frame.ellipse((0, 0, frame_width, frame_height), outline=(235, 237, 239), width=30)

    background.save("gui/resources/images/rendered/" + name)

    imgQT = ImageQt.ImageQt(background)
    imgQT = QPixmap.fromImage(imgQT)
    return imgQT
