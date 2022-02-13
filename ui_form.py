# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'formXRdxTl.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

import icon_rc
import icon_rc
import icon_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1292, 888)
        MainWindow.setStyleSheet(u"background-color: rgb(66, 76, 85);")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setStyleSheet(u"border-raidus:none;")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setStyleSheet(u"")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.header = QFrame(self.frame)
        self.header.setObjectName(u"header")
        self.header.setMinimumSize(QSize(0, 50))
        self.header.setMaximumSize(QSize(16777215, 100))
        self.header.setFrameShape(QFrame.StyledPanel)
        self.header.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.header)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.frame_4 = QFrame(self.header)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setMinimumSize(QSize(0, 200))
        self.frame_4.setMaximumSize(QSize(16777215, 200))
        self.frame_4.setStyleSheet(u"background-color: rgb(31, 109, 120);\n"
"")
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.frame_2 = QFrame(self.frame_4)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setGeometry(QRect(0, 0, 91, 51))
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.label = QLabel(self.frame_4)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(460, 20, 71, 51))
        self.label.setPixmap(QPixmap(u":/icons/icons/high-temperature.png"))
        self.label.setScaledContents(True)
        self.label_2 = QLabel(self.frame_4)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(550, 20, 451, 51))
        font = QFont()
        font.setFamily(u"Segoe UI Black")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.pushButton_2 = QPushButton(self.frame_4)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setGeometry(QRect(0, 50, 141, 51))
        self.pushButton_2.setStyleSheet(u"QPushButton {\n"
"color:#FFF;\n"
"background-color: rgb(24, 24, 24);\n"
"border:none;\n"
"\n"
"border-radius:none;\n"
"text-align: left; \n"
"border:2px solid rgb(37,39,48);\n"
"padding-left:5px;\n"
"padding-right:5px;\n"
"\n"
"}")
        icon = QIcon()
        icon.addFile(u":/icons/icons/list.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_2.setIcon(icon)
        self.pushButton_2.setIconSize(QSize(40, 40))
        self.pushButton = QPushButton(self.frame_4)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(110, 50, 91, 51))
        self.pushButton.setStyleSheet(u"QPushButton {\n"
"color:#FFF;\n"
"background-color: rgb(24, 24, 24);\n"
"border:none;\n"
"border-radius:10px;\n"
"text-align: left; \n"
"border:2px solid rgb(37,39,48);\n"
"padding-left:5px;\n"
"padding-right:5px;\n"
"\n"
"}")
        icon1 = QIcon()
        icon1.addFile(u":/icons/icons/full-screen (1).png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton.setIcon(icon1)
        self.pushButton.setIconSize(QSize(40, 40))
        self.frame_2.raise_()
        self.label.raise_()
        self.label_2.raise_()
        self.pushButton.raise_()
        self.pushButton_2.raise_()

        self.horizontalLayout_4.addWidget(self.frame_4)


        self.verticalLayout_2.addWidget(self.header)

        self.frame_3 = QFrame(self.frame)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.frame_3)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.frame_5 = QFrame(self.frame_3)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setStyleSheet(u"QFrame{\n"
"  background-color:rgb(56, 58, 85);\n"
"  color:rgb(220, 220, 220);\n"
"	\n"
"	border-radius:none;\n"
"\n"
"\n"
"}")
        self.frame_5.setFrameShape(QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.stackedWidget = QStackedWidget(self.frame_5)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.stackedWidget.setGeometry(QRect(60, -20, 1141, 761))
        self.stackedWidget.setStyleSheet(u"background-color: rgb(56, 58, 85);")
        self.page = QWidget()
        self.page.setObjectName(u"page")
        self.verticalLayoutWidget = QWidget(self.page)
        self.verticalLayoutWidget.setObjectName(u"verticalLayoutWidget")
        self.verticalLayoutWidget.setGeometry(QRect(30, 30, 981, 411))
        self.verticalLayout_3 = QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setSizeConstraint(QLayout.SetFixedSize)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.frame_8 = QFrame(self.page)
        self.frame_8.setObjectName(u"frame_8")
        self.frame_8.setGeometry(QRect(550, 585, 451, 171))
        self.frame_8.setStyleSheet(u"QFrame{\n"
"\n"
"border:8px solid rgb(48,50,62);\n"
"color:#FFF;\n"
"padding-left:20px;\n"
"padding-right:20px;\n"
"background-color:rgb(34,36,40)\n"
"}\n"
"QFrame:hover{\n"
"border:2px solid rgb(48,50,62)\n"
"}\n"
"QFrame:focus{\n"
"border:2px solid rgb(85,170,255);\n"
"background-color:rgb(43,45,56)\n"
"}")
        self.frame_8.setFrameShape(QFrame.StyledPanel)
        self.frame_8.setFrameShadow(QFrame.Raised)
        self.gridLayout = QGridLayout(self.frame_8)
        self.gridLayout.setObjectName(u"gridLayout")
        self.label_5 = QLabel(self.frame_8)
        self.label_5.setObjectName(u"label_5")
        font1 = QFont()
        font1.setFamily(u"Segoe UI Emoji")
        font1.setPointSize(48)
        font1.setBold(True)
        font1.setWeight(75)
        self.label_5.setFont(font1)
#if QT_CONFIG(accessibility)
        self.label_5.setAccessibleName(u"")
#endif // QT_CONFIG(accessibility)
        self.label_5.setStyleSheet(u"text-align:left;\n"
"margin:-20px;")

        self.gridLayout.addWidget(self.label_5, 0, 0, 1, 1)

        self.label_6 = QLabel(self.frame_8)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setMinimumSize(QSize(395, 30))
        self.label_6.setMaximumSize(QSize(500, 30))
        font2 = QFont()
        font2.setFamily(u"Segoe UI")
        font2.setPointSize(9)
        font2.setBold(True)
        font2.setWeight(75)
        self.label_6.setFont(font2)
        self.label_6.setStyleSheet(u"margin:-20px;")

        self.gridLayout.addWidget(self.label_6, 2, 0, 1, 1)

        self.stackedWidget.addWidget(self.page)
        self.page_2 = QWidget()
        self.page_2.setObjectName(u"page_2")
        self.frame_6 = QFrame(self.page_2)
        self.frame_6.setObjectName(u"frame_6")
        self.frame_6.setGeometry(QRect(0, 80, 1141, 621))
        self.frame_6.setFrameShape(QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QFrame.Raised)
        self.frame_9 = QFrame(self.frame_6)
        self.frame_9.setObjectName(u"frame_9")
        self.frame_9.setGeometry(QRect(160, 0, 981, 441))
        self.frame_9.setStyleSheet(u"background-color: qlineargradient(spread:pad, x1:1, y1:1, x2:1, y2:1, stop:1 rgba(47, 49, 54, 175));")
        self.frame_9.setFrameShape(QFrame.StyledPanel)
        self.frame_9.setFrameShadow(QFrame.Raised)
        self.label_3 = QLabel(self.frame_9)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(20, 0, 391, 41))
        font3 = QFont()
        font3.setPointSize(18)
        font3.setBold(True)
        font3.setWeight(75)
        self.label_3.setFont(font3)
        self.label_3.setStyleSheet(u"background-color:none;")
        self.label_4 = QLabel(self.frame_9)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(20, 60, 841, 61))
        font4 = QFont()
        font4.setFamily(u"Segoe UI")
        font4.setPointSize(14)
        font4.setBold(False)
        font4.setItalic(False)
        font4.setWeight(50)
        self.label_4.setFont(font4)
        self.label_4.setStyleSheet(u"font: 14pt \"Segoe UI\";\n"
"background-color:none;")
        self.listWidget = QListWidget(self.frame_9)
        self.listWidget.setObjectName(u"listWidget")
        self.listWidget.setGeometry(QRect(20, 150, 591, 71))
        font5 = QFont()
        font5.setPointSize(14)
        self.listWidget.setFont(font5)
        self.listWidget.setStyleSheet(u"background-color: rgb(128, 131, 136);")
        self.listWidget.setAutoScrollMargin(2)
        self.listWidget.setProperty("showDropIndicator", False)
        self.listWidget.setViewMode(QListView.ListMode)
        self.listWidget.setSelectionRectVisible(False)
        self.listWidget.setSortingEnabled(False)
        self.textEdit = QTextEdit(self.frame_9)
        self.textEdit.setObjectName(u"textEdit")
        self.textEdit.setGeometry(QRect(20, 260, 401, 41))
        font6 = QFont()
        font6.setPointSize(12)
        self.textEdit.setFont(font6)
        self.textEdit.setStyleSheet(u"background-color: rgb(128, 131, 136);")
        self.radioButton_2 = QRadioButton(self.frame_9)
        self.radioButton_2.setObjectName(u"radioButton_2")
        self.radioButton_2.setGeometry(QRect(130, 320, 95, 20))
        font7 = QFont()
        font7.setPointSize(10)
        self.radioButton_2.setFont(font7)
        self.radioButton_2.setStyleSheet(u"background-color:none;")
        self.radioButton = QRadioButton(self.frame_9)
        self.radioButton.setObjectName(u"radioButton")
        self.radioButton.setGeometry(QRect(20, 320, 95, 20))
        self.radioButton.setFont(font7)
        self.radioButton.setStyleSheet(u"background-color:none;")
        self.pushButton_6 = QPushButton(self.frame_9)
        self.pushButton_6.setObjectName(u"pushButton_6")
        self.pushButton_6.setGeometry(QRect(20, 370, 171, 41))
        self.pushButton_6.setFont(font5)
        self.pushButton_6.setStyleSheet(u"QPushButton{\n"
"background-color: rgb(128, 131, 136);\n"
"border:none;\n"
"}\n"
"QPushButton:hover{\n"
"border:5px solid rgb(31, 109, 120)\n"
"}")
        self.pushButton_7 = QPushButton(self.frame_9)
        self.pushButton_7.setObjectName(u"pushButton_7")
        self.pushButton_7.setGeometry(QRect(210, 370, 171, 41))
        self.pushButton_7.setFont(font5)
        self.pushButton_7.setStyleSheet(u"QPushButton{\n"
"background-color: rgb(128, 131, 136);\n"
"border:none;\n"
"}\n"
"QPushButton:hover{\n"
"border:5px solid rgb(31, 109, 120)\n"
"}")
        self.label_7 = QLabel(self.frame_9)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setGeometry(QRect(20, 225, 171, 31))
        self.label_7.setFont(font5)
        self.label_7.setStyleSheet(u"background-color: none;")
        self.stackedWidget.addWidget(self.page_2)
        self.frame_7 = QFrame(self.frame_5)
        self.frame_7.setObjectName(u"frame_7")
        self.frame_7.setGeometry(QRect(0, 0, 0, 761))
        self.frame_7.setMaximumSize(QSize(16777215, 16777215))
        self.frame_7.setStyleSheet(u"background-color: rgb(31, 109, 120);\n"
"border-radius:1px;")
        self.frame_7.setFrameShape(QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.frame_7)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.pushButton_3 = QPushButton(self.frame_7)
        self.pushButton_3.setObjectName(u"pushButton_3")
        self.pushButton_3.setEnabled(True)
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(150)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_3.sizePolicy().hasHeightForWidth())
        self.pushButton_3.setSizePolicy(sizePolicy)
        self.pushButton_3.setMinimumSize(QSize(0, 80))
        self.pushButton_3.setMaximumSize(QSize(200, 80))
        self.pushButton_3.setLayoutDirection(Qt.LeftToRight)
        self.pushButton_3.setStyleSheet(u"QPushButton {\n"
"color:#FFF;\n"
"background-color: rgb(24, 24, 24);\n"
"border:none;\n"
"border-radius:10px;\n"
"text-align: left; \n"
"border:2px solid rgb(37,39,48);\n"
"padding-left:5px;\n"
"padding-right:5px;\n"
"\n"
"}\n"
"QPushButton:hover{\n"
"border:5px solid rgb(48,50,62)\n"
"}")
        icon2 = QIcon()
        icon2.addFile(u":/icons/icons/radioactivity.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_3.setIcon(icon2)
        self.pushButton_3.setIconSize(QSize(40, 40))

        self.verticalLayout_4.addWidget(self.pushButton_3)

        self.pushButton_5 = QPushButton(self.frame_7)
        self.pushButton_5.setObjectName(u"pushButton_5")
        self.pushButton_5.setMinimumSize(QSize(0, 80))
        self.pushButton_5.setMaximumSize(QSize(200, 80))
        self.pushButton_5.setStyleSheet(u"QPushButton {\n"
"color:#FFF;\n"
"background-color: rgb(24, 24, 24);\n"
"border:none;\n"
"border-radius:10px;\n"
"text-align: left; \n"
"border:2px solid rgb(37,39,48);\n"
"padding-left:5px;\n"
"padding-right:5px;\n"
"\n"
"}\n"
"QPushButton:hover{\n"
"border:5px solid rgb(48,50,62)\n"
"}")
        icon3 = QIcon()
        icon3.addFile(u":/icons/icons/notification.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_5.setIcon(icon3)
        self.pushButton_5.setIconSize(QSize(40, 40))

        self.verticalLayout_4.addWidget(self.pushButton_5)

        self.pushButton_4 = QPushButton(self.frame_7)
        self.pushButton_4.setObjectName(u"pushButton_4")
        sizePolicy1 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.pushButton_4.sizePolicy().hasHeightForWidth())
        self.pushButton_4.setSizePolicy(sizePolicy1)
        self.pushButton_4.setMinimumSize(QSize(0, 80))
        self.pushButton_4.setMaximumSize(QSize(200, 80))
        self.pushButton_4.setStyleSheet(u"QPushButton {\n"
"color:#FFF;\n"
"background-color: rgb(24, 24, 24);\n"
"border:none;\n"
"border-radius:10px;\n"
"text-align: left; \n"
"border:2px solid rgb(37,39,48);\n"
"padding-left:5px;\n"
"padding-right:5px;\n"
"\n"
"}\n"
"QPushButton:hover{\n"
"border:5px solid rgb(48,50,62)\n"
"}")
        icon4 = QIcon()
        icon4.addFile(u":/icons/icons/share.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_4.setIcon(icon4)
        self.pushButton_4.setIconSize(QSize(40, 40))

        self.verticalLayout_4.addWidget(self.pushButton_4)


        self.horizontalLayout_3.addWidget(self.frame_5)


        self.verticalLayout_2.addWidget(self.frame_3)


        self.verticalLayout.addWidget(self.frame)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.listWidget.setCurrentRow(-1)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label.setText("")
        self.label_2.setText(QCoreApplication.translate("MainWindow", u" TEMP DATA REPORTER", None))
        self.pushButton_2.setText(QCoreApplication.translate("MainWindow", u"       MENU", None))
        self.pushButton.setText("")
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"22", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"Last update", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Automated email reports", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Set up your email for temperature data to receive them at the frequency you need.", None))
        self.radioButton_2.setText(QCoreApplication.translate("MainWindow", u"60 min", None))
        self.radioButton.setText(QCoreApplication.translate("MainWindow", u"30 min", None))
        self.pushButton_6.setText(QCoreApplication.translate("MainWindow", u"Add", None))
        self.pushButton_7.setText(QCoreApplication.translate("MainWindow", u"Remove", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"Mail Adress:", None))
        self.pushButton_3.setText(QCoreApplication.translate("MainWindow", u"  TEMP GRAPH", None))
        self.pushButton_5.setText(QCoreApplication.translate("MainWindow", u"  Automated email", None))
        self.pushButton_4.setText(QCoreApplication.translate("MainWindow", u"  Export", None))
    # retranslateUi

