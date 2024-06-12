import os

from PySide6.QtCore import QSize, Signal, QPoint, Qt, QTimer, QEvent
from PySide6.QtGui import QIcon
from PySide6.QtWidgets import QWidget, QLineEdit, QLabel

from src.main.gui.design.login.login import Ui_form_LogIn
from src.main.objects.ImageTools import ImageTools
from src.main.objects.server.Authorization import Authorization
from src.main.objects.server.FileManager import FileManager


class LogInForm(Ui_form_LogIn, QWidget):
    exitSignal = Signal(str, QPoint)

    formChangedSignal = Signal(str, QPoint)

    widgetToIndex = {"main": 0, "reset": 1, "new": 2}

    tempLogInBgFileName = "tempLogInBg.png"

    awaitingTime = 90

    def __init__(self, auth: Authorization, fileManger: FileManager):
        super(Ui_form_LogIn, self).__init__()

        self.ui = Ui_form_LogIn()
        self.ui.setupUi(self)

        self.__auth = auth
        self.__fileManager = fileManger

        self.__email = None

        self.timer = QTimer(self)
        self.timeCounter = 0

        self.dictPasswordVisIcons = {}
        self.dictCodeSentIcons = {}

        self.__setIconsSVG()
        self.__initSetup()

    def __setIconsSVG(self):

        icon_Back = QIcon()
        icon_Back.addFile(":icons/icons/AuthBack.svg", QSize(), QIcon.Normal)
        self.ui.button_ControlBack.setIcon(icon_Back)
        self.ui.button_ControlBack.setIconSize(QSize(30, 30))

        icon_PasswordVisibilityOn = QIcon()
        icon_PasswordVisibilityOn.addFile(":icons/icons/PasswordVisibilityOn.svg", QSize(), QIcon.Normal)
        self.ui.button_PasswordVisibility.setIcon(icon_PasswordVisibilityOn)
        self.ui.button_PasswordVisibility.setIconSize(QSize(25, 25))

        self.ui.button_PwdVis.setIcon(icon_PasswordVisibilityOn)
        self.ui.button_PwdVis.setIconSize(QSize(25, 25))

        icon_PasswordVisibilityOff = QIcon()
        icon_PasswordVisibilityOff.addFile(":icons/icons/PasswordVisibilityOff.svg", QSize(), QIcon.Normal)

        self.dictPasswordVisIcons[True] = icon_PasswordVisibilityOn
        self.dictPasswordVisIcons[False] = icon_PasswordVisibilityOff

        icon_SendCode = QIcon()
        icon_SendCode.addFile(":icons/icons/SendCode.svg", QSize(), QIcon.Normal)
        self.ui.button_CodeSend.setIcon(icon_SendCode)
        self.ui.button_CodeSend.setIconSize(QSize(25, 25))

        icon_CodeSent = QIcon()
        icon_CodeSent.addFile(":icons/icons/CodeSent.svg", QSize(), QIcon.Normal)

        self.dictCodeSentIcons[True] = icon_CodeSent
        self.dictCodeSentIcons[False] = icon_SendCode

    def __initSetup(self):

        logInBgPath = ImageTools.getPictureForWidget(self.ui.page_Main.width(),
                                                     self.ui.page_Main.height(),
                                                     150,
                                                     os.path.abspath("gui/resources/images/logInBg.png"),
                                                     self.__fileManager.tempPath,
                                                     self.tempLogInBgFileName)

        self.ui.frame_Main.setStyleSheet(
            f"QFrame#frame_Main {{border-image: url('{logInBgPath}') 0 0 0 0 stretch stretch}}")
        self.ui.frame_Reset.setStyleSheet(
            f"QFrame#frame_Reset {{border-image: url('{logInBgPath}') 0 0 0 0 stretch stretch}}")
        self.ui.frame_New.setStyleSheet(
            f"QFrame#frame_New {{border-image: url('{logInBgPath}') 0 0 0 0 stretch stretch}}")

        self.ui.stacked_Main.setCurrentIndex(self.widgetToIndex["main"])

        self.ui.label_NewError.setHidden(True)
        self.ui.label_ResetError.setHidden(True)
        self.ui.label_LogInError.setHidden(True)
        self.ui.textBrowser_ResendTimer.setHidden(True)

        self.ui.button_CodeSend.setIcon(self.dictCodeSentIcons[False])
        self.ui.button_CodeSend.setIconSize(QSize(25, 25))

        self.ui.button_PwdVis.toggled.connect(self.setPasswordVisibility)
        self.ui.button_PasswordVisibility.toggled.connect(self.setPasswordVisibility)

        self.ui.textBrowser_Rules.setAcceptRichText(True)
        with open(os.path.abspath("gui/resources/html/rules.txt")) as f:
            self.ui.textBrowser_Rules.append(f.read())
        self.ui.textBrowser_Rules.document().setDocumentMargin(0)

        self.ui.textBrowser_ResetAbout.setAcceptRichText(True)
        with open(os.path.abspath("gui/resources/html/resetAbout.txt")) as f:
            self.ui.textBrowser_ResetAbout.append(f.read())
        self.ui.textBrowser_ResetAbout.document().setDocumentMargin(0)

        self.ui.textBrowser_NewAbout.setAcceptRichText(True)
        with open(os.path.abspath("gui/resources/html/new.txt")) as f:
            self.ui.textBrowser_NewAbout.append(f.read())
        self.ui.textBrowser_NewAbout.document().setDocumentMargin(0)

        self.ui.textBrowser_toSignUp.setAcceptRichText(True)
        with open(os.path.abspath("gui/resources/html/toSignUp.txt")) as f:
            self.ui.textBrowser_toSignUp.append(f.read())
        self.ui.textBrowser_toSignUp.document().setDocumentMargin(0)
        self.ui.textBrowser_toSignUp.anchorClicked.connect(self.switchPage)

        self.ui.textBrowser_BackFromReset.setAcceptRichText(True)
        with open(os.path.abspath("gui/resources/html/goBack.txt")) as f:
            self.ui.textBrowser_BackFromReset.append(f.read())
        self.ui.textBrowser_BackFromReset.document().setDocumentMargin(0)
        self.ui.textBrowser_BackFromReset.anchorClicked.connect(self.switchPage)

        self.ui.textBrowser_BackFromNew.setAcceptRichText(True)
        with open(os.path.abspath("gui/resources/html/goBack.txt")) as f:
            self.ui.textBrowser_BackFromNew.append(f.read())
        self.ui.textBrowser_BackFromNew.document().setDocumentMargin(0)
        self.ui.textBrowser_BackFromNew.anchorClicked.connect(self.switchPage)

        self.ui.textBrowser_Reset.setAcceptRichText(True)
        with open(os.path.abspath("gui/resources/html/reset.txt")) as f:
            self.ui.textBrowser_Reset.append(f.read())
        self.ui.textBrowser_Reset.document().setDocumentMargin(0)
        self.ui.textBrowser_Reset.anchorClicked.connect(self.switchPage)

        self.ui.textBrowser_ResendTimer.setAcceptRichText(True)
        self.ui.textBrowser_ResendTimer.document().setDocumentMargin(0)
        self.ui.textBrowser_ResendTimer.anchorClicked.connect(self.sendCode)

        self.ui.textBrowser_Reset.setLineWrapColumnOrWidth(0)
        self.ui.textBrowser_toSignUp.setLineWrapColumnOrWidth(0)
        self.ui.textBrowser_BackFromNew.setLineWrapColumnOrWidth(0)
        self.ui.textBrowser_ResendTimer.setLineWrapColumnOrWidth(0)
        self.ui.textBrowser_BackFromReset.setLineWrapColumnOrWidth(0)

        self.ui.textBrowser_Reset.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.ui.textBrowser_toSignUp.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.ui.textBrowser_BackFromNew.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.ui.textBrowser_ResendTimer.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.ui.textBrowser_BackFromReset.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)

        self.ui.line_Email.installEventFilter(self)
        self.ui.line_Password.installEventFilter(self)
        self.ui.line_EmailToReset.installEventFilter(self)
        self.ui.line_PwdSecond.installEventFilter(self)
        self.ui.line_Code.installEventFilter(self)

        self.ui.button_VerifyCode.clicked.connect(self.switchPage)
        self.ui.button_ControlBack.clicked.connect(self.switchPage)

        self.timer.timeout.connect(self.timeUpdate)
        self.ui.button_LogIn.clicked.connect(self.logIn)
        self.ui.button_CodeSend.clicked.connect(self.sendCode)
        self.ui.button_Submit.clicked.connect(self.submitPassword)

    def eventFilter(self, watched, event):

        if watched == self.ui.line_PwdSecond:

            if event.type() == QEvent.Type.KeyRelease:

                if self.ui.line_PwdFirst.text() != self.ui.line_PwdSecond.text():

                    self.ui.frame_PwdFirst.setStyleSheet("QFrame#frame_PwdFirst { border: 1px solid red; }")
                    self.ui.line_PwdFirst.setStyleSheet("QLineEdit { color: red; }")
                    self.ui.line_PwdSecond.setStyleSheet("QLineEdit { border: 1px solid red; color: red; }")

                else:

                    self.ui.frame_PwdFirst.setStyleSheet("QFrame#frame_PwdFirst { border: 0; }")
                    self.ui.line_PwdFirst.setStyleSheet("QLineEdit { color: black; }")
                    self.ui.line_PwdSecond.setStyleSheet("QLineEdit { border: 0; color: black; }")

                return True

        elif watched == self.ui.line_EmailToReset:

            if event.type() == QEvent.Type.KeyRelease:

                if self.ui.line_EmailToReset.text():

                    self.ui.frame_EmailToReset.setStyleSheet("QFrame#frame_EmailToReset { border: 0; }")
                    self.ui.line_EmailToReset.setStyleSheet("QLineEdit {  color: black; }")

                else:

                    self.ui.frame_EmailToReset.setStyleSheet("QFrame#frame_EmailToReset { border: 1px solid red; }")
                    self.ui.line_EmailToReset.setStyleSheet("QLineEdit {  color: red; }")

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

            if self.sender() == self.ui.button_PasswordVisibility:
                self.ui.line_Password.setEchoMode(QLineEdit.EchoMode.Normal)

            elif self.sender() == self.ui.button_PwdVis:
                self.ui.line_PwdFirst.setEchoMode(QLineEdit.EchoMode.Normal)

            self.sender().setIcon(self.dictPasswordVisIcons[False])

        else:

            if self.sender() == self.ui.button_PasswordVisibility:
                self.ui.line_Password.setEchoMode(QLineEdit.EchoMode.Password)

            elif self.sender() == self.ui.button_PwdVis:
                self.ui.line_PwdFirst.setEchoMode(QLineEdit.EchoMode.Password)

            self.sender().setIcon(self.dictPasswordVisIcons[True])

        self.ui.button_PasswordVisibility.setIconSize(QSize(25, 25))

    def setCodeSentButton(self, value: bool):

        self.ui.button_CodeSend.setChecked(value)
        self.ui.button_CodeSend.setIcon(self.dictCodeSentIcons[value])

    def setResendTimerText(self):

        with open(os.path.abspath("gui/resources/html/resendCode.txt")) as f:
            self.ui.textBrowser_ResendTimer.setText("")
            self.ui.textBrowser_ResendTimer.append(f.read())
        self.ui.textBrowser_ResendTimer.anchorClicked.connect(self.sendCode)
        self.ui.textBrowser_ResendTimer.setOpenLinks(True)
        self.ui.textBrowser_ResendTimer.setVisible(True)

    def switchPage(self):

        if self.sender() == self.ui.textBrowser_Reset:

            self.ui.line_Code.setReadOnly(True)
            self.setCodeSentButton(False)
            self.ui.line_Code.setText("")
            self.ui.line_EmailToReset.setText("")
            self.ui.label_ResetError.setHidden(True)
            self.ui.textBrowser_ResendTimer.setHidden(True)
            self.ui.line_Code.setStyleSheet("QLineEdit { border: 0; color: black; }")
            self.ui.frame_EmailToReset.setStyleSheet("QFrame#frame_EmailToReset { border: 0; }")
            self.ui.line_EmailToReset.setStyleSheet("QLineEdit {  color: black; }")
            self.ui.stacked_Main.setCurrentIndex(self.widgetToIndex["reset"])

        elif (self.sender() == self.ui.textBrowser_BackFromReset
              or self.sender() == self.ui.textBrowser_BackFromNew):

            self.__email = None
            self.ui.line_Email.clear()
            self.ui.line_Password.clear()
            self.ui.label_LogInError.setVisible(False)
            self.ui.line_Email.setStyleSheet("QLineEdit { border: 0; color: black; }")
            self.ui.frame_PasswordInput.setStyleSheet("QFrame#frame_PasswordInput { border: 0; }")
            self.ui.line_Password.setStyleSheet("QLineEdit { color: black; }")
            self.ui.stacked_Main.setCurrentIndex(self.widgetToIndex["main"])

        elif self.sender() == self.ui.button_VerifyCode:

            self.ui.label_NewError.setText("")
            self.ui.line_PwdFirst.setText("")
            self.ui.line_PwdSecond.setText("")
            self.ui.frame_PwdFirst.setStyleSheet("QFrame#frame_PwdFirst { border: 0; }")
            self.ui.line_PwdFirst.setStyleSheet("QLineEdit { color: black; }")
            self.ui.line_PwdSecond.setStyleSheet("QLineEdit { border: 0; color: black; }")

            self.verifyCode()

        elif self.sender() == self.ui.textBrowser_toSignUp:

            self.toSignUp()

        elif self.sender() == self.ui.button_ControlBack:

            self.exit()

    @staticmethod
    def isError(label: QLabel, execute: dict) -> bool:

        if not execute["error"]:
            return False

        label.setStyleSheet("color: red;")
        label.setVisible(True)

        if execute["error"]["connection"]:
            label.setText(execute["error"]["connection"])

        elif execute["error"]["format"]:
            label.setText(execute["error"]["format"])

        elif execute["error"]["auth"]:
            label.setText(execute["error"]["auth"])

        return True

    def logIn(self):

        email = self.ui.line_Email.text()
        password = self.ui.line_Password.text()

        if not email or not password:
            if not email:
                self.ui.line_Email.setStyleSheet("QLineEdit { border: 1px solid red; color: red; }")
            if not password:
                self.ui.frame_PasswordInput.setStyleSheet("QFrame#frame_PasswordInput { border: 1px solid red; }")
                self.ui.line_Password.setStyleSheet("QLineEdit { color: red; }")
            return

        execute = self.__auth.logIn(email, password)
        if self.isError(self.ui.label_LogInError, execute):
            return

        self.exit()

    def sendCode(self):

        self.setCodeSentButton(False)

        self.__email = self.ui.line_EmailToReset.text()

        if not self.__email:
            self.ui.frame_EmailToReset.setStyleSheet("QFrame#frame_EmailToReset { border: 1px solid red; color: red; }")
            return

        execute = self.__auth.resetPassword(self.__email)
        if self.isError(self.ui.label_ResetError, execute):
            return

        self.ui.textBrowser_ResendTimer.clearFocus()
        self.ui.textBrowser_ResendTimer.clear()
        self.ui.textBrowser_ResendTimer.anchorClicked.disconnect(self.sendCode)
        self.ui.textBrowser_ResendTimer.setOpenLinks(False)
        self.ui.line_Code.setReadOnly(False)
        self.ui.label_ResetError.setHidden(True)
        self.setCodeSentButton(True)
        self.timer.start(1000)

    def timeUpdate(self):

        if (self.ui.textBrowser_ResendTimer.isHidden()
                and self.ui.stacked_Main.currentIndex() == self.widgetToIndex["reset"]
                and self.ui.button_CodeSend.isChecked()):
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

    def verifyCode(self):

        if not self.ui.line_EmailToReset.text() or not self.ui.line_Code.text():
            if not self.ui.line_EmailToReset.text():
                self.ui.frame_EmailToReset.setStyleSheet("QFrame#frame_EmailToReset { border: 1px solid red; }")
                self.ui.line_EmailToReset.setStyleSheet("QLineEdit {  color: red; }")
            if not self.ui.line_Code.text():
                self.ui.line_Code.setStyleSheet("QLineEdit { border: 1px solid red; color: red; }")
            return

        if not self.ui.line_Code.text().isnumeric():
            return

        code = int(self.ui.line_Code.text())

        execute = self.__auth.verificationSession(code)
        if self.isError(self.ui.label_ResetError, execute):
            return

        self.ui.stacked_Main.setCurrentIndex(self.widgetToIndex["new"])

    def submitPassword(self):

        passwordFirst = self.ui.line_PwdFirst.text()
        passwordSecond = self.ui.line_PwdSecond.text()

        if not passwordFirst or not passwordSecond:
            if not passwordFirst:
                self.ui.frame_PwdFirst.setStyleSheet("QFrame#frame_PwdFirst { border: 1px solid red; }")
                self.ui.line_PwdFirst.setStyleSheet("QLineEdit { color: red; }")
            if not passwordSecond:
                self.ui.line_PwdSecond.setStyleSheet("QLineEdit { border: 1px solid red; color: red; }")
            return

        if passwordFirst != passwordSecond:
            return

        execute = self.__auth.setNewPassword(passwordSecond)
        if self.isError(self.ui.label_NewError, execute):
            return

        self.exit()

    def toSignUp(self):

        pos = QPoint(self.pos().x(), self.pos().y())
        self.close()

        self.formChangedSignal.emit("signup", pos)

    def exit(self):

        pos = QPoint(self.pos().x(), self.pos().y())
        self.close()

        self.exitSignal.emit("home", pos)
