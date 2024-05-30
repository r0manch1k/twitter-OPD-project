from PySide6.QtWidgets import QWidget, QGraphicsDropShadowEffect
from PySide6.QtGui import QIcon, QFontDatabase, QFont, QColor
from PySide6.QtCore import QSize, Qt, QEvent

from src.main.gui.design.post.post import Ui_form_Post
from src.main.objects.widgets import ProfilePictureFrame

from src.main.gui.resources import resources


class Post(Ui_form_Post, QWidget):

    userNameStyle = ("font-size:14px;"
                     "font-weight:800")

    userLoginStyle = ("color:rgb(184,191,195);"
                      "font-size:14px;"
                      "font-weight:350")

    postDataStyle = ("color:rgb(184,191,195);"
                     "font-size:13px;"
                     "font-weight:350")

    postReactionsStyle_1 = ("font-size:13px;"
                            "font-weight:800")

    postReactionsStyle_2 = ("color:rgb(184,191,195);"
                            "font-size:13px;"
                            "font-weight:350")

    postTextStyle = ("font-size:13px;"
                     "font-weight:350")

    def __init__(self, userName: str, userLogin: str, photoPath: str, postText: str, postData: str, postLikes: int,
                 postDislikes: int, postComments: int):

        super(Ui_form_Post, self).__init__()
        self.ui = Ui_form_Post()
        self.ui.setupUi(self)

        fontId = QFontDatabase.addApplicationFont(":/files/fonts/Roboto/Roboto-Bold.ttf")
        families = QFontDatabase.applicationFontFamilies(fontId)
        self.fontBold = QFont(families[0])

        fontId = QFontDatabase.addApplicationFont(":/files/fonts/Roboto/Roboto-Medium.ttf")
        families = QFontDatabase.applicationFontFamilies(fontId)
        self.fontMedium = QFont(families[0])

        fontId = QFontDatabase.addApplicationFont(":/files/fonts/Roboto/Roboto-Regular.ttf")
        families = QFontDatabase.applicationFontFamilies(fontId)
        self.fontRegular = QFont(families[0])

        fontId = QFontDatabase.addApplicationFont(":/files/fonts/Roboto/Roboto-Light.ttf")
        families = QFontDatabase.applicationFontFamilies(fontId)
        self.fontThin = QFont(families[0])

        self.setPost(userName, userLogin, photoPath, postText, postData, postLikes,
                     postDislikes, postComments)

        self.__initSetup()
        self.__setIconsSVG()
        self.__setMyFont()
        self.__setShadow()

    def __initSetup(self):

        self.setMaximumHeight(300)

        self.setWindowFlags(Qt.Window | Qt.FramelessWindowHint | Qt.WindowMinMaxButtonsHint)
        shadow = QGraphicsDropShadowEffect(blurRadius=5, xOffset=3, yOffset=3)
        self.setGraphicsEffect(shadow)

        self.ui.button_More.installEventFilter(self)

    def __setIconsSVG(self):

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

        icon_More = QIcon()
        icon_More.addFile("gui/resources/icons/MoreGrey.svg", QSize(), QIcon.Normal)
        self.ui.button_More.setIcon(icon_More)
        self.ui.button_More.setIconSize(QSize(20, 20))

    def __setMyFont(self):

        self.ui.label_UserName.setFont(self.fontRegular)
        self.ui.label_PostText.setFont(self.fontRegular)
        self.ui.label_PostData.setFont(self.fontRegular)
        self.ui.label_Likes.setFont(self.fontRegular)
        self.ui.label_Dislikes.setFont(self.fontRegular)
        self.ui.label_Comments.setFont(self.fontRegular)

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

    @classmethod
    def getUserName(cls, userName, userLogin):
        name = f"""<p style="vertical-align: middle;"><span style="{cls.userNameStyle}">{userName}</span><br>"""
        login = f"""<span style="{cls.userLoginStyle}">@{userLogin}</span></p>"""
        return name + login

    @classmethod
    def getPostData(cls, postData):
        data = f"""<p style="{cls.postDataStyle}">{postData}</p>"""
        return data

    @classmethod
    def getLikes(cls, postLikes):
        likes = f"""<p><span style="{cls.postReactionsStyle_1}">{postLikes} </span>
                <span style="{cls.postReactionsStyle_2}">Likes</span></p>"""
        return likes

    @classmethod
    def getDislikes(cls, postDislikes):
        likes = f"""<p><span style="{cls.postReactionsStyle_1}">{postDislikes} </span>
                    <span style="{cls.postReactionsStyle_2}">Dislikes</span></p>"""
        return likes

    @classmethod
    def getComments(cls, postComments):
        likes = f"""<p><span style="{cls.postReactionsStyle_1}">{postComments} </span>
                    <span style="{cls.postReactionsStyle_2}">Comments</span></p>"""
        return likes

    @classmethod
    def getText(cls, postText):
        text = f"""<p style="{cls.postTextStyle}">{postText}</p>"""
        return text

    def eventFilter(self, watched, event):

        if watched == self.ui.button_More:

            if event.type() == QEvent.Type.HoverEnter:

                icon = QIcon()
                icon.addFile("gui/resources/icons/MoreBlack.svg", QSize(), QIcon.Normal)
                watched.setIcon(icon)
                watched.setIconSize(QSize(20, 20))

                return True

            elif event.type() == QEvent.Type.HoverLeave:

                icon = QIcon()
                icon.addFile("gui/resources/icons/MoreGrey.svg", QSize(), QIcon.Normal)
                watched.setIcon(icon)
                watched.setIconSize(QSize(20, 20))

                return True

        return False

    def setPost(self, userName: str, userLogin: str, photoPath: str, postText: str, postData: str, postLikes: int,
                postDislikes: int, postComments: int):

        name = self.getUserName(userName, userLogin)
        self.ui.label_UserName.setText(name)

        text = self.getText(postText)
        self.ui.label_PostText.setText(text)

        data = self.getPostData(postData)
        self.ui.label_PostData.setText(data)

        likes = self.getLikes(postLikes)
        self.ui.label_Likes.setText(likes)

        dislikes = self.getDislikes(postDislikes)
        self.ui.label_Dislikes.setText(dislikes)

        comments = self.getComments(postComments)
        self.ui.label_Comments.setText(comments)

        photo = ProfilePictureFrame(photoPath, 50, 50, 25, shadowOffset=0)
        self.ui.layout_userName.insertWidget(0, photo)


