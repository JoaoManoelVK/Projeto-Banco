# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'menupadrao.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


import requests
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.uic import loadUi
from saque import Ui_Saque as saque
from deposito import Ui_Deposito as deposito
from Extrato import Ui_Extrato as extrato
import logincliente

baseurl = "http://localhost:3000"

class Ui_menucliente(object):
    
    def options (self,x):
        if x == 1:
            self.window1 = QtWidgets.QMainWindow()
            self.ui = saque()
            self.ui.setupUi (self.window1)
            self.window1.show()
        elif x == 2:
            self.window2 = QtWidgets.QMainWindow()
            self.ui = deposito()
            self.ui.setupUi (self.window2)
            self.window2.show()
        else:
            self.window3 = QtWidgets.QMainWindow()
            self.ui = extrato()
            self.ui.setupUi (self.window3)
            self.window3.show()
    
    
    def setupUi(self, menu):
        menu.setObjectName("menu")
        menu.resize(500, 500)
        menu.setMaximumSize(QtCore.QSize(500, 500))
        self.centralwidget = QtWidgets.QWidget(menu)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(0, 0, 501, 511))
        self.label.setStyleSheet("background-image: url(InternalMenu.png);")
        self.label.setText("")
        self.label.setObjectName("label")
        self.nametext = QtWidgets.QTextBrowser(self.centralwidget)
        self.nametext.setGeometry(QtCore.QRect(50, 50, 401, 31))
        self.nametext.setStyleSheet("background-color: rgb(238, 186, 43);")
        self.nametext.setObjectName("nametext")
        self.balancetext = QtWidgets.QTextBrowser(self.centralwidget)
        self.balancetext.setGeometry(QtCore.QRect(50, 104, 400, 45))
        self.balancetext.setStyleSheet("background-color: rgb(238, 186, 43);")
        self.balancetext.setObjectName("balancetext")
        self.withdrawbutton = QtWidgets.QPushButton(self.centralwidget)
        self.withdrawbutton.clicked.connect(lambda: self.options(1))
        self.withdrawbutton.clicked.connect(lambda: menu.close())
        self.withdrawbutton.setGeometry(QtCore.QRect(39, 370, 121, 111))
        self.withdrawbutton.setStyleSheet("background-color: rgb(238, 186, 43);\n"
"background-image: url(Withdrawbutton.png);")
        self.withdrawbutton.setText("")
        self.withdrawbutton.setObjectName("withdrawbutton")
        self.depositbutton = QtWidgets.QPushButton(self.centralwidget)
        self.depositbutton.clicked.connect(lambda: self.options(2))
        self.depositbutton.clicked.connect(lambda: menu.close())
        self.depositbutton.setGeometry(QtCore.QRect(189, 370, 121, 111))
        self.depositbutton.setStyleSheet("background-color: rgb(238, 186, 43);\n"
"background-image: url(depositbutton.png);")
        self.depositbutton.setText("")
        self.depositbutton.setObjectName("depositbutton")
        self.extractbutton = QtWidgets.QPushButton(self.centralwidget)
        self.extractbutton.clicked.connect(lambda: self.options(0))
        self.extractbutton.clicked.connect(lambda: menu.close())
        self.extractbutton.setGeometry(QtCore.QRect(340, 370, 121, 111))
        self.extractbutton.setStyleSheet("background-color: rgb(238, 186, 43);\n"
"background-image: url(ExtractButton.png);")
        self.extractbutton.setText("")
        self.extractbutton.setObjectName("extractbutton")
        menu.setCentralWidget(self.centralwidget)

        self.retranslateUi(menu)
        QtCore.QMetaObject.connectSlotsByName(menu)

    def retranslateUi(self, menu):
        _translate = QtCore.QCoreApplication.translate
        menu.setWindowTitle(_translate("menu", "Banco Assemble"))
        self.nametext.setHtml(_translate("menu", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Segoe UI\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:11pt;\">Bem vindo, "+  +" </span></p></body></html>"))
        self.balancetext.setHtml(_translate("menu", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Segoe UI\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:16pt;\">R$:"+  +"</span></p></body></html>"))

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    w = QtWidgets.QMainWindow()
    ui = Ui_menucliente()
    ui.setupUi(w)
    w.show()
    sys.exit(app.exec_())