from PySide6.QtWidgets import QWidget
from PySide6.QtGui import QIcon
from PySide6.QtCore import QSize

from src.main.gui.design.post.post import Ui_form_Post

from .ImageTools import getPicture


class Post(Ui_form_Post, QWidget):
    def __init__(self):
        super(Ui_form_Post, self).__init__()
        self.ui = Ui_form_Post()
        self.ui.setupUi(self)

        self.setIconsSVG()
        self.setAuthor("Admin", "05.19.1995", "i want it i got it", 40, 30, 100)

    def setAuthor(self, author, date, header, likes, dislikes, comments):

        # profile_img = QIcon(getPicture("photo3.png"))
        # self.ui.button_PostAuthorAccount.setIcon(profile_img)
        self.ui.button_PostAuthorAccount.setIconSize(QSize(30, 30))
        self.ui.button_PostAuthorAccount.setText(author)
        self.ui.label_PostAuthorDate.setText(date)

        self.ui.label_PostContentHeader.setText(header)

        self.ui.button_PostInfoLikes.setText(str(likes))
        self.ui.button_PostInfoDislikes.setText(str(dislikes))
        self.ui.button_PostInfoComments.setText(str(comments))

    def setIconsSVG(self):

        icon_Likes = QIcon()
        icon_Likes.addFile("gui/resources/icons/Like.svg", QSize(), QIcon.Normal)
        self.ui.button_PostInfoLikes.setIcon(icon_Likes)
        self.ui.button_PostInfoLikes.setIconSize(QSize(25, 25))

        icon_Dislikes = QIcon()
        icon_Dislikes.addFile("gui/resources/icons/Dislike.svg", QSize(), QIcon.Normal)
        self.ui.button_PostInfoDislikes.setIcon(icon_Dislikes)
        self.ui.button_PostInfoDislikes.setIconSize(QSize(25, 52))

        icon_Comments = QIcon()
        icon_Comments.addFile("gui/resources/icons/Comments.svg", QSize(), QIcon.Normal)
        self.ui.button_PostInfoComments.setIcon(icon_Comments)
        self.ui.button_PostInfoComments.setIconSize(QSize(25, 25))