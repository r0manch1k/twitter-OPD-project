# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'x.ui'
##
## Created by: Qt User Interface Compiler version 6.7.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QButtonGroup, QFrame, QGridLayout,
    QHBoxLayout, QLabel, QLineEdit, QMainWindow,
    QPushButton, QScrollArea, QSizePolicy, QSpacerItem,
    QStackedWidget, QTextEdit, QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1000, 550)
        MainWindow.setMinimumSize(QSize(1000, 550))
        MainWindow.setMaximumSize(QSize(1000, 550))
        MainWindow.setStyleSheet(u"QScrollBar { \n"
"	background-color: none; \n"
"} \n"
"\n"
"/* ------ ------- */\n"
"\n"
"QScrollBar:vertical {\n"
"	background-color: rgb(235, 237, 239);\n"
"	width: 8px;\n"
"	border-radius: 4px;\n"
"}\n"
"\n"
"QScrollBar::handle:vertical {\n"
"	background-color: rgb(184,191,195);\n"
"	min-height: 5px;\n"
"	border-radius: 4px;\n"
"}\n"
"\n"
"QScrollBar::add-line:horizontal {\n"
"	width: 0px;\n"
"	height: 0px;\n"
"	border: none;\n"
"	background: none;\n"
"}\n"
"\n"
"QScrollBar::sub-line:horizontal {\n"
"	width: 0px;\n"
"	height: 0px;\n"
"	border: none;\n"
"	background: none;\n"
"}")
        self.central_widget = QWidget(MainWindow)
        self.central_widget.setObjectName(u"central_widget")
        self.central_widget.setStyleSheet(u"")
        self.gridLayout_2 = QGridLayout(self.central_widget)
        self.gridLayout_2.setSpacing(0)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.frame_Main = QFrame(self.central_widget)
        self.frame_Main.setObjectName(u"frame_Main")
        self.frame_Main.setStyleSheet(u"QToolTip {\n"
"	opacity: 180;\n"
"	border: 0;\n"
"	padding: 1px;\n"
"	border-radius: 3px;\n"
"	background-color: black;\n"
"	color: white;\n"
"}\n"
"\n"
"QWidget {\n"
"	border: 0;\n"
"	background-color: white;\n"
"}\n"
"\n"
"QFrame {\n"
"	background-color: white;\n"
"}\n"
"\n"
"QFrame#frame_SideBarChat, QFrame#frame_SideBarNotifications {\n"
"	border: 0;\n"
"	border-left: 1px solid rgb(235, 237, 239);\n"
"}\n"
"\n"
"/* ----- -BUTTONS ------ */\n"
"\n"
"QPushButton {\n"
"	width: 40px;\n"
"	height: 40px;\n"
"	color: black;\n"
"	margin: 0;\n"
"	border-radius: 20px;\n"
"	background-color:  rgb(229,235,238);\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color:  rgb(219,228,233);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"	background-color: rgb(184,191,195);\n"
"}\n"
"\n"
"\n"
"QPushButton::menu-indicator {\n"
"	width: 0px;\n"
"}\n"
"\n"
"")
        self.frame_Main.setFrameShape(QFrame.StyledPanel)
        self.frame_Main.setFrameShadow(QFrame.Raised)
        self.gridLayout = QGridLayout(self.frame_Main)
        self.gridLayout.setSpacing(0)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.frame_MainBar = QFrame(self.frame_Main)
        self.frame_MainBar.setObjectName(u"frame_MainBar")
        self.frame_MainBar.setMinimumSize(QSize(0, 60))
        self.frame_MainBar.setMaximumSize(QSize(16777215, 60))
        self.frame_MainBar.setStyleSheet(u"QFrame {\n"
"	border: 0;		\n"
"	border-bottom: 1px solid rgb(235, 237, 239);\n"
"} \n"
"\n"
"QFrame#frame_ButtonHomeFilterPosts {\n"
"	background-color:  rgb(235, 237, 239);\n"
"	border-top-right-radius: 20px;\n"
"	border-bottom-right-radius: 20px;\n"
"	\n"
"}\n"
"\n"
"QFrame#frame_SearchBar {\n"
"	border: 0;\n"
"}\n"
"\n"
"QPushButton {\n"
"	width: 40px;\n"
"	height: 40px;\n"
"	color: black;\n"
"	margin: 0;\n"
"	border-radius: 20px;\n"
"	background-color:  white;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color:  rgb(235, 237, 239);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"	background-color: rgb(184,191,195);\n"
"}\n"
"\n"
"QPushButton:checked {\n"
"	background-color: rgb(235, 237, 239);\n"
"}\n"
"\n"
"QLineEdit {\n"
"	height: 40px;\n"
"	color: black;\n"
"	background-color:  rgb(235, 237, 239);\n"
"	padding-left: 10px;\n"
"	border-top-left-radius: 20px;\n"
"	border-bottom-left-radius: 20px;\n"
"}\n"
"\n"
"QLineEdit:hover {\n"
"	background-color:  rgb(226,231,233);\n"
"}\n"
"\n"
"QPushButton#button_Log"
                        "o {\n"
"	width: 60px;\n"
"	border-radius: 0;\n"
"}\n"
"\n"
"QPushButton:hover#button_Logo {\n"
"	background-color:  white;\n"
"}\n"
"\n"
"QPushButton:pressed#button_Logo {\n"
"	background-color: white;\n"
"}\n"
"\n"
"QPushButton#button_Notifications:checked, \n"
"QPushButton#button_Chat:checked  {\n"
"	background-color:  rgb(226,231,233);\n"
"}\n"
"\n"
"QPushButton#button_HomeFilterPosts {\n"
"	width: 30px;\n"
"	height: 30px;\n"
"	border-radius: 15px;\n"
"	background-color:  rgb(235, 237, 239);\n"
"}\n"
"\n"
"QPushButton#button_HomeFilterPosts::hover {\n"
"	background-color:  rgb(226,231,233);\n"
"}\n"
"\n"
"")
        self.frame_MainBar.setFrameShape(QFrame.StyledPanel)
        self.frame_MainBar.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.frame_MainBar)
        self.horizontalLayout.setSpacing(10)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(10, 0, 10, 0)
        self.button_Logo = QPushButton(self.frame_MainBar)
        self.buttonGroup_MainTabs = QButtonGroup(MainWindow)
        self.buttonGroup_MainTabs.setObjectName(u"buttonGroup_MainTabs")
        self.buttonGroup_MainTabs.addButton(self.button_Logo)
        self.button_Logo.setObjectName(u"button_Logo")
        self.button_Logo.setStyleSheet(u"QPushButton#button_Logo,\n"
"QPushButton#button_Logo:pressed,\n"
"QPushButton#button_Logo:hover,\n"
"QPushButton#button_Logo:checked {\n"
"	background-color: white;\n"
"}")
        self.button_Logo.setCheckable(True)

        self.horizontalLayout.addWidget(self.button_Logo)

        self.frame_SearchBar = QFrame(self.frame_MainBar)
        self.frame_SearchBar.setObjectName(u"frame_SearchBar")
        self.frame_SearchBar.setMinimumSize(QSize(50, 0))
        self.frame_SearchBar.setStyleSheet(u"")
        self.frame_SearchBar.setFrameShape(QFrame.StyledPanel)
        self.frame_SearchBar.setFrameShadow(QFrame.Raised)
        self.layout_SearchBar = QHBoxLayout(self.frame_SearchBar)
        self.layout_SearchBar.setSpacing(0)
        self.layout_SearchBar.setObjectName(u"layout_SearchBar")
        self.layout_SearchBar.setContentsMargins(0, 0, 0, 0)
        self.line_SearchBar = QLineEdit(self.frame_SearchBar)
        self.line_SearchBar.setObjectName(u"line_SearchBar")
        self.line_SearchBar.setMaximumSize(QSize(16777215, 40))

        self.layout_SearchBar.addWidget(self.line_SearchBar)

        self.frame_ButtonHomeFilterPosts = QFrame(self.frame_SearchBar)
        self.frame_ButtonHomeFilterPosts.setObjectName(u"frame_ButtonHomeFilterPosts")
        self.frame_ButtonHomeFilterPosts.setMinimumSize(QSize(40, 40))
        self.frame_ButtonHomeFilterPosts.setMaximumSize(QSize(50, 40))
        self.frame_ButtonHomeFilterPosts.setStyleSheet(u"")
        self.frame_ButtonHomeFilterPosts.setFrameShape(QFrame.StyledPanel)
        self.frame_ButtonHomeFilterPosts.setFrameShadow(QFrame.Raised)
        self.gridLayout_3 = QGridLayout(self.frame_ButtonHomeFilterPosts)
        self.gridLayout_3.setSpacing(0)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.gridLayout_3.setContentsMargins(5, 5, 5, 5)
        self.button_HomeFilterPosts = QPushButton(self.frame_ButtonHomeFilterPosts)
        self.button_HomeFilterPosts.setObjectName(u"button_HomeFilterPosts")
        self.button_HomeFilterPosts.setMinimumSize(QSize(30, 30))
        self.button_HomeFilterPosts.setMaximumSize(QSize(30, 30))

        self.gridLayout_3.addWidget(self.button_HomeFilterPosts, 0, 0, 1, 1)


        self.layout_SearchBar.addWidget(self.frame_ButtonHomeFilterPosts)


        self.horizontalLayout.addWidget(self.frame_SearchBar)

        self.button_Apps = QPushButton(self.frame_MainBar)
        self.buttonGroup_MainSideBar = QButtonGroup(MainWindow)
        self.buttonGroup_MainSideBar.setObjectName(u"buttonGroup_MainSideBar")
        self.buttonGroup_MainSideBar.addButton(self.button_Apps)
        self.button_Apps.setObjectName(u"button_Apps")
        self.button_Apps.setStyleSheet(u"")
        self.button_Apps.setCheckable(True)

        self.horizontalLayout.addWidget(self.button_Apps)

        self.button_Chat = QPushButton(self.frame_MainBar)
        self.buttonGroup_MainSideBar.addButton(self.button_Chat)
        self.button_Chat.setObjectName(u"button_Chat")
        self.button_Chat.setCheckable(True)

        self.horizontalLayout.addWidget(self.button_Chat)

        self.button_Notifications = QPushButton(self.frame_MainBar)
        self.buttonGroup_MainSideBar.addButton(self.button_Notifications)
        self.button_Notifications.setObjectName(u"button_Notifications")
        self.button_Notifications.setCheckable(True)

        self.horizontalLayout.addWidget(self.button_Notifications)

        self.button_Account = QPushButton(self.frame_MainBar)
        self.buttonGroup_MainTabs.addButton(self.button_Account)
        self.button_Account.setObjectName(u"button_Account")
        self.button_Account.setStyleSheet(u"")
        self.button_Account.setCheckable(True)

        self.horizontalLayout.addWidget(self.button_Account)


        self.gridLayout.addWidget(self.frame_MainBar, 0, 0, 1, 2)

        self.stacked_Pages = QStackedWidget(self.frame_Main)
        self.stacked_Pages.setObjectName(u"stacked_Pages")
        self.stacked_Pages.setStyleSheet(u"QFrame {\n"
"	border: 0;		\n"
"}\n"
"\n"
"QFrame#frame_AccountTabsContainer {\n"
"	border-top: 1px solid rgb(229,235,238);\n"
"}")
        self.page_Home = QWidget()
        self.page_Home.setObjectName(u"page_Home")
        self.page_Home.setStyleSheet(u"")
        self.horizontalLayout_9 = QHBoxLayout(self.page_Home)
        self.horizontalLayout_9.setSpacing(10)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.horizontalLayout_9.setContentsMargins(0, 0, 20, 0)
        self.scrollArea_HomePosts = QScrollArea(self.page_Home)
        self.scrollArea_HomePosts.setObjectName(u"scrollArea_HomePosts")
        self.scrollArea_HomePosts.setMinimumSize(QSize(620, 0))
        self.scrollArea_HomePosts.setMaximumSize(QSize(620, 16777215))
        self.scrollArea_HomePosts.setStyleSheet(u"QWidget {\n"
"	border: 0;\n"
"	background: transponent;\n"
"}\n"
"\n"
"QFrame {\n"
"	background: transponent;\n"
"}\n"
"\n"
"QScrollArea {\n"
"	background: transponent;\n"
"}\n"
"\n"
"\n"
"")
        self.scrollArea_HomePosts.setWidgetResizable(True)
        self.scrollAreaWidget_Posts = QWidget()
        self.scrollAreaWidget_Posts.setObjectName(u"scrollAreaWidget_Posts")
        self.scrollAreaWidget_Posts.setGeometry(QRect(0, 0, 620, 490))
        self.scrollAreaWidget_Posts.setStyleSheet(u"")
        self.layout_ScrollAreaPosts = QVBoxLayout(self.scrollAreaWidget_Posts)
        self.layout_ScrollAreaPosts.setSpacing(20)
        self.layout_ScrollAreaPosts.setObjectName(u"layout_ScrollAreaPosts")
        self.layout_ScrollAreaPosts.setContentsMargins(0, 20, 0, 20)
        self.stacked_Posts = QStackedWidget(self.scrollAreaWidget_Posts)
        self.stacked_Posts.setObjectName(u"stacked_Posts")
        self.stacked_Posts.setStyleSheet(u"QStackedWidget {\n"
"	background: transponent;\n"
"}")

        self.layout_ScrollAreaPosts.addWidget(self.stacked_Posts)

        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.layout_ScrollAreaPosts.addItem(self.verticalSpacer_3)

        self.frame_SetPostsPage = QFrame(self.scrollAreaWidget_Posts)
        self.frame_SetPostsPage.setObjectName(u"frame_SetPostsPage")
        self.frame_SetPostsPage.setMinimumSize(QSize(0, 30))
        self.frame_SetPostsPage.setMaximumSize(QSize(16777215, 30))
        self.frame_SetPostsPage.setStyleSheet(u"QPushButton { \n"
"	width: 30px;\n"
"	height: 30px;\n"
"	border-radius: 15px;\n"
"	background-color: white;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color:  rgb(219,228,233);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"	background-color: rgb(184,191,195);\n"
"}\n"
"\n"
"QPushButton:checked {\n"
"	background-color: rgb(219,228,233);\n"
"}\n"
"")
        self.frame_SetPostsPage.setFrameShape(QFrame.StyledPanel)
        self.frame_SetPostsPage.setFrameShadow(QFrame.Raised)
        self.layout_SetPostsPage = QHBoxLayout(self.frame_SetPostsPage)
        self.layout_SetPostsPage.setSpacing(5)
        self.layout_SetPostsPage.setObjectName(u"layout_SetPostsPage")
        self.layout_SetPostsPage.setContentsMargins(10, 0, 10, 0)
        self.horizontalSpacer = QSpacerItem(277, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.layout_SetPostsPage.addItem(self.horizontalSpacer)

        self.horizontalSpacer_16 = QSpacerItem(277, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.layout_SetPostsPage.addItem(self.horizontalSpacer_16)


        self.layout_ScrollAreaPosts.addWidget(self.frame_SetPostsPage)

        self.label_HomeSign = QLabel(self.scrollAreaWidget_Posts)
        self.label_HomeSign.setObjectName(u"label_HomeSign")
        self.label_HomeSign.setMinimumSize(QSize(0, 20))
        self.label_HomeSign.setMaximumSize(QSize(16777215, 20))
        font = QFont()
        font.setBold(True)
        font.setItalic(True)
        self.label_HomeSign.setFont(font)
        self.label_HomeSign.setStyleSheet(u"color: rgba(255, 255, 255, 100);")
        self.label_HomeSign.setAlignment(Qt.AlignCenter)

        self.layout_ScrollAreaPosts.addWidget(self.label_HomeSign)

        self.scrollArea_HomePosts.setWidget(self.scrollAreaWidget_Posts)

        self.horizontalLayout_9.addWidget(self.scrollArea_HomePosts)

        self.stacked_SideBar = QStackedWidget(self.page_Home)
        self.stacked_SideBar.setObjectName(u"stacked_SideBar")
        self.stacked_SideBar.setMinimumSize(QSize(0, 420))
        self.stacked_SideBar.setMaximumSize(QSize(16777215, 450))
        self.stacked_SideBar.setStyleSheet(u"QStackedWidget {\n"
"	background: transponent;\n"
"	border-radius: 20px;\n"
"}\n"
"\n"
"QWidget {\n"
"	border: 0;\n"
"	background: transponent;\n"
"	border-radius: 20px;\n"
"}\n"
"\n"
"QFrame {\n"
"	border: 0;\n"
"	background: white;\n"
"	border-radius: 20px;\n"
"}\n"
"\n"
"")
        self.page_Apps = QWidget()
        self.page_Apps.setObjectName(u"page_Apps")
        self.page_Apps.setStyleSheet(u"")
        self.gridLayout_14 = QGridLayout(self.page_Apps)
        self.gridLayout_14.setSpacing(0)
        self.gridLayout_14.setObjectName(u"gridLayout_14")
        self.gridLayout_14.setContentsMargins(0, 0, 0, 0)
        self.frame_SideBarApps = QFrame(self.page_Apps)
        self.frame_SideBarApps.setObjectName(u"frame_SideBarApps")
        self.frame_SideBarApps.setStyleSheet(u"QLabel {\n"
"	border-bottom: 1px solid  rgb(235, 237, 239);\n"
"}\n"
"\n"
"QScrollArea, QWidget {\n"
"	background-color: white;\n"
"}\n"
"\n"
"QPushButton {\n"
"	height: 40px;\n"
"	color: black;\n"
"	margin: 0;\n"
"	padding-left: 10px;\n"
"	border-radius: 15px;\n"
"	background-color: white;\n"
"	text-align: left;\n"
"}\n"
"\n"
"QPushButton:hover, QPushButton:checked {\n"
"	background-color:  rgb(229,235,238);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"	background-color: rgb(219,228,233);\n"
"}")
        self.frame_SideBarApps.setFrameShape(QFrame.StyledPanel)
        self.frame_SideBarApps.setFrameShadow(QFrame.Raised)
        self.gridLayout_19 = QGridLayout(self.frame_SideBarApps)
        self.gridLayout_19.setSpacing(10)
        self.gridLayout_19.setObjectName(u"gridLayout_19")
        self.gridLayout_19.setContentsMargins(10, 10, 10, 10)
        self.scrollArea = QScrollArea(self.frame_SideBarApps)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 330, 430))
        self.scrollAreaWidgetContents.setStyleSheet(u"")
        self.verticalLayout_11 = QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_11.setSpacing(5)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.verticalLayout_11.setContentsMargins(0, 0, 0, 0)
        self.button_SortByTime = QPushButton(self.scrollAreaWidgetContents)
        self.buttonGroup_Apps = QButtonGroup(MainWindow)
        self.buttonGroup_Apps.setObjectName(u"buttonGroup_Apps")
        self.buttonGroup_Apps.addButton(self.button_SortByTime)
        self.button_SortByTime.setObjectName(u"button_SortByTime")
        self.button_SortByTime.setCheckable(True)
        self.button_SortByTime.setChecked(True)

        self.verticalLayout_11.addWidget(self.button_SortByTime)

        self.button_SortByLikes = QPushButton(self.scrollAreaWidgetContents)
        self.buttonGroup_Apps.addButton(self.button_SortByLikes)
        self.button_SortByLikes.setObjectName(u"button_SortByLikes")
        self.button_SortByLikes.setCheckable(True)

        self.verticalLayout_11.addWidget(self.button_SortByLikes)

        self.button_SortByDislikes = QPushButton(self.scrollAreaWidgetContents)
        self.buttonGroup_Apps.addButton(self.button_SortByDislikes)
        self.button_SortByDislikes.setObjectName(u"button_SortByDislikes")
        self.button_SortByDislikes.setCheckable(True)

        self.verticalLayout_11.addWidget(self.button_SortByDislikes)

        self.button_SortByComments = QPushButton(self.scrollAreaWidgetContents)
        self.buttonGroup_Apps.addButton(self.button_SortByComments)
        self.button_SortByComments.setObjectName(u"button_SortByComments")
        self.button_SortByComments.setCheckable(True)

        self.verticalLayout_11.addWidget(self.button_SortByComments)

        self.button_SortByHot = QPushButton(self.scrollAreaWidgetContents)
        self.buttonGroup_Apps.addButton(self.button_SortByHot)
        self.button_SortByHot.setObjectName(u"button_SortByHot")
        self.button_SortByHot.setCheckable(True)

        self.verticalLayout_11.addWidget(self.button_SortByHot)

        self.label = QLabel(self.scrollAreaWidgetContents)
        self.label.setObjectName(u"label")
        self.label.setMaximumSize(QSize(16777215, 5))

        self.verticalLayout_11.addWidget(self.label)

        self.button_AppsAccount = QPushButton(self.scrollAreaWidgetContents)
        self.buttonGroup_Apps.addButton(self.button_AppsAccount)
        self.button_AppsAccount.setObjectName(u"button_AppsAccount")
        self.button_AppsAccount.setCheckable(True)

        self.verticalLayout_11.addWidget(self.button_AppsAccount)

        self.verticalSpacer_15 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_11.addItem(self.verticalSpacer_15)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.gridLayout_19.addWidget(self.scrollArea, 0, 0, 1, 1)


        self.gridLayout_14.addWidget(self.frame_SideBarApps, 0, 0, 1, 1)

        self.stacked_SideBar.addWidget(self.page_Apps)
        self.page_Chat = QWidget()
        self.page_Chat.setObjectName(u"page_Chat")
        self.page_Chat.setStyleSheet(u"")
        self.gridLayout_13 = QGridLayout(self.page_Chat)
        self.gridLayout_13.setSpacing(0)
        self.gridLayout_13.setObjectName(u"gridLayout_13")
        self.gridLayout_13.setContentsMargins(0, 0, 0, 0)
        self.frame_SideBarChat = QFrame(self.page_Chat)
        self.frame_SideBarChat.setObjectName(u"frame_SideBarChat")
        self.frame_SideBarChat.setFrameShape(QFrame.StyledPanel)
        self.frame_SideBarChat.setFrameShadow(QFrame.Raised)
        self.label_2 = QLabel(self.frame_SideBarChat)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(220, 220, 60, 16))

        self.gridLayout_13.addWidget(self.frame_SideBarChat, 0, 0, 1, 1)

        self.stacked_SideBar.addWidget(self.page_Chat)
        self.page_Notifications = QWidget()
        self.page_Notifications.setObjectName(u"page_Notifications")
        self.gridLayout_12 = QGridLayout(self.page_Notifications)
        self.gridLayout_12.setSpacing(0)
        self.gridLayout_12.setObjectName(u"gridLayout_12")
        self.gridLayout_12.setContentsMargins(0, 0, 0, 0)
        self.frame_SideBarNotifications = QFrame(self.page_Notifications)
        self.frame_SideBarNotifications.setObjectName(u"frame_SideBarNotifications")
        self.frame_SideBarNotifications.setFrameShape(QFrame.StyledPanel)
        self.frame_SideBarNotifications.setFrameShadow(QFrame.Raised)
        self.label_5 = QLabel(self.frame_SideBarNotifications)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(50, 230, 131, 16))

        self.gridLayout_12.addWidget(self.frame_SideBarNotifications, 0, 0, 1, 1)

        self.stacked_SideBar.addWidget(self.page_Notifications)

        self.horizontalLayout_9.addWidget(self.stacked_SideBar)

        self.stacked_Pages.addWidget(self.page_Home)
        self.page_Account = QWidget()
        self.page_Account.setObjectName(u"page_Account")
        self.page_Account.setStyleSheet(u"")
        self.gridLayout_5 = QGridLayout(self.page_Account)
        self.gridLayout_5.setSpacing(0)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.gridLayout_5.setContentsMargins(0, 0, 0, 0)
        self.scrollArea_Account = QScrollArea(self.page_Account)
        self.scrollArea_Account.setObjectName(u"scrollArea_Account")
        self.scrollArea_Account.setStyleSheet(u"")
        self.scrollArea_Account.setWidgetResizable(True)
        self.scrollAreaWidget_Account = QWidget()
        self.scrollAreaWidget_Account.setObjectName(u"scrollAreaWidget_Account")
        self.scrollAreaWidget_Account.setGeometry(QRect(0, 0, 1000, 1065))
        self.scrollAreaWidget_Account.setStyleSheet(u"QFrame#frame_AccountTabsContainer {\n"
"	border: 0;\n"
"}")
        self.gridLayout_4 = QGridLayout(self.scrollAreaWidget_Account)
        self.gridLayout_4.setSpacing(0)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.gridLayout_4.setContentsMargins(0, 0, 0, 0)
        self.frame_AccountTabsContainer = QFrame(self.scrollAreaWidget_Account)
        self.frame_AccountTabsContainer.setObjectName(u"frame_AccountTabsContainer")
        self.frame_AccountTabsContainer.setMinimumSize(QSize(0, 800))
        self.frame_AccountTabsContainer.setMaximumSize(QSize(1000, 16777215))
        self.frame_AccountTabsContainer.setStyleSheet(u"")
        self.frame_AccountTabsContainer.setFrameShape(QFrame.StyledPanel)
        self.frame_AccountTabsContainer.setFrameShadow(QFrame.Raised)
        self.verticalLayout_6 = QVBoxLayout(self.frame_AccountTabsContainer)
        self.verticalLayout_6.setSpacing(0)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(10, 15, 10, 0)
        self.frame_AccountTabs = QFrame(self.frame_AccountTabsContainer)
        self.frame_AccountTabs.setObjectName(u"frame_AccountTabs")
        self.frame_AccountTabs.setMinimumSize(QSize(0, 60))
        self.frame_AccountTabs.setMaximumSize(QSize(16777215, 60))
        self.frame_AccountTabs.setStyleSheet(u"QFrame {\n"
"	border-radius: 0;\n"
"	border-top-left-radius: 20px;\n"
"	border-top-right-radius: 20px;\n"
"	border-bottom: 1px solid rgb(235, 237, 239);\n"
"	border-top: 1px solid rgb(235, 237, 239);\n"
"}\n"
"\n"
"QPushButton {\n"
"	height: 40px;\n"
"	width: 150px;\n"
"	border-radius: 15px;\n"
"	color: black;\n"
"	background-color:  white;\n"
"}\n"
"\n"
"QPushButton:checked  {\n"
"	background-color:  rgb(235, 237, 239);\n"
"}\n"
"\n"
"QPushButton:hover  {\n"
"	background-color:  rgb(235, 237, 239);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"	background-color: rgb(184,191,195);\n"
"}\n"
"")
        self.frame_AccountTabs.setFrameShape(QFrame.StyledPanel)
        self.frame_AccountTabs.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.frame_AccountTabs)
        self.horizontalLayout_3.setSpacing(10)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(10, 10, 10, 10)
        self.button_AccountTabsPosts = QPushButton(self.frame_AccountTabs)
        self.buttonGroup_AccountTabs = QButtonGroup(MainWindow)
        self.buttonGroup_AccountTabs.setObjectName(u"buttonGroup_AccountTabs")
        self.buttonGroup_AccountTabs.addButton(self.button_AccountTabsPosts)
        self.button_AccountTabsPosts.setObjectName(u"button_AccountTabsPosts")
        self.button_AccountTabsPosts.setCheckable(True)

        self.horizontalLayout_3.addWidget(self.button_AccountTabsPosts)

        self.button_AccountTabsFollows = QPushButton(self.frame_AccountTabs)
        self.buttonGroup_AccountTabs.addButton(self.button_AccountTabsFollows)
        self.button_AccountTabsFollows.setObjectName(u"button_AccountTabsFollows")
        self.button_AccountTabsFollows.setCheckable(True)

        self.horizontalLayout_3.addWidget(self.button_AccountTabsFollows)


        self.verticalLayout_6.addWidget(self.frame_AccountTabs)

        self.stacked_AccountTabs = QStackedWidget(self.frame_AccountTabsContainer)
        self.stacked_AccountTabs.setObjectName(u"stacked_AccountTabs")
        self.stacked_AccountTabs.setMinimumSize(QSize(0, 800))
        self.page_AccountTabsPosts = QWidget()
        self.page_AccountTabsPosts.setObjectName(u"page_AccountTabsPosts")
        self.verticalLayout_5 = QVBoxLayout(self.page_AccountTabsPosts)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.frame = QFrame(self.page_AccountTabsPosts)
        self.frame.setObjectName(u"frame")
        self.frame.setMinimumSize(QSize(0, 400))
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)

        self.verticalLayout_5.addWidget(self.frame)

        self.stacked_AccountTabs.addWidget(self.page_AccountTabsPosts)
        self.page_AccountTabsFollows = QWidget()
        self.page_AccountTabsFollows.setObjectName(u"page_AccountTabsFollows")
        self.stacked_AccountTabs.addWidget(self.page_AccountTabsFollows)

        self.verticalLayout_6.addWidget(self.stacked_AccountTabs)


        self.gridLayout_4.addWidget(self.frame_AccountTabsContainer, 1, 0, 1, 2)

        self.frame_AccountInfoContainer = QFrame(self.scrollAreaWidget_Account)
        self.frame_AccountInfoContainer.setObjectName(u"frame_AccountInfoContainer")
        self.frame_AccountInfoContainer.setMinimumSize(QSize(0, 190))
        self.frame_AccountInfoContainer.setMaximumSize(QSize(1000, 190))
        self.frame_AccountInfoContainer.setStyleSheet(u"QFrame {\n"
"	background: transponent;\n"
"	color: white;\n"
"}\n"
"\n"
"QLabel#label_AccountPhoto {\n"
"	border-radius: 75px;\n"
"}\n"
"\n"
"QFrame#frame_AccountInfoContainer {\n"
"	border-radius: 0;\n"
"}\n"
"\n"
"")
        self.frame_AccountInfoContainer.setFrameShape(QFrame.StyledPanel)
        self.frame_AccountInfoContainer.setFrameShadow(QFrame.Raised)
        self.layout_AccountInfoContainer = QHBoxLayout(self.frame_AccountInfoContainer)
        self.layout_AccountInfoContainer.setSpacing(10)
        self.layout_AccountInfoContainer.setObjectName(u"layout_AccountInfoContainer")
        self.layout_AccountInfoContainer.setContentsMargins(20, 15, 10, 0)
        self.frame_AccountInfo = QFrame(self.frame_AccountInfoContainer)
        self.frame_AccountInfo.setObjectName(u"frame_AccountInfo")
        self.frame_AccountInfo.setMinimumSize(QSize(0, 150))
        self.frame_AccountInfo.setMaximumSize(QSize(16777215, 150))
        font1 = QFont()
        font1.setFamilies([u".AppleSystemUIFont"])
        font1.setBold(False)
        self.frame_AccountInfo.setFont(font1)
        self.frame_AccountInfo.setStyleSheet(u"QFrame {\n"
"	border-top-left-radius: 0;\n"
"	border-top-right-radius: 0;\n"
"}\n"
"\n"
"QLabel#label_AccountInformationText {\n"
"	padding-bottom: 5px;\n"
"	border-bottom: 1px solid rgb(229,235,238);\n"
"}\n"
"\n"
"QLabel#label_AccountInformationID {\n"
"	margin: 0;\n"
"	border-bottom-left-radius: 10px;\n"
"}\n"
"\n"
"QLabel#label_AccountInformationAccess{\n"
"	margin: 0;\n"
"	border-bottom-right-radius: 10px;\n"
"}\n"
"\n"
"\n"
"/* ------- EXIT BUTTONS ------- */\n"
"\n"
"\n"
"QFrame#frame_AccountInfoConfirmation {\n"
"	background: transponent;\n"
"	border-radius: 20px;\n"
"}\n"
"\n"
"QPushButton#button_AccountEdit,\n"
"QPushButton#button_AccountExit,\n"
"QPushButton#button_AccountExitYes,\n"
"QPushButton#button_AccountExitNo {\n"
"	background-color: white;\n"
"}\n"
"\n"
"QPushButton#button_AccountEdit::hover {\n"
"	background-color: rgb(235, 237, 239);\n"
"}\n"
"\n"
"QPushButton#button_AccountEdit::pressed {\n"
"	background-color: rgb(184,191,195);\n"
"}\n"
"\n"
"\n"
"QPushButton#button_AccountExit:pressed "
                        "{\n"
"	background-color: rgb(240,0,0);\n"
"}\n"
"\n"
"QPushButton#button_AccountExitYes {\n"
"	border-top-right-radius: 0;\n"
"	border-bottom-right-radius: 0;\n"
"}\n"
"\n"
"QPushButton#button_AccountExitYes:pressed {\n"
"	background-color: rgb(167,0,0);\n"
"}\n"
"\n"
"QPushButton#button_AccountExitNo {\n"
"	border-top-left-radius: 0;\n"
"	border-bottom-left-radius: 0;\n"
"}\n"
"\n"
"QPushButton#button_AccountExitNo:pressed {\n"
"	background-color: #007200;\n"
"}\n"
"\n"
"\n"
"")
        self.frame_AccountInfo.setFrameShape(QFrame.StyledPanel)
        self.frame_AccountInfo.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame_AccountInfo)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(10, 0, 5, 0)
        self.verticalSpacer_2 = QSpacerItem(20, 60, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Maximum)

        self.verticalLayout_2.addItem(self.verticalSpacer_2)

        self.frame_AccountLabels_1 = QFrame(self.frame_AccountInfo)
        self.frame_AccountLabels_1.setObjectName(u"frame_AccountLabels_1")
        self.frame_AccountLabels_1.setMinimumSize(QSize(0, 30))
        self.frame_AccountLabels_1.setMaximumSize(QSize(16777215, 30))
        self.frame_AccountLabels_1.setStyleSheet(u"")
        self.frame_AccountLabels_1.setFrameShape(QFrame.StyledPanel)
        self.frame_AccountLabels_1.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.frame_AccountLabels_1)
        self.horizontalLayout_4.setSpacing(5)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.label_AccountNickname = QLabel(self.frame_AccountLabels_1)
        self.label_AccountNickname.setObjectName(u"label_AccountNickname")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_AccountNickname.sizePolicy().hasHeightForWidth())
        self.label_AccountNickname.setSizePolicy(sizePolicy)
        self.label_AccountNickname.setMinimumSize(QSize(0, 30))
        self.label_AccountNickname.setMaximumSize(QSize(16777215, 30))
        font2 = QFont()
        font2.setPointSize(28)
        self.label_AccountNickname.setFont(font2)
        self.label_AccountNickname.setStyleSheet(u"")
        self.label_AccountNickname.setScaledContents(False)
        self.label_AccountNickname.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)
        self.label_AccountNickname.setMargin(0)
        self.label_AccountNickname.setIndent(0)
        self.label_AccountNickname.setTextInteractionFlags(Qt.LinksAccessibleByMouse|Qt.TextSelectableByKeyboard|Qt.TextSelectableByMouse)

        self.horizontalLayout_4.addWidget(self.label_AccountNickname)

        self.label_AccountStatus = QLabel(self.frame_AccountLabels_1)
        self.label_AccountStatus.setObjectName(u"label_AccountStatus")
        self.label_AccountStatus.setMinimumSize(QSize(0, 0))
        self.label_AccountStatus.setMaximumSize(QSize(16777215, 16777215))
        self.label_AccountStatus.setTextFormat(Qt.RichText)
        self.label_AccountStatus.setAlignment(Qt.AlignBottom|Qt.AlignLeading|Qt.AlignLeft)
        self.label_AccountStatus.setTextInteractionFlags(Qt.LinksAccessibleByMouse|Qt.TextSelectableByMouse)

        self.horizontalLayout_4.addWidget(self.label_AccountStatus)

        self.horizontalSpacer_5 = QSpacerItem(151, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer_5)


        self.verticalLayout_2.addWidget(self.frame_AccountLabels_1)

        self.frame_AccountButtons = QFrame(self.frame_AccountInfo)
        self.frame_AccountButtons.setObjectName(u"frame_AccountButtons")
        self.frame_AccountButtons.setMinimumSize(QSize(0, 0))
        self.frame_AccountButtons.setMaximumSize(QSize(16777215, 90))
        self.frame_AccountButtons.setStyleSheet(u"")
        self.frame_AccountButtons.setFrameShape(QFrame.StyledPanel)
        self.frame_AccountButtons.setFrameShadow(QFrame.Raised)
        self.gridLayout_6 = QGridLayout(self.frame_AccountButtons)
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.gridLayout_6.setHorizontalSpacing(5)
        self.gridLayout_6.setVerticalSpacing(10)
        self.gridLayout_6.setContentsMargins(0, 0, 5, 5)
        self.horizontalSpacer_4 = QSpacerItem(182, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_6.addItem(self.horizontalSpacer_4, 0, 1, 1, 4)

        self.button_AccountExit = QPushButton(self.frame_AccountButtons)
        self.buttonGroup_AccountExit = QButtonGroup(MainWindow)
        self.buttonGroup_AccountExit.setObjectName(u"buttonGroup_AccountExit")
        self.buttonGroup_AccountExit.addButton(self.button_AccountExit)
        self.button_AccountExit.setObjectName(u"button_AccountExit")
        self.button_AccountExit.setCheckable(True)
        self.button_AccountExit.setChecked(False)

        self.gridLayout_6.addWidget(self.button_AccountExit, 1, 4, 1, 1)

        self.horizontalSpacer_7 = QSpacerItem(7, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_6.addItem(self.horizontalSpacer_7, 1, 1, 1, 1)

        self.frame_AccountInformationContainer = QFrame(self.frame_AccountButtons)
        self.frame_AccountInformationContainer.setObjectName(u"frame_AccountInformationContainer")
        self.frame_AccountInformationContainer.setMinimumSize(QSize(200, 60))
        self.frame_AccountInformationContainer.setMaximumSize(QSize(16777215, 90))
        self.frame_AccountInformationContainer.setStyleSheet(u"")
        self.frame_AccountInformationContainer.setFrameShape(QFrame.StyledPanel)
        self.frame_AccountInformationContainer.setFrameShadow(QFrame.Raised)
        self.gridLayout_7 = QGridLayout(self.frame_AccountInformationContainer)
        self.gridLayout_7.setSpacing(0)
        self.gridLayout_7.setObjectName(u"gridLayout_7")
        self.gridLayout_7.setContentsMargins(0, 0, 0, 5)
        self.label_AccountInformationID = QLabel(self.frame_AccountInformationContainer)
        self.label_AccountInformationID.setObjectName(u"label_AccountInformationID")
        self.label_AccountInformationID.setMinimumSize(QSize(0, 20))
        self.label_AccountInformationID.setMaximumSize(QSize(100, 20))
        font3 = QFont()
        font3.setPointSize(12)
        font3.setItalic(False)
        self.label_AccountInformationID.setFont(font3)
        self.label_AccountInformationID.setStyleSheet(u"")
        self.label_AccountInformationID.setIndent(0)
        self.label_AccountInformationID.setTextInteractionFlags(Qt.LinksAccessibleByMouse|Qt.TextSelectableByKeyboard|Qt.TextSelectableByMouse)

        self.gridLayout_7.addWidget(self.label_AccountInformationID, 1, 0, 1, 1)

        self.label_AccountAbout = QLabel(self.frame_AccountInformationContainer)
        self.label_AccountAbout.setObjectName(u"label_AccountAbout")
        self.label_AccountAbout.setMinimumSize(QSize(300, 20))
        self.label_AccountAbout.setMaximumSize(QSize(300, 70))
        font4 = QFont()
        font4.setItalic(False)
        self.label_AccountAbout.setFont(font4)
        self.label_AccountAbout.setStyleSheet(u"")
        self.label_AccountAbout.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.label_AccountAbout.setWordWrap(True)
        self.label_AccountAbout.setIndent(0)
        self.label_AccountAbout.setTextInteractionFlags(Qt.LinksAccessibleByMouse|Qt.TextSelectableByMouse)

        self.gridLayout_7.addWidget(self.label_AccountAbout, 0, 0, 1, 2)

        self.label_AccountInformationAccess = QLabel(self.frame_AccountInformationContainer)
        self.label_AccountInformationAccess.setObjectName(u"label_AccountInformationAccess")
        self.label_AccountInformationAccess.setMaximumSize(QSize(100, 16777215))
        self.label_AccountInformationAccess.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.label_AccountInformationAccess.setIndent(0)

        self.gridLayout_7.addWidget(self.label_AccountInformationAccess, 1, 1, 1, 1)


        self.gridLayout_6.addWidget(self.frame_AccountInformationContainer, 0, 0, 2, 1)

        self.frame_AccountExitConfirmation = QFrame(self.frame_AccountButtons)
        self.frame_AccountExitConfirmation.setObjectName(u"frame_AccountExitConfirmation")
        self.frame_AccountExitConfirmation.setMinimumSize(QSize(80, 40))
        self.frame_AccountExitConfirmation.setMaximumSize(QSize(80, 40))
        self.frame_AccountExitConfirmation.setStyleSheet(u"")
        self.frame_AccountExitConfirmation.setFrameShape(QFrame.StyledPanel)
        self.frame_AccountExitConfirmation.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_8 = QHBoxLayout(self.frame_AccountExitConfirmation)
        self.horizontalLayout_8.setSpacing(0)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.horizontalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.button_AccountExitYes = QPushButton(self.frame_AccountExitConfirmation)
        self.button_AccountExitYes.setObjectName(u"button_AccountExitYes")
        self.button_AccountExitYes.setCheckable(False)
        self.button_AccountExitYes.setChecked(False)

        self.horizontalLayout_8.addWidget(self.button_AccountExitYes)

        self.button_AccountExitNo = QPushButton(self.frame_AccountExitConfirmation)
        self.buttonGroup_AccountExit.addButton(self.button_AccountExitNo)
        self.button_AccountExitNo.setObjectName(u"button_AccountExitNo")
        self.button_AccountExitNo.setCheckable(True)
        self.button_AccountExitNo.setChecked(True)

        self.horizontalLayout_8.addWidget(self.button_AccountExitNo)


        self.gridLayout_6.addWidget(self.frame_AccountExitConfirmation, 1, 3, 1, 1)

        self.button_AccountEdit = QPushButton(self.frame_AccountButtons)
        self.buttonGroup_MainTabs.addButton(self.button_AccountEdit)
        self.button_AccountEdit.setObjectName(u"button_AccountEdit")
        self.button_AccountEdit.setCheckable(True)

        self.gridLayout_6.addWidget(self.button_AccountEdit, 1, 2, 1, 1)


        self.verticalLayout_2.addWidget(self.frame_AccountButtons)


        self.layout_AccountInfoContainer.addWidget(self.frame_AccountInfo)


        self.gridLayout_4.addWidget(self.frame_AccountInfoContainer, 0, 0, 1, 2)

        self.scrollArea_Account.setWidget(self.scrollAreaWidget_Account)

        self.gridLayout_5.addWidget(self.scrollArea_Account, 0, 0, 1, 1)

        self.stacked_Pages.addWidget(self.page_Account)
        self.page_AccountEdit = QWidget()
        self.page_AccountEdit.setObjectName(u"page_AccountEdit")
        self.page_AccountEdit.setStyleSheet(u"")
        self.verticalLayout_10 = QVBoxLayout(self.page_AccountEdit)
        self.verticalLayout_10.setSpacing(0)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.verticalLayout_10.setContentsMargins(0, 0, 0, 0)
        self.frame_AccountEditContainer = QFrame(self.page_AccountEdit)
        self.frame_AccountEditContainer.setObjectName(u"frame_AccountEditContainer")
        self.frame_AccountEditContainer.setMinimumSize(QSize(0, 0))
        self.frame_AccountEditContainer.setStyleSheet(u"")
        self.frame_AccountEditContainer.setFrameShape(QFrame.StyledPanel)
        self.frame_AccountEditContainer.setFrameShadow(QFrame.Raised)
        self.verticalLayout_13 = QVBoxLayout(self.frame_AccountEditContainer)
        self.verticalLayout_13.setSpacing(10)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.verticalLayout_13.setContentsMargins(20, 0, 0, 10)
        self.scrollArea_AccountEdit = QScrollArea(self.frame_AccountEditContainer)
        self.scrollArea_AccountEdit.setObjectName(u"scrollArea_AccountEdit")
        self.scrollArea_AccountEdit.setStyleSheet(u"")
        self.scrollArea_AccountEdit.setWidgetResizable(True)
        self.scrollAreaWidget_AccountEdit = QWidget()
        self.scrollAreaWidget_AccountEdit.setObjectName(u"scrollAreaWidget_AccountEdit")
        self.scrollAreaWidget_AccountEdit.setGeometry(QRect(0, 0, 980, 761))
        self.scrollAreaWidget_AccountEdit.setStyleSheet(u"")
        self.verticalLayout_8 = QVBoxLayout(self.scrollAreaWidget_AccountEdit)
        self.verticalLayout_8.setSpacing(10)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.verticalLayout_8.setContentsMargins(0, 0, 20, 0)
        self.frame_AccountEditTabsContainer = QFrame(self.scrollAreaWidget_AccountEdit)
        self.frame_AccountEditTabsContainer.setObjectName(u"frame_AccountEditTabsContainer")
        self.frame_AccountEditTabsContainer.setStyleSheet(u"QLabel {\n"
"	border: 0;\n"
"	color: black;\n"
"}")
        self.frame_AccountEditTabsContainer.setFrameShape(QFrame.StyledPanel)
        self.frame_AccountEditTabsContainer.setFrameShadow(QFrame.Raised)
        self.verticalLayout_12 = QVBoxLayout(self.frame_AccountEditTabsContainer)
        self.verticalLayout_12.setSpacing(0)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.verticalLayout_12.setContentsMargins(0, 0, 0, 0)
        self.label_AccountEditSettings = QLabel(self.frame_AccountEditTabsContainer)
        self.label_AccountEditSettings.setObjectName(u"label_AccountEditSettings")
        self.label_AccountEditSettings.setMinimumSize(QSize(0, 50))
        self.label_AccountEditSettings.setMaximumSize(QSize(16777215, 50))
        font5 = QFont()
        font5.setPointSize(20)
        font5.setBold(False)
        font5.setItalic(False)
        font5.setUnderline(False)
        font5.setStrikeOut(False)
        self.label_AccountEditSettings.setFont(font5)
        self.label_AccountEditSettings.setStyleSheet(u"")
        self.label_AccountEditSettings.setLineWidth(0)
        self.label_AccountEditSettings.setIndent(0)

        self.verticalLayout_12.addWidget(self.label_AccountEditSettings)

        self.frame_AccountEditTabs = QFrame(self.frame_AccountEditTabsContainer)
        self.frame_AccountEditTabs.setObjectName(u"frame_AccountEditTabs")
        self.frame_AccountEditTabs.setMinimumSize(QSize(0, 50))
        self.frame_AccountEditTabs.setMaximumSize(QSize(16777215, 50))
        self.frame_AccountEditTabs.setStyleSheet(u"QFrame {\n"
"	border-radius: 0;\n"
"	border-top-left-radius: 20px;\n"
"	border-top-right-radius: 20px;\n"
"	border-bottom: 1px solid rgb(235, 237, 239);\n"
"}\n"
"\n"
"QPushButton {\n"
"	width: 150px;\n"
"	border-radius: 15px;\n"
"	color: black;\n"
"	background-color:  white;\n"
"}\n"
"\n"
"\n"
"QPushButton:checked  {\n"
"	background-color:  rgb(235, 237, 239);\n"
"}\n"
"\n"
"QPushButton:hover  {\n"
"	background-color:  rgb(235, 237, 239);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"	background-color: rgb(184,191,195);\n"
"}\n"
"\n"
"")
        self.frame_AccountEditTabs.setFrameShape(QFrame.StyledPanel)
        self.frame_AccountEditTabs.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_11 = QHBoxLayout(self.frame_AccountEditTabs)
        self.horizontalLayout_11.setSpacing(10)
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.horizontalLayout_11.setContentsMargins(0, 0, 0, 10)
        self.button_AccountEditTabsProfile = QPushButton(self.frame_AccountEditTabs)
        self.buttonGroup_AccountEditTabs = QButtonGroup(MainWindow)
        self.buttonGroup_AccountEditTabs.setObjectName(u"buttonGroup_AccountEditTabs")
        self.buttonGroup_AccountEditTabs.addButton(self.button_AccountEditTabsProfile)
        self.button_AccountEditTabsProfile.setObjectName(u"button_AccountEditTabsProfile")
        self.button_AccountEditTabsProfile.setCheckable(True)
        self.button_AccountEditTabsProfile.setChecked(True)

        self.horizontalLayout_11.addWidget(self.button_AccountEditTabsProfile)

        self.horizontalSpacer_10 = QSpacerItem(20, 20, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_11.addItem(self.horizontalSpacer_10)

        self.button_AccountEditTabsPrivacy = QPushButton(self.frame_AccountEditTabs)
        self.buttonGroup_AccountEditTabs.addButton(self.button_AccountEditTabsPrivacy)
        self.button_AccountEditTabsPrivacy.setObjectName(u"button_AccountEditTabsPrivacy")
        self.button_AccountEditTabsPrivacy.setCheckable(True)

        self.horizontalLayout_11.addWidget(self.button_AccountEditTabsPrivacy)

        self.horizontalSpacer_11 = QSpacerItem(20, 20, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_11.addItem(self.horizontalSpacer_11)

        self.button_AccountEditTabsChat = QPushButton(self.frame_AccountEditTabs)
        self.buttonGroup_AccountEditTabs.addButton(self.button_AccountEditTabsChat)
        self.button_AccountEditTabsChat.setObjectName(u"button_AccountEditTabsChat")
        self.button_AccountEditTabsChat.setCheckable(True)

        self.horizontalLayout_11.addWidget(self.button_AccountEditTabsChat)


        self.verticalLayout_12.addWidget(self.frame_AccountEditTabs)


        self.verticalLayout_8.addWidget(self.frame_AccountEditTabsContainer)

        self.stacked_AccountEditTabs = QStackedWidget(self.scrollAreaWidget_AccountEdit)
        self.stacked_AccountEditTabs.setObjectName(u"stacked_AccountEditTabs")
        self.stacked_AccountEditTabs.setMinimumSize(QSize(0, 0))
        self.stacked_AccountEditTabs.setStyleSheet(u"")
        self.page_AccountEditTabsProfile = QWidget()
        self.page_AccountEditTabsProfile.setObjectName(u"page_AccountEditTabsProfile")
        self.page_AccountEditTabsProfile.setStyleSheet(u"QLabel {\n"
"	color: rgb(184,191,195);\n"
"	border-bottom: 1px solid rgb(235, 237, 239);\n"
"}\n"
"\n"
"QLabel#label_AccountEditProfileWarning {\n"
"	color: red;\n"
"}")
        self.verticalLayout_9 = QVBoxLayout(self.page_AccountEditTabsProfile)
        self.verticalLayout_9.setSpacing(20)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.verticalLayout_9.setContentsMargins(10, 10, 10, 10)
        self.frame_AccountEditProfileContainer = QFrame(self.page_AccountEditTabsProfile)
        self.frame_AccountEditProfileContainer.setObjectName(u"frame_AccountEditProfileContainer")
        self.frame_AccountEditProfileContainer.setStyleSheet(u"QLabel {\n"
"	color: rgb(184,191,195);\n"
"	border-bottom: 1px solid rgb(235, 237, 239);\n"
"}\n"
"\n"
"QLabel#label_AccountEditProfileWarning {\n"
"	color: red;\n"
"}\n"
"\n"
"QPushButton#button_AccountEditProfileCancel {\n"
"	color: white;\n"
"	background-color: rgb(255,0,0);\n"
"}\n"
"\n"
"QPushButton#button_AccountEditProfileCancel::hover {	\n"
"	background-color: rgb(240,0,0);\n"
"}\n"
"\n"
"QPushButton#button_AccountEditProfileCancel::pressed {\n"
"	background-color: rgb(225,0,0);\n"
"}\n"
"\n"
"QPushButton#button_AccountEditPhotoDelete::pressed {\n"
"	background-color: rgb(225,0,0);\n"
"}\n"
"\n"
"QPushButton#button_AccountEditAboutDelete::pressed {\n"
"	background-color: rgb(225,0,0);\n"
"}\n"
"\n"
"\n"
"QPushButton#button_AccountEditProfileSave {\n"
"	color: white;\n"
"	background-color: rgb(0,210,0);\n"
"}\n"
"\n"
"QPushButton#button_AccountEditProfileSave::hover {\n"
"	background-color: rgb(0,195,0);\n"
"}\n"
"\n"
"QPushButton#button_AccountEditProfileSave::pressed{\n"
"	background-color: rgb(0,180,"
                        "0);\n"
"}\n"
"\n"
"\n"
"\n"
"")
        self.frame_AccountEditProfileContainer.setFrameShape(QFrame.StyledPanel)
        self.frame_AccountEditProfileContainer.setFrameShadow(QFrame.Raised)
        self.verticalLayout_14 = QVBoxLayout(self.frame_AccountEditProfileContainer)
        self.verticalLayout_14.setSpacing(0)
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.verticalLayout_14.setContentsMargins(0, 0, 0, 0)
        self.label_AccountEditPhoto = QLabel(self.frame_AccountEditProfileContainer)
        self.label_AccountEditPhoto.setObjectName(u"label_AccountEditPhoto")
        self.label_AccountEditPhoto.setMaximumSize(QSize(16777215, 20))
        font6 = QFont()
        font6.setPointSize(10)
        self.label_AccountEditPhoto.setFont(font6)
        self.label_AccountEditPhoto.setIndent(0)

        self.verticalLayout_14.addWidget(self.label_AccountEditPhoto)

        self.verticalSpacer_9 = QSpacerItem(20, 20, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Minimum)

        self.verticalLayout_14.addItem(self.verticalSpacer_9)

        self.frame_AccountEditPhotoContainer = QFrame(self.frame_AccountEditProfileContainer)
        self.frame_AccountEditPhotoContainer.setObjectName(u"frame_AccountEditPhotoContainer")
        self.frame_AccountEditPhotoContainer.setMinimumSize(QSize(0, 150))
        self.frame_AccountEditPhotoContainer.setMaximumSize(QSize(16777215, 150))
        self.frame_AccountEditPhotoContainer.setStyleSheet(u"")
        self.frame_AccountEditPhotoContainer.setFrameShape(QFrame.StyledPanel)
        self.frame_AccountEditPhotoContainer.setFrameShadow(QFrame.Raised)
        self.layout_AccountEditImages = QHBoxLayout(self.frame_AccountEditPhotoContainer)
        self.layout_AccountEditImages.setSpacing(20)
        self.layout_AccountEditImages.setObjectName(u"layout_AccountEditImages")
        self.layout_AccountEditImages.setContentsMargins(0, 0, 0, 0)
        self.frame_AccountEditPhoto = QFrame(self.frame_AccountEditPhotoContainer)
        self.frame_AccountEditPhoto.setObjectName(u"frame_AccountEditPhoto")
        self.frame_AccountEditPhoto.setMinimumSize(QSize(150, 150))
        self.frame_AccountEditPhoto.setMaximumSize(QSize(150, 150))
        self.frame_AccountEditPhoto.setStyleSheet(u"")
        self.frame_AccountEditPhoto.setFrameShape(QFrame.StyledPanel)
        self.frame_AccountEditPhoto.setFrameShadow(QFrame.Raised)
        self.gridLayout_8 = QGridLayout(self.frame_AccountEditPhoto)
        self.gridLayout_8.setSpacing(10)
        self.gridLayout_8.setObjectName(u"gridLayout_8")
        self.gridLayout_8.setContentsMargins(0, 0, 0, 0)
        self.button_AccountEditPhotoAdd = QPushButton(self.frame_AccountEditPhoto)
        self.button_AccountEditPhotoAdd.setObjectName(u"button_AccountEditPhotoAdd")
        self.button_AccountEditPhotoAdd.setMinimumSize(QSize(40, 40))
        self.button_AccountEditPhotoAdd.setMaximumSize(QSize(40, 40))

        self.gridLayout_8.addWidget(self.button_AccountEditPhotoAdd, 2, 2, 1, 1)

        self.horizontalSpacer_6 = QSpacerItem(97, 37, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_8.addItem(self.horizontalSpacer_6, 2, 1, 1, 1)

        self.verticalSpacer_6 = QSpacerItem(20, 97, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout_8.addItem(self.verticalSpacer_6, 1, 0, 2, 1)

        self.verticalSpacer_4 = QSpacerItem(37, 97, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout_8.addItem(self.verticalSpacer_4, 0, 2, 2, 1)

        self.button_AccountEditPhotoDelete = QPushButton(self.frame_AccountEditPhoto)
        self.button_AccountEditPhotoDelete.setObjectName(u"button_AccountEditPhotoDelete")
        self.button_AccountEditPhotoDelete.setMinimumSize(QSize(40, 40))
        self.button_AccountEditPhotoDelete.setMaximumSize(QSize(40, 40))
        self.button_AccountEditPhotoDelete.setStyleSheet(u"")

        self.gridLayout_8.addWidget(self.button_AccountEditPhotoDelete, 0, 0, 1, 1)


        self.layout_AccountEditImages.addWidget(self.frame_AccountEditPhoto)

        self.horizontalSpacer_12 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.layout_AccountEditImages.addItem(self.horizontalSpacer_12)


        self.verticalLayout_14.addWidget(self.frame_AccountEditPhotoContainer)

        self.verticalSpacer_5 = QSpacerItem(20, 20, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Minimum)

        self.verticalLayout_14.addItem(self.verticalSpacer_5)

        self.label_AccountEditPhoto_2 = QLabel(self.frame_AccountEditProfileContainer)
        self.label_AccountEditPhoto_2.setObjectName(u"label_AccountEditPhoto_2")
        self.label_AccountEditPhoto_2.setMaximumSize(QSize(16777215, 20))
        self.label_AccountEditPhoto_2.setFont(font6)
        self.label_AccountEditPhoto_2.setStyleSheet(u"")
        self.label_AccountEditPhoto_2.setIndent(0)

        self.verticalLayout_14.addWidget(self.label_AccountEditPhoto_2)

        self.frame_AccountEditAccountContainer = QFrame(self.frame_AccountEditProfileContainer)
        self.frame_AccountEditAccountContainer.setObjectName(u"frame_AccountEditAccountContainer")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(215)
        sizePolicy1.setHeightForWidth(self.frame_AccountEditAccountContainer.sizePolicy().hasHeightForWidth())
        self.frame_AccountEditAccountContainer.setSizePolicy(sizePolicy1)
        self.frame_AccountEditAccountContainer.setMinimumSize(QSize(0, 0))
        self.frame_AccountEditAccountContainer.setMaximumSize(QSize(16777215, 16777215))
        self.frame_AccountEditAccountContainer.setStyleSheet(u"QFrame {\n"
"	background: white;\n"
"}\n"
"\n"
"QPushButton#button_AccountEditAboutDelete {\n"
"	border-radius: 15px;\n"
"}\n"
"\n"
"QLabel { \n"
"	border: 0;\n"
"	color: black;\n"
"}\n"
"\n"
"QLabel#label_Sign_1,\n"
"QLabel#label_AccountEditNameSymbols,\n"
"QLabel#label_Sign_3,\n"
"QLabel#label_AccountEditAboutSymbols,\n"
"QLabel#label_Sign_4,\n"
"QLabel#label_AccountEditUsernameSymbols { \n"
"	color: rgb(184,191,195);\n"
"}\n"
"\n"
"\n"
"QLineEdit {\n"
"	border: 1px solid rgb(235, 237, 239);\n"
"	border-radius: 5px;\n"
"}\n"
"\n"
"QLineEdit::focus {\n"
"	border: 2px solid rgb(64,135,216);\n"
"}\n"
"\n"
"QTextEdit {\n"
"	border: 1px solid rgb(235, 237, 239);\n"
"	border-radius: 5px;\n"
"}\n"
"\n"
"QTextEdit::focus {\n"
"	border: 2px solid rgb(64,135,216);\n"
"}")
        self.frame_AccountEditAccountContainer.setFrameShape(QFrame.StyledPanel)
        self.frame_AccountEditAccountContainer.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.frame_AccountEditAccountContainer)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.frame_AccountEditNickname = QFrame(self.frame_AccountEditAccountContainer)
        self.frame_AccountEditNickname.setObjectName(u"frame_AccountEditNickname")
        self.frame_AccountEditNickname.setMinimumSize(QSize(0, 105))
        self.frame_AccountEditNickname.setMaximumSize(QSize(16777215, 105))
        self.frame_AccountEditNickname.setStyleSheet(u"")
        self.frame_AccountEditNickname.setFrameShape(QFrame.StyledPanel)
        self.frame_AccountEditNickname.setFrameShadow(QFrame.Raised)
        self.gridLayout_9 = QGridLayout(self.frame_AccountEditNickname)
        self.gridLayout_9.setObjectName(u"gridLayout_9")
        self.gridLayout_9.setHorizontalSpacing(10)
        self.gridLayout_9.setVerticalSpacing(0)
        self.gridLayout_9.setContentsMargins(0, 0, 0, 0)
        self.label_3 = QLabel(self.frame_AccountEditNickname)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setMinimumSize(QSize(0, 25))
        self.label_3.setMaximumSize(QSize(16777215, 25))
        font7 = QFont()
        font7.setPointSize(15)
        self.label_3.setFont(font7)
        self.label_3.setAlignment(Qt.AlignBottom|Qt.AlignLeading|Qt.AlignLeft)
        self.label_3.setTextInteractionFlags(Qt.LinksAccessibleByMouse)

        self.gridLayout_9.addWidget(self.label_3, 1, 0, 1, 1)

        self.horizontalSpacer_8 = QSpacerItem(151, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_9.addItem(self.horizontalSpacer_8, 1, 1, 4, 1)

        self.label_Sign_3 = QLabel(self.frame_AccountEditNickname)
        self.label_Sign_3.setObjectName(u"label_Sign_3")
        self.label_Sign_3.setMinimumSize(QSize(0, 15))
        self.label_Sign_3.setMaximumSize(QSize(16777215, 15))
        self.label_Sign_3.setFont(font6)
        self.label_Sign_3.setIndent(0)
        self.label_Sign_3.setTextInteractionFlags(Qt.LinksAccessibleByMouse)

        self.gridLayout_9.addWidget(self.label_Sign_3, 2, 0, 1, 1)

        self.line_AccountEditName = QLineEdit(self.frame_AccountEditNickname)
        self.line_AccountEditName.setObjectName(u"line_AccountEditName")
        self.line_AccountEditName.setMinimumSize(QSize(265, 35))
        self.line_AccountEditName.setMaximumSize(QSize(265, 35))

        self.gridLayout_9.addWidget(self.line_AccountEditName, 3, 0, 1, 1)

        self.label_AccountEditNameSymbols = QLabel(self.frame_AccountEditNickname)
        self.label_AccountEditNameSymbols.setObjectName(u"label_AccountEditNameSymbols")
        self.label_AccountEditNameSymbols.setMinimumSize(QSize(0, 15))
        self.label_AccountEditNameSymbols.setMaximumSize(QSize(16777215, 15))
        self.label_AccountEditNameSymbols.setFont(font6)
        self.label_AccountEditNameSymbols.setIndent(0)
        self.label_AccountEditNameSymbols.setTextInteractionFlags(Qt.LinksAccessibleByMouse)

        self.gridLayout_9.addWidget(self.label_AccountEditNameSymbols, 4, 0, 1, 1)


        self.verticalLayout_3.addWidget(self.frame_AccountEditNickname)

        self.frame_AccountEditUsername = QFrame(self.frame_AccountEditAccountContainer)
        self.frame_AccountEditUsername.setObjectName(u"frame_AccountEditUsername")
        self.frame_AccountEditUsername.setMinimumSize(QSize(0, 105))
        self.frame_AccountEditUsername.setMaximumSize(QSize(16777215, 105))
        self.frame_AccountEditUsername.setStyleSheet(u"")
        self.frame_AccountEditUsername.setFrameShape(QFrame.StyledPanel)
        self.frame_AccountEditUsername.setFrameShadow(QFrame.Raised)
        self.gridLayout_11 = QGridLayout(self.frame_AccountEditUsername)
        self.gridLayout_11.setObjectName(u"gridLayout_11")
        self.gridLayout_11.setHorizontalSpacing(10)
        self.gridLayout_11.setVerticalSpacing(0)
        self.gridLayout_11.setContentsMargins(0, 0, 0, 0)
        self.horizontalSpacer_14 = QSpacerItem(151, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_11.addItem(self.horizontalSpacer_14, 1, 1, 4, 1)

        self.label_Sign_4 = QLabel(self.frame_AccountEditUsername)
        self.label_Sign_4.setObjectName(u"label_Sign_4")
        self.label_Sign_4.setMinimumSize(QSize(0, 15))
        self.label_Sign_4.setMaximumSize(QSize(16777215, 15))
        self.label_Sign_4.setFont(font6)
        self.label_Sign_4.setIndent(0)
        self.label_Sign_4.setTextInteractionFlags(Qt.LinksAccessibleByMouse)

        self.gridLayout_11.addWidget(self.label_Sign_4, 2, 0, 1, 1)

        self.line_AccountEditUsername = QLineEdit(self.frame_AccountEditUsername)
        self.line_AccountEditUsername.setObjectName(u"line_AccountEditUsername")
        self.line_AccountEditUsername.setMinimumSize(QSize(265, 35))
        self.line_AccountEditUsername.setMaximumSize(QSize(265, 35))
        self.line_AccountEditUsername.setMaxLength(32)

        self.gridLayout_11.addWidget(self.line_AccountEditUsername, 3, 0, 1, 1)

        self.label_6 = QLabel(self.frame_AccountEditUsername)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setMinimumSize(QSize(0, 25))
        self.label_6.setMaximumSize(QSize(16777215, 25))
        self.label_6.setFont(font7)
        self.label_6.setAlignment(Qt.AlignBottom|Qt.AlignLeading|Qt.AlignLeft)
        self.label_6.setTextInteractionFlags(Qt.LinksAccessibleByMouse)

        self.gridLayout_11.addWidget(self.label_6, 1, 0, 1, 1)

        self.label_AccountEditUsernameSymbols = QLabel(self.frame_AccountEditUsername)
        self.label_AccountEditUsernameSymbols.setObjectName(u"label_AccountEditUsernameSymbols")
        self.label_AccountEditUsernameSymbols.setMinimumSize(QSize(0, 15))
        self.label_AccountEditUsernameSymbols.setMaximumSize(QSize(16777215, 15))
        self.label_AccountEditUsernameSymbols.setFont(font6)
        self.label_AccountEditUsernameSymbols.setIndent(0)
        self.label_AccountEditUsernameSymbols.setTextInteractionFlags(Qt.LinksAccessibleByMouse)

        self.gridLayout_11.addWidget(self.label_AccountEditUsernameSymbols, 4, 0, 1, 1)


        self.verticalLayout_3.addWidget(self.frame_AccountEditUsername)

        self.frame_AccountEditInfo = QFrame(self.frame_AccountEditAccountContainer)
        self.frame_AccountEditInfo.setObjectName(u"frame_AccountEditInfo")
        self.frame_AccountEditInfo.setMinimumSize(QSize(0, 120))
        self.frame_AccountEditInfo.setMaximumSize(QSize(16777215, 120))
        self.frame_AccountEditInfo.setStyleSheet(u"")
        self.frame_AccountEditInfo.setFrameShape(QFrame.StyledPanel)
        self.frame_AccountEditInfo.setFrameShadow(QFrame.Raised)
        self.gridLayout_10 = QGridLayout(self.frame_AccountEditInfo)
        self.gridLayout_10.setObjectName(u"gridLayout_10")
        self.gridLayout_10.setHorizontalSpacing(10)
        self.gridLayout_10.setVerticalSpacing(0)
        self.gridLayout_10.setContentsMargins(0, 0, 0, 0)
        self.label_4 = QLabel(self.frame_AccountEditInfo)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setMinimumSize(QSize(0, 25))
        self.label_4.setMaximumSize(QSize(16777215, 25))
        self.label_4.setFont(font7)
        self.label_4.setAlignment(Qt.AlignBottom|Qt.AlignLeading|Qt.AlignLeft)
        self.label_4.setTextInteractionFlags(Qt.LinksAccessibleByMouse)

        self.gridLayout_10.addWidget(self.label_4, 0, 0, 1, 1)

        self.horizontalSpacer_13 = QSpacerItem(262, 78, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_10.addItem(self.horizontalSpacer_13, 0, 2, 4, 1)

        self.label_Sign_1 = QLabel(self.frame_AccountEditInfo)
        self.label_Sign_1.setObjectName(u"label_Sign_1")
        self.label_Sign_1.setMinimumSize(QSize(0, 15))
        self.label_Sign_1.setMaximumSize(QSize(16777215, 15))
        self.label_Sign_1.setFont(font6)
        self.label_Sign_1.setIndent(0)
        self.label_Sign_1.setTextInteractionFlags(Qt.LinksAccessibleByMouse)

        self.gridLayout_10.addWidget(self.label_Sign_1, 1, 0, 1, 1)

        self.button_AccountEditAboutDelete = QPushButton(self.frame_AccountEditInfo)
        self.button_AccountEditAboutDelete.setObjectName(u"button_AccountEditAboutDelete")
        self.button_AccountEditAboutDelete.setMinimumSize(QSize(30, 30))
        self.button_AccountEditAboutDelete.setMaximumSize(QSize(30, 30))
        self.button_AccountEditAboutDelete.setStyleSheet(u"")

        self.gridLayout_10.addWidget(self.button_AccountEditAboutDelete, 2, 1, 1, 1)

        self.label_AccountEditAboutSymbols = QLabel(self.frame_AccountEditInfo)
        self.label_AccountEditAboutSymbols.setObjectName(u"label_AccountEditAboutSymbols")
        self.label_AccountEditAboutSymbols.setMinimumSize(QSize(0, 15))
        self.label_AccountEditAboutSymbols.setMaximumSize(QSize(16777215, 15))
        self.label_AccountEditAboutSymbols.setFont(font6)
        self.label_AccountEditAboutSymbols.setIndent(0)
        self.label_AccountEditAboutSymbols.setTextInteractionFlags(Qt.LinksAccessibleByMouse)

        self.gridLayout_10.addWidget(self.label_AccountEditAboutSymbols, 3, 0, 1, 1)

        self.line_AccountEditAbout = QTextEdit(self.frame_AccountEditInfo)
        self.line_AccountEditAbout.setObjectName(u"line_AccountEditAbout")
        self.line_AccountEditAbout.setMinimumSize(QSize(265, 50))
        self.line_AccountEditAbout.setMaximumSize(QSize(265, 50))

        self.gridLayout_10.addWidget(self.line_AccountEditAbout, 2, 0, 1, 1)


        self.verticalLayout_3.addWidget(self.frame_AccountEditInfo)


        self.verticalLayout_14.addWidget(self.frame_AccountEditAccountContainer)

        self.verticalSpacer = QSpacerItem(20, 20, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Minimum)

        self.verticalLayout_14.addItem(self.verticalSpacer)

        self.label_AccountEditProfileWarning = QLabel(self.frame_AccountEditProfileContainer)
        self.label_AccountEditProfileWarning.setObjectName(u"label_AccountEditProfileWarning")
        self.label_AccountEditProfileWarning.setMinimumSize(QSize(0, 15))
        self.label_AccountEditProfileWarning.setMaximumSize(QSize(16777215, 15))
        self.label_AccountEditProfileWarning.setFont(font6)
        self.label_AccountEditProfileWarning.setIndent(0)

        self.verticalLayout_14.addWidget(self.label_AccountEditProfileWarning)

        self.verticalSpacer_11 = QSpacerItem(20, 10, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Minimum)

        self.verticalLayout_14.addItem(self.verticalSpacer_11)

        self.frame_AccountEditButtonsContainer = QFrame(self.frame_AccountEditProfileContainer)
        self.frame_AccountEditButtonsContainer.setObjectName(u"frame_AccountEditButtonsContainer")
        self.frame_AccountEditButtonsContainer.setMinimumSize(QSize(0, 40))
        self.frame_AccountEditButtonsContainer.setMaximumSize(QSize(16777215, 40))
        self.frame_AccountEditButtonsContainer.setStyleSheet(u"")
        self.frame_AccountEditButtonsContainer.setFrameShape(QFrame.StyledPanel)
        self.frame_AccountEditButtonsContainer.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_5 = QHBoxLayout(self.frame_AccountEditButtonsContainer)
        self.horizontalLayout_5.setSpacing(10)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.horizontalSpacer_9 = QSpacerItem(247, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_5.addItem(self.horizontalSpacer_9)

        self.button_AccountEditProfileCancel = QPushButton(self.frame_AccountEditButtonsContainer)
        self.button_AccountEditProfileCancel.setObjectName(u"button_AccountEditProfileCancel")
        self.button_AccountEditProfileCancel.setMinimumSize(QSize(120, 0))
        font8 = QFont()
        font8.setPointSize(13)
        font8.setBold(True)
        self.button_AccountEditProfileCancel.setFont(font8)

        self.horizontalLayout_5.addWidget(self.button_AccountEditProfileCancel)

        self.button_AccountEditProfileSave = QPushButton(self.frame_AccountEditButtonsContainer)
        self.button_AccountEditProfileSave.setObjectName(u"button_AccountEditProfileSave")
        self.button_AccountEditProfileSave.setMinimumSize(QSize(150, 0))
        self.button_AccountEditProfileSave.setFont(font8)

        self.horizontalLayout_5.addWidget(self.button_AccountEditProfileSave)


        self.verticalLayout_14.addWidget(self.frame_AccountEditButtonsContainer)


        self.verticalLayout_9.addWidget(self.frame_AccountEditProfileContainer)

        self.stacked_AccountEditTabs.addWidget(self.page_AccountEditTabsProfile)
        self.page_AccountEditTabsPrivacy = QWidget()
        self.page_AccountEditTabsPrivacy.setObjectName(u"page_AccountEditTabsPrivacy")
        self.stacked_AccountEditTabs.addWidget(self.page_AccountEditTabsPrivacy)
        self.page_AccountEditTabsChat = QWidget()
        self.page_AccountEditTabsChat.setObjectName(u"page_AccountEditTabsChat")
        self.stacked_AccountEditTabs.addWidget(self.page_AccountEditTabsChat)

        self.verticalLayout_8.addWidget(self.stacked_AccountEditTabs)

        self.scrollArea_AccountEdit.setWidget(self.scrollAreaWidget_AccountEdit)

        self.verticalLayout_13.addWidget(self.scrollArea_AccountEdit)


        self.verticalLayout_10.addWidget(self.frame_AccountEditContainer)

        self.stacked_Pages.addWidget(self.page_AccountEdit)
        self.page_Report = QWidget()
        self.page_Report.setObjectName(u"page_Report")
        self.page_Report.setStyleSheet(u"")
        self.horizontalLayout_2 = QHBoxLayout(self.page_Report)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.frame_Report_1 = QFrame(self.page_Report)
        self.frame_Report_1.setObjectName(u"frame_Report_1")
        self.frame_Report_1.setStyleSheet(u"QWidget {\n"
"	background: transponent;\n"
"}\n"
"\n"
"QFrame#frame_Report_Container,\n"
"QFrame#frame_Report {\n"
"	background-color: white;\n"
"	border: 0;\n"
"	border-radius: 20px;\n"
"}\n"
"\n"
"QLabel {\n"
"	background-color: white;\n"
"	border: 0;\n"
"}\n"
"\n"
"QPushButton {\n"
"	width: 40px;\n"
"	height: 40px;\n"
"	color: white;\n"
"	margin: 0;\n"
"	border-radius: 20px;\n"
"	background-color:  white;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color:  rgb(229,235,238);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"	background-color: rgb(219,228,233);\n"
"}\n"
"\n"
"QPushButton#button_Report {\n"
"	background-color: rgb(255, 0, 0);\n"
"}\n"
"\n"
"QPushButton#button_Report:hover {\n"
"	background-color:  rgb(235, 0, 0);\n"
"}\n"
"\n"
"QPushButton#button_Report:pressed {\n"
"	background-color: rgb(215, 0, 0);\n"
"}")
        self.frame_Report_1.setFrameShape(QFrame.StyledPanel)
        self.frame_Report_1.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.frame_Report_1)
        self.verticalLayout_4.setSpacing(10)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.frame_ReportBack = QFrame(self.frame_Report_1)
        self.frame_ReportBack.setObjectName(u"frame_ReportBack")
        self.frame_ReportBack.setMinimumSize(QSize(0, 60))
        self.frame_ReportBack.setMaximumSize(QSize(16777215, 60))
        self.frame_ReportBack.setFrameShape(QFrame.StyledPanel)
        self.frame_ReportBack.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_6 = QHBoxLayout(self.frame_ReportBack)
        self.horizontalLayout_6.setSpacing(10)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 20)
        self.button_ReportBack = QPushButton(self.frame_ReportBack)
        self.button_ReportBack.setObjectName(u"button_ReportBack")

        self.horizontalLayout_6.addWidget(self.button_ReportBack)

        self.horizontalSpacer_2 = QSpacerItem(244, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_6.addItem(self.horizontalSpacer_2)


        self.verticalLayout_4.addWidget(self.frame_ReportBack)

        self.verticalSpacer_10 = QSpacerItem(20, 393, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_4.addItem(self.verticalSpacer_10)


        self.horizontalLayout_2.addWidget(self.frame_Report_1)

        self.frame_ReportContainer = QFrame(self.page_Report)
        self.frame_ReportContainer.setObjectName(u"frame_ReportContainer")
        self.frame_ReportContainer.setMinimumSize(QSize(370, 0))
        self.frame_ReportContainer.setMaximumSize(QSize(370, 16777215))
        self.frame_ReportContainer.setStyleSheet(u"QWidget {\n"
"	background: transponent;\n"
"}\n"
"\n"
"QFrame#frame_Report_Container,\n"
"QFrame#frame_Report {\n"
"	background-color: white;\n"
"	border: 0;\n"
"	border-radius: 20px;\n"
"}\n"
"\n"
"QLabel, QTextEdit {\n"
"	background-color: white;\n"
"	border: 0;\n"
"}\n"
"\n"
"QPushButton {\n"
"	width: 40px;\n"
"	height: 40px;\n"
"	color: white;\n"
"	margin: 0;\n"
"	border-radius: 20px;\n"
"	background-color:  white;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color:  rgb(229,235,238);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"	background-color: rgb(219,228,233);\n"
"}\n"
"\n"
"QPushButton#button_Report {\n"
"	border-radius: 15px;\n"
"	background-color: rgb(255, 0, 0);\n"
"}\n"
"\n"
"QPushButton#button_Report:hover {\n"
"	background-color:  rgb(235, 0, 0);\n"
"}\n"
"\n"
"QPushButton#button_Report:pressed {\n"
"	background-color: rgb(215, 0, 0);\n"
"}")
        self.frame_ReportContainer.setFrameShape(QFrame.StyledPanel)
        self.frame_ReportContainer.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(self.frame_ReportContainer)
        self.verticalLayout.setSpacing(10)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(20, 0, 20, 0)
        self.verticalSpacer_7 = QSpacerItem(20, 5, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer_7)

        self.frame_Report = QFrame(self.frame_ReportContainer)
        self.frame_Report.setObjectName(u"frame_Report")
        self.frame_Report.setMinimumSize(QSize(330, 400))
        self.frame_Report.setMaximumSize(QSize(330, 400))
        self.frame_Report.setStyleSheet(u"")
        self.frame_Report.setFrameShape(QFrame.StyledPanel)
        self.frame_Report.setFrameShadow(QFrame.Raised)
        self.verticalLayout_7 = QVBoxLayout(self.frame_Report)
        self.verticalLayout_7.setSpacing(10)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_7.setContentsMargins(20, 20, 20, 20)
        self.label_Report = QLabel(self.frame_Report)
        self.label_Report.setObjectName(u"label_Report")
        self.label_Report.setMaximumSize(QSize(16777215, 50))
        font9 = QFont()
        font9.setPointSize(25)
        font9.setBold(True)
        self.label_Report.setFont(font9)

        self.verticalLayout_7.addWidget(self.label_Report)

        self.label_ReportText = QLabel(self.frame_Report)
        self.label_ReportText.setObjectName(u"label_ReportText")
        self.label_ReportText.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)
        self.label_ReportText.setWordWrap(True)
        self.label_ReportText.setIndent(0)

        self.verticalLayout_7.addWidget(self.label_ReportText)

        self.textEdit_ReportText = QTextEdit(self.frame_Report)
        self.textEdit_ReportText.setObjectName(u"textEdit_ReportText")
        font10 = QFont()
        font10.setItalic(True)
        self.textEdit_ReportText.setFont(font10)
        self.textEdit_ReportText.setReadOnly(False)

        self.verticalLayout_7.addWidget(self.textEdit_ReportText)

        self.button_Report = QPushButton(self.frame_Report)
        self.button_Report.setObjectName(u"button_Report")
        self.button_Report.setMinimumSize(QSize(0, 50))
        self.button_Report.setMaximumSize(QSize(16777215, 50))
        font11 = QFont()
        font11.setPointSize(14)
        font11.setBold(True)
        self.button_Report.setFont(font11)

        self.verticalLayout_7.addWidget(self.button_Report)


        self.verticalLayout.addWidget(self.frame_Report)

        self.verticalSpacer_8 = QSpacerItem(20, 39, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer_8)


        self.horizontalLayout_2.addWidget(self.frame_ReportContainer)

        self.frame_Report_2 = QFrame(self.page_Report)
        self.frame_Report_2.setObjectName(u"frame_Report_2")
        self.frame_Report_2.setStyleSheet(u"QWidget {\n"
"	background: transponent;\n"
"}\n"
"\n"
"QFrame#frame_Report_Container,\n"
"QFrame#frame_Report {\n"
"	background-color: white;\n"
"	border: 0;\n"
"	border-radius: 20px;\n"
"}\n"
"\n"
"QLabel {\n"
"	background-color: white;\n"
"	border: 0;\n"
"}\n"
"\n"
"QPushButton {\n"
"	width: 40px;\n"
"	height: 40px;\n"
"	color: white;\n"
"	margin: 0;\n"
"	border-radius: 20px;\n"
"	background-color:  white;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color:  rgb(229,235,238);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"	background-color: rgb(219,228,233);\n"
"}\n"
"\n"
"QPushButton#button_Report {\n"
"	background-color: rgb(255, 0, 0);\n"
"}\n"
"\n"
"QPushButton#button_Report:hover {\n"
"	background-color:  rgb(235, 0, 0);\n"
"}\n"
"\n"
"QPushButton#button_Report:pressed {\n"
"	background-color: rgb(215, 0, 0);\n"
"}")
        self.frame_Report_2.setFrameShape(QFrame.StyledPanel)
        self.frame_Report_2.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_7 = QHBoxLayout(self.frame_Report_2)
        self.horizontalLayout_7.setSpacing(10)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_7.addItem(self.horizontalSpacer_3)


        self.horizontalLayout_2.addWidget(self.frame_Report_2)

        self.stacked_Pages.addWidget(self.page_Report)
        self.page_Comments = QWidget()
        self.page_Comments.setObjectName(u"page_Comments")
        self.page_Comments.setStyleSheet(u"")
        self.horizontalLayout_10 = QHBoxLayout(self.page_Comments)
        self.horizontalLayout_10.setSpacing(10)
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.horizontalLayout_10.setContentsMargins(10, 0, 10, 0)
        self.frame_PostContainer = QFrame(self.page_Comments)
        self.frame_PostContainer.setObjectName(u"frame_PostContainer")
        self.frame_PostContainer.setMinimumSize(QSize(485, 0))
        self.frame_PostContainer.setStyleSheet(u"QWidget, QScrollArea {\n"
"	background: transponent;\n"
"}\n"
"\n"
"QLabel#label_CommentsSign {\n"
"	color: white;\n"
"}\n"
"\n"
"QPushButton {\n"
"	margin: 0;\n"
"	background-color:  white;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color:  rgb(229,235,238);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"	background-color: rgb(219,228,233);\n"
"}")
        self.frame_PostContainer.setFrameShape(QFrame.StyledPanel)
        self.frame_PostContainer.setFrameShadow(QFrame.Raised)
        self.layout_CommentsPost = QVBoxLayout(self.frame_PostContainer)
        self.layout_CommentsPost.setSpacing(0)
        self.layout_CommentsPost.setObjectName(u"layout_CommentsPost")
        self.layout_CommentsPost.setContentsMargins(0, 20, 0, 0)
        self.frame_CommentsBack = QFrame(self.frame_PostContainer)
        self.frame_CommentsBack.setObjectName(u"frame_CommentsBack")
        self.frame_CommentsBack.setMinimumSize(QSize(0, 50))
        self.frame_CommentsBack.setMaximumSize(QSize(16777215, 50))
        self.frame_CommentsBack.setStyleSheet(u"")
        self.frame_CommentsBack.setFrameShape(QFrame.StyledPanel)
        self.frame_CommentsBack.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_14 = QHBoxLayout(self.frame_CommentsBack)
        self.horizontalLayout_14.setSpacing(10)
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.horizontalLayout_14.setContentsMargins(10, 0, 5, 10)
        self.button_CommentsBack = QPushButton(self.frame_CommentsBack)
        self.button_CommentsBack.setObjectName(u"button_CommentsBack")

        self.horizontalLayout_14.addWidget(self.button_CommentsBack)

        self.horizontalSpacer_21 = QSpacerItem(244, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_14.addItem(self.horizontalSpacer_21)


        self.layout_CommentsPost.addWidget(self.frame_CommentsBack)

        self.scrollArea_CommentsPost = QScrollArea(self.frame_PostContainer)
        self.scrollArea_CommentsPost.setObjectName(u"scrollArea_CommentsPost")
        self.scrollArea_CommentsPost.setWidgetResizable(True)
        self.scrollAreaWidget_CommentsPost = QWidget()
        self.scrollAreaWidget_CommentsPost.setObjectName(u"scrollAreaWidget_CommentsPost")
        self.scrollAreaWidget_CommentsPost.setGeometry(QRect(0, 0, 485, 420))
        self.layout_CommentsPostScroll = QVBoxLayout(self.scrollAreaWidget_CommentsPost)
        self.layout_CommentsPostScroll.setSpacing(20)
        self.layout_CommentsPostScroll.setObjectName(u"layout_CommentsPostScroll")
        self.layout_CommentsPostScroll.setContentsMargins(10, 0, 5, 20)
        self.verticalSpacer_12 = QSpacerItem(467, 157, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.layout_CommentsPostScroll.addItem(self.verticalSpacer_12)

        self.verticalSpacer_13 = QSpacerItem(20, 217, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.layout_CommentsPostScroll.addItem(self.verticalSpacer_13)

        self.scrollArea_CommentsPost.setWidget(self.scrollAreaWidget_CommentsPost)

        self.layout_CommentsPost.addWidget(self.scrollArea_CommentsPost)


        self.horizontalLayout_10.addWidget(self.frame_PostContainer)

        self.scrollArea_Comments = QScrollArea(self.page_Comments)
        self.scrollArea_Comments.setObjectName(u"scrollArea_Comments")
        self.scrollArea_Comments.setStyleSheet(u"QWidget, QScrollArea {\n"
"	background: transponent;\n"
"}\n"
"\n"
"QLabel#label_CommentsSign {\n"
"	color: rgba(255,255,255,180);\n"
"}\n"
"\n"
"QPushButton {\n"
"	margin: 0;\n"
"	background-color:  white;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color:  rgb(229,235,238);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"	background-color: rgb(219,228,233);\n"
"}")
        self.scrollArea_Comments.setWidgetResizable(True)
        self.scrollAreaWidget_Comments = QWidget()
        self.scrollAreaWidget_Comments.setObjectName(u"scrollAreaWidget_Comments")
        self.scrollAreaWidget_Comments.setGeometry(QRect(0, 0, 485, 490))
        self.layout_ScrollAreaComments = QVBoxLayout(self.scrollAreaWidget_Comments)
        self.layout_ScrollAreaComments.setSpacing(0)
        self.layout_ScrollAreaComments.setObjectName(u"layout_ScrollAreaComments")
        self.layout_ScrollAreaComments.setContentsMargins(0, 20, 0, 20)
        self.stacked_Comments = QStackedWidget(self.scrollAreaWidget_Comments)
        self.stacked_Comments.setObjectName(u"stacked_Comments")

        self.layout_ScrollAreaComments.addWidget(self.stacked_Comments)

        self.frame_SetCommentPage = QFrame(self.scrollAreaWidget_Comments)
        self.frame_SetCommentPage.setObjectName(u"frame_SetCommentPage")
        self.frame_SetCommentPage.setMinimumSize(QSize(0, 30))
        self.frame_SetCommentPage.setMaximumSize(QSize(16777215, 30))
        self.frame_SetCommentPage.setStyleSheet(u"QPushButton { \n"
"	width: 30px;\n"
"	height: 30px;\n"
"	border-radius: 15px;\n"
"	background-color: white;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color:  rgb(219,228,233);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"	background-color: rgb(184,191,195);\n"
"}\n"
"\n"
"QPushButton:checked {\n"
"	background-color: rgb(219,228,233);\n"
"}")
        self.frame_SetCommentPage.setFrameShape(QFrame.StyledPanel)
        self.frame_SetCommentPage.setFrameShadow(QFrame.Raised)
        self.layout_SetCommentsPage = QHBoxLayout(self.frame_SetCommentPage)
        self.layout_SetCommentsPage.setSpacing(5)
        self.layout_SetCommentsPage.setObjectName(u"layout_SetCommentsPage")
        self.layout_SetCommentsPage.setContentsMargins(0, 0, 0, 0)
        self.horizontalSpacer_15 = QSpacerItem(277, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.layout_SetCommentsPage.addItem(self.horizontalSpacer_15)

        self.horizontalSpacer_17 = QSpacerItem(277, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.layout_SetCommentsPage.addItem(self.horizontalSpacer_17)


        self.layout_ScrollAreaComments.addWidget(self.frame_SetCommentPage)

        self.label_CommentsSign = QLabel(self.scrollAreaWidget_Comments)
        self.label_CommentsSign.setObjectName(u"label_CommentsSign")
        font12 = QFont()
        font12.setBold(True)
        self.label_CommentsSign.setFont(font12)
        self.label_CommentsSign.setAlignment(Qt.AlignCenter)
        self.label_CommentsSign.setIndent(0)

        self.layout_ScrollAreaComments.addWidget(self.label_CommentsSign)

        self.scrollArea_Comments.setWidget(self.scrollAreaWidget_Comments)

        self.horizontalLayout_10.addWidget(self.scrollArea_Comments)

        self.stacked_Pages.addWidget(self.page_Comments)
        self.page_User = QWidget()
        self.page_User.setObjectName(u"page_User")
        self.gridLayout_18 = QGridLayout(self.page_User)
        self.gridLayout_18.setSpacing(0)
        self.gridLayout_18.setObjectName(u"gridLayout_18")
        self.gridLayout_18.setContentsMargins(0, 0, 0, 0)
        self.scrollArea_User = QScrollArea(self.page_User)
        self.scrollArea_User.setObjectName(u"scrollArea_User")
        self.scrollArea_User.setStyleSheet(u"")
        self.scrollArea_User.setWidgetResizable(True)
        self.scrollAreaWidget_User = QWidget()
        self.scrollAreaWidget_User.setObjectName(u"scrollAreaWidget_User")
        self.scrollAreaWidget_User.setGeometry(QRect(0, 0, 1000, 1065))
        self.scrollAreaWidget_User.setStyleSheet(u"QFrame#frame_UserTabsContainer {\n"
"	border: 0;\n"
"}")
        self.gridLayout_15 = QGridLayout(self.scrollAreaWidget_User)
        self.gridLayout_15.setSpacing(0)
        self.gridLayout_15.setObjectName(u"gridLayout_15")
        self.gridLayout_15.setContentsMargins(0, 0, 0, 0)
        self.frame_UserTabsContainer = QFrame(self.scrollAreaWidget_User)
        self.frame_UserTabsContainer.setObjectName(u"frame_UserTabsContainer")
        self.frame_UserTabsContainer.setMinimumSize(QSize(0, 800))
        self.frame_UserTabsContainer.setMaximumSize(QSize(1000, 16777215))
        self.frame_UserTabsContainer.setStyleSheet(u"")
        self.frame_UserTabsContainer.setFrameShape(QFrame.StyledPanel)
        self.frame_UserTabsContainer.setFrameShadow(QFrame.Raised)
        self.verticalLayout_15 = QVBoxLayout(self.frame_UserTabsContainer)
        self.verticalLayout_15.setSpacing(0)
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self.verticalLayout_15.setContentsMargins(10, 15, 10, 0)
        self.frame_UserTabs = QFrame(self.frame_UserTabsContainer)
        self.frame_UserTabs.setObjectName(u"frame_UserTabs")
        self.frame_UserTabs.setMinimumSize(QSize(0, 60))
        self.frame_UserTabs.setMaximumSize(QSize(16777215, 60))
        self.frame_UserTabs.setStyleSheet(u"QFrame {\n"
"	border-radius: 0;\n"
"	border-top-left-radius: 20px;\n"
"	border-top-right-radius: 20px;\n"
"	border-bottom: 1px solid rgb(235, 237, 239);\n"
"	border-top: 1px solid rgb(235, 237, 239);\n"
"}\n"
"\n"
"QPushButton {\n"
"	height: 40px;\n"
"	width: 150px;\n"
"	border-radius: 15px;\n"
"	color: black;\n"
"	background-color:  white;\n"
"}\n"
"\n"
"QPushButton:checked  {\n"
"	background-color:  rgb(235, 237, 239);\n"
"}\n"
"\n"
"QPushButton:hover  {\n"
"	background-color:  rgb(235, 237, 239);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"	background-color: rgb(184,191,195);\n"
"}\n"
"")
        self.frame_UserTabs.setFrameShape(QFrame.StyledPanel)
        self.frame_UserTabs.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_12 = QHBoxLayout(self.frame_UserTabs)
        self.horizontalLayout_12.setSpacing(10)
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.horizontalLayout_12.setContentsMargins(10, 10, 10, 10)
        self.button_UserTabsPosts = QPushButton(self.frame_UserTabs)
        self.button_UserTabsPosts.setObjectName(u"button_UserTabsPosts")
        self.button_UserTabsPosts.setCheckable(True)

        self.horizontalLayout_12.addWidget(self.button_UserTabsPosts)

        self.button_UserTabsFollows = QPushButton(self.frame_UserTabs)
        self.button_UserTabsFollows.setObjectName(u"button_UserTabsFollows")
        self.button_UserTabsFollows.setCheckable(True)

        self.horizontalLayout_12.addWidget(self.button_UserTabsFollows)


        self.verticalLayout_15.addWidget(self.frame_UserTabs)

        self.stacked_UserTabs = QStackedWidget(self.frame_UserTabsContainer)
        self.stacked_UserTabs.setObjectName(u"stacked_UserTabs")
        self.stacked_UserTabs.setMinimumSize(QSize(0, 800))
        self.page_UserTabsPosts = QWidget()
        self.page_UserTabsPosts.setObjectName(u"page_UserTabsPosts")
        self.verticalLayout_16 = QVBoxLayout(self.page_UserTabsPosts)
        self.verticalLayout_16.setObjectName(u"verticalLayout_16")
        self.frame_2 = QFrame(self.page_UserTabsPosts)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setMinimumSize(QSize(0, 400))
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)

        self.verticalLayout_16.addWidget(self.frame_2)

        self.stacked_UserTabs.addWidget(self.page_UserTabsPosts)
        self.page_UserTabsFollows = QWidget()
        self.page_UserTabsFollows.setObjectName(u"page_UserTabsFollows")
        self.stacked_UserTabs.addWidget(self.page_UserTabsFollows)

        self.verticalLayout_15.addWidget(self.stacked_UserTabs)


        self.gridLayout_15.addWidget(self.frame_UserTabsContainer, 1, 0, 1, 2)

        self.frame_UserInfoContainer = QFrame(self.scrollAreaWidget_User)
        self.frame_UserInfoContainer.setObjectName(u"frame_UserInfoContainer")
        self.frame_UserInfoContainer.setMinimumSize(QSize(0, 190))
        self.frame_UserInfoContainer.setMaximumSize(QSize(1000, 190))
        self.frame_UserInfoContainer.setStyleSheet(u"QFrame {\n"
"	background: transponent;\n"
"	color: white;\n"
"}\n"
"\n"
"QFrame#frame_UsertInfoContainer {\n"
"	border-radius: 0;\n"
"}\n"
"\n"
"")
        self.frame_UserInfoContainer.setFrameShape(QFrame.StyledPanel)
        self.frame_UserInfoContainer.setFrameShadow(QFrame.Raised)
        self.layout_UserInfoContainer = QHBoxLayout(self.frame_UserInfoContainer)
        self.layout_UserInfoContainer.setSpacing(10)
        self.layout_UserInfoContainer.setObjectName(u"layout_UserInfoContainer")
        self.layout_UserInfoContainer.setContentsMargins(20, 15, 10, 0)
        self.frame_UserInfo = QFrame(self.frame_UserInfoContainer)
        self.frame_UserInfo.setObjectName(u"frame_UserInfo")
        self.frame_UserInfo.setMinimumSize(QSize(0, 150))
        self.frame_UserInfo.setMaximumSize(QSize(16777215, 150))
        self.frame_UserInfo.setFont(font1)
        self.frame_UserInfo.setStyleSheet(u"QFrame {\n"
"	border-top-left-radius: 0;\n"
"	border-top-right-radius: 0;\n"
"}\n"
"\n"
"QLabel#label_UserAbout {\n"
"	padding-bottom: 5px;\n"
"	border-bottom: 1px solid rgb(229,235,238);\n"
"}\n"
"\n"
"QLabel#label_UsertInformationID {\n"
"	margin: 0;\n"
"	border-bottom-left-radius: 10px;\n"
"}\n"
"\n"
"QLabel#label_UserInformationAccess{\n"
"	margin: 0;\n"
"	border-bottom-right-radius: 10px;\n"
"}\n"
"\n"
"")
        self.frame_UserInfo.setFrameShape(QFrame.StyledPanel)
        self.frame_UserInfo.setFrameShadow(QFrame.Raised)
        self.verticalLayout_17 = QVBoxLayout(self.frame_UserInfo)
        self.verticalLayout_17.setSpacing(0)
        self.verticalLayout_17.setObjectName(u"verticalLayout_17")
        self.verticalLayout_17.setContentsMargins(10, 0, 5, 0)
        self.verticalSpacer_14 = QSpacerItem(20, 60, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Maximum)

        self.verticalLayout_17.addItem(self.verticalSpacer_14)

        self.frame_UserLabels = QFrame(self.frame_UserInfo)
        self.frame_UserLabels.setObjectName(u"frame_UserLabels")
        self.frame_UserLabels.setMinimumSize(QSize(0, 30))
        self.frame_UserLabels.setMaximumSize(QSize(16777215, 30))
        self.frame_UserLabels.setStyleSheet(u"")
        self.frame_UserLabels.setFrameShape(QFrame.StyledPanel)
        self.frame_UserLabels.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_13 = QHBoxLayout(self.frame_UserLabels)
        self.horizontalLayout_13.setSpacing(5)
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.horizontalLayout_13.setContentsMargins(0, 0, 0, 0)
        self.label_UserNickname = QLabel(self.frame_UserLabels)
        self.label_UserNickname.setObjectName(u"label_UserNickname")
        sizePolicy.setHeightForWidth(self.label_UserNickname.sizePolicy().hasHeightForWidth())
        self.label_UserNickname.setSizePolicy(sizePolicy)
        self.label_UserNickname.setMinimumSize(QSize(0, 30))
        self.label_UserNickname.setMaximumSize(QSize(16777215, 30))
        self.label_UserNickname.setFont(font2)
        self.label_UserNickname.setStyleSheet(u"")
        self.label_UserNickname.setScaledContents(False)
        self.label_UserNickname.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)
        self.label_UserNickname.setMargin(0)
        self.label_UserNickname.setIndent(0)
        self.label_UserNickname.setTextInteractionFlags(Qt.LinksAccessibleByMouse|Qt.TextSelectableByKeyboard|Qt.TextSelectableByMouse)

        self.horizontalLayout_13.addWidget(self.label_UserNickname)

        self.label_UserStatus = QLabel(self.frame_UserLabels)
        self.label_UserStatus.setObjectName(u"label_UserStatus")
        self.label_UserStatus.setMinimumSize(QSize(0, 0))
        self.label_UserStatus.setMaximumSize(QSize(16777215, 16777215))
        self.label_UserStatus.setTextFormat(Qt.RichText)
        self.label_UserStatus.setAlignment(Qt.AlignBottom|Qt.AlignLeading|Qt.AlignLeft)
        self.label_UserStatus.setTextInteractionFlags(Qt.LinksAccessibleByMouse|Qt.TextSelectableByMouse)

        self.horizontalLayout_13.addWidget(self.label_UserStatus)

        self.horizontalSpacer_18 = QSpacerItem(151, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_13.addItem(self.horizontalSpacer_18)


        self.verticalLayout_17.addWidget(self.frame_UserLabels)

        self.frame_UserButtons = QFrame(self.frame_UserInfo)
        self.frame_UserButtons.setObjectName(u"frame_UserButtons")
        self.frame_UserButtons.setMinimumSize(QSize(0, 0))
        self.frame_UserButtons.setMaximumSize(QSize(16777215, 90))
        self.frame_UserButtons.setStyleSheet(u"")
        self.frame_UserButtons.setFrameShape(QFrame.StyledPanel)
        self.frame_UserButtons.setFrameShadow(QFrame.Raised)
        self.gridLayout_16 = QGridLayout(self.frame_UserButtons)
        self.gridLayout_16.setObjectName(u"gridLayout_16")
        self.gridLayout_16.setHorizontalSpacing(5)
        self.gridLayout_16.setVerticalSpacing(10)
        self.gridLayout_16.setContentsMargins(0, 0, 5, 5)
        self.horizontalSpacer_20 = QSpacerItem(7, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_16.addItem(self.horizontalSpacer_20, 1, 1, 1, 1)

        self.horizontalSpacer_19 = QSpacerItem(182, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_16.addItem(self.horizontalSpacer_19, 0, 1, 1, 4)

        self.button_UserReport = QPushButton(self.frame_UserButtons)
        self.button_UserReport.setObjectName(u"button_UserReport")

        self.gridLayout_16.addWidget(self.button_UserReport, 1, 4, 1, 1)

        self.button_UserFollow = QPushButton(self.frame_UserButtons)
        self.button_UserFollow.setObjectName(u"button_UserFollow")

        self.gridLayout_16.addWidget(self.button_UserFollow, 1, 2, 1, 1)

        self.button_UserMessage = QPushButton(self.frame_UserButtons)
        self.button_UserMessage.setObjectName(u"button_UserMessage")

        self.gridLayout_16.addWidget(self.button_UserMessage, 1, 3, 1, 1)

        self.frame_UserAboutContainer = QFrame(self.frame_UserButtons)
        self.frame_UserAboutContainer.setObjectName(u"frame_UserAboutContainer")
        self.frame_UserAboutContainer.setMinimumSize(QSize(200, 60))
        self.frame_UserAboutContainer.setMaximumSize(QSize(16777215, 90))
        self.frame_UserAboutContainer.setStyleSheet(u"")
        self.frame_UserAboutContainer.setFrameShape(QFrame.StyledPanel)
        self.frame_UserAboutContainer.setFrameShadow(QFrame.Raised)
        self.gridLayout_17 = QGridLayout(self.frame_UserAboutContainer)
        self.gridLayout_17.setSpacing(0)
        self.gridLayout_17.setObjectName(u"gridLayout_17")
        self.gridLayout_17.setContentsMargins(0, 0, 0, 5)
        self.label_UserId = QLabel(self.frame_UserAboutContainer)
        self.label_UserId.setObjectName(u"label_UserId")
        self.label_UserId.setMinimumSize(QSize(0, 20))
        self.label_UserId.setMaximumSize(QSize(100, 20))
        self.label_UserId.setFont(font3)
        self.label_UserId.setStyleSheet(u"")
        self.label_UserId.setIndent(0)
        self.label_UserId.setTextInteractionFlags(Qt.LinksAccessibleByMouse|Qt.TextSelectableByKeyboard|Qt.TextSelectableByMouse)

        self.gridLayout_17.addWidget(self.label_UserId, 1, 0, 1, 1)

        self.label_UserAbout = QLabel(self.frame_UserAboutContainer)
        self.label_UserAbout.setObjectName(u"label_UserAbout")
        self.label_UserAbout.setMinimumSize(QSize(300, 20))
        self.label_UserAbout.setMaximumSize(QSize(300, 70))
        self.label_UserAbout.setFont(font4)
        self.label_UserAbout.setStyleSheet(u"")
        self.label_UserAbout.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.label_UserAbout.setWordWrap(True)
        self.label_UserAbout.setIndent(0)
        self.label_UserAbout.setTextInteractionFlags(Qt.LinksAccessibleByMouse|Qt.TextSelectableByMouse)

        self.gridLayout_17.addWidget(self.label_UserAbout, 0, 0, 1, 2)

        self.label_UserAccess = QLabel(self.frame_UserAboutContainer)
        self.label_UserAccess.setObjectName(u"label_UserAccess")
        self.label_UserAccess.setMaximumSize(QSize(100, 16777215))
        self.label_UserAccess.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.label_UserAccess.setIndent(0)

        self.gridLayout_17.addWidget(self.label_UserAccess, 1, 1, 1, 1)


        self.gridLayout_16.addWidget(self.frame_UserAboutContainer, 0, 0, 2, 1)

        self.button_UserDelete = QPushButton(self.frame_UserButtons)
        self.button_UserDelete.setObjectName(u"button_UserDelete")

        self.gridLayout_16.addWidget(self.button_UserDelete, 1, 5, 1, 1)


        self.verticalLayout_17.addWidget(self.frame_UserButtons)


        self.layout_UserInfoContainer.addWidget(self.frame_UserInfo)


        self.gridLayout_15.addWidget(self.frame_UserInfoContainer, 0, 0, 1, 2)

        self.scrollArea_User.setWidget(self.scrollAreaWidget_User)

        self.gridLayout_18.addWidget(self.scrollArea_User, 0, 0, 1, 1)

        self.stacked_Pages.addWidget(self.page_User)

        self.gridLayout.addWidget(self.stacked_Pages, 1, 0, 1, 1)


        self.gridLayout_2.addWidget(self.frame_Main, 0, 0, 1, 1)

        MainWindow.setCentralWidget(self.central_widget)

        self.retranslateUi(MainWindow)
        self.button_AccountExit.toggled.connect(self.frame_AccountExitConfirmation.setVisible)
        self.button_AccountExit.toggled.connect(self.button_AccountExit.setHidden)

        self.stacked_Pages.setCurrentIndex(4)
        self.stacked_SideBar.setCurrentIndex(0)
        self.stacked_AccountEditTabs.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"R&R", None))
#if QT_CONFIG(tooltip)
        self.button_Logo.setToolTip(QCoreApplication.translate("MainWindow", u"Home", None))
#endif // QT_CONFIG(tooltip)
        self.button_Logo.setText("")
        self.line_SearchBar.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Search...", None))
#if QT_CONFIG(tooltip)
        self.button_HomeFilterPosts.setToolTip(QCoreApplication.translate("MainWindow", u"Filter", None))
#endif // QT_CONFIG(tooltip)
        self.button_HomeFilterPosts.setText("")
#if QT_CONFIG(tooltip)
        self.button_Apps.setToolTip(QCoreApplication.translate("MainWindow", u"Apps", None))
#endif // QT_CONFIG(tooltip)
        self.button_Apps.setText("")
#if QT_CONFIG(tooltip)
        self.button_Chat.setToolTip(QCoreApplication.translate("MainWindow", u"Chat", None))
#endif // QT_CONFIG(tooltip)
        self.button_Chat.setText("")
#if QT_CONFIG(tooltip)
        self.button_Notifications.setToolTip(QCoreApplication.translate("MainWindow", u"Notifications", None))
#endif // QT_CONFIG(tooltip)
        self.button_Notifications.setText("")
#if QT_CONFIG(tooltip)
        self.button_Account.setToolTip(QCoreApplication.translate("MainWindow", u"Account", None))
#endif // QT_CONFIG(tooltip)
        self.button_Account.setText("")
        self.label_HomeSign.setText(QCoreApplication.translate("MainWindow", u"fdf", None))
        self.button_SortByTime.setText(QCoreApplication.translate("MainWindow", u"New", None))
        self.button_SortByLikes.setText(QCoreApplication.translate("MainWindow", u"Likes", None))
        self.button_SortByDislikes.setText(QCoreApplication.translate("MainWindow", u"Dislikes", None))
        self.button_SortByComments.setText(QCoreApplication.translate("MainWindow", u"Comments", None))
        self.button_SortByHot.setText(QCoreApplication.translate("MainWindow", u"Hot", None))
        self.label.setText("")
        self.button_AppsAccount.setText(QCoreApplication.translate("MainWindow", u"My Account", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Chat", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Notifications", None))
        self.button_AccountTabsPosts.setText(QCoreApplication.translate("MainWindow", u"Posts", None))
        self.button_AccountTabsFollows.setText(QCoreApplication.translate("MainWindow", u"Follows", None))
        self.label_AccountNickname.setText(QCoreApplication.translate("MainWindow", u"Nickname", None))
        self.label_AccountStatus.setText("")
#if QT_CONFIG(tooltip)
        self.button_AccountExit.setToolTip(QCoreApplication.translate("MainWindow", u"Log Out", None))
#endif // QT_CONFIG(tooltip)
        self.button_AccountExit.setText("")
        self.label_AccountInformationID.setText("")
        self.label_AccountAbout.setText(QCoreApplication.translate("MainWindow", u"\u0413\u0435\u043d\u0438\u0439, \u043c\u0438\u043b\u043b\u0438\u0430\u0440\u0434\u0435\u0440, \u043f\u043b\u044d\u0439\u0431\u043e\u0439, \u0444\u0438\u043b\u0430\u043d\u0442\u0440\u043e\u043f...", None))
        self.label_AccountInformationAccess.setText("")
        self.button_AccountExitYes.setText("")
        self.button_AccountExitNo.setText("")
#if QT_CONFIG(tooltip)
        self.button_AccountEdit.setToolTip(QCoreApplication.translate("MainWindow", u"Settings", None))
#endif // QT_CONFIG(tooltip)
        self.button_AccountEdit.setText("")
        self.label_AccountEditSettings.setText(QCoreApplication.translate("MainWindow", u"User settings", None))
        self.button_AccountEditTabsProfile.setText(QCoreApplication.translate("MainWindow", u"Profile", None))
        self.button_AccountEditTabsPrivacy.setText(QCoreApplication.translate("MainWindow", u"Privacy", None))
        self.button_AccountEditTabsChat.setText(QCoreApplication.translate("MainWindow", u"Chat", None))
        self.label_AccountEditPhoto.setText(QCoreApplication.translate("MainWindow", u"IMAGES", None))
#if QT_CONFIG(tooltip)
        self.button_AccountEditPhotoAdd.setToolTip(QCoreApplication.translate("MainWindow", u"Choose File", None))
#endif // QT_CONFIG(tooltip)
        self.button_AccountEditPhotoAdd.setText("")
#if QT_CONFIG(tooltip)
        self.button_AccountEditPhotoDelete.setToolTip(QCoreApplication.translate("MainWindow", u"Set To Default", None))
#endif // QT_CONFIG(tooltip)
        self.button_AccountEditPhotoDelete.setText("")
        self.label_AccountEditPhoto_2.setText(QCoreApplication.translate("MainWindow", u"PROFILE INFORMATION", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Name", None))
        self.label_Sign_3.setText(QCoreApplication.translate("MainWindow", u"Set a profile name", None))
        self.line_AccountEditName.setPlaceholderText("")
        self.label_AccountEditNameSymbols.setText(QCoreApplication.translate("MainWindow", u"Maximum 20 chrachters", None))
        self.label_Sign_4.setText(QCoreApplication.translate("MainWindow", u"Set an username", None))
        self.line_AccountEditUsername.setPlaceholderText("")
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"Username", None))
        self.label_AccountEditUsernameSymbols.setText(QCoreApplication.translate("MainWindow", u"Maximum 32 chrachters", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"About (optional)", None))
        self.label_Sign_1.setText(QCoreApplication.translate("MainWindow", u"A brief description of yourself shown on your profile.", None))
#if QT_CONFIG(tooltip)
        self.button_AccountEditAboutDelete.setToolTip(QCoreApplication.translate("MainWindow", u"Clear About", None))
#endif // QT_CONFIG(tooltip)
        self.button_AccountEditAboutDelete.setText("")
        self.label_AccountEditAboutSymbols.setText(QCoreApplication.translate("MainWindow", u"Maximum 50 chrachters", None))
        self.line_AccountEditAbout.setPlaceholderText("")
        self.label_AccountEditProfileWarning.setText(QCoreApplication.translate("MainWindow", u"There are unsaved changes!", None))
        self.button_AccountEditProfileCancel.setText(QCoreApplication.translate("MainWindow", u"Cancel", None))
        self.button_AccountEditProfileSave.setText(QCoreApplication.translate("MainWindow", u"Save Changes", None))
        self.button_ReportBack.setText("")
        self.label_Report.setText(QCoreApplication.translate("MainWindow", u"Report @skyskyskyy?", None))
        self.label_ReportText.setText(QCoreApplication.translate("MainWindow", u"The report email will send to admins", None))
        self.textEdit_ReportText.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'.AppleSystemUIFont'; font-size:13pt; font-weight:400; font-style:italic;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>", None))
        self.textEdit_ReportText.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Report message", None))
        self.button_Report.setText(QCoreApplication.translate("MainWindow", u"Report", None))
        self.button_CommentsBack.setText("")
        self.label_CommentsSign.setText(QCoreApplication.translate("MainWindow", u"Seems like there are no comments yet", None))
        self.button_UserTabsPosts.setText(QCoreApplication.translate("MainWindow", u"Posts", None))
        self.button_UserTabsFollows.setText(QCoreApplication.translate("MainWindow", u"Follows", None))
        self.label_UserNickname.setText(QCoreApplication.translate("MainWindow", u"Nickname", None))
        self.label_UserStatus.setText("")
        self.button_UserReport.setText("")
        self.button_UserFollow.setText("")
        self.button_UserMessage.setText("")
        self.label_UserId.setText("")
        self.label_UserAbout.setText(QCoreApplication.translate("MainWindow", u"\u0413\u0435\u043d\u0438\u0439, \u043c\u0438\u043b\u043b\u0438\u0430\u0440\u0434\u0435\u0440, \u043f\u043b\u044d\u0439\u0431\u043e\u0439, \u0444\u0438\u043b\u0430\u043d\u0442\u0440\u043e\u043f...", None))
        self.label_UserAccess.setText("")
        self.button_UserDelete.setText("")
    # retranslateUi

