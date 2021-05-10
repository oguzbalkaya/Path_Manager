# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'neworedit.ui'
##
## Created by: Qt User Interface Compiler version 6.0.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *


class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(515, 180)
        Form.setMinimumSize(QSize(515, 180))
        Form.setMaximumSize(QSize(515, 180))
        icon = QIcon()
        icon.addFile(u"./icon.png", QSize(), QIcon.Normal, QIcon.Off)
        Form.setWindowIcon(icon)
        self.saveButton = QPushButton(Form)
        self.saveButton.setObjectName(u"saveButton")
        self.saveButton.setGeometry(QRect(410, 110, 80, 23))
        self.lineEdit = QLineEdit(Form)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setGeometry(QRect(20, 60, 471, 22))
        self.cancelButton = QPushButton(Form)
        self.cancelButton.setObjectName(u"cancelButton")
        self.cancelButton.setGeometry(QRect(310, 110, 80, 23))
        self.label = QLabel(Form)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(20, 30, 491, 21))

        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Path Manager", None))
        self.saveButton.setText(QCoreApplication.translate("Form", u"Save", None))
        self.cancelButton.setText(QCoreApplication.translate("Form", u"Cancel", None))
        self.label.setText(QCoreApplication.translate("Form", u"Write PATH :", None))
    # retranslateUi

