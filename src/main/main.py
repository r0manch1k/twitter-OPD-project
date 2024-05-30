import filecmp
import sys

from PIL import Image, ImageFilter
from PySide6.QtCore import QSize, Qt, QEvent, Signal
from PySide6.QtGui import QIcon, Qt, QFontDatabase, QFont
from PySide6.QtWidgets import QMainWindow, QWidget, QLineEdit, QApplication

from gui.design.login.login import Ui_form_Login
from gui.design.main.x import Ui_MainWindow
from gui.design.registration.reg import Ui_form_Registration
from objects.ImageTools import ImageTools
from objects.Post import Post
from objects.server.Authorization import Authorization
from objects.server.DataBase import DataBase
from objects.server.FileManager import FileManager
from objects.server.UserInfo import UserInfo
from src.main.objects.server.PostTools import PostTools
from src.main.objects.widgets import DragNDrop, ProfilePictureFrame

indexToWidget = {0: "home", 1: "create", 2: "account", 3: "edit"}
widgetToIndex = {"home": 0, "create": 1, "account": 2, "edit": 3}

widgetToIndexAccountEdit = {"profile": 0, "privacy": 1, "chat": 2}


class App(Ui_MainWindow, QMainWindow):

    # photoAccountEditSet = pyqtSignal(None)

    tempAccountPictureFileName = "tempAccountPicture.png"
    tempAccountEditProfilePictureFileName = "tempAccountEditProfilePicture.png"
    tempProfileBackgroundFileName = "tempProfileBackgroundFileName.png"

    amountMaximumNameSymbols = 20
    amountMaximumAboutSymbols = 50

    def __init__(self):
        super(Ui_MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.__db = DataBase()
        self.__userInfo = UserInfo()
        self.__auth = Authorization()
        self.__fileManager = FileManager()
        self.__postTools = PostTools()

        self.__userInfo.updateConfig()

        self.authForm = None

        self.AccountEditPhotoReset = False

        self.fontThin = None  # Make cls
        self.fontMedium = None
        self.fontRegular = None
        self.fontBold = None

        self.__setMyFont()
        self.__setIconsSVG()
        self.__initSetup()
        self.setAccountPage()

        posts = self.__postTools.getPostIds(sort_by_time=True)
        for post in posts:
            self.addPost([post])

    @staticmethod
    def getTextHTML(text, color="black", size=28, weight=None):

        if weight:
            text = f"""<p><span style="color:{color};font-size:{size}px;font-weight:{weight}">{text}</span></p>"""
        else:
            text = f"""<p><span style="color:{color};font-size:{size}px;">{text}</span></p>"""
        return text

    def __setIconsSVG(self):

        # Lets Light Line Interface Icons Collection:
        # https://www.svgrepo.com/collection/lets-light-line-interface-icons/8

        icon_Logo = QIcon()
        icon_Logo.addFile("gui/resources/icons/Logo.svg", QSize(), QIcon.Normal)
        self.ui.button_Logo.setIcon(icon_Logo)
        self.ui.button_Logo.setIconSize(QSize(60, 40))

        icon_Add = QIcon()
        icon_Add.addFile("gui/resources/icons/Add.svg", QSize(), QIcon.Normal)
        self.ui.button_CreatePost.setIcon(icon_Add)
        self.ui.button_CreatePost.setIconSize(QSize(30, 30))

        icon_Chat = QIcon()
        icon_Chat.addFile("gui/resources/icons/Chat.svg", QSize(), QIcon.Normal)
        self.ui.button_Chat.setIcon(icon_Chat)
        self.ui.button_Chat.setIconSize(QSize(30, 30))

        icon_Notifications = QIcon()
        icon_Notifications.addFile("gui/resources/icons/Notifications.svg", QSize(), QIcon.Normal)
        self.ui.button_Notifications.setIcon(icon_Notifications)
        self.ui.button_Notifications.setIconSize(QSize(30, 30))

        icon_Account = QIcon()
        icon_Account.addFile("gui/resources/icons/Account.svg", QSize(), QIcon.Normal)
        self.ui.button_Account.setIcon(icon_Account)
        self.ui.button_Account.setIconSize(QSize(30, 30))

        icon_FilterPosts = QIcon()
        icon_FilterPosts.addFile("gui/resources/icons/FilterPosts.svg", QSize(), QIcon.Normal)
        self.ui.button_HomeFilterPosts.setIcon(icon_FilterPosts)
        self.ui.button_HomeFilterPosts.setIconSize(QSize(30, 30))

        icon_AccountPhotoAdd = QIcon()
        icon_AccountPhotoAdd.addFile("gui/resources/icons/AccountPhotoAdd.svg", QSize(), QIcon.Normal)
        # self.ui.button_AccountPhotoAdd.setIcon(icon_AccountPhotoAdd)
        # self.ui.button_AccountPhotoAdd.setIconSize(QSize(30, 30))

        self.ui.button_AccountEditPhotoAdd.setIcon(icon_AccountPhotoAdd)
        self.ui.button_AccountEditPhotoAdd.setIconSize(QSize(30, 30))

        icon_AccountEdit = QIcon()
        icon_AccountEdit.addFile("gui/resources/icons/AccountEdit.svg", QSize(), QIcon.Normal)
        self.ui.button_AccountEdit.setIcon(icon_AccountEdit)
        self.ui.button_AccountEdit.setIconSize(QSize(25, 25))

        icon_AccountExit = QIcon()
        icon_AccountExit.addFile("gui/resources/icons/AccountExitBlack.svg", QSize(), QIcon.Normal)
        self.ui.button_AccountExit.setIcon(icon_AccountExit)
        self.ui.button_AccountExit.setIconSize(QSize(22, 22))

        icon_AccountExitNo = QIcon()
        icon_AccountExitNo.addFile("gui/resources/icons/AccountExitNoBlack.svg", QSize(), QIcon.Normal)
        self.ui.button_AccountExitNo.setIcon(icon_AccountExitNo)
        self.ui.button_AccountExitNo.setIconSize(QSize(25, 25))

        icon_AccountExitYes = QIcon()
        icon_AccountExitYes.addFile("gui/resources/icons/AccountExitYesBlack.svg", QSize(), QIcon.Normal)
        self.ui.button_AccountExitYes.setIcon(icon_AccountExitYes)
        self.ui.button_AccountExitYes.setIconSize(QSize(25, 25))

        icon_AccountEditPhotoDelete = QIcon()
        icon_AccountEditPhotoDelete.addFile("gui/resources/icons/AccountEditPhotoDeleteBlack.svg", QSize(),
                                            QIcon.Normal)
        self.ui.button_AccountEditPhotoDelete.setIcon(icon_AccountEditPhotoDelete)
        self.ui.button_AccountEditPhotoDelete.setIconSize(QSize(30, 30))

    def __initSetup(self):

        self.ui.stacked_Pages.setCurrentIndex(widgetToIndex["home"])

        for button in self.ui.buttonGroup_MainTabs.buttons():
            button.clicked.connect(self.switchPage)
        self.ui.button_AccountEdit.clicked.connect(self.switchPage)
        for button in self.ui.buttonGroup_AccountEditTabs.buttons():
            button.clicked.connect(self.switchPage)

        self.ui.frame_SideBarChat.setHidden(True)
        self.ui.frame_SideBarNotifications.setHidden(True)
        self.ui.frame_AccountExitConfirmation.setHidden(True)
        self.ui.frame_Error.setHidden(True)

        self.ui.button_AccountExitNo.installEventFilter(self)
        self.ui.button_AccountExitYes.installEventFilter(self)
        self.ui.button_AccountExit.installEventFilter(self)
        self.ui.button_AccountEditPhotoDelete.installEventFilter(self)
        self.ui.line_AccountEditName.installEventFilter(self)
        self.ui.line_AccountEditAbout.installEventFilter(self)

        self.ui.button_AccountExitYes.clicked.connect(self.logOut)
        self.ui.button_AccountEditProfileSave.clicked.connect(self.saveProfileChanges)
        self.ui.button_AccountEditPhotoDelete.clicked.connect(self.setAccountPhotoToDefault)
        self.ui.button_AccountEditProfileCancel.clicked.connect(self.setAccountEditPage)

        self.setLabelAccountEditProfileWarning(closed=True)

        self.ui.frame_AccountInfo.setAttribute(Qt.WidgetAttribute.WA_TranslucentBackground)
        self.ui.frame_AccountButtons.setAttribute(Qt.WidgetAttribute.WA_TranslucentBackground)
        self.ui.frame_AccountLabels_1.setAttribute(Qt.WidgetAttribute.WA_TranslucentBackground)
        self.ui.label_AccountStatus.setAttribute(Qt.WidgetAttribute.WA_TranslucentBackground)
        self.ui.label_AccountNickname.setAttribute(Qt.WidgetAttribute.WA_TranslucentBackground)
        self.ui.frame_AccountExitConfirmation.setAttribute(Qt.WidgetAttribute.WA_TranslucentBackground)
        self.ui.frame_AccountInformationContainer.setAttribute(Qt.WidgetAttribute.WA_TranslucentBackground)
        self.ui.label_AccountInformationText.setAttribute(Qt.WidgetAttribute.WA_TranslucentBackground)
        self.ui.label_AccountInformationID.setAttribute(Qt.WidgetAttribute.WA_TranslucentBackground)
        self.ui.label_AccountInformationAccess.setAttribute(Qt.WidgetAttribute.WA_TranslucentBackground)

        self.ui.frame_AccountInfoContainer.setStyleSheet(f"QFrame#frame_AccountInfoContainer {{border-image: url("
                                                         f":/files/images/profileBgSource.png) 0 0 0"
                                                         f" 0 stretch stretch}};")

        self.ui.line_AccountEditName.setMaxLength(self.amountMaximumNameSymbols)

        self.ui.label_AccountEditNameSymbols.setText(
            f"There are {self.amountMaximumNameSymbols - len(self.ui.line_AccountEditName.text())} characters left.")
        self.ui.label_AccountEditAboutSymbols.setText(
            f"There are {self.amountMaximumAboutSymbols - len(self.ui.line_AccountEditAbout.toPlainText())} "
            f"characters left.")

        # self.ui.label_AccountEditSettings.setFont(self.fontRegular)
        #
        # self.ui.label.setFont(self.fontThin)
        # self.ui.label_AccountInformationAccess.setFont(self.fontThin)
        # self.ui.label_2.setFont(self.fontThin)
        # self.ui.label_AccountEditProfileWarning.setFont(self.fontThin)

        self.ui.label_AccountNickname.setFont(self.fontBold)
        self.ui.label_AccountInformationText.setFont(self.fontRegular)
        self.ui.label_AccountInformationID.setFont(self.fontRegular)
        self.ui.label_AccountInformationAccess.setFont(self.fontRegular)

        self.ui.frame_HomePosts.setStyleSheet(
            "#frame_HomePosts {border-image: url('postsBg.png') 0 0 0 0  stretch stretch}")

    def __setMyFont(self):

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

    def eventFilter(self, watched, event):

        if watched == self.ui.button_AccountExitYes:

            if event.type() == QEvent.Type.HoverEnter:

                icon = QIcon()
                icon.addFile("gui/resources/icons/AccountExitYesWhite.svg", QSize(), QIcon.Normal)
                watched.setIcon(icon)
                watched.setIconSize(QSize(25, 25))

                watched.setStyleSheet("background-color: rgb(255, 0, 0)")
                return True

            elif event.type() == QEvent.Type.HoverLeave:

                icon = QIcon()
                icon.addFile("gui/resources/icons/AccountExitYesBlack.svg", QSize(), QIcon.Normal)
                watched.setIcon(icon)
                watched.setIconSize(QSize(25, 25))

                watched.setStyleSheet("background-color: rgb(229, 235, 238)")
                return True

        elif watched == self.ui.button_AccountExitNo:

            if event.type() == QEvent.Type.HoverEnter:

                icon = QIcon()
                icon.addFile("gui/resources/icons/AccountExitNoWhite.svg", QSize(), QIcon.Normal)
                watched.setIcon(icon)
                watched.setIconSize(QSize(25, 25))

                watched.setStyleSheet("background-color: #208b3a")
                return True

            elif event.type() == QEvent.Type.HoverLeave:

                icon = QIcon()
                icon.addFile("gui/resources/icons/AccountExitNoBlack.svg", QSize(), QIcon.Normal)
                watched.setIcon(icon)
                watched.setIconSize(QSize(25, 25))

                watched.setStyleSheet("background-color: rgb(229, 235, 238)")
                return True

        elif watched == self.ui.button_AccountExit:

            if event.type() == QEvent.Type.HoverEnter:

                icon = QIcon()
                icon.addFile("gui/resources/icons/AccountExitWhite.svg", QSize(), QIcon.Normal)
                watched.setIcon(icon)
                watched.setIconSize(QSize(22, 22))

                watched.setStyleSheet("background-color: rgb(255, 0, 0)")
                return True

            elif event.type() == QEvent.Type.HoverLeave:

                icon = QIcon()
                icon.addFile("gui/resources/icons/AccountExitBlack.svg", QSize(), QIcon.Normal)
                watched.setIcon(icon)
                watched.setIconSize(QSize(22, 22))

                watched.setStyleSheet("background-color: rgb(229,235,238)")
                return True

        elif watched == self.ui.button_AccountEditPhotoDelete:

            if event.type() == QEvent.Type.HoverEnter:

                icon = QIcon()
                icon.addFile("gui/resources/icons/AccountEditPhotoDeleteWhite.svg", QSize(), QIcon.Normal)
                watched.setIcon(icon)
                watched.setIconSize(QSize(30, 30))

                watched.setStyleSheet("background-color: rgb(240, 0, 0)")
                return True

            elif event.type() == QEvent.Type.HoverLeave:

                icon = QIcon()
                icon.addFile("gui/resources/icons/AccountEditPhotoDeleteBlack.svg", QSize(), QIcon.Normal)
                watched.setIcon(icon)
                watched.setIconSize(QSize(30, 30))

                watched.setStyleSheet("background-color: rgb(229,235,238)")
                return True

        elif watched == self.ui.line_AccountEditName or watched == self.ui.line_AccountEditAbout:

            if event.type() == QEvent.Type.KeyPress:

                if len(self.ui.line_AccountEditAbout.toPlainText()) > self.amountMaximumAboutSymbols:
                    self.ui.line_AccountEditAbout.textCursor().deletePreviousChar()

            if event.type() == QEvent.Type.KeyRelease:

                if len(self.ui.line_AccountEditAbout.toPlainText()) > self.amountMaximumAboutSymbols:
                    self.ui.line_AccountEditAbout.textCursor().deletePreviousChar()

                self.ui.label_AccountEditNameSymbols.setText(
                    f"There is {self.amountMaximumNameSymbols - len(self.ui.line_AccountEditName.text())} "
                    f"characters left.")
                self.ui.label_AccountEditAboutSymbols.setText(
                    f"There is {self.amountMaximumAboutSymbols - len(self.ui.line_AccountEditAbout.toPlainText())} "
                    f"characters left.")

                if (self.ui.line_AccountEditName.text() or self.ui.line_AccountEditAbout.toPlainText()
                        or self.AccountEditPhotoReset):

                    self.setLabelAccountEditProfileWarning(saved=False)

                else:

                    self.setLabelAccountEditProfileWarning(closed=True)

        return False

    def switchPage(self):

        if self.sender() == self.ui.button_Logo:
            self.ui.stacked_Pages.setCurrentIndex(widgetToIndex["home"])

        elif self.sender() == self.ui.button_CreatePost:
            self.ui.stacked_Pages.setCurrentIndex(widgetToIndex["create"])

        elif self.sender() == self.ui.button_Account:

            self.ui.button_AccountExitNo.setChecked(True)

            if self.__userInfo.userID < 0:
                self.openAuthForm()

            self.setAccountPage()

            self.ui.stacked_Pages.setCurrentIndex(widgetToIndex["account"])

        elif self.sender() == self.ui.button_AccountEdit:

            self.setAccountEditPage()

            self.ui.stacked_Pages.setCurrentIndex(widgetToIndex["edit"])

        elif self.sender() == self.ui.button_AccountEditTabsProfile:

            self.ui.stacked_AccountEditTabs.setCurrentIndex(widgetToIndexAccountEdit["profile"])

        elif self.sender() == self.ui.button_AccountEditTabsPrivacy:

            self.ui.stacked_AccountEditTabs.setCurrentIndex(widgetToIndexAccountEdit["privacy"])

        elif self.sender() == self.ui.button_AccountEditTabsChat:

            self.ui.stacked_AccountEditTabs.setCurrentIndex(widgetToIndexAccountEdit["chat"])

    def setAccountPage(self):

        if self.__userInfo.userID > 0:

            fp = self.__fileManager.getFilePath(imageID=self.__userInfo.imageID)
            # imagePath = ImageTools.getProfilePicture(fp, self.__fileManager.tempPath, self.tempAccountPictureFileName)

            # print(imagePath)

            for i in range(self.ui.layout_AccountInfoContainer.count()):
                if (self.ui.layout_AccountInfoContainer.itemAt(i).widget()
                        and isinstance(self.ui.layout_AccountInfoContainer.itemAt(i).widget(), ProfilePictureFrame)):
                    self.ui.layout_AccountInfoContainer.itemAt(i).widget().setVisible(False)
                    self.ui.layout_AccountInfoContainer.removeWidget(
                        self.ui.layout_AccountInfoContainer.itemAt(i).widget())
                    break

            profilePictureFrame = ProfilePictureFrame(fp)
            self.ui.layout_AccountInfoContainer.insertWidget(0, profilePictureFrame)

            self.ui.label_AccountNickname.setText(self.getTextHTML(self.__userInfo.name))

            self.ui.label_AccountStatus.setText(self.getTextHTML("●", "rgb(5,168,22)", 18))

            self.ui.label_AccountInformationText.setText(self.getTextHTML(self.__userInfo.info, size=13, weight=100))

            self.ui.label_AccountInformationID.setText(
                self.getTextHTML("ID: " + str(self.__userInfo.userID), size=10, weight=100))

        else:
            self.ui.stacked_Pages.setCurrentIndex(widgetToIndex["home"])

    def setLabelAccountEditProfileWarning(self, saved=False, closed=False):

        if not closed:
            if saved:
                self.ui.label_AccountEditProfileWarning.setStyleSheet("color:rgb(0,210,0);")
                self.ui.label_AccountEditProfileWarning.setText("Saved successfully!")
            else:
                self.ui.label_AccountEditProfileWarning.setStyleSheet("color:rgb(255,0,0);")
                self.ui.label_AccountEditProfileWarning.setText("You have unsaved changes!")
        else:
            self.ui.label_AccountEditProfileWarning.setStyleSheet("color:rgb(0,210,0);")
            self.ui.label_AccountEditProfileWarning.setText("")

    def setAccountEditPage(self):

        self.AccountEditPhotoReset = False
        self.setLabelAccountEditProfileWarning(closed=True)
        self.ui.line_AccountEditName.setText("")
        self.ui.line_AccountEditAbout.setText("")

        if self.__userInfo.userID >= 0:
            fp = self.__fileManager.getFilePath(imageID=self.__userInfo.imageID)
            imagePath = ImageTools.getProfilePicture(fp, self.__fileManager.tempPath,
                                                     self.tempAccountEditProfilePictureFileName)

            self.ui.frame_AccountEditPhoto.setStyleSheet(f"""QFrame {{border-image: url({imagePath}) 0 0 0 0}}""")

            widgetsToDelete = []
            for i in range(self.ui.layout_AccountEditImages.count()):
                if (self.ui.layout_AccountEditImages.itemAt(i).widget()
                        and self.ui.layout_AccountEditImages.itemAt(i).widget() != self.ui.frame_AccountEditPhoto):
                    widgetsToDelete.append(self.ui.layout_AccountEditImages.itemAt(i).widget())
            for widget in widgetsToDelete:
                widget.setVisible(False)
                self.ui.layout_AccountEditImages.removeWidget(widget)

            drag = DragNDrop(self.ui.frame_AccountEditPhoto, self.__fileManager.tempPath,
                             "Just" + self.tempAccountEditProfilePictureFileName)
            self.ui.layout_AccountEditImages.insertWidget(self.ui.layout_AccountEditImages.count() - 1, drag)

            # drag.

            self.ui.line_AccountEditName.setPlaceholderText(self.__userInfo.name)
            self.ui.line_AccountEditAbout.setPlaceholderText(self.__userInfo.info)

    def setAccountPhotoToDefault(self):

        if self.__userInfo.imageID > 1:
            fp = self.__fileManager.getFilePath(imageID=1)
            imagePath = ImageTools.getProfilePicture(fp, self.__fileManager.tempPath,
                                                     self.tempAccountEditProfilePictureFileName)

            self.ui.frame_AccountEditPhoto.setStyleSheet(f"""QFrame {{border-image: url({imagePath}) 0 0 0 0}}""")

            self.AccountEditPhotoReset = True
            self.setLabelAccountEditProfileWarning(saved=False)

    def saveProfileChanges(self):

        newName = self.ui.line_AccountEditName.text()
        newAbout = self.ui.line_AccountEditAbout.toPlainText()

        if newName:
            self.__userInfo.changeName(newName)

        if newAbout:
            self.__userInfo.changeInfo(newAbout)

        if not self.__db.connect():
            return

        if not filecmp.cmp(self.__fileManager.tempPath + self.tempAccountEditProfilePictureFileName,
                           self.__fileManager.tempPath + self.tempAccountPictureFileName):

            if self.AccountEditPhotoReset:
                self.__fileManager.deleteFile(self.__userInfo.imageID)
                imageID = 1
            else:
                imageID = self.__fileManager.loadFile(
                    self.__fileManager.tempPath + "Just" + self.tempAccountEditProfilePictureFileName,
                    imageID=self.__userInfo.imageID)

            self.__userInfo.changeImageID(imageID)

        self.setAccountEditPage()
        self.setLabelAccountEditProfileWarning(saved=True)

    def addPost(self, id):

        postInfo = self.__postTools.getPostInfo(id)[0]

        userImagePath = self.__fileManager.getFilePath(1)


        postUI = Post("Petya", "xuesosina", userImagePath, postInfo["post_text"],
                      postInfo["post_time"], 100, 20, 2)

        self.ui.layout_Posts.addWidget(postUI)

    def logOut(self):

        self.__auth.logOut()
        self.refresh()
        self.ui.stacked_Pages.setCurrentIndex(0)

    def openAuthForm(self, form="login"):

        if form == "login":
            self.authForm = LoginForm(self)

        elif form == "reg":
            self.authForm = RegistrationForm(self)

        self.hide()
        self.authForm.move(self.pos().x(), self.pos().y())
        self.authForm.show()

    def refresh(self):

        self.__initSetup()
        self.setAccountPage()
        self.authForm = None


class RegistrationForm(Ui_form_Registration, QWidget):
    def __init__(self, parent: App):
        super(Ui_form_Registration, self).__init__()
        self.login = None
        self.ui = Ui_form_Registration()
        self.ui.setupUi(self)

        self.db = DataBase()
        self.auth = Authorization()

        self.parent = parent
        self.button_IconPasswordVisibility = {}

        self.setIconsSVG()
        self.initSetup()

    def setIconsSVG(self):

        icon_Back = QIcon()
        icon_Back.addFile("gui/resources/icons/AuthBack.svg", QSize(), QIcon.Normal)
        self.ui.button_ControlBack.setIcon(icon_Back)
        self.ui.button_ControlBack.setIconSize(QSize(30, 30))

        icon_PasswordVisibilityOn = QIcon()
        icon_PasswordVisibilityOn.addFile("gui/resources/icons/PasswordVisibilityOn.svg", QSize(), QIcon.Normal)
        self.ui.button_PasswordVisibility.setIcon(icon_PasswordVisibilityOn)
        self.ui.button_PasswordVisibility.setIconSize(QSize(25, 25))

        icon_PasswordVisibilityOff = QIcon()
        icon_PasswordVisibilityOff.addFile("gui/resources/icons/PasswordVisibilityOff.svg", QSize(), QIcon.Normal)

        self.button_IconPasswordVisibility[True] = icon_PasswordVisibilityOn
        self.button_IconPasswordVisibility[False] = icon_PasswordVisibilityOff

    def setPasswordVisibility(self):

        if self.sender().isChecked():
            self.ui.line_Password.setEchoMode(QLineEdit.EchoMode.Normal)
            self.ui.button_PasswordVisibility.setIcon(self.button_IconPasswordVisibility[False])
        else:
            self.ui.line_Password.setEchoMode(QLineEdit.EchoMode.Password)
            self.ui.button_PasswordVisibility.setIcon(self.button_IconPasswordVisibility[True])
        self.ui.button_PasswordVisibility.setIconSize(QSize(25, 25))

    def initSetup(self, bg_fp="gui/resources/images/RegistrationForm.png"):

        window_width = 1000
        window_height = 550
        image = Image.open(bg_fp)
        image_width, image_height = image.size
        image = image.filter(ImageFilter.SMOOTH)
        for _ in range(10):
            image = image.filter(ImageFilter.SMOOTH_MORE)
        image = image.crop((int((image_width - window_width) / 2), int((image_height - window_height) / 2),
                            int(image_width - (image_width - window_width) / 2),
                            int(image_height - (image_height - window_height) / 2)))
        image.save("gui/resources/images/rendered/RegistrationForm.png")
        self.ui.frame_Main.setStyleSheet("""
                                         QFrame#frame_Main {border-image: url(
                                         gui/resources/images/rendered/RegistrationForm.png) 0 0 0 0 stretch stretch}
                                         """)

        self.ui.label_FormatError.setHidden(True)
        self.ui.button_PasswordVisibility.toggled.connect(self.setPasswordVisibility)

        self.ui.textBrowser_Rules.setAcceptRichText(True)
        with open("gui/resources/html/AuthRules") as f:
            self.ui.textBrowser_Rules.append(f.read())
        self.ui.textBrowser_Rules.document().setDocumentMargin(0)

        self.ui.textBrowser_LogIn.setAcceptRichText(True)
        with open("gui/resources/html/AuthToLogin") as f:
            self.ui.textBrowser_LogIn.append(f.read())
        self.ui.textBrowser_LogIn.document().setDocumentMargin(0)
        self.ui.textBrowser_LogIn.anchorClicked.connect(self.setLogInForm)

        self.ui.button_ControlBack.clicked.connect(self.exit)
        self.ui.button_SignIn.clicked.connect(self.signIn)

    def signIn(self):

        if not self.db.connect():
            self.ui.label_FormatError.setVisible(True)
            self.ui.label_FormatError.setText("CONNECTION ERROR")
            return

        name = self.ui.line_Login_2.text()
        login = self.ui.line_Login.text()
        password = self.ui.line_Password.text()

        error = self.auth.signIn(login, password, name)

        if self.auth.logIn(login, password):
            self.ui.label_FormatError.setVisible(True)
            self.ui.label_FormatError.setText(error)
        else:
            self.exit()

    def setLogInForm(self):

        self.hide()
        self.login = LoginForm(self.parent)
        self.login.move(self.pos().x(), self.pos().y())
        self.login.show()

    def exit(self):

        self.hide()
        self.parent.move(self.pos().x(), self.pos().y())
        self.parent.show()
        self.parent.refresh()


class LoginForm(Ui_form_Login, QWidget):
    def __init__(self, parent: App):
        super(Ui_form_Login, self).__init__()
        self.ui = Ui_form_Login()
        self.ui.setupUi(self)

        self.parent = parent

        self.auth = Authorization()
        self.db = DataBase()
        self.regForm = RegistrationForm(self.parent)

        self.button_IconPasswordVisibility = {}

        self.setIconsSVG()
        self.initSetup()

    def setIconsSVG(self):

        icon_Back = QIcon()
        icon_Back.addFile("gui/resources/icons/AuthBack.svg", QSize(), QIcon.Normal)
        self.ui.button_ControlBack.setIcon(icon_Back)
        self.ui.button_ControlBack.setIconSize(QSize(30, 30))

        icon_PasswordVisibilityOn = QIcon()
        icon_PasswordVisibilityOn.addFile("gui/resources/icons/PasswordVisibilityOn.svg", QSize(), QIcon.Normal)
        self.ui.button_PasswordVisibility.setIcon(icon_PasswordVisibilityOn)
        self.ui.button_PasswordVisibility.setIconSize(QSize(25, 25))

        icon_PasswordVisibilityOff = QIcon()
        icon_PasswordVisibilityOff.addFile("gui/resources/icons/PasswordVisibilityOff.svg", QSize(), QIcon.Normal)

        self.button_IconPasswordVisibility[True] = icon_PasswordVisibilityOn
        self.button_IconPasswordVisibility[False] = icon_PasswordVisibilityOff

    def initSetup(self, bg_fp="gui/resources/images/LoginForm.png"):

        window_width, window_height = 1000, 550
        image = Image.open(bg_fp)
        image_width, image_height = image.size
        # image_rgba = Image.new("RGBA", (image_width, image_height), 255)
        # image_rgba.paste(image, (0, 0))
        image_rgba = image.crop((int((image_width - window_width) / 2), int((image_height - window_height) / 2),
                                 int(image_width - (image_width - window_width) / 2),
                                 int(image_height - (image_height - window_height) / 2)))
        image_rgba.save("gui/resources/images/rendered/LoginForm.png")
        self.ui.frame_Main.setStyleSheet("""
                                         QFrame#frame_Main {border-image: url(
                                         gui/resources/images/rendered/LoginForm.png) 0 0 0 0 stretch stretch}
                                         """)

        self.ui.label_FormatError.setHidden(True)
        self.ui.button_PasswordVisibility.toggled.connect(self.setPasswordVisibility)

        self.ui.textBrowser_Rules.setAcceptRichText(True)
        with open("gui/resources/html/AuthRules") as f:
            self.ui.textBrowser_Rules.append(f.read())
        self.ui.textBrowser_Rules.document().setDocumentMargin(0)

        self.ui.textBrowser_LogIn.setAcceptRichText(True)
        with open("gui/resources/html/AuthToReg") as f:
            self.ui.textBrowser_LogIn.append(f.read())
        self.ui.textBrowser_LogIn.document().setDocumentMargin(0)
        self.ui.textBrowser_LogIn.anchorClicked.connect(self.setRegForm)

        self.ui.button_ControlBack.clicked.connect(self.exit)
        self.ui.button_LogIn.clicked.connect(self.logIn)

    def setPasswordVisibility(self):

        if self.sender().isChecked():
            self.ui.line_Password.setEchoMode(QLineEdit.EchoMode.Normal)
            self.ui.button_PasswordVisibility.setIcon(self.button_IconPasswordVisibility[False])
        else:
            self.ui.line_Password.setEchoMode(QLineEdit.EchoMode.Password)
            self.ui.button_PasswordVisibility.setIcon(self.button_IconPasswordVisibility[True])
        self.ui.button_PasswordVisibility.setIconSize(QSize(25, 25))

    def logIn(self):

        if not self.db.connect():
            self.ui.label_FormatError.setVisible(True)
            self.ui.label_FormatError.setText("CONNECTION ERROR")
            return

        login = self.ui.line_Login.text()
        password = self.ui.line_Password.text()

        error = self.auth.logIn(login, password)

        if self.auth.logIn(login, password):
            self.ui.label_FormatError.setVisible(True)
            self.ui.label_FormatError.setText(error)
        else:
            self.exit()

    def setRegForm(self):

        self.hide()
        self.regForm = RegistrationForm(self.parent)
        self.regForm.move(self.pos().x(), self.pos().y())
        self.regForm.show()

    def exit(self):

        self.hide()
        self.parent.move(self.pos().x(), self.pos().y())
        self.parent.show()
        self.parent.refresh()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = App()
    window.show()
    sys.exit(app.exec())
