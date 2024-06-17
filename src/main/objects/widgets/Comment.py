from PySide6.QtCore import QSize, Qt, QEvent, Signal
from PySide6.QtGui import QIcon, QFontDatabase, QFont, QColor, QAction
from PySide6.QtWidgets import QWidget, QGraphicsDropShadowEffect, QMenu, QMainWindow

from src.main.gui.design.comment import Ui_form_Comment
from src.main.objects.server.FileManager import FileManager
from src.main.objects.server.PostTools import PostTools
from src.main.objects.server.UserInfo import CurrentUser
from src.main.objects.widgets import ProfilePictureFrame


class Comment(Ui_form_Comment, QWidget):
    nameStyle = ("font-size:14px;"
                 "font-weight:800")

    usernameStyle = ("color:rgb(184,191,195);"
                     "font-size:14px;"
                     "font-weight:350")

    accessStyle = ("color:rgb(184,191,195);"
                   "font-size:14px;"
                   "font-weight:550")

    commentDataStyle = ("color:rgb(184,191,195);"
                        "font-size:13px;"
                        "font-weight:350")

    commentReactionsStyle_1 = ("font-size:13px;"
                               "font-weight:800")

    commentReactionsStyle_2 = ("color:rgb(184,191,195);"
                               "font-size:13px;"
                               "font-weight:350")

    commentTextStyle = ("font-size:13px;"
                        "font-weight:350")

    connectionErrorSignal = Signal(str)
    formatErrorSignal = Signal(str)
    authErrorSignal = Signal(str)
    openUserPageSignal = Signal(int)
    reportUserSignal = Signal(dict)
    followUserSignal = Signal(str)
    unfollowUserSignal = Signal(str)
    deleteCommentSignal = Signal(int)

    def __init__(self, commentInfo: dict, postTools: PostTools, currentUser: CurrentUser,
                 fileManager: FileManager, currentUserAccess: str = None, currentUserId: int = None):
        super(Ui_form_Comment, self).__init__()
        self.ui = Ui_form_Comment()
        self.ui.setupUi(self)

        self.__postTools = postTools
        self.__currentUser = currentUser
        self.__fileManager = fileManager

        self.menuParentStyle = QMainWindow()
        self.buttonsReactionDict = {}

        self.commentInfo = commentInfo
        self.commentId = commentInfo["comment_id"]
        self.userId = commentInfo["user_id"]
        self.commentText = commentInfo["comment_text"]
        self.likes = commentInfo["likes"]
        self.userIsFollowing = commentInfo["is_following"]
        self.dislikes = commentInfo["dislikes"]
        self.commentTime = commentInfo["comment_time"]
        self.username = commentInfo["username"]
        self.name = commentInfo["name"]
        self.access = commentInfo["access"]
        self.userImageId = commentInfo["image_id"]

        self.currentUserAccess = currentUserAccess
        self.currentUserId = currentUserId

        self.__initSetup()
        self.__setIconsSVG()
        self.__setMyFont()
        self.__setShadow()

        self.setComment()

    def __setIconsSVG(self):

        icon_More = QIcon()
        icon_More.addFile(":icons/icons/MoreGrey.svg", QSize(), QIcon.Normal)
        self.ui.button_More.setIcon(icon_More)
        self.ui.button_More.setIconSize(QSize(18, 18))

        icon_Like = QIcon()
        icon_Like.addFile(":icons/icons/Like.svg", QSize(), QIcon.Normal)
        self.ui.button_CommentLike.setIcon(icon_Like)
        self.ui.button_CommentLike.setIconSize(QSize(20, 20))

        icon_LikeSelected = QIcon()
        icon_LikeSelected.addFile(":icons/icons/LikeSelected.svg", QSize(), QIcon.Normal)

        icon_Dislike = QIcon()
        icon_Dislike.addFile(":icons/icons/Dislike.svg", QSize(), QIcon.Normal)
        self.ui.button_CommentDislike.setIcon(icon_Dislike)
        self.ui.button_CommentDislike.setIconSize(QSize(16, 16))

        icon_DislikeSelected = QIcon()
        icon_DislikeSelected.addFile(":icons/icons/DislikeSelected.svg", QSize(), QIcon.Normal)

        self.buttonsReactionDict = {"like": {True: icon_LikeSelected, False: icon_Like},
                                    "dislike": {True: icon_DislikeSelected, False: icon_Dislike}}

    def __initSetup(self):

        self.setAttribute(Qt.WidgetAttribute.WA_Hover)

        self.setWindowFlags(Qt.Window | Qt.FramelessWindowHint | Qt.WindowMinMaxButtonsHint)

        self.ui.textBrowser_UserName.document().setDocumentMargin(0)
        self.ui.textBrowser_UserName.setStyleSheet("QTextBrowser { margin-top: 3px; }")
        self.ui.textBrowser_CommentText.document().setDocumentMargin(0)
        self.ui.textBrowser_CommentText.setLineWrapColumnOrWidth(0)
        self.ui.textBrowser_CommentText.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.ui.textBrowser_CommentText.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)

        self.ui.button_More.installEventFilter(self)
        self.ui.textBrowser_UserName.installEventFilter(self)
        self.ui.button_CommentDislike.installEventFilter(self)
        self.ui.button_CommentLike.installEventFilter(self)

        self.ui.button_More.setToolTip("More")
        self.ui.button_CommentDislike.setToolTip("Dislike")
        self.ui.button_CommentLike.setToolTip("Like")

        self.setMore()

    def __setMyFont(self):

        fontId = QFontDatabase.addApplicationFont(":fonts/fonts/Roboto/Roboto-Regular.ttf")
        families = QFontDatabase.applicationFontFamilies(fontId)
        self.fontRegular = QFont(families[0])

        self.ui.textBrowser_UserName.setFont(self.fontRegular)
        self.ui.textBrowser_CommentText.setFont(self.fontRegular)
        self.ui.label_CommentData.setFont(self.fontRegular)
        self.ui.label_Likes.setFont(self.fontRegular)
        self.ui.label_Dislikes.setFont(self.fontRegular)

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
    def getPostData(cls, commentData):
        data = f"""<p style="{cls.commentDataStyle}">{commentData}</p>"""
        return data

    @classmethod
    def getLikes(cls, commentLikes):
        likes = f"""<p><span style="{cls.commentReactionsStyle_1}">{commentLikes} </span>
                    <span style="{cls.commentReactionsStyle_2}">Likes</span></p>"""
        return likes

    @classmethod
    def getDislikes(cls, commentDislikes):
        likes = f"""<p><span style="{cls.commentReactionsStyle_1}">{commentDislikes} </span>
                        <span style="{cls.commentReactionsStyle_2}">Dislikes</span></p>"""
        return likes

    @classmethod
    def getText(cls, commentText):
        text = f"""<p style="{cls.commentTextStyle}">{commentText}</p>"""
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

        elif watched == self.ui.button_CommentLike:

            if event.type() == QEvent.Type.MouseButtonPress:
                self.setReaction(isLike=True)
                return True

        elif watched == self.ui.button_CommentDislike:

            if event.type() == QEvent.Type.MouseButtonPress:
                self.setReaction(isDislike=True)
                return True

        return False

    def setComment(self):

        execute = self.__fileManager.getFilePath(self.userImageId)
        if self.isError(execute):
            return

        userImagePath = execute["data"]

        execute = self.__postTools.checkReaction(comment_id=self.commentId)
        if self.isError(execute, openAuth=False):
            return

        reaction = execute["data"]
        if reaction == "like":
            self.ui.button_CommentLike.setIcon(self.buttonsReactionDict["like"][True])
            self.ui.button_CommentLike.setChecked(True)
        elif reaction == "dislike":
            self.ui.button_CommentDislike.setIcon(self.buttonsReactionDict["dislike"][True])
            self.ui.button_CommentDislike.setChecked(True)

        name = self.getUserName(self.name, self.username, self.access)
        self.ui.textBrowser_UserName.setText(name)

        text = self.getText(self.commentText)
        self.ui.textBrowser_CommentText.setText(text)

        time = self.getPostData(self.commentTime)
        self.ui.label_CommentData.setText(time)

        likes = self.getLikes(self.likes)
        self.ui.label_Likes.setText(likes)

        dislikes = self.getDislikes(self.dislikes)
        self.ui.label_Dislikes.setText(dislikes)

        photo = ProfilePictureFrame(userImagePath, 40, 40, 20, shadowOffset=0, hoverOn=True)
        photo.setToolTip("@" + self.username)
        photo.mouseClickedSignal.connect(self.__openUserAccountPage)
        self.ui.layout_userName.insertWidget(0, photo)

    def setReaction(self, isLike: bool = False, isDislike: bool = False):

        execute = self.__postTools.createReaction(comment_id=self.commentId, is_like=isLike, is_dislike=isDislike)
        if self.isError(execute):
            return

        checked = execute["data"]

        self.ui.button_CommentLike.setIcon(self.buttonsReactionDict["like"][checked["like"]["set"]])
        self.ui.button_CommentDislike.setIcon(self.buttonsReactionDict["dislike"][checked["dislike"]["set"]])

        self.likes = checked["like"]["count"]
        likes = self.getLikes(self.likes)
        self.ui.label_Likes.setText(likes)

        self.dislikes = checked["dislike"]["count"]
        dislikes = self.getDislikes(self.dislikes)
        self.ui.label_Dislikes.setText(dislikes)

    def setMore(self, report: bool = True, delete: bool = True):

        if self.ui.button_More.menu():
            menu_More = self.ui.button_More.menu()
            menu_More.clear()
        else:
            menu_More = QMenu(self.menuParentStyle)

        if not self.userIsFollowing and (self.currentUserId and (self.currentUserId != self.userId)):
            action_FollowUser = QAction(f"&Follow @{self.username}", self)
            action_FollowUser.triggered.connect(self.__followUser)
            menu_More.addAction(action_FollowUser)
        elif self.currentUserId and (self.currentUserId != self.userId):
            action_FollowUser = QAction(f"&Unfollow @{self.username}", self)
            action_FollowUser.triggered.connect(self.__unfollowUser)
            menu_More.addAction(action_FollowUser)

        if report:
            action_Report = QAction(f"&Report @{self.username}", self)
            action_Report.triggered.connect(self.__reportUser)
            menu_More.addAction(action_Report)

        if delete and ((self.currentUserAccess == "Admin") or self.currentUserId and (self.currentUserId == self.userId)):
            action_DeletePost = QAction(f"&Delete Comment", self)
            action_DeletePost.triggered.connect(self.__deleteComment)
            menu_More.addAction(action_DeletePost)

        self.ui.button_More.setMenu(menu_More)

    def __openUserAccountPage(self):

        self.openUserPageSignal.emit(self.userId)

    def __followUser(self):

        execute = self.__currentUser.followTo(self.userId)
        if self.isError(execute):
            return
        self.userIsFollowing = True
        self.setMore()
        self.followUserSignal.emit(self.username)

    def __unfollowUser(self):

        execute = self.__currentUser.unfollowTo(self.userId)
        if self.isError(execute):
            return
        self.userIsFollowing = False
        self.setMore()
        self.unfollowUserSignal.emit(self.username)

    def __reportUser(self):

        self.reportUserSignal.emit(self.commentInfo)

    def __deleteComment(self):

        self.deleteCommentSignal.emit(self.commentId)

    def showConnectionError(self, error: str):

        self.connectionErrorSignal.emit(error)

    def toAuth(self, error: str):

        self.authErrorSignal.emit(error)

