import os

from PySide6.QtCore import QSize, Signal, QPoint, QTimer, Qt
from PySide6.QtGui import QIcon
from PySide6.QtWidgets import QWidget, QLineEdit

from src.main.gui.design.signup.signup import Ui_form_SignUp
from src.main.objects.server.Authorization import Authorization
from src.main.objects.server.FileManager import FileManager

from src.main.objects.ImageTools import ImageTools


class SignUpForm(Ui_form_SignUp, QWidget):
    exitSignal = Signal(str, QPoint)

    formChangedSignal = Signal(str, QPoint)

    widgetToIndex = {"main": 0, "submit": 1}

    tempSignUpBgFileName = "tempSignUpBg.png"

    awaitingTime = 180000

    def __init__(self, auth: Authorization, fileManger: FileManager):
        super(Ui_form_SignUp, self).__init__()

        self.ui = Ui_form_SignUp()
        self.ui.setupUi(self)

        self.__auth = auth
        self.__fileManager = fileManger

        self.timer = None

        self.__name = None
        self.__username = None
        self.__email = None
        self.__password = None

        self.button_IconPasswordVisibility = {}

        self.__setIconsSVG()
        self.__initSetup()

    def __setIconsSVG(self):

        icon_Back = QIcon()
        icon_Back.addFile(":icons/icons/AuthBack.svg", QSize(), QIcon.Normal)
        self.ui.button_ControlBack.setIcon(icon_Back)
        self.ui.button_ControlBack.setIconSize(QSize(30, 30))

        icon_PasswordVisibilityOn = QIcon()
        icon_PasswordVisibilityOn.addFile(":icons/icons/PasswordVisibilityOn.svg", QSize(),
                                          QIcon.Normal)
        self.ui.button_PasswordVisibility.setIcon(icon_PasswordVisibilityOn)
        self.ui.button_PasswordVisibility.setIconSize(QSize(25, 25))

        icon_PasswordVisibilityOff = QIcon()
        icon_PasswordVisibilityOff.addFile(":icons/icons/PasswordVisibilityOff.svg", QSize(),
                                           QIcon.Normal)

        self.button_IconPasswordVisibility[True] = icon_PasswordVisibilityOn
        self.button_IconPasswordVisibility[False] = icon_PasswordVisibilityOff

    def __initSetup(self):

        signUpBgPath = ImageTools.getPictureForWidget(self.ui.page_Main.width(),
                                                      self.ui.page_Main.height(),
                                                      250,
                                                      os.path.abspath("gui/resources/images/signUpBg.png"),
                                                      self.__fileManager.tempPath,
                                                      self.tempSignUpBgFileName)

        self.ui.frame_Main.setStyleSheet(
            f"QFrame#frame_Main {{border-image: url('{signUpBgPath}') 0 0 0 0 stretch stretch}}")
        self.ui.frame_Submit.setStyleSheet(
            f"QFrame#frame_Submit {{border-image: url('{signUpBgPath}') 0 0 0 0 stretch stretch}}")

        self.ui.stacked_Main.setCurrentIndex(self.widgetToIndex["main"])

        self.ui.label_SignUpError.setHidden(True)
        self.ui.label_SubmitError.setHidden(True)
        self.ui.textBrowser_SubmitTimer.setHidden(True)
        self.ui.button_PasswordVisibility.toggled.connect(self.setPasswordVisibility)

        self.ui.textBrowser_Rules.setAcceptRichText(True)
        with open(os.path.abspath("gui/resources/html/rules.txt")) as f:
            self.ui.textBrowser_Rules.append(f.read())
        self.ui.textBrowser_Rules.document().setDocumentMargin(0)

        self.ui.textBrowser_SubmitAbout.setAcceptRichText(True)
        with open(os.path.abspath("gui/resources/html/submitAbout.txt")) as f:
            self.ui.textBrowser_SubmitAbout.append(f.read())
        self.ui.textBrowser_SubmitAbout.document().setDocumentMargin(0)

        self.ui.textBrowser_toLogIn.setAcceptRichText(True)
        with open(os.path.abspath("gui/resources/html/toLogIn.txt")) as f:
            self.ui.textBrowser_toLogIn.append(f.read())
        self.ui.textBrowser_toLogIn.document().setDocumentMargin(0)
        self.ui.textBrowser_toLogIn.anchorClicked.connect(self.goToLogIn)

        self.ui.textBrowser_SubmitBack.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.ui.textBrowser_toLogIn.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.ui.textBrowser_SubmitTimer.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)

        self.ui.button_ControlBack.clicked.connect(self.exit)
        self.ui.button_CheckEmail.clicked.connect(self.submitEmail)
        self.ui.button_SignUp.clicked.connect(self.signUp)

    def setPasswordVisibility(self):

        if self.sender().isChecked():
            self.ui.line_Password.setEchoMode(QLineEdit.EchoMode.Normal)
            self.ui.button_PasswordVisibility.setIcon(self.button_IconPasswordVisibility[False])
        else:
            self.ui.line_Password.setEchoMode(QLineEdit.EchoMode.Password)
            self.ui.button_PasswordVisibility.setIcon(self.button_IconPasswordVisibility[True])
        self.ui.button_PasswordVisibility.setIconSize(QSize(25, 25))

    def switchPage(self, index):

        self.ui.stacked_Main.setCurrentIndex(index)

    def setSubmitAboutText(self, email: str):

        self.ui.textBrowser_SubmitAbout.setAcceptRichText(True)
        with open(os.path.abspath("gui/resources/html/rules.txt")) as f:
            text = f.read().replace("###", email)
            self.ui.textBrowser_SubmitAbout.append(text)
        self.ui.textBrowser_SubmitAbout.document().setDocumentMargin(0)

    def setSubmitTimerText(self):

        self.ui.textBrowser_SubmitTimer.setAcceptRichText(True)
        with open(os.path.abspath("gui/resources/html/toLogIn.txt")) as f:
            self.ui.textBrowser_SubmitTimer.append(f.read())
        self.ui.textBrowser_SubmitTimer.document().setDocumentMargin(0)
        self.ui.textBrowser_SubmitTimer.anchorClicked.connect(self.resendCode)

    def submitEmail(self):

        self.__name = self.ui.line_Name.text()
        self.__username = self.ui.line_Username.text()
        self.__email = self.ui.line_Email.text()
        self.__password = self.ui.line_Password.text()

        error = self.__auth.signUp(self.__email, self.__username, self.__password, self.__name)

        if error:
            self.ui.label_SignUpError.setStyleSheet("color: red;")
            self.ui.label_SignUpError.setVisible(True)
            self.ui.label_SignUpError.setText(error)
            return

        self.setSubmitAboutText(self.__email)

        self.timer = QTimer(self)
        self.timer.timeout.connect(self.timeUpdate)
        self.timer.start(1000)
        self.ui.textBrowser_SubmitTimer.setVisible(True)

        self.ui.stacked_Main.setCurrentIndex(self.widgetToIndex["submit"])

    def timeUpdate(self):

        timeLeft = self.awaitingTime - self.timer.interval()
        self.ui.textBrowser_SubmitTimer.setText(f"We can resend code in {int(timeLeft / 1000)} seconds")

        if timeLeft < 0:
            self.setSubmitTimerText()
            self.timer.stop()

    def resendCode(self):

        self.ui.label_SubmitError.setVisible(False)

        error = self.__auth.signUp(self.__email, self.__username, self.__password, self.__name)

        if error:
            self.ui.label_SubmitError.setStyleSheet("color: red;")
            self.ui.label_SubmitError.setVisible(True)
            self.ui.label_SubmitError.setText(error)
            return

        self.timer = QTimer(self)
        self.timer.timeout.connect(self.timeUpdate)
        self.timer.start(1000)

    def signUp(self):

        self.ui.label_SubmitError.setVisible(False)

        code = self.ui.line_SubmitCode.text()

        error = self.__auth.verificationSession(int(code), "signUp")

        if error:
            self.ui.label_SubmitError.setStyleSheet("color: red;")
            self.ui.label_SubmitError.setVisible(True)
            self.ui.label_SubmitError.setText(error)
            return

        self.exit()

    def goToLogIn(self):

        pos = QPoint(self.pos().x(), self.pos().y())
        self.close()

        self.formChangedSignal.emit("login", pos)

    def exit(self):

        pos = QPoint(self.pos().x(), self.pos().y())
        self.close()

        self.exitSignal.emit("home", pos)
