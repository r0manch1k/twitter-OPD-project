import os.path
import random
import sys
import math

from PySide6.QtCore import QSize, Qt, QEvent, Slot, QPoint, QPropertyAnimation, QEasingCurve
from PySide6.QtGui import QIcon, Qt, QFontDatabase, QFont, QAction, QWindow, QColor
from PySide6.QtWidgets import QMainWindow, QApplication, QMenu, QFileDialog, QWidget, QVBoxLayout, \
    QPushButton, QGraphicsDropShadowEffect, QButtonGroup, QStackedWidget, QHBoxLayout

from gui.design.main import Ui_MainWindow
from objects.ImageTools import ImageTools
from objects.forms import LogInForm, SignUpForm
from objects.server.Authorization import Authorization
from objects.server.DataBase import DataBase
from objects.server.FileManager import FileManager
from objects.server.UserInfo import CurrentUser, User
from src.main.objects.server.PostTools import PostTools
from src.main.objects.widgets import DragNDrop, ProfilePictureFrame, Post, CreatePost, InfoBar, GoUp, Comment, Advert, \
    CreateComment
from src.main.gui.resources import resources


class App(Ui_MainWindow, QMainWindow):
    widgetToIndexHome = {"home": 0, "account": 1, "edit": 2, "report": 3, "comments": 4, "user": 5}
    widgetToIndexAccountEdit = {"profile": 0, "privacy": 1, "chat": 2}
    widgetToIndexAccount = {"posts": 0, "follows": 1}
    widgetToIndexSideBar = {"apps": 0, "chat": 1, "notifications": 2}

    filenameHomeBackground = "tempHomeBackgroundFileName.png"
    filenameAccountPicture = "tempAccountPicture.png"
    filenameAccountEditProfilePicture = "tempAccountEditProfilePicture.png"
    filenameProfileBackground = "tempProfileBackground.png"
    filenameAccountTabsBackground = "tempAccountTabsBackgroundFileName.png"
    filenameReportBackground = "tempReportBackgroundFileName.png"

    amountMaximumNameSymbols = 20
    amountMaximumUsernameSymbols = 32
    amountMaximumAboutSymbols = 70

    amountPostsOnPage = 10
    amountCommentsOnPage = 10

    advertOn = True

    def __init__(self):
        super(Ui_MainWindow, self).__init__()

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.__db = DataBase()
        self.__auth = Authorization()
        self.__currentUser = CurrentUser()
        self.__fileManager = FileManager()
        self.__postTools = PostTools()

        self.currentUserId = None
        self.currentUserAccess = None
        self.currentPostInfo = None

        self.logInForm = None
        self.signUpForm = None
        self.postCreateWidget = None
        self.commentCreateWidget = None
        self.errorBar = None
        self.goUpWidget = GoUp(self)

        self.flagAccountEditPhotoReset = False
        self.flagAccountEditPhotoSet = False
        self.flagAccountAboutReset = False

        self.dictButtonsSideBarIcons = {}
        self.listPosts = []
        self.listComments = []
        self.groupButtonsPostsPages = QButtonGroup()
        self.groupButtonsCommentsPages = QButtonGroup()
        self.reportInfo = None

        self.pathHomeBg = None
        self.pathAccountBg = None

        self.pageAnimation = None

        self.fontThin = None
        self.fontMedium = None
        self.fontRegular = None
        self.fontBold = None

        self.__setIconsSVG()
        self.__setMyFont()
        self.__initSetup()
        self.__setShadow()

        self.setHomePage()

    def __setIconsSVG(self):

        # Lets Light Line Interface Icons Collection:
        # https://www.svgrepo.com/collection/lets-light-line-interface-icons/8

        icon_Logo = QIcon()
        icon_Logo.addFile(":icons/icons/Logo.svg", QSize(), QIcon.Normal)
        self.ui.button_Logo.setIcon(icon_Logo)
        self.ui.button_Logo.setIconSize(QSize(60, 40))

        icon_Apps = QIcon()
        icon_Apps.addFile(":icons/icons/Apps.svg", QSize(), QIcon.Normal)
        self.ui.button_Apps.setIcon(icon_Apps)
        self.ui.button_Apps.setIconSize(QSize(22, 22))

        icon_Chat = QIcon()
        icon_Chat.addFile(":icons/icons/Chat.svg", QSize(), QIcon.Normal)
        self.ui.button_Chat.setIcon(icon_Chat)
        self.ui.button_Chat.setIconSize(QSize(30, 30))

        icon_Notifications = QIcon()
        icon_Notifications.addFile(":icons/icons/Notifications.svg", QSize(), QIcon.Normal)
        self.ui.button_Notifications.setIcon(icon_Notifications)
        self.ui.button_Notifications.setIconSize(QSize(30, 30))

        icon_Account = QIcon()
        icon_Account.addFile(":icons/icons/Account.svg", QSize(), QIcon.Normal)
        self.ui.button_Account.setIcon(icon_Account)
        self.ui.button_Account.setIconSize(QSize(30, 30))

        icon_FilterPosts = QIcon()
        icon_FilterPosts.addFile(":icons/icons/FilterPosts.svg", QSize(), QIcon.Normal)
        self.ui.button_HomeFilterPosts.setIcon(icon_FilterPosts)
        self.ui.button_HomeFilterPosts.setIconSize(QSize(20, 20))

        icon_AccountPhotoAdd = QIcon()
        icon_AccountPhotoAdd.addFile(":icons/icons/AccountPhotoAdd.svg", QSize(), QIcon.Normal)

        self.ui.button_AccountEditPhotoAdd.setIcon(icon_AccountPhotoAdd)
        self.ui.button_AccountEditPhotoAdd.setIconSize(QSize(30, 30))

        icon_AccountEdit = QIcon()
        icon_AccountEdit.addFile(":icons/icons/AccountEdit.svg", QSize(), QIcon.Normal)
        self.ui.button_AccountEdit.setIcon(icon_AccountEdit)
        self.ui.button_AccountEdit.setIconSize(QSize(25, 25))

        icon_AccountExit = QIcon()
        icon_AccountExit.addFile(":icons/icons/AccountExitBlack.svg", QSize(), QIcon.Normal)
        self.ui.button_AccountExit.setIcon(icon_AccountExit)
        self.ui.button_AccountExit.setIconSize(QSize(22, 22))

        icon_AccountExitNo = QIcon()
        icon_AccountExitNo.addFile(":icons/icons/AccountExitNoBlack.svg", QSize(), QIcon.Normal)
        self.ui.button_AccountExitNo.setIcon(icon_AccountExitNo)
        self.ui.button_AccountExitNo.setIconSize(QSize(25, 25))

        icon_AccountExitYes = QIcon()
        icon_AccountExitYes.addFile(":icons/icons/AccountExitYesBlack.svg", QSize(), QIcon.Normal)
        self.ui.button_AccountExitYes.setIcon(icon_AccountExitYes)
        self.ui.button_AccountExitYes.setIconSize(QSize(25, 25))

        icon_AccountEditPhotoDelete = QIcon()
        icon_AccountEditPhotoDelete.addFile(":icons/icons/AccountEditPhotoDeleteBlack.svg", QSize(),
                                            QIcon.Normal)
        self.ui.button_AccountEditPhotoDelete.setIcon(icon_AccountEditPhotoDelete)
        self.ui.button_AccountEditPhotoDelete.setIconSize(QSize(30, 30))

        self.ui.button_AccountEditAboutDelete.setIcon(icon_AccountEditPhotoDelete)
        self.ui.button_AccountEditAboutDelete.setIconSize(QSize(20, 20))

        icon_AppsDisabled = QIcon()
        icon_AppsDisabled.addFile(":icons/icons/AppsDisabled.svg", QSize(), QIcon.Normal)

        icon_NotificationsDisabled = QIcon()
        icon_NotificationsDisabled.addFile(":icons/icons/NotificationsDisabled.svg", QSize(), QIcon.Normal)

        icon_ChatDisabled = QIcon()
        icon_ChatDisabled.addFile(":icons/icons/ChatDisabled.svg", QSize(), QIcon.Normal)

        self.dictButtonsSideBarIcons["apps"] = {True: icon_Apps, False: icon_AppsDisabled}
        self.dictButtonsSideBarIcons["notifications"] = {True: icon_Notifications, False: icon_NotificationsDisabled}
        self.dictButtonsSideBarIcons["chat"] = {True: icon_Chat, False: icon_ChatDisabled}

        icon_ReportBack = QIcon()
        icon_ReportBack.addFile(":icons/icons/AuthBack.svg", QSize(), QIcon.Normal)
        self.ui.button_ReportBack.setIcon(icon_ReportBack)
        self.ui.button_ReportBack.setIconSize(QSize(30, 30))

        icon_CommentsBack = QIcon()
        icon_CommentsBack.addFile(":icons/icons/AuthBack.svg", QSize(), QIcon.Normal)
        self.ui.button_CommentsBack.setIcon(icon_CommentsBack)
        self.ui.button_CommentsBack.setIconSize(QSize(30, 30))

    def __initSetup(self):

        self.ui.stacked_Pages.setCurrentIndex(self.widgetToIndexHome["home"])
        self.ui.stacked_SideBar.setCurrentIndex(self.widgetToIndexSideBar["apps"])

        for button in self.ui.buttonGroup_MainTabs.buttons():
            button.clicked.connect(self.switchPage)
        self.ui.button_AccountEdit.clicked.connect(self.switchPage)
        for button in self.ui.buttonGroup_AccountEditTabs.buttons():
            button.clicked.connect(self.switchPage)

        self.goUpWidget.setHidden(True)
        self.ui.label_HomeSign.setHidden(True)
        self.ui.frame_SideBarChat.setHidden(True)
        self.ui.frame_SideBarNotifications.setHidden(True)
        self.ui.frame_AccountExitConfirmation.setHidden(True)
        self.ui.frame_AccountEditButtonsContainer.setHidden(True)

        self.ui.button_Apps.setChecked(True)
        self.ui.frame_SideBarApps.setMinimumWidth(350)
        self.ui.frame_SideBarChat.setMinimumWidth(350)
        self.ui.frame_SideBarNotifications.setMinimumWidth(350)
        self.ui.line_AccountEditName.setMaxLength(self.amountMaximumNameSymbols)
        self.ui.label_AccountEditNameSymbols.setText(f"There are {self.amountMaximumNameSymbols} characters left.")
        self.ui.label_AccountEditAboutSymbols.setText(f"There are {self.amountMaximumAboutSymbols} characters left.")

        self.ui.line_SearchBar.installEventFilter(self)
        self.ui.button_AccountExit.installEventFilter(self)
        self.ui.line_AccountEditName.installEventFilter(self)
        self.ui.button_AccountExitNo.installEventFilter(self)
        self.ui.button_AccountExitYes.installEventFilter(self)
        self.ui.line_AccountEditAbout.installEventFilter(self)
        self.ui.line_AccountEditUsername.installEventFilter(self)
        self.ui.button_AccountEditPhotoDelete.installEventFilter(self)
        self.ui.button_AccountEditAboutDelete.installEventFilter(self)

        self.goUpWidget.move(
            QPoint(self.ui.scrollArea_HomePosts.size().width() // 2 - self.goUpWidget.size().width() // 2,
                   self.size().height()))
        self.ui.scrollArea_HomePosts.verticalScrollBar().valueChanged.connect(self.setGoUpPosition)
        self.ui.scrollArea_User.verticalScrollBar().valueChanged.connect(self.setGoUpPosition)
        self.ui.scrollArea_Comments.verticalScrollBar().valueChanged.connect(self.setGoUpPosition)

        self.ui.button_Chat.clicked.connect(self.switchPage)
        self.ui.button_Apps.clicked.connect(self.switchPage)
        self.ui.button_Report.clicked.connect(self.reportUser)
        self.ui.button_SortByHot.clicked.connect(self.sortByHot)
        self.ui.button_SortByTime.clicked.connect(self.sortByTime)
        self.ui.button_ReportBack.clicked.connect(self.switchPage)
        self.goUpWidget.clickedSignal.connect(self.animationPageUp)
        self.ui.button_AppsAccount.clicked.connect(self.switchPage)
        self.ui.button_SortByLikes.clicked.connect(self.sortByLikes)
        self.ui.button_CommentsBack.clicked.connect(self.switchPage)
        self.ui.button_Notifications.clicked.connect(self.switchPage)
        self.ui.button_AccountExitYes.clicked.connect(self.switchPage)
        self.ui.stacked_Pages.currentChanged.connect(self.setGoUpPosition)
        self.ui.button_SortByDislikes.clicked.connect(self.sortByDislikes)
        self.ui.button_SortByComments.clicked.connect(self.sortByComments)
        self.ui.button_AccountEditAboutDelete.clicked.connect(self.deleteAbout)
        self.ui.button_AccountEditProfileSave.clicked.connect(self.saveProfileChanges)
        self.ui.button_AccountEditProfileCancel.clicked.connect(self.setAccountEditPage)
        self.ui.button_AccountEditPhotoDelete.clicked.connect(self.setAccountImageToDefault)
        self.ui.button_AccountEditPhotoAdd.clicked.connect(self.setAccountEditImageFromFile)

        self.ui.page_Apps.setAttribute(Qt.WidgetAttribute.WA_TranslucentBackground)
        self.ui.page_Chat.setAttribute(Qt.WidgetAttribute.WA_TranslucentBackground)
        self.ui.stacked_Posts.setAttribute(Qt.WidgetAttribute.WA_TranslucentBackground)
        self.ui.frame_Report_1.setAttribute(Qt.WidgetAttribute.WA_TranslucentBackground)
        self.ui.label_HomeSign.setAttribute(Qt.WidgetAttribute.WA_TranslucentBackground)
        self.ui.frame_Report_2.setAttribute(Qt.WidgetAttribute.WA_TranslucentBackground)
        self.ui.frame_ReportBack.setAttribute(Qt.WidgetAttribute.WA_TranslucentBackground)
        self.ui.stacked_Comments.setAttribute(Qt.WidgetAttribute.WA_TranslucentBackground)
        self.ui.frame_AccountInfo.setAttribute(Qt.WidgetAttribute.WA_TranslucentBackground)
        self.ui.frame_CommentsBack.setAttribute(Qt.WidgetAttribute.WA_TranslucentBackground)
        self.ui.page_Notifications.setAttribute(Qt.WidgetAttribute.WA_TranslucentBackground)
        self.ui.frame_SetPostsPage.setAttribute(Qt.WidgetAttribute.WA_TranslucentBackground)
        self.ui.label_CommentsSign.setAttribute(Qt.WidgetAttribute.WA_TranslucentBackground)
        self.ui.label_AccountAbout.setAttribute(Qt.WidgetAttribute.WA_TranslucentBackground)
        self.ui.scrollArea_Comments.setAttribute(Qt.WidgetAttribute.WA_TranslucentBackground)
        self.ui.frame_PostContainer.setAttribute(Qt.WidgetAttribute.WA_TranslucentBackground)
        self.ui.label_AccountStatus.setAttribute(Qt.WidgetAttribute.WA_TranslucentBackground)
        self.ui.scrollArea_HomePosts.setAttribute(Qt.WidgetAttribute.WA_TranslucentBackground)
        self.ui.frame_SetCommentPage.setAttribute(Qt.WidgetAttribute.WA_TranslucentBackground)
        self.ui.frame_AccountButtons.setAttribute(Qt.WidgetAttribute.WA_TranslucentBackground)
        self.ui.frame_ReportContainer.setAttribute(Qt.WidgetAttribute.WA_TranslucentBackground)
        self.ui.frame_AccountLabels_1.setAttribute(Qt.WidgetAttribute.WA_TranslucentBackground)
        self.ui.label_AccountNickname.setAttribute(Qt.WidgetAttribute.WA_TranslucentBackground)
        self.ui.scrollAreaWidget_Posts.setAttribute(Qt.WidgetAttribute.WA_TranslucentBackground)
        self.ui.scrollArea_CommentsPost.setAttribute(Qt.WidgetAttribute.WA_TranslucentBackground)
        self.ui.scrollAreaWidget_Comments.setAttribute(Qt.WidgetAttribute.WA_TranslucentBackground)
        self.ui.label_AccountInformationID.setAttribute(Qt.WidgetAttribute.WA_TranslucentBackground)
        self.ui.scrollAreaWidget_CommentsPost.setAttribute(Qt.WidgetAttribute.WA_TranslucentBackground)
        self.ui.frame_AccountExitConfirmation.setAttribute(Qt.WidgetAttribute.WA_TranslucentBackground)
        self.ui.label_AccountInformationAccess.setAttribute(Qt.WidgetAttribute.WA_TranslucentBackground)
        self.ui.frame_AccountInformationContainer.setAttribute(Qt.WidgetAttribute.WA_TranslucentBackground)

        self.ui.scrollArea_HomePosts.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.ui.scrollArea_Comments.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.ui.scrollArea_CommentsPost.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)

        self.ui.textEdit_ReportText.document().setDocumentMargin(0)

        menu_FilterPosts = QMenu(self)
        action_Sort = QMenu("&Sort By", self)

        action_SortByTime = QAction("&New", self)
        action_SortByTime.setShortcut("Ctrl+N")
        action_SortByTime.triggered.connect(self.sortByTime)
        action_Sort.addAction(action_SortByTime)

        action_SortByLikes = QAction("&Likes", self)
        action_SortByLikes.setShortcut("Ctrl+N")
        action_SortByLikes.triggered.connect(self.sortByLikes)
        action_Sort.addAction(action_SortByLikes)

        action_SortByDislikes = QAction("&Dislikes", self)
        action_SortByDislikes.setShortcut("Ctrl+N")
        action_SortByDislikes.triggered.connect(self.sortByDislikes)
        action_Sort.addAction(action_SortByDislikes)

        action_SortByComments = QAction("&Comments", self)
        action_SortByComments.setShortcut("Ctrl+N")
        action_SortByComments.triggered.connect(self.sortByComments)
        action_Sort.addAction(action_SortByComments)

        action_SortByLikes = QAction("&Hot", self)
        action_SortByLikes.setShortcut("Ctrl+H")
        action_SortByLikes.triggered.connect(self.sortByHot)
        action_Sort.addAction(action_SortByLikes)

        menu_FilterPosts.addMenu(action_Sort)
        self.ui.button_HomeFilterPosts.setMenu(menu_FilterPosts)

        pathReportBg = ImageTools.getPictureForWidget(self.ui.page_Report.size().width(),
                                                      self.ui.page_Report.size().height(), 100, os.path.abspath(
                "gui/resources/images/reportBg.png"),
                                                      self.__fileManager.tempPath,
                                                      self.filenameReportBackground)
        self.ui.page_Report.setStyleSheet(
            f"QWidget#page_Report {{border-image: url('{pathReportBg}') 0 0 0 0  stretch stretch}}")

    def __setMyFont(self):

        fontId = QFontDatabase.addApplicationFont(":/fonts/fonts/Roboto/Roboto-Regular.ttf")
        families = QFontDatabase.applicationFontFamilies(fontId)
        self.fontRegular = QFont(families[0])

        fontId = QFontDatabase.addApplicationFont(":/fonts/fonts/Roboto/Roboto-Thin.ttf")
        families = QFontDatabase.applicationFontFamilies(fontId)
        self.fontThin = QFont(families[0])

        fontId = QFontDatabase.addApplicationFont(":/fonts/fonts/Great_Vibes/GreatVibes-Regular.ttf")
        families = QFontDatabase.applicationFontFamilies(fontId)
        self.fontCursive = QFont(families[0])

        self.ui.label_AccountAbout.setFont(self.fontCursive)
        self.ui.label_AccountNickname.setFont(self.fontRegular)
        self.ui.label_AccountInformationID.setFont(self.fontRegular)
        self.ui.label_AccountInformationAccess.setFont(self.fontRegular)

    def __setShadow(self):

        self.__shadowBlurRadius = 10.0
        self.__borderWidth = 1
        self.__shadowMargin = 0
        self.__borderRadius = 12.0

        self.__effectSideBar = QGraphicsDropShadowEffect()
        self.__effectSideBar.setBlurRadius(self.__shadowBlurRadius)
        self.__effectSideBar.setColor(QColor(0, 0, 0, 127))
        self.__effectSideBar.setOffset(5.0)
        self.ui.stacked_SideBar.setGraphicsEffect(self.__effectSideBar)
        self.ui.stacked_SideBar.repaint()

        self.__effectReport = QGraphicsDropShadowEffect()
        self.__effectReport.setBlurRadius(self.__shadowBlurRadius)
        self.__effectReport.setColor(QColor(0, 0, 0, 127))
        self.__effectReport.setOffset(5.0)
        self.ui.frame_Report.setGraphicsEffect(self.__effectReport)
        self.ui.frame_Report.repaint()

        self.__effectReportBack = QGraphicsDropShadowEffect()
        self.__effectReportBack.setBlurRadius(self.__shadowBlurRadius)
        self.__effectReportBack.setColor(QColor(0, 0, 0, 127))
        self.__effectReportBack.setOffset(3.0)
        self.ui.button_ReportBack.setGraphicsEffect(self.__effectReportBack)
        self.ui.button_ReportBack.repaint()

        self.__effectCommentsBack = QGraphicsDropShadowEffect()
        self.__effectCommentsBack.setBlurRadius(self.__shadowBlurRadius)
        self.__effectCommentsBack.setColor(QColor(0, 0, 0, 127))
        self.__effectCommentsBack.setOffset(3.0)
        self.ui.button_CommentsBack.setGraphicsEffect(self.__effectCommentsBack)
        self.ui.button_CommentsBack.repaint()

        self.__effectAccountEdit = QGraphicsDropShadowEffect()
        self.__effectAccountEdit.setBlurRadius(self.__shadowBlurRadius)
        self.__effectAccountEdit.setColor(QColor(0, 0, 0, 127))
        self.__effectAccountEdit.setOffset(3.0)
        self.ui.button_AccountEdit.setGraphicsEffect(self.__effectAccountEdit)
        self.ui.button_AccountEdit.repaint()

        self.__effectAccountExit = QGraphicsDropShadowEffect()
        self.__effectAccountExit.setBlurRadius(self.__shadowBlurRadius)
        self.__effectAccountExit.setColor(QColor(0, 0, 0, 127))
        self.__effectAccountExit.setOffset(3.0)
        self.ui.button_AccountExit.setGraphicsEffect(self.__effectAccountExit)
        self.ui.button_AccountExit.repaint()

        self.__effectAccountExitConfirmation = QGraphicsDropShadowEffect()
        self.__effectAccountExitConfirmation.setBlurRadius(self.__shadowBlurRadius)
        self.__effectAccountExitConfirmation.setColor(QColor(0, 0, 0, 127))
        self.__effectAccountExitConfirmation.setOffset(3.0)
        self.ui.frame_AccountExitConfirmation.setGraphicsEffect(self.__effectAccountExitConfirmation)
        self.ui.frame_AccountExitConfirmation.repaint()

        self.__effectAccountTabs = QGraphicsDropShadowEffect()
        self.__effectAccountTabs.setBlurRadius(self.__shadowBlurRadius)
        self.__effectAccountTabs.setColor(QColor(0, 0, 0, 127))
        self.__effectAccountTabs.setOffset(5.0)
        self.ui.frame_AccountTabs.setGraphicsEffect(self.__effectAccountTabs)
        self.ui.frame_AccountTabs.repaint()

        self.__effectAccountStackedTabs = QGraphicsDropShadowEffect()
        self.__effectAccountStackedTabs.setBlurRadius(self.__shadowBlurRadius)
        self.__effectAccountStackedTabs.setColor(QColor(0, 0, 0, 127))
        self.__effectAccountStackedTabs.setOffset(5.0)
        self.ui.stacked_AccountTabs.setGraphicsEffect(self.__effectAccountStackedTabs)
        self.ui.stacked_AccountTabs.repaint()

        self.__effectName = QGraphicsDropShadowEffect()
        self.__effectName.setBlurRadius(self.__shadowBlurRadius)
        self.__effectName.setColor(QColor(0, 0, 0, 127))
        self.__effectName.setOffset(3.0)
        self.ui.label_AccountNickname.setGraphicsEffect(self.__effectName)
        self.ui.label_AccountNickname.repaint()

        self.__effectStatus = QGraphicsDropShadowEffect()
        self.__effectStatus.setBlurRadius(self.__shadowBlurRadius)
        self.__effectStatus.setColor(QColor(0, 0, 0, 127))
        self.__effectStatus.setOffset(3.0)
        self.ui.label_AccountStatus.setGraphicsEffect(self.__effectStatus)
        self.ui.label_AccountStatus.repaint()

        self.__effectAbout = QGraphicsDropShadowEffect()
        self.__effectAbout.setBlurRadius(self.__shadowBlurRadius)
        self.__effectAbout.setColor(QColor(0, 0, 0, 127))
        self.__effectAbout.setOffset(2.0)
        self.ui.label_AccountAbout.setGraphicsEffect(self.__effectAbout)
        self.ui.label_AccountAbout.repaint()

    def eventFilter(self, watched, event):

        if watched == self.ui.button_AccountExitYes:

            if event.type() == QEvent.Type.HoverEnter:

                icon = QIcon()
                icon.addFile(":icons/icons/AccountExitYesWhite.svg", QSize(25, 25), QIcon.Normal)
                watched.setIcon(icon)
                watched.setStyleSheet("background-color: rgb(255, 0, 0);")
                return True

            elif event.type() == QEvent.Type.HoverLeave:

                icon = QIcon()
                icon.addFile(":icons/icons/AccountExitYesBlack.svg", QSize(25, 25), QIcon.Normal)
                watched.setIcon(icon)
                watched.setStyleSheet("background-color: white;")
                return True

        elif watched == self.ui.button_AccountExitNo:

            if event.type() == QEvent.Type.HoverEnter:

                icon = QIcon()
                icon.addFile(":icons/icons/AccountExitNoWhite.svg", QSize(25, 25), QIcon.Normal)
                watched.setIcon(icon)
                watched.setStyleSheet("background-color: #208b3a;")
                return True

            elif event.type() == QEvent.Type.HoverLeave:

                icon = QIcon()
                icon.addFile(":icons/icons/AccountExitNoBlack.svg", QSize(25, 25), QIcon.Normal)
                watched.setIcon(icon)
                watched.setStyleSheet("background-color: white;")
                return True

        elif watched == self.ui.button_AccountExit:

            if event.type() == QEvent.Type.HoverEnter:

                icon = QIcon()
                icon.addFile(":icons/icons/AccountExitWhite.svg", QSize(22, 22), QIcon.Normal)
                watched.setIcon(icon)
                watched.setStyleSheet("background-color: rgb(255, 0, 0)")
                return True

            elif event.type() == QEvent.Type.HoverLeave:

                icon = QIcon()
                icon.addFile(":icons/icons/AccountExitBlack.svg", QSize(22, 22), QIcon.Normal)
                watched.setIcon(icon)
                watched.setStyleSheet("background-color: white;")
                return True

        elif watched == self.ui.button_AccountEditPhotoDelete:

            if event.type() == QEvent.Type.HoverEnter:

                icon = QIcon()
                icon.addFile(":icons/icons/AccountEditPhotoDeleteWhite.svg", QSize(30, 30), QIcon.Normal)
                watched.setIcon(icon)
                watched.setStyleSheet("background-color: rgb(240, 0, 0)")
                return True

            elif event.type() == QEvent.Type.HoverLeave:

                icon = QIcon()
                icon.addFile(":icons/icons/AccountEditPhotoDeleteBlack.svg", QSize(30, 30), QIcon.Normal)
                watched.setIcon(icon)
                watched.setStyleSheet("background-color: rgb(229,235,238)")
                return True

        elif watched == self.ui.button_AccountEditAboutDelete:

            if event.type() == QEvent.Type.HoverEnter:

                icon = QIcon()
                icon.addFile(":icons/icons/AccountEditPhotoDeleteWhite.svg", QSize(20, 20), QIcon.Normal)
                watched.setIcon(icon)
                watched.setStyleSheet("background-color: rgb(240, 0, 0)")
                return True

            elif event.type() == QEvent.Type.HoverLeave:

                icon = QIcon()
                icon.addFile(":icons/icons/AccountEditPhotoDeleteBlack.svg", QSize(20, 20), QIcon.Normal)
                watched.setIcon(icon)
                watched.setStyleSheet("background-color: rgb(229,235,238)")
                return True

        elif watched == self.ui.line_SearchBar:

            if event.type() == QEvent.Type.HoverEnter:

                self.ui.frame_ButtonHomeFilterPosts.setStyleSheet("QFrame { background-color: rgb(226,231,233); }")

            elif event.type() == QEvent.Type.HoverLeave:

                self.ui.frame_ButtonHomeFilterPosts.setStyleSheet("QFrame { background-color: rgb(235, 237, 239); }")

        elif (watched == self.ui.line_AccountEditName or watched == self.ui.line_AccountEditUsername
              or watched == self.ui.line_AccountEditAbout):

            if event.type() == QEvent.Type.KeyRelease:

                if len(self.ui.line_AccountEditAbout.toPlainText()) - self.amountMaximumAboutSymbols == 1:
                    self.ui.line_AccountEditAbout.textCursor().deletePreviousChar()

                if len(self.ui.line_AccountEditAbout.toPlainText()) - self.amountMaximumAboutSymbols > 1:
                    self.ui.line_AccountEditAbout.setText("")

                self.ui.label_AccountEditNameSymbols.setText(
                    f"There is {self.amountMaximumNameSymbols - len(self.ui.line_AccountEditName.text())} "
                    f"characters left.")
                self.ui.label_AccountEditUsernameSymbols.setText(
                    f"There is {self.amountMaximumUsernameSymbols - len(self.ui.line_AccountEditUsername.text())} "
                    f"characters left.")
                self.ui.label_AccountEditAboutSymbols.setText(
                    f"There is {self.amountMaximumAboutSymbols - len(self.ui.line_AccountEditAbout.toPlainText())} "
                    f"characters left.")

                if (self.ui.line_AccountEditName.text() or self.ui.line_AccountEditAbout.toPlainText()
                        or self.ui.line_AccountEditUsername.text() or self.flagAccountEditPhotoSet
                        or self.flagAccountEditPhotoReset or self.flagAccountAboutReset):
                    self.setLabelAccountEditProfileWarning(show=True, save=False)
                    self.ui.frame_AccountEditButtonsContainer.setVisible(True)
                else:
                    self.setLabelAccountEditProfileWarning(show=False)
                    self.ui.frame_AccountEditButtonsContainer.setHidden(True)

        return False

    def keyPressEvent(self, event):

        if event.key() == Qt.Key.Key_Enter or event.key() == Qt.Key.Key_Return:

            key = self.ui.line_SearchBar.text()
            if key:
                self.searchByKey(key)

    @staticmethod
    def getTextHTML(text, color: str = "black", size: int = 28, weight: int = None, style: str = "normal") -> str:
        if weight:
            text = f"""<span style="color:{color};font-size:{size}px;font-weight:{weight};font-style:{style};
                ">{text}</span>"""
        else:
            text = f"""<span style="color:{color};font-size:{size}px;font-style:{style};">{text}</span>"""
        return text

    def getOnlineCircle(self, online: bool) -> str:
        if online:
            onlineCircle = self.getTextHTML("●", "rgb(5,168,22)", 18)
        else:
            onlineCircle = self.getTextHTML("●", "rgb(184,191,195)", 18)
        return onlineCircle

    @Slot(str)
    def showConnectionError(self, error: str):
        if self.errorBar is None or self.errorBar.isHidden():
            self.errorBar = InfoBar(self, error, error=True)
            self.errorBar.show()

    def isError(self, execute: dict) -> bool:
        if execute["error"]:
            if execute["error"]["connection"]:
                self.showConnectionError(execute["error"]["connection"])
            elif execute["error"]["format"]:
                self.showConnectionError(execute["error"]["format"])
            elif execute["error"]["auth"]:
                self.changeForm("login", QPoint(self.pos().x(), self.pos().y()))
            return True
        return False

    def setHomeSign(self, text=None):
        if text:
            self.ui.label_HomeSign.setVisible(True)
            self.ui.label_HomeSign.setText(text)
        else:
            self.ui.label_HomeSign.setVisible(False)

    def setGoUpPosition(self, value: int):

        if (self.ui.stacked_Pages.currentIndex() != self.widgetToIndexHome["home"]
                and self.ui.stacked_Pages.currentIndex() != self.widgetToIndexHome["user"]
                and self.ui.stacked_Pages.currentIndex() != self.widgetToIndexHome["comments"]):
            self.goUpWidget.setVisible(False)
            return

        self.goUpWidget.setVisible(True)

        x = None

        if ((self.ui.stacked_Pages.currentIndex() == self.widgetToIndexHome["home"])
                or (self.sender() == self.ui.scrollArea_HomePosts.verticalScrollBar())):
            x = (self.ui.scrollArea_HomePosts.pos().x() + self.ui.scrollArea_HomePosts.size().width()
                 - self.goUpWidget.size().width())

        elif ((self.ui.stacked_Pages.currentIndex() == self.widgetToIndexHome["user"])
              or (self.sender() == self.ui.scrollArea_User.verticalScrollBar())):
            x = (self.ui.scrollArea_User.pos().x() + self.ui.scrollArea_User.size().width()
                 - self.goUpWidget.size().width())

        elif ((self.ui.stacked_Pages.currentIndex() == self.widgetToIndexHome["comments"])
              or (self.sender() == self.ui.scrollArea_Comments.verticalScrollBar())):
            x = (self.ui.scrollArea_Comments.pos().x() + self.ui.scrollArea_Comments.size().width()
                 - self.goUpWidget.size().width())

        if value > 20 + self.goUpWidget.size().height():
            value = 20 + self.goUpWidget.size().height()

        self.goUpWidget.move(QPoint(x, self.size().height() - value))

    def updateOnline(self) -> bool:
        execute = self.__currentUser.updateOnline()
        return self.isError(execute)

    def chooseFile(self, rootDir: str, nameFilter: str) -> str:
        fileName, ok = QFileDialog.getOpenFileName(self, "Select a File", rootDir, nameFilter)
        if ok:
            return fileName

    def postCreated(self):
        self.refresh(homePage=True)
        bar = InfoBar(self, "Posted successfully!")
        bar.show()

    def postDeleted(self, postId: int):
        execute = self.__postTools.deletePost(postId)
        if self.isError(execute):
            return
        self.refresh(homePage=True)
        bar = InfoBar(self, "Deleted successfully!")
        bar.show()

    def commentCreated(self, postId: int):
        execute = self.__postTools.getPostsInfo([postId])
        if self.isError(execute):
            return
        self.currentPostInfo = execute["data"][0]
        self.refresh(commentsPage=True)
        bar = InfoBar(self, "Commented successfully!")
        bar.show()

    def commentDeleted(self, commentId: int):
        execute = self.__postTools.deleteComment(commentId)
        if self.isError(execute):
            return
        self.refresh(commentsPage=True)
        bar = InfoBar(self, "Deleted successfully!")
        bar.show()

    def userFollowed(self, username: str):
        pageLayout = self.ui.stacked_Posts.currentWidget().layout()
        for postIndex in range(pageLayout.count() - 1, -1, -1):
            if isinstance(pageLayout.itemAt(postIndex).widget(), Post):
                if pageLayout.itemAt(postIndex).widget().username == username:
                    pageLayout.itemAt(postIndex).widget().setMore(follow=False)
        bar = InfoBar(self, f"You follow @{username}!")
        bar.show()

    def userUnfollowed(self, username: str):
        pageLayout = self.ui.stacked_Posts.currentWidget().layout()
        for postIndex in range(pageLayout.count() - 1, -1, -1):
            if isinstance(pageLayout.itemAt(postIndex).widget(), Post):
                if pageLayout.itemAt(postIndex).widget().username == username:
                    pageLayout.itemAt(postIndex).widget().setMore(follow=True)
        bar = InfoBar(self, f"You unfollow @{username}!")
        bar.show()

    def animationPageUp(self):
        if self.ui.stacked_Pages.currentIndex() == self.widgetToIndexHome["home"]:
            scrollArea = self.ui.scrollArea_HomePosts

        elif self.ui.stacked_Pages.currentIndex() == self.widgetToIndexHome["user"]:
            scrollArea = self.ui.scrollArea_User

        elif self.ui.stacked_Pages.currentIndex() == self.widgetToIndexHome["comments"]:
            scrollArea = self.ui.scrollArea_Comments

        else:
            return

        if scrollArea.verticalScrollBar().value() == 0:
            return

        duration = int(math.log(scrollArea.verticalScrollBar().value(), 2) * 50)

        self.pageAnimation = QPropertyAnimation(scrollArea.verticalScrollBar(), b"value")
        self.pageAnimation.setStartValue(scrollArea.verticalScrollBar().value())
        self.pageAnimation.setDuration(duration)
        self.pageAnimation.setEasingCurve(QEasingCurve.Type.OutQuad)
        self.pageAnimation.setEndValue(0)
        self.pageAnimation.start()

    def setSideBarButtonEnabled(self, value: bool):
        if value:
            self.ui.button_Apps.setStyleSheet("QPushButton:checked { background-color: rgb(235, 237, 239); }")
            self.ui.button_Notifications.setStyleSheet("QPushButton:checked { background-color: rgb(235, 237, 239); }")
            self.ui.button_Chat.setStyleSheet("QPushButton:checked { background-color: rgb(235, 237, 239); }")
        else:
            self.ui.button_Apps.setStyleSheet("QPushButton:checked { background-color: white; }")
            self.ui.button_Notifications.setStyleSheet("QPushButton:checked { background-color: white; }")
            self.ui.button_Chat.setStyleSheet("QPushButton:checked { background-color: white; }")

        self.ui.button_Apps.setIcon(self.dictButtonsSideBarIcons["apps"][value])
        self.ui.button_Notifications.setIcon(self.dictButtonsSideBarIcons["notifications"][value])
        self.ui.button_Chat.setIcon(self.dictButtonsSideBarIcons["chat"][value])
        self.ui.button_Apps.setEnabled(value)
        self.ui.button_Notifications.setEnabled(value)
        self.ui.button_Chat.setEnabled(value)

    def switchPage(self):
        if self.sender() == self.ui.button_Logo:

            if not self.setHomePage():
                return
            self.goUpWidget.setHidden(False)
            self.setSideBarButtonEnabled(True)
            self.ui.line_SearchBar.setText("")
            self.ui.stacked_Pages.setCurrentIndex(self.widgetToIndexHome["home"])

        elif self.sender() == self.ui.button_Account or self.sender() == self.ui.button_AppsAccount:

            if not self.updateOnline:
                return

            if not self.setAccountPage():
                return

            self.goUpWidget.setHidden(True)
            self.setSideBarButtonEnabled(False)
            self.ui.button_AccountExitNo.setChecked(True)
            self.ui.button_AccountEdit.setVisible(True)
            self.ui.button_AccountEdit.setVisible(True)
            self.ui.line_SearchBar.setText("")
            self.ui.stacked_Pages.setCurrentIndex(self.widgetToIndexHome["account"])

        elif self.sender() == self.ui.button_AccountEdit:

            if not self.updateOnline:
                return
            if not self.setAccountEditPage():
                return
            self.goUpWidget.setHidden(True)
            self.ui.line_SearchBar.setText("")
            self.ui.stacked_Pages.setCurrentIndex(self.widgetToIndexHome["edit"])

        elif self.sender() == self.ui.button_AccountExitYes:

            if not self.logOut(openForm=False):
                return

            if not self.setHomePage():
                return False

            self.ui.button_Logo.setChecked(True)
            self.ui.line_SearchBar.setText("")
            self.ui.stacked_Pages.setCurrentIndex(self.widgetToIndexHome["home"])

        elif self.sender() == self.ui.button_Apps:

            self.ui.stacked_SideBar.setCurrentIndex(self.widgetToIndexSideBar["apps"])

        elif self.sender() == self.ui.button_Chat:

            self.ui.stacked_SideBar.setCurrentIndex(self.widgetToIndexSideBar["chat"])

        elif self.sender() == self.ui.button_Notifications:

            self.ui.stacked_SideBar.setCurrentIndex(self.widgetToIndexSideBar["notifications"])

        elif self.sender() == self.ui.button_AccountEditTabsProfile:

            if not self.updateOnline:
                return

            self.ui.stacked_AccountEditTabs.setCurrentIndex(self.widgetToIndexAccountEdit["profile"])

        elif self.sender() == self.ui.button_AccountEditTabsPrivacy:

            if not self.updateOnline:
                return

            self.ui.stacked_AccountEditTabs.setCurrentIndex(self.widgetToIndexAccountEdit["privacy"])

        elif self.sender() == self.ui.button_AccountEditTabsChat:

            if not self.updateOnline:
                return

            self.ui.stacked_AccountEditTabs.setCurrentIndex(self.widgetToIndexAccountEdit["chat"])

        elif self.sender() == self.ui.button_ReportBack:

            if not self.setHomePage():
                return
            self.goUpWidget.setHidden(False)
            self.setSideBarButtonEnabled(True)
            self.ui.line_SearchBar.setText("")
            self.ui.stacked_Pages.setCurrentIndex(self.widgetToIndexHome["home"])

        elif self.sender() == self.ui.button_CommentsBack:

            if not self.setHomePage():
                return
            self.goUpWidget.setHidden(False)
            self.ui.line_SearchBar.setText("")
            self.setSideBarButtonEnabled(True)
            self.ui.stacked_Pages.setCurrentIndex(self.widgetToIndexHome["home"])

    def openReportPage(self, reportInfo: dict):
        if not self.setReportPage(reportInfo):
            return
        self.goUpWidget.setHidden(True)
        self.ui.line_SearchBar.setText("")
        self.setSideBarButtonEnabled(False)
        self.ui.stacked_Pages.setCurrentIndex(self.widgetToIndexHome["report"])

    def openUserPage(self, userId: int):
        if not self.setUserPage(userId):
            return

        self.ui.scrollArea_User.verticalScrollBar().setValue(0)
        self.setSideBarButtonEnabled(False)
        self.ui.line_SearchBar.setText("")
        self.ui.stacked_Pages.setCurrentIndex(self.widgetToIndexHome["user"])

    def openCommentsPage(self, postInfo: dict):
        if not self.setCommentsPage(postInfo):
            return
        self.ui.scrollArea_Comments.verticalScrollBar().setValue(0)
        self.setSideBarButtonEnabled(False)
        self.ui.line_SearchBar.setText("")
        self.ui.stacked_Pages.setCurrentIndex(self.widgetToIndexHome["comments"])

    @staticmethod
    def addPage(stackedWidget: QStackedWidget, layoutMargins: tuple, buttonsLayout: QHBoxLayout,
                buttonGroup: QButtonGroup,
                methodSetPage):
        layout = QVBoxLayout()
        layout.setSpacing(20)
        layout.setContentsMargins(*layoutMargins)
        layout.setSizeConstraint(QVBoxLayout.SizeConstraint.SetMinimumSize)

        page = QWidget()
        page.setAttribute(Qt.WidgetAttribute.WA_TranslucentBackground)
        page.setLayout(layout)
        stackedWidget.insertWidget(stackedWidget.count() - 1, page)

        buttonPage = QPushButton(str(stackedWidget.count()))
        buttonPage.clicked.connect(methodSetPage)
        buttonPage.setCheckable(True)
        buttonGroup.addButton(buttonPage)
        if stackedWidget.count() == 1:
            buttonPage.setChecked(True)
        buttonsLayout.insertWidget(buttonsLayout.count() - 1, buttonPage)

    def setHomePage(self, sort_by_likes=False, sort_by_dislikes=False, sort_by_comments=False,
                    sort_by_all_reactions=False, search_by_key="") -> bool:

        self.ui.line_SearchBar.setText("")

        for postIndex in range(self.ui.layout_ScrollAreaPosts.count() - 1, -1, -1):
            if isinstance(self.ui.layout_ScrollAreaPosts.itemAt(postIndex).widget(), CreatePost):
                self.ui.layout_ScrollAreaPosts.itemAt(postIndex).widget().setHidden(True)
                self.ui.layout_ScrollAreaPosts.removeWidget(self.ui.layout_ScrollAreaPosts.itemAt(postIndex).widget())

        execute = self.__auth.checkAuthorization()
        if self.isError(execute):
            return False

        authorized = execute["data"]
        if authorized and not search_by_key:
            execute = self.__currentUser.access
            if self.isError(execute):
                return False
            self.currentUserAccess = execute["data"]

            execute = self.__currentUser.userID
            if self.isError(execute):
                return False

            self.currentUserId = execute["data"]
            self.postCreateWidget = self.getCreatePostWidget()
            if not self.postCreateWidget:
                return False
            self.postCreateWidget.errorSignal.connect(self.isError)
            self.postCreateWidget.postCreatedSignal.connect(self.postCreated)
            self.ui.layout_ScrollAreaPosts.insertWidget(0, self.postCreateWidget)

        if not (self.pathHomeBg and os.path.exists(self.pathHomeBg)):
            self.pathHomeBg = ImageTools.getPictureForWidget(self.ui.page_Home.size().width(),
                                                             self.ui.page_Home.size().height(),
                                                             0,
                                                             os.path.abspath(
                                                                 "gui/resources/images/homeBg.png"),
                                                             self.__fileManager.tempPath,
                                                             self.filenameHomeBackground)
        self.ui.page_Home.setStyleSheet(
            f"QWidget#page_Home {{border-image: url('{self.pathHomeBg}') 0 0 0 0  stretch stretch}}")
        self.goUpWidget.setHidden(False)

        execute = self.__postTools.getPostIds(sort_by_likes=sort_by_likes, sort_by_dislikes=sort_by_dislikes,
                                              sort_by_comments=sort_by_comments,
                                              sort_by_all_reactions=sort_by_all_reactions, search_by_key=search_by_key)
        if self.isError(execute):
            return False

        if not sort_by_likes and not sort_by_comments and not sort_by_dislikes and not search_by_key:
            self.ui.button_SortByTime.setChecked(True)

        self.listPosts = execute["data"]
        if not self.listPosts:
            self.setHomeSign("Seems like there are no posts yet.")
            return True
        self.setHomeSign()

        for i in range(self.ui.stacked_Posts.count() - 1, -1, -1):
            page = self.ui.stacked_Posts.widget(i)
            page.setHidden(True)
            self.ui.stacked_Posts.removeWidget(page)

        for i in range(self.ui.layout_SetPostsPage.count() - 1, -1, -1):
            widget = self.ui.layout_SetPostsPage.itemAt(i)
            if isinstance(widget.widget(), QPushButton):
                widget.widget().setHidden(True)
                self.ui.layout_SetPostsPage.removeWidget(widget.widget())

        self.groupButtonsPostsPages = QButtonGroup()

        for _ in range(math.ceil(len(self.listPosts) / self.amountPostsOnPage)):
            self.addPage(stackedWidget=self.ui.stacked_Posts, layoutMargins=(20, 0, 10, 10),
                         buttonsLayout=self.ui.layout_SetPostsPage, buttonGroup=self.groupButtonsPostsPages,
                         methodSetPage=self.setPosts)
        if not self.setPosts(pageIndex=1):
            return False

        return True

    def getCreatePostWidget(self):

        execute = self.__auth.checkAuthorization()
        if self.isError(execute):
            return False

        authorized = execute["data"]
        if not authorized:
            return True

        imageIdExe = self.__currentUser.imageID
        if self.isError(imageIdExe):
            return False

        imageId = imageIdExe["data"]
        execute = self.__fileManager.getFilePath(imageId=imageId)
        if self.isError(execute):
            return False

        imagePath = execute["data"]
        postCreate = CreatePost(imagePath, self.__postTools, self.__fileManager)
        return postCreate

    def getCommentCreateWidget(self, postId: int):

        execute = self.__auth.checkAuthorization()
        if self.isError(execute):
            return False

        authorized = execute["data"]
        if not authorized:
            return True

        imageIdExe = self.__currentUser.imageID
        if self.isError(imageIdExe):
            return False

        imageId = imageIdExe["data"]
        execute = self.__fileManager.getFilePath(imageId=imageId)
        if self.isError(execute):
            return False

        imagePath = execute["data"]

        commentCreate = CreateComment(imagePath, postId, self.__postTools)
        return commentCreate

    @staticmethod
    def getAdvertWidget(widgetWidth: int):
        widgetAd = Advert(widgetWidth)
        widgetAd.setAdvert(os.path.abspath("gui/resources/images/Ad/karmen1.png"), offsetY=35,
                           url="https://drive.google.com/drive/folders/1LRuyE-nsm95ONkVcVmHtXFex0aUc0GOg?usp=drive_link")
        widgetAd.setAdvert(os.path.abspath("gui/resources/images/Ad/karmen2.png"), offsetY=50,
                           url="https://drive.google.com/drive/folders/1LRuyE-nsm95ONkVcVmHtXFex0aUc0GOg?usp=drive_link")
        widgetAd.setAdvert(os.path.abspath("gui/resources/images/Ad/racing.png"), offsetY=115,
                           url="https://github.com/teenxsky/racing_game")
        return widgetAd

    def setPosts(self, pageIndex: int = None) -> bool:
        if not self.listPosts:
            return False

        if isinstance(self.sender(), QPushButton) and self.sender().text().isnumeric():
            pageIndex = int(self.sender().text())

        postsOnPageList = self.listPosts[(pageIndex - 1) * self.amountPostsOnPage: pageIndex * self.amountPostsOnPage]
        execute = self.__postTools.getPostsInfo(postsOnPageList)
        if self.isError(execute):
            return False

        postsOnPageInfo = execute["data"]

        pageLayout = self.ui.stacked_Posts.widget(pageIndex - 1).layout()
        for postIndex in range(pageLayout.count() - 1, -1, -1):
            if isinstance(pageLayout.itemAt(postIndex).widget(), Post) or isinstance(
                    pageLayout.itemAt(postIndex).widget(), Advert):
                pageLayout.itemAt(postIndex).widget().setHidden(True)
                pageLayout.removeWidget(pageLayout.itemAt(postIndex).widget())

        adIndex = random.randint(0, len(postsOnPageInfo) - 1)

        pageLayout = self.ui.stacked_Posts.widget(pageIndex - 1).layout()
        pageLayout.setSizeConstraint(QVBoxLayout.SizeConstraint.SetMinimumSize)
        pageLayout.addStretch()
        for postInfo in postsOnPageInfo:
            if not adIndex and self.advertOn:
                widgetAd = self.getAdvertWidget(
                    self.ui.stacked_Posts.size().width() - pageLayout.contentsMargins().left()
                    - pageLayout.contentsMargins().right())
                pageLayout.addWidget(widgetAd)
                widgetAd.start()
            adIndex -= 1
            post = Post(postInfo, self.__postTools, self.__currentUser, self.__fileManager,
                        self.currentUserAccess, self.currentUserId)
            post.connectionErrorSignal.connect(self.showConnectionError)
            post.unfollowUserSignal.connect(self.userUnfollowed)
            post.reportUserSignal.connect(self.openReportPage)
            post.followUserSignal.connect(self.userFollowed)
            post.deletePostSignal.connect(self.postDeleted)
            post.openCommentsSignal.connect(self.openCommentsPage)
            post.authErrorSignal.connect(self.logOut)
            pageLayout.addWidget(post)
        # pageLayout.addStretch()

        self.ui.scrollArea_HomePosts.verticalScrollBar().setValue(0)
        self.ui.stacked_Posts.setCurrentIndex(pageIndex - 1)

        return True

    def setCommentsPage(self, postInfo: dict = None) -> bool:
        execute = self.__auth.checkAuthorization()
        if self.isError(execute):
            return False

        for i in range(self.ui.layout_CommentsPostScroll.count() - 1, -1, -1):
            widget = self.ui.layout_CommentsPostScroll.itemAt(i).widget()
            if isinstance(widget, Post) or isinstance(widget, CreateComment):
                widget.setHidden(True)
                self.ui.layout_CommentsPostScroll.removeWidget(widget)

        authorized = execute["data"]
        if authorized:
            self.commentCreateWidget = self.getCommentCreateWidget(postInfo["post_id"])
            if not self.commentCreateWidget:
                return False
            self.commentCreateWidget.errorSignal.connect(self.isError)
            self.commentCreateWidget.commentCreatedSignal.connect(self.commentCreated)
            self.commentCreateWidget.focusInSignal.connect(
                lambda: self.ui.scrollArea_CommentsPost.verticalScrollBar().setValue())
            self.commentCreateWidget.setFixedWidth(
                self.ui.frame_PostContainer.size().width() - self.ui.layout_CommentsPostScroll.contentsMargins().left()
                - self.ui.layout_CommentsPostScroll.contentsMargins().right())
            self.ui.layout_CommentsPostScroll.insertWidget(1, self.commentCreateWidget)

        if postInfo:
            self.listComments = postInfo["comments"]
            self.currentPostInfo = postInfo
        else:
            execute = self.__postTools.getPostsInfo([self.listComments[0]["post_id"]])
            if self.isError(execute):
                return False
            postInfo = execute["data"]

        for i in range(self.ui.stacked_Comments.count() - 1, -1, -1):
            page = self.ui.stacked_Comments.widget(i)
            page.setHidden(True)
            self.ui.stacked_Comments.removeWidget(page)

        if not (self.pathHomeBg and os.path.exists(self.pathHomeBg)):
            self.pathHomeBg = ImageTools.getPictureForWidget(self.ui.page_Home.size().width(),
                                                             self.ui.page_Home.size().height(),
                                                             0,
                                                             os.path.abspath(
                                                                 "gui/resources/images/homeBg.png"),
                                                             self.__fileManager.tempPath,
                                                             self.filenameHomeBackground)
        self.ui.page_Comments.setStyleSheet(
            f"QWidget#page_Comments {{border-image: url('{self.pathHomeBg}') 0 0 0 0  stretch stretch}}")

        post = Post(postInfo, self.__postTools, self.__currentUser, self.__fileManager,
                    self.currentUserAccess, self.currentUserId, True)
        post.setFixedWidth(
            self.ui.frame_PostContainer.size().width() - self.ui.layout_CommentsPostScroll.contentsMargins().left()
            - self.ui.layout_CommentsPostScroll.contentsMargins().right())
        post.resizeImage(
            self.ui.frame_PostContainer.size().width() - self.ui.layout_CommentsPostScroll.contentsMargins().left()
            - self.ui.layout_CommentsPostScroll.contentsMargins().right())
        post.connectionErrorSignal.connect(self.showConnectionError)
        post.unfollowUserSignal.connect(self.userUnfollowed)
        post.reportUserSignal.connect(self.openReportPage)
        post.followUserSignal.connect(self.userFollowed)
        post.deletePostSignal.connect(self.postDeleted)
        post.openCommentsSignal.connect(self.openCommentsPage)
        post.authErrorSignal.connect(self.logOut)
        self.ui.layout_CommentsPostScroll.insertWidget(1, post)

        for i in range(self.ui.layout_SetCommentsPage.count() - 1, -1, -1):
            widget = self.ui.layout_SetCommentsPage.itemAt(i)
            if isinstance(widget.widget(), QPushButton):
                widget.widget().setHidden(True)
                self.ui.layout_SetCommentsPage.removeWidget(widget.widget())

        self.groupButtonsCommentsPages = QButtonGroup()

        if not self.listComments:
            self.setCommentsSign("Seems like there are no comments yet.")
            return True
        self.setCommentsSign()

        for _ in range(math.ceil(len(self.listComments) / self.amountCommentsOnPage)):
            self.addPage(stackedWidget=self.ui.stacked_Comments, layoutMargins=(5, 0, 10, 20),
                         buttonsLayout=self.ui.layout_SetCommentsPage, buttonGroup=self.groupButtonsCommentsPages,
                         methodSetPage=self.setComments)
        if not self.setComments(pageIndex=1):
            return False

        return True

    def setComments(self, pageIndex: int = None) -> bool:
        if not self.listComments:
            return False

        if isinstance(self.sender(), QPushButton) and self.sender().text().isnumeric():
            pageIndex = int(self.sender().text())

        listCommentsOnPage = self.listComments[
                             (pageIndex - 1) * self.amountPostsOnPage: pageIndex * self.amountPostsOnPage]

        pageLayout = self.ui.stacked_Comments.widget(pageIndex - 1).layout()
        for commentIndex in range(pageLayout.count() - 1, -1, -1):
            if isinstance(pageLayout.itemAt(commentIndex).widget(), Post):
                pageLayout.itemAt(commentIndex).widget().setHidden(True)
                pageLayout.removeWidget(pageLayout.itemAt(commentIndex).widget())

        execute = self.__currentUser.access
        if self.isError(execute):
            return False
        currentUserAccess = execute["data"]

        execute = self.__currentUser.userID
        if self.isError(execute):
            return False
        currentUserId = execute["data"]

        pageLayout = self.ui.stacked_Comments.widget(pageIndex - 1).layout()
        pageLayout.setSizeConstraint(QVBoxLayout.SizeConstraint.SetMinimumSize)
        for commentInfo in listCommentsOnPage:
            comment = Comment(commentInfo, self.__postTools, self.__currentUser, self.__fileManager,
                              currentUserAccess, currentUserId)
            comment.connectionErrorSignal.connect(self.showConnectionError)
            comment.unfollowUserSignal.connect(self.userUnfollowed)
            comment.reportUserSignal.connect(self.openReportPage)
            comment.followUserSignal.connect(self.userFollowed)
            comment.deleteCommentSignal.connect(self.commentDeleted)
            comment.authErrorSignal.connect(self.logOut)
            pageLayout.addWidget(comment)
        pageLayout.addStretch()

        self.ui.scrollArea_Comments.verticalScrollBar().setValue(0)
        self.ui.stacked_Comments.setCurrentIndex(pageIndex - 1)

        return True

    def setCommentsSign(self, text: str = None):
        if text:
            self.ui.label_CommentsSign.setText(text)
            self.ui.label_CommentsSign.setVisible(True)
        else:
            self.ui.label_CommentsSign.setHidden(True)

    def setUserPage(self, userId: int):

        user = User(userId)
        execute = user.userInfo
        if self.isError(execute):
            return False

        userInfo = execute["data"]
        imageId = userInfo["image_id"]
        name = userInfo["name"]
        username = userInfo["username"]
        access = userInfo["access"]
        about = userInfo["about"]
        online = userInfo["online"]

        profileBgPicturePath = ImageTools.getPictureForWidget(self.ui.frame_UserInfoContainer.size().width(),
                                                              self.ui.frame_UserInfoContainer.size().height(),
                                                              0,
                                                              os.path.abspath(
                                                                  "gui/resources/images/profileBgSource.png"),
                                                              self.__fileManager.tempPath,
                                                              self.filenameProfileBackground)

        self.ui.frame_UserInfoContainer.setStyleSheet(
            f"QFrame#frame_UserInfoContainer {{border-image: url('{profileBgPicturePath}') "
            f"0 0 0 0  stretch stretch}}")

        accountTabsBgPath = ImageTools.getPictureForWidget(self.ui.frame_UserTabsContainer.size().width(),
                                                           self.ui.frame_UserTabsContainer.size().height(),
                                                           self.ui.frame_UserInfoContainer.size().height()
                                                           * QWindow().devicePixelRatio(),
                                                           os.path.abspath(
                                                               "gui/resources/images/profileBgSource.png"),
                                                           self.__fileManager.tempPath,
                                                           self.filenameAccountTabsBackground)

        self.ui.frame_UserTabsContainer.setStyleSheet(
            f"QFrame#frame_UserTabsContainer {{border-image: url('{accountTabsBgPath}') 0 0 0 0  stretch stretch}}")

        execute = self.__fileManager.getFilePath(imageId=imageId)
        if self.isError(execute):
            return False

        for i in range(self.ui.layout_UserInfoContainer.count()):
            if (self.ui.layout_UserInfoContainer.itemAt(i).widget()
                    and isinstance(self.ui.layout_UserInfoContainer.itemAt(i).widget(), ProfilePictureFrame)):
                self.ui.layout_UserInfoContainer.itemAt(i).widget().setVisible(False)
                self.ui.layout_UserInfoContainer.removeWidget(
                    self.ui.layout_UserInfoContainer.itemAt(i).widget())
                break

        profilePictureFrame = ProfilePictureFrame(execute["data"], frame=2)
        self.ui.layout_UserInfoContainer.insertWidget(0, profilePictureFrame)
        profilePictureFrame.setToolTip("@" + username)

        if access == "Admin":
            self.ui.label_UserNickname.setText(
                self.getTextHTML(name, color="white", weight=700) + " " + self.getTextHTML("(" + access + ")",
                                                                                           color="rgb(219,228,233)",
                                                                                           weight=400))
        else:
            self.ui.label_UserNickname.setText(self.getTextHTML(name, color="white", weight=700))
        self.ui.label_UserNickname.setToolTip("@" + username)

        self.ui.label_UserStatus.setText(self.getTextHTML(self.getOnlineCircle(online)))

        if online:
            self.ui.label_UserStatus.setToolTip("Online")
        else:
            self.ui.label_UserStatus.setToolTip("Offline")

        self.ui.label_UserAbout.setText(
            self.getTextHTML(about, color="rgb(229,235,238)", size=19, weight=100))

    def setAccountPage(self) -> bool:

        execute = self.__currentUser.userInfo
        if self.isError(execute):
            return False

        currentUserInfo = execute["data"]
        imageId = currentUserInfo["image_id"]
        name = currentUserInfo["name"]
        username = currentUserInfo["username"]
        access = currentUserInfo["access"]
        about = currentUserInfo["about"]
        online = currentUserInfo["online"]

        profileBgPicturePath = ImageTools.getPictureForWidget(self.ui.frame_AccountInfoContainer.size().width(),
                                                              self.ui.frame_AccountInfoContainer.size().height(),
                                                              0,
                                                              os.path.abspath(
                                                                  "gui/resources/images/profileBgSource.png"),
                                                              self.__fileManager.tempPath,
                                                              self.filenameProfileBackground)

        self.ui.frame_AccountInfoContainer.setStyleSheet(
            f"QFrame#frame_AccountInfoContainer {{border-image: url('{profileBgPicturePath}') "
            f"0 0 0 0  stretch stretch}}")

        accountTabsBgPath = ImageTools.getPictureForWidget(self.ui.frame_AccountTabsContainer.size().width(),
                                                           self.ui.frame_AccountTabsContainer.size().height(),
                                                           self.ui.frame_AccountInfoContainer.size().height()
                                                           * QWindow().devicePixelRatio(),
                                                           os.path.abspath(
                                                               "gui/resources/images/profileBgSource.png"),
                                                           self.__fileManager.tempPath,
                                                           self.filenameAccountTabsBackground)

        self.ui.frame_AccountTabsContainer.setStyleSheet(
            f"QFrame#frame_AccountTabsContainer {{border-image: url('{accountTabsBgPath}') 0 0 0 0  stretch stretch}}")

        execute = self.__fileManager.getFilePath(imageId=imageId)
        if self.isError(execute):
            return False

        for i in range(self.ui.layout_AccountInfoContainer.count()):
            if (self.ui.layout_AccountInfoContainer.itemAt(i).widget()
                    and isinstance(self.ui.layout_AccountInfoContainer.itemAt(i).widget(), ProfilePictureFrame)):
                self.ui.layout_AccountInfoContainer.itemAt(i).widget().setVisible(False)
                self.ui.layout_AccountInfoContainer.removeWidget(
                    self.ui.layout_AccountInfoContainer.itemAt(i).widget())
                break

        profilePictureFrame = ProfilePictureFrame(execute["data"], frame=2)
        self.ui.layout_AccountInfoContainer.insertWidget(0, profilePictureFrame)
        profilePictureFrame.setToolTip("@" + username)

        if access == "Admin":
            self.ui.label_AccountNickname.setText(
                self.getTextHTML(name, color="white", weight=700) + " " + self.getTextHTML("(" + access + ")",
                                                                                           color="rgb(219,228,233)",
                                                                                           weight=400))
        else:
            self.ui.label_AccountNickname.setText(self.getTextHTML(name, color="white", weight=700))
        self.ui.label_AccountNickname.setToolTip("@" + username)

        self.ui.label_AccountStatus.setText(self.getTextHTML(self.getOnlineCircle(online)))

        if online:
            self.ui.label_AccountStatus.setToolTip("Online")
        else:
            self.ui.label_AccountStatus.setToolTip("Offline")

        self.ui.label_AccountAbout.setText(
            self.getTextHTML(about, color="rgb(229,235,238)", size=19, weight=100))

        return True

    def setLabelAccountEditProfileWarning(self, show=False, save=False, error=None):
        if show:
            if save:
                self.ui.label_AccountEditProfileWarning.setStyleSheet("color:rgb(0,210,0);")
                self.ui.label_AccountEditProfileWarning.setText("Saved successfully!")
                self.ui.frame_AccountEditButtonsContainer.setVisible(False)
                self.flagAccountAboutReset = False
                self.flagAccountEditPhotoSet = False
                self.flagAccountEditPhotoReset = False

            elif error:
                self.ui.label_AccountEditProfileWarning.setStyleSheet("color:rgb(255,0,0);")
                self.ui.label_AccountEditProfileWarning.setText(error)
                self.ui.frame_AccountEditButtonsContainer.setVisible(False)

            else:
                self.ui.label_AccountEditProfileWarning.setStyleSheet("color:rgb(255,0,0);")
                self.ui.label_AccountEditProfileWarning.setText("You have unsaved changes!")
                self.ui.frame_AccountEditButtonsContainer.setVisible(True)
        else:
            self.ui.frame_AccountEditButtonsContainer.setVisible(False)
            self.ui.label_AccountEditProfileWarning.setStyleSheet("color:rgb(0,210,0);")
            self.ui.label_AccountEditProfileWarning.setText("")
            self.flagAccountAboutReset = False
            self.flagAccountEditPhotoSet = False
            self.flagAccountEditPhotoReset = False

    def setAccountEditPage(self) -> bool:
        self.flagAccountAboutReset = False
        self.flagAccountEditPhotoReset = False
        self.ui.line_AccountEditName.setText("")
        self.ui.line_AccountEditAbout.setText("")
        self.ui.line_AccountEditUsername.setText("")
        self.setLabelAccountEditProfileWarning(show=False)
        self.ui.frame_AccountEditButtonsContainer.setHidden(True)
        self.ui.label_AccountEditNameSymbols.setText(
            f"There is {self.amountMaximumNameSymbols - len(self.ui.line_AccountEditName.text())} "
            f"characters left.")
        self.ui.label_AccountEditUsernameSymbols.setText(
            f"There is {self.amountMaximumUsernameSymbols - len(self.ui.line_AccountEditUsername.text())} "
            f"characters left.")
        self.ui.label_AccountEditAboutSymbols.setText(
            f"There is {self.amountMaximumAboutSymbols - len(self.ui.line_AccountEditAbout.toPlainText())} "
            f"characters left.")

        infoExe = self.__currentUser.userInfo
        if self.isError(infoExe):
            return False

        imageId = infoExe["data"]["image_id"]
        name = infoExe["data"]["name"]
        username = infoExe["data"]["username"]
        about = infoExe["data"]["about"]

        execute = self.__fileManager.getFilePath(imageId=imageId)
        if self.isError(execute):
            return False

        imagePath = ImageTools.getProfilePicture(execute["data"], self.__fileManager.tempPath,
                                                 self.filenameAccountEditProfilePicture)

        self.ui.frame_AccountEditPhoto.setStyleSheet(f"""QFrame {{border-image: url({imagePath}) 0 0 0 0}}""")
        self.ui.frame_AccountEditPhoto.setToolTip("@" + username)

        widgetsToDelete = []
        for i in range(self.ui.layout_AccountEditImages.count()):
            if (self.ui.layout_AccountEditImages.itemAt(i).widget()
                    and self.ui.layout_AccountEditImages.itemAt(i).widget() != self.ui.frame_AccountEditPhoto):
                widgetsToDelete.append(self.ui.layout_AccountEditImages.itemAt(i).widget())
        for widget in widgetsToDelete:
            widget.setVisible(False)
            self.ui.layout_AccountEditImages.removeWidget(widget)

        drag = DragNDrop(self.ui.frame_AccountEditPhoto, self.__fileManager.tempPath,
                         self.filenameAccountEditProfilePicture)
        self.ui.layout_AccountEditImages.insertWidget(self.ui.layout_AccountEditImages.count() - 1, drag)
        drag.setToolTip("Drag images as files or URLs from browser")
        drag.imageDropped.connect(self.isAccountEditProfilePhotoSet)

        self.ui.line_AccountEditName.setPlaceholderText(name)
        self.ui.line_AccountEditUsername.setPlaceholderText(username)
        self.ui.line_AccountEditAbout.setPlaceholderText(about)

        return True

    def setAccountImageToDefault(self) -> bool:
        if not self.updateOnline:
            return False

        imageIdExe = self.__currentUser.imageID
        if self.isError(imageIdExe):
            return False

        imageId = imageIdExe["data"]
        if imageId == 1:
            return True

        execute = self.__fileManager.getFilePath(imageId=1)
        if self.isError(execute):
            return False

        imagePath = ImageTools.getProfilePicture(execute["data"], self.__fileManager.tempPath,
                                                 self.filenameAccountEditProfilePicture)

        self.ui.frame_AccountEditPhoto.setStyleSheet(f"""QFrame {{border-image: url({imagePath}) 0 0 0 0}}""")
        self.flagAccountEditPhotoSet = True
        self.flagAccountEditPhotoReset = True
        self.setLabelAccountEditProfileWarning(show=True, save=False)

        return True

    def setAccountEditImageFromFile(self) -> bool:
        fp = self.chooseFile(os.path.expanduser("~/Desktop"), "Images (*.png)")
        if not fp:
            self.setLabelAccountEditProfileWarning(show=True, save=False, error="File Not Found")
            return True

        if not self.updateOnline:
            return False

        imagePath = ImageTools.getProfilePicture(fp, self.__fileManager.tempPath,
                                                 self.filenameAccountEditProfilePicture)
        self.ui.frame_AccountEditPhoto.setStyleSheet(f"""QFrame {{border-image: url({imagePath}) 0 0 0 0}}""")
        self.flagAccountEditPhotoSet = True
        self.setLabelAccountEditProfileWarning(show=True, save=False)
        return True

    def deleteAbout(self):
        self.flagAccountAboutReset = True
        self.ui.line_AccountEditAbout.setText("")
        self.ui.line_AccountEditAbout.setPlaceholderText("")
        self.setLabelAccountEditProfileWarning(show=True, save=False)

    @Slot(bool)
    def isAccountEditProfilePhotoSet(self, value: bool):
        self.flagAccountEditPhotoSet = value
        if value:
            self.ui.frame_AccountEditButtonsContainer.setVisible(True)
            self.setLabelAccountEditProfileWarning(show=True, save=False)

    def saveProfileChanges(self) -> bool:
        if not self.updateOnline:
            return False

        newName = self.ui.line_AccountEditName.text()
        newUsername = self.ui.line_AccountEditUsername.text()
        newAbout = self.ui.line_AccountEditAbout.toPlainText()

        if newName:
            formatError = self.__currentUser.changeName(newName)
            if formatError["error"]:
                if formatError["error"]["connection"]:
                    self.showConnectionError(formatError["error"]["connection"])
                elif formatError["error"]["format"]:
                    self.setLabelAccountEditProfileWarning(show=True, error=formatError["error"]["format"])
                elif formatError["error"]["auth"]:
                    self.changeForm("login", QPoint(self.pos().x(), self.pos().y()))
                return False

        if newUsername:
            formatError = self.__currentUser.changeUsername(newUsername)
            if formatError["error"]:
                if formatError["error"]["connection"]:
                    self.showConnectionError(formatError["error"]["connection"])
                elif formatError["error"]["format"]:
                    self.setLabelAccountEditProfileWarning(show=True, error=formatError["error"]["format"])
                elif formatError["error"]["auth"]:
                    self.changeForm("login", QPoint(self.pos().x(), self.pos().y()))
                return False

        if newAbout or self.flagAccountAboutReset:
            formatError = self.__currentUser.changeAbout(newAbout)
            if formatError["error"]:
                if formatError["error"]["connection"]:
                    self.showConnectionError(formatError["error"]["connection"])
                elif formatError["error"]["format"]:
                    self.setLabelAccountEditProfileWarning(show=True, error=formatError["error"]["format"])
                elif formatError["error"]["auth"]:
                    self.changeForm("login", QPoint(self.pos().x(), self.pos().y()))
                return False

        imageIdExe = self.__currentUser.imageID
        if self.isError(imageIdExe):
            return False

        imageId = imageIdExe["data"]
        if self.flagAccountEditPhotoSet:
            if self.flagAccountEditPhotoReset:
                execute = self.__fileManager.deleteFile(imageId)
            else:
                execute = self.__fileManager.loadFile(
                    self.__fileManager.tempPath + "Just" + self.filenameAccountEditProfilePicture,
                    imageId=imageId)

            if self.isError(execute):
                return False

            execute = self.__currentUser.changeImageID(execute["data"])
            if self.isError(execute):
                return False

        if not self.setAccountEditPage():
            return False

        self.setLabelAccountEditProfileWarning(show=True, save=True)
        return True

    def setReportPage(self, reportInfo: dict) -> bool:
        self.setSideBarButtonEnabled(False)
        self.ui.label_Report.setText(f"Report @{reportInfo['username']}?")
        self.ui.label_ReportText.setText(f"The user {reportInfo['name']} will be reviewed by our team. "
                                         f"Please do not send a complaint if the user does not violate "
                                         f"the rules of our platform.")
        self.ui.textEdit_ReportText.setText("")
        self.reportInfo = reportInfo

        return True

    def reportUser(self):
        execute = self.__currentUser.makeReportTo(self.reportInfo["post_id"])
        if self.isError(execute):
            return
        self.refresh(homePage=True)
        bar = InfoBar(self, text="Report created")
        bar.show()

    def sortByTime(self):

        if not self.setHomePage():
            return False
        self.ui.button_SortByTime.setChecked(True)
        self.ui.button_Logo.setChecked(True)
        self.ui.stacked_Pages.setCurrentIndex(self.widgetToIndexHome["home"])

    def sortByLikes(self):
        if not self.setHomePage(sort_by_likes=True):
            return False
        self.ui.button_SortByLikes.setChecked(True)
        self.ui.button_Logo.setChecked(True)
        self.ui.stacked_Pages.setCurrentIndex(self.widgetToIndexHome["home"])

    def sortByDislikes(self):
        if not self.setHomePage(sort_by_dislikes=True):
            return False
        self.ui.button_Logo.setChecked(True)
        self.ui.button_SortByDislikes.setChecked(True)
        self.ui.stacked_Pages.setCurrentIndex(self.widgetToIndexHome["home"])

    def sortByComments(self):
        if not self.setHomePage(sort_by_comments=True):
            return False
        self.ui.button_Logo.setChecked(True)
        self.ui.button_SortByComments.setChecked(True)
        self.ui.stacked_Pages.setCurrentIndex(self.widgetToIndexHome["home"])

    def sortByHot(self):
        if not self.setHomePage(sort_by_all_reactions=True):
            return False
        self.ui.button_Logo.setChecked(True)
        self.ui.button_SortByHot.setChecked(True)
        self.ui.stacked_Pages.setCurrentIndex(self.widgetToIndexHome["home"])

    def searchByKey(self, key: str):
        if not self.setHomePage(search_by_key=key):
            return False
        self.ui.button_Logo.setChecked(True)
        self.ui.stacked_Pages.setCurrentIndex(self.widgetToIndexHome["home"])

    @Slot(str, QPoint)
    def changeForm(self, form: str, pos: QPoint = None):
        """If form=='login' then Log In form sets
           If form=='signup' then SIgn Up form sets
           If form=='home' then Main App form sets"""

        if form not in {"login", "signup", "home"}:
            raise ValueError("Wrong argument's name!")

        if self.isVisible():
            self.hide()

        if form == "login":
            self.logInForm = LogInForm(self.__auth, self.__fileManager)
            self.logInForm.formChangedSignal.connect(self.changeForm)
            self.logInForm.exitSignal.connect(self.changeForm)
            self.logInForm.move(pos)
            self.logInForm.show()

        elif form == "signup":
            self.signUpForm = SignUpForm(self.__auth, self.__fileManager)
            self.signUpForm.formChangedSignal.connect(self.changeForm)
            self.signUpForm.exitSignal.connect(self.changeForm)
            self.signUpForm.move(pos)
            self.signUpForm.show()

        elif form == "home":
            self.refresh(homePage=True)
            if pos:
                self.move(pos)
            if not self.isVisible():
                self.show()

    def logOut(self, openForm: bool = True) -> bool:
        execute = self.__auth.logOut()
        if self.isError(execute):
            return False

        if openForm:
            self.changeForm("login", QPoint(self.pos().x(), self.pos().y()))

        return True

    def refresh(self, homePage: bool = False, commentsPage: bool = False) -> bool:
        if homePage:
            if not self.setHomePage():
                return False
            self.ui.button_Logo.setChecked(True)
            self.ui.stacked_Pages.setCurrentIndex(self.widgetToIndexHome["home"])

        if commentsPage:
            execute = self.__postTools.getPostsInfo([self.currentPostInfo["post_id"]])
            if self.isError(execute):
                return False
            self.currentPostInfo = execute["data"][0]
            if not self.setCommentsPage(self.currentPostInfo):
                return False
            self.ui.stacked_Pages.setCurrentIndex(self.widgetToIndexHome["comments"])

        self.setSideBarButtonEnabled(True)
        return True


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = App()
    window.show()
    sys.exit(app.exec())
