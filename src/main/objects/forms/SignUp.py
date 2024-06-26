import os

from PySide6.QtCore import QSize, Signal, QPoint, QTimer, Qt, QEvent
from PySide6.QtGui import QIcon, QColor
from PySide6.QtWidgets import QWidget, QLineEdit, QLabel, QGraphicsDropShadowEffect

from src.main.gui.design.signup.signup import Ui_form_SignUp
from src.main.objects.ImageTools import ImageTools
from src.main.objects.server.Authorization import Authorization
from src.main.objects.server.FileManager import FileManager

from src.main.objects.widgets import InfoBar


class SignUpForm(Ui_form_SignUp, QWidget):

    exitSignal = Signal(str, QPoint)

    formChangedSignal = Signal(str, QPoint)

    widgetToIndex = {"main": 0, "verify": 1}

    tempSignUpBgFileName = "tempSignUpBg.png"

    awaitingTime = 90

    def __init__(self, auth: Authorization, fileManger: FileManager):
        super(Ui_form_SignUp, self).__init__()

        self.ui = Ui_form_SignUp()
        self.ui.setupUi(self)

        self.__auth = auth
        self.__fileManager = fileManger

        self.timer = QTimer(self)
        self.timeCounter = 0

        self.__name = None
        self.__username = None
        self.__email = None
        self.__password = None

        self.dictPasswordVisIcons = {}
        self.dictCodeSentIcons = {}
        self.errorBar = None

        self.__setIconsSVG()
        self.__initSetup()
        self.__setShadow()

    def __setIconsSVG(self):

        icon_Back = QIcon()
        icon_Back.addFile(":icons/icons/AuthBack.svg", QSize(), QIcon.Normal)
        self.ui.button_ControlBack.setIcon(icon_Back)
        self.ui.button_ControlBack.setIconSize(QSize(30, 30))

        icon_PasswordVisibilityOn = QIcon()
        icon_PasswordVisibilityOn.addFile(":icons/icons/PasswordVisibilityOn.svg", QSize(), QIcon.Normal)
        self.ui.button_PasswordVisibility.setIcon(icon_PasswordVisibilityOn)
        self.ui.button_PasswordVisibility.setIconSize(QSize(25, 25))

        icon_PasswordVisibilityOff = QIcon()
        icon_PasswordVisibilityOff.addFile(":icons/icons/PasswordVisibilityOff.svg", QSize(), QIcon.Normal)
        self.dictPasswordVisIcons[True] = icon_PasswordVisibilityOn
        self.dictPasswordVisIcons[False] = icon_PasswordVisibilityOff

    def __initSetup(self):

        signUpBgPath = ImageTools.getPictureForWidget(self.ui.page_Main.width(),
                                                      self.ui.page_Main.height(),
                                                      250,
                                                      os.path.abspath("gui/resources/images/signUpBg.png"),
                                                      self.__fileManager.tempPath,
                                                      self.tempSignUpBgFileName)

        self.ui.frame_Main.setStyleSheet(
            f"QFrame#frame_Main {{border-image: url('{signUpBgPath}') 0 0 0 0 stretch stretch}}")
        self.ui.frame_Verify.setStyleSheet(
            f"QFrame#frame_Verify {{border-image: url('{signUpBgPath}') 0 0 0 0 stretch stretch}}")

        self.ui.stacked_Main.setCurrentIndex(self.widgetToIndex["main"])

        self.ui.label_SignUpError.setHidden(True)
        self.ui.label_VerifyError.setHidden(True)
        self.ui.textBrowser_ResendTimer.setHidden(True)
        self.ui.button_PasswordVisibility.toggled.connect(self.setPasswordVisibility)

        self.ui.textBrowser_ResendTimer.setAcceptRichText(True)
        self.ui.textBrowser_ResendTimer.document().setDocumentMargin(0)
        self.ui.textBrowser_ResendTimer.anchorClicked.connect(self.sendCode)

        self.ui.textBrowser_Rules.setAcceptRichText(True)
        with open(os.path.abspath("gui/resources/html/rules.txt")) as f:
            self.ui.textBrowser_Rules.append(f.read())
        self.ui.textBrowser_Rules.document().setDocumentMargin(0)

        self.ui.textBrowser_VerifyAbout.document().setDocumentMargin(0)

        self.ui.textBrowser_toLogIn.setAcceptRichText(True)
        with open(os.path.abspath("gui/resources/html/toLogIn.txt")) as f:
            self.ui.textBrowser_toLogIn.append(f.read())
        self.ui.textBrowser_toLogIn.document().setDocumentMargin(0)
        self.ui.textBrowser_toLogIn.anchorClicked.connect(self.switchPage)

        self.ui.textBrowser_VerifyBack.setAcceptRichText(True)
        with open(os.path.abspath("gui/resources/html/goBack.txt")) as f:
            self.ui.textBrowser_VerifyBack.append(f.read())
        self.ui.textBrowser_VerifyBack.document().setDocumentMargin(0)
        self.ui.textBrowser_VerifyBack.anchorClicked.connect(self.switchPage)

        self.ui.textBrowser_toLogIn.setLineWrapColumnOrWidth(0)
        self.ui.textBrowser_VerifyBack.setLineWrapColumnOrWidth(0)
        self.ui.textBrowser_ResendTimer.setLineWrapColumnOrWidth(0)

        self.ui.textBrowser_toLogIn.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.ui.textBrowser_VerifyBack.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.ui.textBrowser_ResendTimer.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)

        self.ui.line_Name.installEventFilter(self)
        self.ui.line_Code.installEventFilter(self)
        self.ui.line_Email.installEventFilter(self)
        self.ui.line_Password.installEventFilter(self)
        self.ui.line_Username.installEventFilter(self)

        self.ui.button_NextStep.clicked.connect(self.switchPage)
        self.ui.button_ControlBack.clicked.connect(self.switchPage)
        self.ui.button_VerifyEmail.clicked.connect(self.verifyEmail)

        self.timer.timeout.connect(self.timeUpdate)

    def __setShadow(self):

        self.__shadowBlurRadius = 10.0
        self.__borderWidth = 1
        self.__shadowMargin = 0
        self.__borderRadius = 12.0

        self.__effectSideBar = QGraphicsDropShadowEffect()
        self.__effectSideBar.setBlurRadius(self.__shadowBlurRadius)
        self.__effectSideBar.setColor(QColor(0, 0, 0, 127))
        self.__effectSideBar.setOffset(3.0)
        self.ui.button_ControlBack.setGraphicsEffect(self.__effectSideBar)
        self.ui.button_ControlBack.repaint()

        self.__effectVerify = QGraphicsDropShadowEffect()
        self.__effectVerify.setBlurRadius(self.__shadowBlurRadius)
        self.__effectVerify.setColor(QColor(0, 0, 0, 127))
        self.__effectVerify.setOffset(5.0)
        self.ui.frame_Verify_2.setGraphicsEffect(self.__effectVerify)
        self.ui.frame_Verify_2.repaint()

        self.__effectSignUp = QGraphicsDropShadowEffect()
        self.__effectSignUp.setBlurRadius(self.__shadowBlurRadius)
        self.__effectSignUp.setColor(QColor(0, 0, 0, 127))
        self.__effectSignUp.setOffset(5.0)
        self.ui.frame_SignUp_2.setGraphicsEffect(self.__effectSignUp)
        self.ui.frame_SignUp_2.repaint()

    def eventFilter(self, watched, event):

        if watched == self.ui.line_Name:

            if event.type() == QEvent.Type.KeyRelease:

                if self.ui.line_Name.text():

                    self.ui.line_Name.setStyleSheet("QLineEdit { border: 0; color: black; }")

                else:

                    self.ui.line_Name.setStyleSheet("QLineEdit { border: 1px solid red; color: red; }")

                return True

        elif watched == self.ui.line_Username:

            if event.type() == QEvent.Type.KeyRelease:

                if self.ui.line_Username.text():

                    self.ui.frame_Username.setStyleSheet("QFrame#frame_Username { border: 0; }")
                    self.ui.line_Username.setStyleSheet("QLineEdit { color: black; }")

                else:

                    self.ui.frame_Username.setStyleSheet("QFrame#frame_Username { border: 1px solid red; }")
                    self.ui.line_Username.setStyleSheet("QLineEdit { color: red; }")

                return True

        elif watched == self.ui.line_Email:

            if event.type() == QEvent.Type.KeyRelease:

                if self.ui.line_Email.text():

                    self.ui.line_Email.setStyleSheet("QLineEdit { border: 0; color: black; }")

                else:

                    self.ui.line_Email.setStyleSheet("QLineEdit { border: 1px solid red; color: red; }")

                return True

        elif watched == self.ui.line_Password:

            if event.type() == QEvent.Type.KeyRelease:

                if self.ui.line_Password.text():

                    self.ui.frame_PasswordInput.setStyleSheet("QFrame#frame_PasswordInput { border: 0; }")
                    self.ui.line_Password.setStyleSheet("QLineEdit { color: black; }")

                else:

                    self.ui.frame_PasswordInput.setStyleSheet("QFrame#frame_PasswordInput { border: 1px solid red; }")
                    self.ui.line_Password.setStyleSheet("QLineEdit { color: red; }")

                return True

        elif watched == self.ui.line_Code:

            if event.type() == QEvent.Type.KeyRelease:

                if self.ui.line_Code.text():

                    self.ui.line_Code.setStyleSheet("QLineEdit { border: 0; color: black; }")

                else:

                    self.ui.line_Code.setStyleSheet("QLineEdit { border: 1px solid red; color: red; }")

                return True

        return False

    def setPasswordVisibility(self):

        if self.sender().isChecked():
            self.ui.line_Password.setEchoMode(QLineEdit.EchoMode.Normal)
            self.ui.button_PasswordVisibility.setIcon(self.dictPasswordVisIcons[False])
        else:
            self.ui.line_Password.setEchoMode(QLineEdit.EchoMode.Password)
            self.ui.button_PasswordVisibility.setIcon(self.dictPasswordVisIcons[True])
        self.ui.button_PasswordVisibility.setIconSize(QSize(25, 25))

    def switchPage(self):

        if self.sender() == self.ui.button_NextStep:

            self.nextStep()
            self.ui.label_VerifyError.setHidden(True)
            self.ui.textBrowser_ResendTimer.setHidden(True)
            self.ui.line_Code.setText("")
            self.ui.line_Code.setStyleSheet("QLineEdit { border: 0; color: black; }")

        elif self.sender() == self.ui.textBrowser_VerifyBack:

            self.ui.label_SignUpError.setHidden(True)
            self.ui.line_Name.setText("")
            self.ui.line_Username.setText("")
            self.ui.line_Email.setText("")
            self.ui.line_Password.setText("")
            self.ui.line_Name.setStyleSheet("QLineEdit { border: 0; color: black; }")
            self.ui.frame_Username.setStyleSheet("QFrame#frame_Username { border: 0; }")
            self.ui.line_Username.setStyleSheet("QLineEdit { color: black; }")
            self.ui.line_Email.setStyleSheet("QLineEdit { border: 0; color: black; }")
            self.ui.frame_PasswordInput.setStyleSheet("QFrame#frame_PasswordInput { border: 0; }")
            self.ui.line_Password.setStyleSheet("QLineEdit { color: black; }")
            self.__name = self.__username = self.__email = self.__password = None
            self.ui.stacked_Main.setCurrentIndex(self.widgetToIndex["main"])

        elif self.sender() == self.ui.textBrowser_toLogIn:

            self.toLogIn()

        elif self.sender() == self.ui.button_ControlBack:

            self.exit()

    def setVerifyAboutText(self):

        self.ui.textBrowser_VerifyAbout.setAcceptRichText(True)
        with open(os.path.abspath("gui/resources/html/submitAbout.txt")) as f:
            self.ui.textBrowser_VerifyAbout.setText("")
            text = f.read().replace("###", self.__email)
            self.ui.textBrowser_VerifyAbout.append(text)
        self.ui.textBrowser_VerifyAbout.document().setDocumentMargin(0)

    def setResendTimerText(self):

        with open(os.path.abspath("gui/resources/html/resendCode.txt")) as f:
            self.ui.textBrowser_ResendTimer.setText("")
            self.ui.textBrowser_ResendTimer.append(f.read())
        self.ui.textBrowser_ResendTimer.anchorClicked.connect(self.sendCode)
        self.ui.textBrowser_ResendTimer.setOpenLinks(True)
        self.ui.textBrowser_ResendTimer.setVisible(True)

    def isError(self, label: QLabel, execute: dict) -> bool:

        if not execute["error"]:
            return False

        if execute["error"]["connection"]:
            self.showError(execute["error"]["connection"])
            # label.setText(execute["error"]["connection"])

        elif execute["error"]["format"]:
            label.setStyleSheet("color: red;")
            label.setVisible(True)
            label.setText(execute["error"]["format"])

        elif execute["error"]["auth"]:
            self.showError(execute["error"]["auth"])
            # label.setText(execute["error"]["auth"])

        return True

    def showError(self, error: str):
        if self.errorBar is None or self.errorBar.isHidden():
            self.errorBar = InfoBar(self, error, error=True)
            self.errorBar.show()

    def nextStep(self):

        self.__name = self.ui.line_Name.text()
        self.__username = self.ui.line_Username.text()
        self.__email = self.ui.line_Email.text()
        self.__password = self.ui.line_Password.text()

        if not self.__name or not self.__username or not self.__email or not self.__password:
            if not self.__name:
                self.ui.line_Name.setStyleSheet("QLineEdit { border: 1px solid red; color: red; }")
            if not self.__username:
                self.ui.frame_Username.setStyleSheet("QFrame#frame_Username { border: 1px solid red; }")
                self.ui.line_Username.setStyleSheet("QLineEdit { color: red; }")
            if not self.__email:
                self.ui.line_Email.setStyleSheet("QLineEdit { border: 1px solid red; color: red; }")
            if not self.__password:
                self.ui.frame_PasswordInput.setStyleSheet("QFrame#frame_PasswordInput { border: 1px solid red; }")
                self.ui.line_Password.setStyleSheet("QLineEdit { color: red; }")
            return

        execute = self.__auth.signUp(self.__email, self.__username, self.__password, self.__name)
        if self.isError(self.ui.label_SignUpError, execute):
            return

        self.ui.textBrowser_ResendTimer.clearFocus()
        self.ui.textBrowser_ResendTimer.clear()
        self.ui.textBrowser_ResendTimer.anchorClicked.disconnect(self.sendCode)
        self.ui.textBrowser_ResendTimer.setOpenLinks(False)
        self.ui.line_Code.setReadOnly(False)
        self.timer.start(1000)

        self.setVerifyAboutText()
        self.ui.stacked_Main.setCurrentIndex(self.widgetToIndex["verify"])

    def timeUpdate(self):

        if (self.ui.textBrowser_ResendTimer.isHidden()
                and self.ui.stacked_Main.currentIndex() == self.widgetToIndex["verify"]):
            self.ui.textBrowser_ResendTimer.setVisible(True)

        self.timeCounter += 1
        self.ui.textBrowser_ResendTimer.setText(
            f"You can get a new code in {self.awaitingTime - self.timeCounter} seconds.")

        if self.timeCounter > self.awaitingTime:
            if not self.__email:
                self.ui.line_Code.setReadOnly(True)
            self.ui.textBrowser_ResendTimer.setHidden(True)
            self.setResendTimerText()
            self.timeCounter = 0
            self.timer.stop()

    def sendCode(self):

        execute = self.__auth.signUp(self.__email, self.__username, self.__password, self.__name)
        if self.isError(self.ui.label_VerifyError, execute):
            return

        self.ui.textBrowser_ResendTimer.anchorClicked.disconnect(self.sendCode)
        self.ui.textBrowser_ResendTimer.setOpenLinks(False)
        self.timer.start(1000)

    def verifyEmail(self):

        code = self.ui.line_Code.text()

        if not code:
            self.ui.line_Code.setStyleSheet("QLineEdit { border: 1px solid red; color: red; }")
            return

        execute = self.__auth.verificationSession(code)
        if self.isError(self.ui.label_VerifyError, execute):
            return

        execute = self.__auth.createNewAccount()
        if self.isError(self.ui.label_VerifyError, execute):
            return

        self.exit()

    def toLogIn(self):

        pos = QPoint(self.pos().x(), self.pos().y())
        self.close()

        self.formChangedSignal.emit("login", pos)

    def exit(self):

        pos = QPoint(self.pos().x(), self.pos().y())
        self.close()

        self.exitSignal.emit("home", pos)
