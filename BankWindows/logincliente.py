# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'loginpadrao.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from asyncio.windows_events import NULL
import json
from optparse import Option
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox, QWidget
from PyQt5.uic import loadUi
from menucliente import Ui_menucliente as menu
from untitled import Ui_Dialog as erro
import requests

baseurl = "http://localhost:3000"

class MainClass(QWidget):
    def __init__(self,text):
        super().__init__()
        self.text = text

    def clickMethod(self):
        QMessageBox.about(self, "Title", self.text)


class Ui_Login(object):
    def setupUi(self, Login):
        Login.setObjectName("Login")
        Login.resize(500, 500)
        Login.setMaximumSize(QtCore.QSize(500, 500))
        self.centralwidget = QtWidgets.QWidget(Login)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(0, 0, 501, 501))
        self.label.setStyleSheet("background-image: url(Login.png);")
        self.label.setText("")
        self.label.setObjectName("label")
        self.user = QtWidgets.QTextEdit(self.centralwidget)
        self.user.setGeometry(QtCore.QRect(155, 179, 191, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.user.setFont(font)
        self.user.setStyleSheet("background-color: rgb(238, 186, 43);\n"
"color: rgb(0, 0, 0);")
        self.user.setObjectName("user")
        self.login = QtWidgets.QPushButton(self.centralwidget)
        self.login.clicked.connect(lambda: self.option(self.user.toPlainText(),self.senha.text()))
        self.close = Login.close
        self.login.setGeometry(QtCore.QRect(220, 320, 61, 32))
        self.login.setStyleSheet("background-color: rgb(238, 186, 43);")
        self.login.setObjectName("login")
        self.senha = QtWidgets.QLineEdit(self.centralwidget)
        self.senha.setGeometry(QtCore.QRect(155, 241, 191, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.senha.setFont(font)
        self.senha.setStyleSheet("background-color: rgb(238, 186, 43);\n"
"color: rgb(0, 0, 0);\n"
"border-color: rgb(0, 0, 0);\n"
"")
        self.senha.setEchoMode(QtWidgets.QLineEdit.Password)
        self.senha.setObjectName("senha")
        Login.setCentralWidget(self.centralwidget)

        self.retranslateUi(Login)
        QtCore.QMetaObject.connectSlotsByName(Login)

    def retranslateUi(self, Login):
        _translate = QtCore.QCoreApplication.translate
        Login.setWindowTitle(_translate("Login", "Banco Assemble"))
        self.user.setHtml(_translate("Login", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Segoe UI\'; font-size:11pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.login.setText(_translate("Login", "Login"))

    def option(self,usuario,senha):
        print(usuario,senha)
        payload = {
    "cpf": usuario,
    "senha": senha
        }
        headers = {"Content-Type": "application/json"}
        response = requests.request("POST", baseurl+"/auth", json=payload, headers=headers)
        if response.status_code == 200:
                global sessao
                sessao = response.json()
                self.window1 = QtWidgets.QMainWindow()
                self.ui = menu()
                self.ui.setupUi (self.window1)
                self.window1.show()
                self.close()
                
        else:
                MainClass(response.json()['message']).clickMethod()

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    w = QtWidgets.QMainWindow()
    ui = Ui_Login()
    ui.setupUi(w)
    w.show()
    sys.exit(app.exec_())