import os.path
import sys
import math

from PySide6.QtCore import QSize, Qt, QEvent, Slot, QPoint
from PySide6.QtGui import QIcon, Qt, QFontDatabase, QFont, QAction, QWindow, QColor
from PySide6.QtWidgets import QMainWindow, QApplication, QMenu, QFileDialog, QPlainTextEdit, QWidget, QVBoxLayout, \
    QPushButton, QGraphicsDropShadowEffect, QButtonGroup

from gui.design.main import Ui_MainWindow
from objects.ImageTools import ImageTools
from objects.forms import LogInForm, SignUpForm
from objects.server.Authorization import Authorization
from objects.server.DataBase import DataBase
from objects.server.FileManager import FileManager
from objects.server.UserInfo import CurrentUser
from src.main.objects.server.PostTools import PostTools
from src.main.objects.widgets import DragNDrop, ProfilePictureFrame, Post, CreatePost
from src.main.gui.resources import resources


class App(Ui_MainWindow, QMainWindow):
    widgetToIndex = {"home": 0, "account": 1, "edit": 2}
    widgetToIndexAccountEdit = {"profile": 0, "privacy": 1, "chat": 2}

    tempHomeBackgroundFileName = "tempHomeBackgroundFileName.png"
    tempAccountPictureFileName = "tempAccountPicture.png"
    tempAccountEditProfilePictureFileName = "tempAccountEditProfilePicture.png"
    tempProfileBackgroundFileName = "tempProfileBackground.png"
    tempAccountTabsBackgroundFileName = "tempAccountTabsBackgroundFileName.png"

    amountMaximumNameSymbols = 20
    amountMaximumUsernameSymbols = 32
    amountMaximumAboutSymbols = 70

    amountPostsOnPage = 5

    def __init__(self):
        super(Ui_MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.__db = DataBase()
        self.__auth = Authorization()
        self.__currentUser = CurrentUser()
        self.__fileManager = FileManager()
        self.__postTools = PostTools()

        self.logInForm = None
        self.signUpForm = None

        self.accountEditPhotoReset = False
        self.accountEditPhotoSet = False
        self.accountAboutReset = False
        self.buttonsSideBarIcons = {}
        self.postsList = []
        self.postCreate = None

        self.buttonsPostsPagesGroup = QButtonGroup()

        self.fontThin = None  # Make cls
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

        icon_ErrorClose = QIcon()
        icon_ErrorClose.addFile(":icons/icons/Close.svg", QSize(), QIcon.Normal)
        self.ui.button_ErrorClose.setIcon(icon_ErrorClose)
        self.ui.button_ErrorClose.setIconSize(QSize(15, 15))

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

        self.buttonsSideBarIcons["apps"] = {"enabled": icon_Apps, "disabled": icon_AppsDisabled}
        self.buttonsSideBarIcons["notifications"] = {"enabled": icon_Notifications,
                                                     "disabled": icon_NotificationsDisabled}
        self.buttonsSideBarIcons["chat"] = {"enabled": icon_Chat, "disabled": icon_ChatDisabled}

    def __initSetup(self):

        self.ui.stacked_Pages.setCurrentIndex(self.widgetToIndex["home"])

        for button in self.ui.buttonGroup_MainTabs.buttons():
            button.clicked.connect(self.switchPage)
        self.ui.button_AccountEdit.clicked.connect(self.switchPage)
        for button in self.ui.buttonGroup_AccountEditTabs.buttons():
            button.clicked.connect(self.switchPage)

        self.ui.frame_SideBarChat.setHidden(True)
        self.ui.frame_SideBarNotifications.setHidden(True)
        self.ui.frame_AccountExitConfirmation.setHidden(True)
        self.ui.frame_Error.setHidden(True)
        self.ui.frame_AccountEditButtonsContainer.setHidden(True)
        self.ui.label_HomeSign.setHidden(True)

        self.ui.button_Apps.setChecked(True)
        self.ui.frame_SideBarApps.setMinimumWidth(350)
        self.ui.frame_SideBarChat.setMinimumWidth(350)
        self.ui.frame_SideBarNotifications.setMinimumWidth(350)

        self.ui.button_AccountExitNo.installEventFilter(self)
        self.ui.button_AccountExitYes.installEventFilter(self)
        self.ui.button_AccountExit.installEventFilter(self)
        self.ui.button_AccountEditPhotoDelete.installEventFilter(self)
        self.ui.line_AccountEditName.installEventFilter(self)
        self.ui.line_AccountEditAbout.installEventFilter(self)
        self.ui.line_SearchBar.installEventFilter(self)
        self.ui.line_AccountEditUsername.installEventFilter(self)
        self.ui.button_AccountEditAboutDelete.installEventFilter(self)

        self.ui.button_AccountExitYes.clicked.connect(self.switchPage)
        self.ui.button_AccountEditProfileSave.clicked.connect(self.saveProfileChanges)
        self.ui.button_AccountEditPhotoDelete.clicked.connect(self.setAccountImageToDefault)
        self.ui.button_AccountEditProfileCancel.clicked.connect(self.setAccountEditPage)
        self.ui.button_ErrorClose.clicked.connect(self.closeError)
        self.ui.button_AccountEditAboutDelete.clicked.connect(self.deleteAbout)
        self.ui.button_AccountEditPhotoAdd.clicked.connect(self.setAccountEditImageFromFile)

        self.ui.frame_AccountInfo.setAttribute(Qt.WidgetAttribute.WA_TranslucentBackground)
        self.ui.frame_AccountButtons.setAttribute(Qt.WidgetAttribute.WA_TranslucentBackground)
        self.ui.frame_AccountLabels_1.setAttribute(Qt.WidgetAttribute.WA_TranslucentBackground)
        self.ui.frame_AccountExitConfirmation.setAttribute(Qt.WidgetAttribute.WA_TranslucentBackground)
        self.ui.frame_AccountInformationContainer.setAttribute(Qt.WidgetAttribute.WA_TranslucentBackground)
        self.ui.frame_SetPostsPage.setAttribute(Qt.WidgetAttribute.WA_TranslucentBackground)
        self.ui.stacked_Posts.setAttribute(Qt.WidgetAttribute.WA_TranslucentBackground)
        self.ui.scrollArea_HomePosts.setAttribute(Qt.WidgetAttribute.WA_TranslucentBackground)
        self.ui.scrollAreaWidget_Posts.setAttribute(Qt.WidgetAttribute.WA_TranslucentBackground)
        self.ui.label_AccountStatus.setAttribute(Qt.WidgetAttribute.WA_TranslucentBackground)
        self.ui.label_AccountNickname.setAttribute(Qt.WidgetAttribute.WA_TranslucentBackground)
        self.ui.label_AccountInformationText.setAttribute(Qt.WidgetAttribute.WA_TranslucentBackground)
        self.ui.label_AccountInformationID.setAttribute(Qt.WidgetAttribute.WA_TranslucentBackground)
        self.ui.label_AccountInformationAccess.setAttribute(Qt.WidgetAttribute.WA_TranslucentBackground)
        self.ui.label_HomeSign.setAttribute(Qt.WidgetAttribute.WA_TranslucentBackground)

        self.ui.line_AccountEditName.setMaxLength(self.amountMaximumNameSymbols)

        self.ui.label_AccountEditNameSymbols.setText(
            f"There are {self.amountMaximumNameSymbols - len(self.ui.line_AccountEditName.text())} characters left.")
        self.ui.label_AccountEditAboutSymbols.setText(
            f"There are {self.amountMaximumAboutSymbols - len(self.ui.line_AccountEditAbout.toPlainText())} "
            f"characters left.")

        menu_FilterPosts = QMenu(self)
        action_Sort = QMenu("&Sort", self)

        action_SortByTime = QAction("&By Time", self)
        action_SortByTime.setShortcut("Ctrl+T")
        action_SortByTime.triggered.connect(self.sortByTime)
        action_Sort.addAction(action_SortByTime)

        action_SortByLikes = QAction("&By Likes", self)
        action_SortByLikes.setShortcut("Ctrl+L")
        action_SortByLikes.triggered.connect(self.sortByLikes)
        action_Sort.addAction(action_SortByLikes)
        menu_FilterPosts.addMenu(action_Sort)
        self.ui.button_HomeFilterPosts.setMenu(menu_FilterPosts)

        self.ui.scrollArea_HomePosts.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)

        shadow = QGraphicsDropShadowEffect(blurRadius=5, xOffset=3, yOffset=3)
        self.ui.frame_SideBarApps.setWindowFlags(Qt.FramelessWindowHint | Qt.WindowMinMaxButtonsHint)
        self.ui.frame_SideBarApps.setGraphicsEffect(shadow)
        self.ui.frame_SideBarChat.setWindowFlags(Qt.FramelessWindowHint | Qt.WindowMinMaxButtonsHint)
        self.ui.frame_SideBarChat.setGraphicsEffect(shadow)
        self.ui.frame_SideBarNotifications.setWindowFlags(Qt.FramelessWindowHint | Qt.WindowMinMaxButtonsHint)
        self.ui.frame_SideBarNotifications.setGraphicsEffect(shadow)

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

        self.ui.label_AccountNickname.setFont(self.fontRegular)
        self.ui.label_AccountInformationID.setFont(self.fontRegular)
        self.ui.label_AccountInformationAccess.setFont(self.fontRegular)
        self.ui.label_AccountInformationText.setFont(self.fontCursive)

    def __setShadow(self):

        self.__shadowBlurRadius = 10.0
        self.__borderWidth = 1
        self.__shadowMargin = 0
        self.__borderRadius = 12.0

        self.__effect = QGraphicsDropShadowEffect()
        self.__effect.setBlurRadius(self.__shadowBlurRadius)
        self.__effect.setColor(QColor(0, 0, 0, 127))
        self.__effect.setOffset(5.0)

        self.ui.frame_SideBarApps.setGraphicsEffect(self.__effect)
        self.ui.frame_SideBarApps.repaint()
        # self.repaint()
        self.ui.frame_SideBarChat.setGraphicsEffect(self.__effect)
        self.ui.frame_SideBarChat.repaint()
        # self.repaint()
        self.ui.frame_SideBarNotifications.setGraphicsEffect(self.__effect)
        self.ui.frame_SideBarNotifications.repaint()
        # self.repaint()

    def eventFilter(self, watched, event):

        if watched == self.ui.button_AccountExitYes:

            if event.type() == QEvent.Type.HoverEnter:

                icon = QIcon()
                icon.addFile(":icons/icons/AccountExitYesWhite.svg", QSize(), QIcon.Normal)
                watched.setIcon(icon)
                watched.setIconSize(QSize(25, 25))

                watched.setStyleSheet("background-color: rgb(255, 0, 0);")
                return True

            elif event.type() == QEvent.Type.HoverLeave:

                icon = QIcon()
                icon.addFile(":icons/icons/AccountExitYesBlack.svg", QSize(), QIcon.Normal)
                watched.setIcon(icon)
                watched.setIconSize(QSize(25, 25))

                watched.setStyleSheet("background-color: white;")
                return True

        elif watched == self.ui.button_AccountExitNo:

            if event.type() == QEvent.Type.HoverEnter:

                icon = QIcon()
                icon.addFile(":icons/icons/AccountExitNoWhite.svg", QSize(), QIcon.Normal)
                watched.setIcon(icon)
                watched.setIconSize(QSize(25, 25))

                watched.setStyleSheet("background-color: #208b3a;")
                return True

            elif event.type() == QEvent.Type.HoverLeave:

                icon = QIcon()
                icon.addFile(":icons/icons/AccountExitNoBlack.svg", QSize(), QIcon.Normal)
                watched.setIcon(icon)
                watched.setIconSize(QSize(25, 25))

                watched.setStyleSheet("background-color: white;")
                return True

        elif watched == self.ui.button_AccountExit:

            if event.type() == QEvent.Type.HoverEnter:

                icon = QIcon()
                icon.addFile(":icons/icons/AccountExitWhite.svg", QSize(), QIcon.Normal)
                watched.setIcon(icon)
                watched.setIconSize(QSize(22, 22))

                watched.setStyleSheet("background-color: rgb(255, 0, 0)")
                return True

            elif event.type() == QEvent.Type.HoverLeave:

                icon = QIcon()
                icon.addFile(":icons/icons/AccountExitBlack.svg", QSize(), QIcon.Normal)
                watched.setIcon(icon)
                watched.setIconSize(QSize(22, 22))

                watched.setStyleSheet("background-color: white;")
                return True

        elif watched == self.ui.button_AccountEditPhotoDelete:

            if event.type() == QEvent.Type.HoverEnter:

                icon = QIcon()
                icon.addFile(":icons/icons/AccountEditPhotoDeleteWhite.svg", QSize(), QIcon.Normal)
                watched.setIcon(icon)
                watched.setIconSize(QSize(30, 30))

                watched.setStyleSheet("background-color: rgb(240, 0, 0)")
                return True

            elif event.type() == QEvent.Type.HoverLeave:

                icon = QIcon()
                icon.addFile(":icons/icons/AccountEditPhotoDeleteBlack.svg", QSize(), QIcon.Normal)
                watched.setIcon(icon)
                watched.setIconSize(QSize(30, 30))

                watched.setStyleSheet("background-color: rgb(229,235,238)")
                return True

        elif watched == self.ui.button_AccountEditAboutDelete:

            if event.type() == QEvent.Type.HoverEnter:

                icon = QIcon()
                icon.addFile(":icons/icons/AccountEditPhotoDeleteWhite.svg", QSize(), QIcon.Normal)
                watched.setIcon(icon)
                watched.setIconSize(QSize(20, 20))

                watched.setStyleSheet("background-color: rgb(240, 0, 0)")
                return True

            elif event.type() == QEvent.Type.HoverLeave:

                icon = QIcon()
                icon.addFile(":icons/icons/AccountEditPhotoDeleteBlack.svg", QSize(), QIcon.Normal)
                watched.setIcon(icon)
                watched.setIconSize(QSize(20, 20))

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
                        or self.ui.line_AccountEditUsername.text() or self.accountEditPhotoSet
                        or self.accountEditPhotoReset or self.accountAboutReset):
                    self.setLabelAccountEditProfileWarning(show=True, save=False)
                    self.ui.frame_AccountEditButtonsContainer.setVisible(True)
                else:
                    self.setLabelAccountEditProfileWarning(show=False)
                    self.ui.frame_AccountEditButtonsContainer.setHidden(True)

        return False

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

        self.ui.label_ErrorText.setText(error)
        self.ui.frame_Error.setVisible(True)

    def setHomeSign(self, text=None):
        if text:
            self.ui.label_HomeSign.setVisible(True)
            self.ui.label_HomeSign.setText(text)
        else:
            self.ui.label_HomeSign.setVisible(False)

    def closeError(self):

        self.ui.frame_Error.setHidden(True)

    def updateOnline(self) -> bool:

        execute = self.__currentUser.updateOnline()
        print(execute)

        if execute["error"]:
            if execute["error"]["connection"]:
                self.showConnectionError(execute["error"]["connection"])
            elif execute["error"]["format"]:
                self.showConnectionError(execute["error"]["format"])
            elif execute["error"]["auth"]:
                self.changeForm("login", QPoint(self.pos().x(), self.pos().y()))
                self.ui.stacked_Pages.setCurrentIndex(self.widgetToIndex["home"])
            self.ui.frame_Error.setHidden(True)
            return False
        return True

    def chooseFile(self, rootDir: str, nameFilter: str) -> str:

        fileName, ok = QFileDialog.getOpenFileName(self, "Select a File", rootDir, nameFilter)
        if ok:
            return fileName

    def setSideBarButtonEnabled(self, value: bool):

        if value:
            self.ui.button_Apps.setStyleSheet("QPushButton:checked { background-color: rgb(235, 237, 239); }")
            self.ui.button_Notifications.setStyleSheet("QPushButton:checked { background-color: rgb(235, 237, 239); }")
            self.ui.button_Chat.setStyleSheet("QPushButton:checked { background-color: rgb(235, 237, 239); }")

            self.ui.button_Apps.setIcon(self.buttonsSideBarIcons["apps"]["enabled"])
            self.ui.button_Notifications.setIcon(self.buttonsSideBarIcons["notifications"]["enabled"])
            self.ui.button_Chat.setIcon(self.buttonsSideBarIcons["chat"]["enabled"])
        else:
            self.ui.button_Apps.setStyleSheet("QPushButton:checked { background-color: white; }")
            self.ui.button_Notifications.setStyleSheet("QPushButton:checked { background-color: white; }")
            self.ui.button_Chat.setStyleSheet("QPushButton:checked { background-color: white; }")

            self.ui.button_Apps.setIcon(self.buttonsSideBarIcons["apps"]["disabled"])
            self.ui.button_Notifications.setIcon(self.buttonsSideBarIcons["notifications"]["disabled"])
            self.ui.button_Chat.setIcon(self.buttonsSideBarIcons["chat"]["disabled"])

        self.ui.button_Apps.setEnabled(value)
        self.ui.button_Notifications.setEnabled(value)
        self.ui.button_Chat.setEnabled(value)

    def switchPage(self):

        if self.sender() == self.ui.button_Logo:

            self.setSideBarButtonEnabled(True)
            self.setHomePage()
            self.ui.stacked_Pages.setCurrentIndex(self.widgetToIndex["home"])

        elif self.sender() == self.ui.button_Account:

            self.setSideBarButtonEnabled(False)
            self.ui.button_AccountExitNo.setChecked(True)
            self.ui.button_AccountEdit.setVisible(True)
            self.ui.button_AccountEdit.setVisible(True)

            if not self.updateOnline:
                return

            self.setAccountPage()

            self.ui.stacked_Pages.setCurrentIndex(self.widgetToIndex["account"])

        elif self.sender() == self.ui.button_AccountEdit:

            if not self.updateOnline:
                return

            self.setSideBarButtonEnabled(False)
            self.setAccountEditPage()

            self.ui.stacked_Pages.setCurrentIndex(self.widgetToIndex["edit"])

        elif self.sender() == self.ui.button_AccountExitYes:

            self.__auth.logOut()
            self.setSideBarButtonEnabled(True)
            self.setHomePage()
            self.ui.stacked_Pages.setCurrentIndex(self.widgetToIndex["home"])

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

    def setHomePage(self):

        execute = self.__auth.checkAuthorization()
        if execute["error"]:
            if execute["error"]["connection"]:
                self.showConnectionError(execute["error"]["connection"])
            elif execute["error"]["auth"]:
                self.changeForm("login", QPoint(self.pos().x(), self.pos().y()))
                self.ui.stacked_Pages.setCurrentIndex(self.widgetToIndex["home"])
            elif execute["error"]["format"]:
                self.showConnectionError(execute["error"]["format"])
            return

        authorized = execute["data"]

        for postIndex in range(self.ui.layout_ScrollAreaPosts.count() - 1, -1, -1):
            if isinstance(self.ui.layout_ScrollAreaPosts.itemAt(postIndex).widget(), CreatePost):
                self.ui.layout_ScrollAreaPosts.itemAt(postIndex).widget().setHidden(True)
                self.ui.layout_ScrollAreaPosts.removeWidget(self.ui.layout_ScrollAreaPosts.itemAt(postIndex).widget())

        if authorized:
            self.postCreate = self.getCreatePostWidget()
            self.ui.layout_ScrollAreaPosts.insertWidget(0, self.postCreate)

        execute = self.__postTools.getPostIds(sort_by_time=True)
        if execute["error"]:
            if execute["error"]["connection"]:
                self.showConnectionError(execute["error"]["connection"])
            elif execute["error"]["auth"]:
                self.changeForm("login", QPoint(self.pos().x(), self.pos().y()))
                self.ui.stacked_Pages.setCurrentIndex(self.widgetToIndex["home"])
            elif execute["error"]["format"]:
                self.showConnectionError(execute["error"]["format"])
            return

        self.postsList = execute["data"]
        if not self.postsList:
            self.setHomeSign("Seems like there are no posts yet.")
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

        self.buttonsPostsPagesGroup = QButtonGroup()

        for _ in range(math.ceil(len(self.postsList) / self.amountPostsOnPage)):
            self.addPostPage()
        self.setPostsPage(pageIndex=1)

        homeBgPicturePath = ImageTools.getPictureForWidget(self.ui.page_Home.size().width(),
                                                           self.ui.page_Home.size().height(),
                                                           0,
                                                           os.path.abspath(
                                                               "gui/resources/images/homeBg.png"),
                                                           self.__fileManager.tempPath,
                                                           self.tempHomeBackgroundFileName)

        self.ui.page_Home.setStyleSheet(
            f"QWidget#page_Home {{border-image: url('{homeBgPicturePath}') 0 0 0 0  stretch stretch}}")

    def getCreatePostWidget(self):

        imageIdExe = self.__currentUser.imageID
        if imageIdExe["error"]:
            if imageIdExe["error"]["connection"]:
                self.showConnectionError(imageIdExe["error"]["connection"])
            elif imageIdExe["error"]["auth"]:
                self.changeForm("login", QPoint(self.pos().x(), self.pos().y()))
                self.ui.stacked_Pages.setCurrentIndex(self.widgetToIndex["home"])
            return
        self.ui.frame_Error.setHidden(True)

        imageId = imageIdExe["data"]
        execute = self.__fileManager.getFilePath(imageID=imageId)
        if execute["error"]:
            if execute["error"]["connection"]:
                self.showConnectionError(execute["error"]["connection"])
            elif execute["error"]["auth"]:
                self.changeForm("login", QPoint(self.pos().x(), self.pos().y()))
                self.ui.stacked_Pages.setCurrentIndex(self.widgetToIndex["home"])
            elif execute["error"]["format"]:
                self.showConnectionError(execute["error"]["format"])
            return

        imagePath = execute["data"]

        postCreate = CreatePost(imagePath)
        return postCreate

    def addPostPage(self):

        layout = QVBoxLayout()
        layout.setContentsMargins(20, 0, 10, 40)
        layout.setSpacing(20)
        page = QWidget()
        page.setAttribute(Qt.WidgetAttribute.WA_TranslucentBackground)
        page.setLayout(layout)
        self.ui.stacked_Posts.insertWidget(self.ui.stacked_Posts.count() - 1, page)

        buttonPage = QPushButton(str(self.ui.stacked_Posts.count()))
        buttonPage.clicked.connect(self.setPostsPage)
        buttonPage.setCheckable(True)
        self.buttonsPostsPagesGroup.addButton(buttonPage)
        if self.ui.stacked_Posts.count() == 1:
            buttonPage.setChecked(True)
        self.ui.layout_SetPostsPage.insertWidget(self.ui.layout_SetPostsPage.count() - 1, buttonPage)

    def setPostsPage(self, pageIndex: int = None):

        if not self.postsList:
            return

        if isinstance(self.sender(), QPushButton) and self.sender().text():
            pageIndex = int(self.sender().text())

        postsOnPageList = self.postsList[(pageIndex - 1) * self.amountPostsOnPage: pageIndex * self.amountPostsOnPage]
        execute = self.__postTools.getPostsInfo(postsOnPageList)
        if execute["error"]:
            if execute["error"]["connection"]:
                self.showConnectionError(execute["error"]["connection"])
            elif execute["error"]["auth"]:
                self.changeForm("login", QPoint(self.pos().x(), self.pos().y()))
                self.ui.stacked_Pages.setCurrentIndex(self.widgetToIndex["home"])
            elif execute["error"]["format"]:
                self.showConnectionError(execute["error"]["format"])
            return

        postsOnPageInfo = execute["data"]

        pageLayout = self.ui.stacked_Posts.widget(pageIndex - 1).layout()
        for postIndex in range(pageLayout.count() - 1, -1, -1):
            if isinstance(pageLayout.itemAt(postIndex).widget(), Post):
                pageLayout.itemAt(postIndex).widget().setHidden(True)
                pageLayout.removeWidget(pageLayout.itemAt(postIndex).widget())

        pageLayout = self.ui.stacked_Posts.widget(pageIndex - 1).layout()
        for postId in postsOnPageInfo.keys():
            post = Post(postId, postsOnPageInfo[postId], self.__postTools, self.__currentUser, self.__fileManager)
            post.connectionErrorSignal.connect(self.showConnectionError)
            post.authErrorSignal.connect(self.logOut)
            pageLayout.addWidget(post)
        pageLayout.addStretch()

        self.ui.scrollArea_HomePosts.verticalScrollBar().setValue(0)
        self.ui.stacked_Posts.setCurrentIndex(pageIndex - 1)

    def setAccountPage(self):

        infoExe = self.__currentUser.userInfo

        if infoExe["error"]:
            if infoExe["error"]["connection"]:
                self.showConnectionError(infoExe["error"]["connection"])
            elif infoExe["error"]["auth"]:
                self.changeForm("login", QPoint(self.pos().x(), self.pos().y()))
                self.ui.stacked_Pages.setCurrentIndex(self.widgetToIndex["home"])
            return
        self.ui.frame_Error.setHidden(True)

        imageId = infoExe["data"]["image_id"]
        name = infoExe["data"]["name"]
        username = infoExe["data"]["username"]
        about = infoExe["data"]["about"]
        online = infoExe["data"]["online"]

        profileBgPicturePath = ImageTools.getPictureForWidget(self.ui.frame_AccountInfoContainer.size().width(),
                                                              self.ui.frame_AccountInfoContainer.size().height(),
                                                              0,
                                                              os.path.abspath(
                                                                  "gui/resources/images/profileBgSource.png"),
                                                              self.__fileManager.tempPath,
                                                              self.tempProfileBackgroundFileName)

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
                                                           self.tempAccountTabsBackgroundFileName)

        self.ui.frame_AccountTabsContainer.setStyleSheet(
            f"QFrame#frame_AccountTabsContainer {{border-image: url('{accountTabsBgPath}') 0 0 0 0  stretch stretch}}")

        execute = self.__fileManager.getFilePath(imageID=imageId)
        if execute["error"]:
            if execute["error"]["connection"]:
                self.showConnectionError(execute["error"]["connection"])
            elif execute["error"]["auth"]:
                self.changeForm("login", QPoint(self.pos().x(), self.pos().y()))
                self.ui.stacked_Pages.setCurrentIndex(self.widgetToIndex["home"])
            elif execute["error"]["format"]:
                self.setLabelAccountEditProfileWarning(show=True, error=execute["error"]["format"])
            return

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

        self.ui.label_AccountNickname.setText(self.getTextHTML(name, color="white", weight=700))
        self.ui.label_AccountNickname.setToolTip("@" + username)

        self.ui.label_AccountStatus.setText(self.getTextHTML(self.getOnlineCircle(online)))

        if online:
            self.ui.label_AccountStatus.setToolTip("Online")
        else:
            self.ui.label_AccountStatus.setToolTip("Offline")

        self.ui.label_AccountInformationText.setText(
            self.getTextHTML(about, color="rgb(229,235,238)", size=19, weight=100))

    def setLabelAccountEditProfileWarning(self, show=False, save=False, error=None):

        if show:
            if save:
                self.ui.label_AccountEditProfileWarning.setStyleSheet("color:rgb(0,210,0);")
                self.ui.label_AccountEditProfileWarning.setText("Saved successfully!")
                self.accountEditPhotoSet = False
                self.accountEditPhotoReset = False

            elif error:
                self.ui.label_AccountEditProfileWarning.setStyleSheet("color:rgb(255,0,0);")
                self.ui.label_AccountEditProfileWarning.setText(error)

            else:
                self.ui.label_AccountEditProfileWarning.setStyleSheet("color:rgb(255,0,0);")
                self.ui.label_AccountEditProfileWarning.setText("You have unsaved changes!")
        else:
            self.ui.label_AccountEditProfileWarning.setStyleSheet("color:rgb(0,210,0);")
            self.ui.label_AccountEditProfileWarning.setText("")
            self.accountEditPhotoSet = False
            self.accountEditPhotoReset = False

    def setAccountEditPage(self):

        self.ui.frame_AccountEditButtonsContainer.setHidden(True)
        self.accountEditPhotoReset = False
        self.accountAboutReset = False
        self.setLabelAccountEditProfileWarning(show=False)
        self.ui.line_AccountEditName.setText("")
        self.ui.line_AccountEditAbout.setText("")

        infoExe = self.__currentUser.userInfo

        if infoExe["error"]:
            if infoExe["error"]["connection"]:
                self.showConnectionError(infoExe["error"]["connection"])
                return
        self.ui.frame_Error.setHidden(True)

        imageId = infoExe["data"]["image_id"]
        name = infoExe["data"]["name"]
        username = infoExe["data"]["username"]
        about = infoExe["data"]["about"]

        execute = self.__fileManager.getFilePath(imageID=imageId)
        if execute["error"]:
            if execute["error"]["connection"]:
                self.showConnectionError(execute["error"]["connection"])
            elif execute["error"]["format"]:
                self.setLabelAccountEditProfileWarning(show=True, error=execute["error"]["format"])
            elif execute["error"]["auth"]:
                self.changeForm("login", QPoint(self.pos().x(), self.pos().y()))
                self.ui.stacked_Pages.setCurrentIndex(self.widgetToIndex["home"])
            return

        imagePath = ImageTools.getProfilePicture(execute["data"], self.__fileManager.tempPath,
                                                 self.tempAccountEditProfilePictureFileName)

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
                         self.tempAccountEditProfilePictureFileName)
        self.ui.layout_AccountEditImages.insertWidget(self.ui.layout_AccountEditImages.count() - 1, drag)
        drag.setToolTip("Drag images as files or URLs from browser")
        drag.imageDropped.connect(self.isAccountEditProfilePhotoSet)

        self.ui.line_AccountEditName.setPlaceholderText(name)
        self.ui.line_AccountEditUsername.setPlaceholderText(username)
        self.ui.line_AccountEditAbout.setPlaceholderText(about)

    def setAccountImageToDefault(self):

        if not self.updateOnline:
            return

        imageIdExe = self.__currentUser.imageID
        if imageIdExe["error"]:
            if imageIdExe["error"]["connection"]:
                self.showConnectionError(imageIdExe["error"]["connection"])
                return
        self.ui.frame_Error.setHidden(True)
        imageId = imageIdExe["data"]

        if imageId > 1:
            execute = self.__fileManager.getFilePath(imageID=1)
            if execute["error"]:
                if execute["error"]["connection"]:
                    self.showConnectionError(execute["error"]["connection"])
                elif execute["error"]["format"]:
                    self.setLabelAccountEditProfileWarning(show=True, error=execute["error"]["format"])
                return

            imagePath = ImageTools.getProfilePicture(execute["data"], self.__fileManager.tempPath,
                                                     self.tempAccountEditProfilePictureFileName)

            self.ui.frame_AccountEditPhoto.setStyleSheet(f"""QFrame {{border-image: url({imagePath}) 0 0 0 0}}""")
            self.accountEditPhotoSet = True
            self.accountEditPhotoReset = True
            self.ui.frame_AccountEditButtonsContainer.setVisible(True)
            self.setLabelAccountEditProfileWarning(show=True, save=False)

    def setAccountEditImageFromFile(self):

        fp = self.chooseFile(os.path.expanduser("~/Desktop"), "Images (*.png)")
        if not fp:
            return

        if not self.updateOnline:
            return

        imagePath = ImageTools.getProfilePicture(fp, self.__fileManager.tempPath,
                                                 self.tempAccountEditProfilePictureFileName)
        self.ui.frame_AccountEditPhoto.setStyleSheet(f"""QFrame {{border-image: url({imagePath}) 0 0 0 0}}""")
        self.accountEditPhotoSet = True
        self.ui.frame_AccountEditButtonsContainer.setVisible(True)
        self.setLabelAccountEditProfileWarning(show=True, save=False)

    def deleteAbout(self):

        self.accountAboutReset = True
        self.ui.line_AccountEditAbout.setText("")
        self.ui.line_AccountEditAbout.setPlaceholderText("")
        self.ui.frame_AccountEditButtonsContainer.setVisible(True)
        self.setLabelAccountEditProfileWarning(show=True, save=False)

    @Slot(bool)
    def isAccountEditProfilePhotoSet(self, value: bool):

        self.accountEditPhotoSet = value
        if value:
            self.ui.frame_AccountEditButtonsContainer.setVisible(True)
            self.setLabelAccountEditProfileWarning(show=True, save=False)

    def saveProfileChanges(self):

        if not self.updateOnline:
            return

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
                    self.ui.stacked_Pages.setCurrentIndex(self.widgetToIndex["home"])
                return

        if newUsername:
            formatError = self.__currentUser.changeUsername(newUsername)
            if formatError["error"]:
                if formatError["error"]["connection"]:
                    self.showConnectionError(formatError["error"]["connection"])
                elif formatError["error"]["format"]:
                    self.setLabelAccountEditProfileWarning(show=True, error=formatError["error"]["format"])
                elif formatError["error"]["auth"]:
                    self.changeForm("login", QPoint(self.pos().x(), self.pos().y()))
                    self.ui.stacked_Pages.setCurrentIndex(self.widgetToIndex["home"])
                return

        if newAbout or self.accountAboutReset:
            formatError = self.__currentUser.changeAbout(newAbout)
            if formatError["error"]:
                if formatError["error"]["connection"]:
                    self.showConnectionError(formatError["error"]["connection"])
                elif formatError["error"]["format"]:
                    self.setLabelAccountEditProfileWarning(show=True, error=formatError["error"]["format"])
                elif formatError["error"]["auth"]:
                    self.changeForm("login", QPoint(self.pos().x(), self.pos().y()))
                    self.ui.stacked_Pages.setCurrentIndex(self.widgetToIndex["home"])
                return

        imageIdExe = self.__currentUser.imageID
        if imageIdExe["error"]:
            if imageIdExe["error"]["connection"]:
                self.showConnectionError(imageIdExe["error"]["connection"])
            elif imageIdExe["error"]["auth"]:
                self.changeForm("login", QPoint(self.pos().x(), self.pos().y()))
                self.ui.stacked_Pages.setCurrentIndex(self.widgetToIndex["home"])
            return
        self.ui.frame_Error.setHidden(True)
        imageId = imageIdExe["data"]

        if self.accountEditPhotoSet:

            if self.accountEditPhotoReset:
                execute = self.__fileManager.deleteFile(imageId)
            else:
                execute = self.__fileManager.loadFile(
                    self.__fileManager.tempPath + "Just" + self.tempAccountEditProfilePictureFileName,
                    imageID=imageId)

            if execute["error"]:
                if execute["error"]["connection"]:
                    self.showConnectionError(execute["error"]["connection"])
                elif execute["error"]["format"]:
                    self.setLabelAccountEditProfileWarning(show=True, error=execute["error"]["format"])
                elif execute["error"]["auth"]:
                    self.changeForm("login", QPoint(self.pos().x(), self.pos().y()))
                    self.ui.stacked_Pages.setCurrentIndex(self.widgetToIndex["home"])
                return

            execute = self.__currentUser.changeImageID(execute["data"])
            if execute["error"]:
                if execute["error"]["connection"]:
                    self.showConnectionError(execute["error"]["connection"])
                elif execute["error"]["format"]:
                    self.setLabelAccountEditProfileWarning(show=True, error=execute["error"]["format"])
                elif execute["error"]["auth"]:
                    self.changeForm("login", QPoint(self.pos().x(), self.pos().y()))
                    self.ui.stacked_Pages.setCurrentIndex(self.widgetToIndex["home"])
                return

        self.setAccountEditPage()
        self.setLabelAccountEditProfileWarning(show=True, save=True)

    # def addPost(self, postId):
    #
    #     postUI = Post(postId, self.__postTools, self.__fileManager)
    #
    #     self.ui.layout_Posts.addWidget(postUI)

    def sortByTime(self):
        pass

    def sortByLikes(self):
        pass

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
            self.refresh()
            if pos:
                self.move(pos)
            if not self.isVisible():
                self.show()

    def logOut(self):

        self.__auth.logOut()
        self.changeForm("login", QPoint(self.pos().x(), self.pos().y()))
        self.setHomePage()
        self.ui.stacked_Pages.setCurrentIndex(self.widgetToIndex["home"])

    def refresh(self):

        self.setSideBarButtonEnabled(True)
        self.setHomePage()
        self.ui.stacked_Pages.setCurrentIndex(self.widgetToIndex["home"])

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = App()
    window.show()
    sys.exit(app.exec())
