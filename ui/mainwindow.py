# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'untitled.ui'
##
## Created by: Qt User Interface Compiler version 6.0.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(600, 465)
        MainWindow.setMinimumSize(QSize(600, 465))
        MainWindow.setMaximumSize(QSize(600, 465))
        icon = QIcon()
        icon.addFile(u"./icon.png", QSize(), QIcon.Normal, QIcon.Off)
        MainWindow.setWindowIcon(icon)
        self.actionAbout = QAction(MainWindow)
        self.actionAbout.setObjectName(u"actionAbout")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.horizontalLayoutWidget = QWidget(self.centralwidget)
        self.horizontalLayoutWidget.setObjectName(u"horizontalLayoutWidget")
        self.horizontalLayoutWidget.setGeometry(QRect(20, 60, 561, 321))
        self.horizontalLayout = QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.listWidget = QListWidget(self.horizontalLayoutWidget)
        self.listWidget.setObjectName(u"listWidget")

        self.horizontalLayout.addWidget(self.listWidget)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(-1, -1, -1, 175)
        self.newButton = QPushButton(self.horizontalLayoutWidget)
        self.newButton.setObjectName(u"newButton")

        self.verticalLayout.addWidget(self.newButton)

        self.editButton = QPushButton(self.horizontalLayoutWidget)
        self.editButton.setObjectName(u"editButton")

        self.verticalLayout.addWidget(self.editButton)

        self.deleteButton = QPushButton(self.horizontalLayoutWidget)
        self.deleteButton.setObjectName(u"deleteButton")

        self.verticalLayout.addWidget(self.deleteButton)


        self.horizontalLayout.addLayout(self.verticalLayout)

        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(20, 20, 551, 21))
        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(20, 400, 471, 21))
        self.saveButton = QPushButton(self.centralwidget)
        self.saveButton.setObjectName(u"saveButton")
        self.saveButton.setGeometry(QRect(460, 400, 121, 23))
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 600, 20))
        self.menuInformation = QMenu(self.menubar)
        self.menuInformation.setObjectName(u"menuInformation")
        MainWindow.setMenuBar(self.menubar)

        self.menubar.addAction(self.menuInformation.menuAction())
        self.menuInformation.addAction(self.actionAbout)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Path Manager", None))
        self.actionAbout.setText(QCoreApplication.translate("MainWindow", u"About", None))
        self.newButton.setText(QCoreApplication.translate("MainWindow", u"New", None))
        self.editButton.setText(QCoreApplication.translate("MainWindow", u"Edit", None))
        self.deleteButton.setText(QCoreApplication.translate("MainWindow", u"Delete", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"You can only change the paths you added with the app.Greens are changeable.", None))
        self.saveButton.setText(QCoreApplication.translate("MainWindow", u"Save All Changes", None))
        self.menuInformation.setTitle(QCoreApplication.translate("MainWindow", u"Information", None))
    # retranslateUi

