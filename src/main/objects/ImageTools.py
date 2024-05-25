import random
import string

from PIL import Image, ImageQt, ImageDraw
from PySide6.QtGui import QPixmap


class ImageTools:

    profilePictureWidth = 500
    profilePictureHeight = 500

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

        imageFrame = Image.new("L", (cls.profilePictureWidth, cls.profilePictureHeight), 0)
        drawFrame_1 = ImageDraw.Draw(imageFrame)
        drawFrame_1.ellipse((0, 0, cls.profilePictureWidth, cls.profilePictureHeight), fill=255)

        image.putalpha(imageFrame)

        drawFrame_2 = ImageDraw.Draw(image)
        drawFrame_2.ellipse((0, 0, cls.profilePictureWidth, cls.profilePictureHeight),
                            outline=(235, 237, 239), width=30)

        image.save(pathToSave + fileName)

        return pathToSave + fileName


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