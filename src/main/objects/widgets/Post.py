from PySide6.QtWidgets import QWidget, QGraphicsDropShadowEffect, QMenu, QMainWindow, QApplication
from PySide6.QtGui import QIcon, QFontDatabase, QFont, QColor, QAction, QCursor
from PySide6.QtCore import QSize, Qt, QEvent, Signal

from src.main.gui.design.post import Ui_form_Post
from src.main.objects.widgets import ProfilePictureFrame
from src.main.objects.server.PostTools import PostTools
from src.main.objects.server.UserInfo import CurrentUser
from src.main.objects.server.FileManager import FileManager
from src.main.gui.resources import resources


class Post(Ui_form_Post, QWidget):
    nameStyle = ("font-size:14px;"
                 "font-weight:800")

    usernameStyle = ("color:rgb(184,191,195);"
                     "font-size:14px;"
                     "font-weight:350")

    accessStyle = ("color:rgb(184,191,195);"
                   "font-size:14px;"
                   "font-weight:550")

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

    connectionErrorSignal = Signal(str)
    formatErrorSignal = Signal(str)
    authErrorSignal = Signal(str)
    userImageClickedSignal = Signal(int)
    reportUserSignal = Signal(int)
    followUserSignal = Signal(int)
    deletePostSignal = Signal(int)

    def __init__(self, postId: int, postInfo: dict, postTools: PostTools, currentUser: CurrentUser,
                 fileManager: FileManager):

        super(Ui_form_Post, self).__init__()
        self.ui = Ui_form_Post()
        self.ui.setupUi(self)

        self.__postTools = postTools
        self.__currentUser = currentUser
        self.__fileManager = fileManager

        self.menuParentStyle = QMainWindow()
        self.buttonsReactionDict = {}

        self.postId = postId
        self.postImageId = postInfo["image_id"]
        self.postVideoId = postInfo["video_id"]
        self.postText = postInfo["post_text"]
        self.likes = postInfo["likes"]
        self.dislikes = postInfo["dislikes"]
        self.postTime = postInfo["post_time"]
        self.username = postInfo["username"]
        self.name = postInfo["name"]
        self.access = postInfo["access"]
        self.userImageId = postInfo["Users.image_id"]
        self.comments = postInfo["comments"]

        execute = self.__currentUser.access
        if self.isError(execute, openAuth=False):
            return
        self.currentUserAccess = execute["data"]

        self.__initSetup()
        self.__setIconsSVG()
        self.__setMyFont()
        self.__setShadow()

        self.setPost()

    def __setIconsSVG(self):

        icon_Comments = QIcon()
        icon_Comments.addFile(":icons/icons/Comments.svg", QSize(), QIcon.Normal)
        self.ui.button_PostComments.setIcon(icon_Comments)
        self.ui.button_PostComments.setIconSize(QSize(25, 25))

        icon_More = QIcon()
        icon_More.addFile(":icons/icons/MoreGrey.svg", QSize(), QIcon.Normal)
        self.ui.button_More.setIcon(icon_More)
        self.ui.button_More.setIconSize(QSize(20, 20))

        icon_Like = QIcon()
        icon_Like.addFile(":icons/icons/Like.svg", QSize(), QIcon.Normal)
        self.ui.button_PostLike.setIcon(icon_Like)
        self.ui.button_PostLike.setIconSize(QSize(23, 23))

        icon_LikeSelected = QIcon()
        icon_LikeSelected.addFile(":icons/icons/LikeSelected.svg", QSize(), QIcon.Normal)

        icon_Dislike = QIcon()
        icon_Dislike.addFile(":icons/icons/Dislike.svg", QSize(), QIcon.Normal)
        self.ui.button_PostDislike.setIcon(icon_Dislike)
        self.ui.button_PostDislike.setIconSize(QSize(18, 18))

        icon_DislikeSelected = QIcon()
        icon_DislikeSelected.addFile(":icons/icons/DislikeSelected.svg", QSize(), QIcon.Normal)

        self.buttonsReactionDict = {"like": {True: icon_LikeSelected, False: icon_Like},
                                    "dislike": {True: icon_DislikeSelected, False: icon_Dislike}}

    def __initSetup(self):

        self.setMaximumHeight(300)
        self.setAttribute(Qt.WidgetAttribute.WA_Hover)

        self.setWindowFlags(Qt.Window | Qt.FramelessWindowHint | Qt.WindowMinMaxButtonsHint)
        shadow = QGraphicsDropShadowEffect(blurRadius=5, xOffset=3, yOffset=3)
        self.setGraphicsEffect(shadow)

        self.ui.textBrowser_UserName.document().setDocumentMargin(0)
        self.ui.textBrowser_UserName.setStyleSheet("QTextBrowser { margin-top: 3px; }")
        self.ui.label_PostData.document().setDocumentMargin(0)
        self.ui.textBrowser_PostText.document().setDocumentMargin(0)
        self.ui.textBrowser_PostText.setLineWrapColumnOrWidth(0)
        self.ui.textBrowser_PostText.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.ui.textBrowser_PostText.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)

        self.ui.button_More.installEventFilter(self)
        self.ui.textBrowser_UserName.installEventFilter(self)
        self.ui.button_PostDislike.installEventFilter(self)
        self.ui.button_PostLike.installEventFilter(self)
        self.ui.button_PostComments.installEventFilter(self)

        self.ui.button_More.setToolTip("More")
        self.ui.button_PostDislike.setToolTip("Dislike")
        self.ui.button_PostLike.setToolTip("Like")
        self.ui.button_PostComments.setToolTip("Comments")

        menu_More = QMenu(self.menuParentStyle)

        action_FollowUser = QAction(f"&Follow @{self.username}", self)
        action_FollowUser.triggered.connect(self.followUser)
        menu_More.addAction(action_FollowUser)

        action_Report = QAction(f"&Report @{self.username}", self)
        action_Report.triggered.connect(self.reportUser)
        menu_More.addAction(action_Report)

        if self.currentUserAccess == "Admin":
            action_DeletePost = QAction(f"&Delete Post", self)
            action_DeletePost.triggered.connect(self.deletePost)
            menu_More.addAction(action_DeletePost)

        self.ui.button_More.setMenu(menu_More)

    def __setMyFont(self):

        fontId = QFontDatabase.addApplicationFont(":fonts/fonts/Roboto/Roboto-Regular.ttf")
        families = QFontDatabase.applicationFontFamilies(fontId)
        self.fontRegular = QFont(families[0])

        self.ui.textBrowser_UserName.setFont(self.fontRegular)
        self.ui.textBrowser_PostText.setFont(self.fontRegular)
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

    def isError(self, execute: dict, openAuth: bool = True) -> bool:

        if execute["error"]:
            if execute["error"]["connection"]:
                self.showConnectionError(execute["error"]["connection"])
                self.hide()
                self.close()
                return True
            elif execute["error"]["format"]:
                self.showConnectionError(execute["error"]["format"])
                self.close()
                return True
            elif execute["error"]["auth"]:
                if openAuth:
                    self.toAuth(execute["error"]["auth"])
                    return True
                return False
        return False

    @classmethod
    def getUserName(cls, name, username, access):
        if access == "Admin":
            name = f"""<p style="vertical-align: middle;"><span style="{cls.nameStyle}">{name}</span>
                        <span style="{cls.accessStyle}"> ({access})</span><br>"""
        else:
            name = f"""<p style="vertical-align: middle;"><span style="{cls.nameStyle}"</span><br>"""
        login = f"""<span style="{cls.usernameStyle}">@{username}</span></p>"""
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
                icon.addFile(":icons/icons/MoreBlack", QSize(), QIcon.Normal)
                watched.setIcon(icon)
                return True

            elif event.type() == QEvent.Type.HoverLeave:

                icon = QIcon()
                icon.addFile(":icons/icons/MoreGrey.svg", QSize(), QIcon.Normal)
                watched.setIcon(icon)
                return True

        elif watched == self.ui.button_PostLike:

            if event.type() == QEvent.Type.MouseButtonPress:
                self.setReaction(isLike=True)
                return True

        elif watched == self.ui.button_PostDislike:

            if event.type() == QEvent.Type.MouseButtonPress:
                self.setReaction(isDislike=True)
                return True

        return False

    def setPost(self):

        execute = self.__fileManager.getFilePath(self.userImageId)
        if self.isError(execute):
            return

        userImagePath = execute["data"]

        execute = self.__postTools.checkReaction(self.postId)
        if self.isError(execute, openAuth=False):
            return

        reaction = execute["data"]
        if reaction == "like":
            self.ui.button_PostLike.setIcon(self.buttonsReactionDict["like"][True])
            self.ui.button_PostLike.setChecked(True)
        elif reaction == "dislike":
            self.ui.button_PostDislike.setIcon(self.buttonsReactionDict["dislike"][True])
            self.ui.button_PostDislike.setChecked(True)

        name = self.getUserName(self.name, self.username, self.access)
        self.ui.textBrowser_UserName.setText(name)

        text = self.getText(self.postText)
        self.ui.textBrowser_PostText.setText(text)

        time = self.getPostData(self.postTime)
        self.ui.label_PostData.setText(time)

        likes = self.getLikes(self.likes)
        self.ui.label_Likes.setText(likes)

        dislikes = self.getDislikes(self.dislikes)
        self.ui.label_Dislikes.setText(dislikes)

        if self.comments:
            comments = self.getComments(len(self.comments))
        else:
            comments = self.getComments(0)
        self.ui.label_Comments.setText(comments)

        photo = ProfilePictureFrame(userImagePath, 40, 40, 20, shadowOffset=0, hoverOn=True)
        photo.setToolTip("@" + self.username)
        photo.mouseClickedSignal.connect(self.openUserAccountPage)
        self.ui.layout_userName.insertWidget(0, photo)

    def setReaction(self, isLike: bool = False, isDislike: bool = False):

        execute = self.__postTools.createReaction(post_id=self.postId, is_like=isLike, is_dislike=isDislike)
        if self.isError(execute):
            return

        checked = execute["data"]

        self.ui.button_PostLike.setIcon(self.buttonsReactionDict["like"][checked["like"]["set"]])
        self.ui.button_PostDislike.setIcon(self.buttonsReactionDict["dislike"][checked["dislike"]["set"]])

        self.likes = checked["like"]["count"]
        likes = self.getLikes(self.likes)
        self.ui.label_Likes.setText(likes)

        self.dislikes = checked["dislike"]["count"]
        dislikes = self.getDislikes(self.dislikes)
        self.ui.label_Dislikes.setText(dislikes)

    def openUserAccountPage(self):

        pass

    def followUser(self):

        pass

    def reportUser(self):

        pass

    def deletePost(self):

        pass

    def showConnectionError(self, error: str):

        self.connectionErrorSignal.emit(error)

    def toAuth(self, error: str):

        self.authErrorSignal.emit(error)
