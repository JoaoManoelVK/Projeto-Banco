        # -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'loginpadrao.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.

import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.uic import loadUi


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
        self.user.setStyleSheet("background-color: rgb(238, 186, 43);\n"
"color: rgb(0, 0, 0);")
        self.user.setObjectName("user")
        self.senha = QtWidgets.QTextEdit(self.centralwidget)
        self.senha.setGeometry(QtCore.QRect(155, 241, 191, 31))
        self.senha.setStyleSheet("background-color: rgb(238, 186, 43);\n"
"color: rgb(0, 0, 0);")
        self.senha.setObjectName("senha")
        self.login = QtWidgets.QPushButton(self.centralwidget)
        self.login.setGeometry(QtCore.QRect(220, 320, 61, 32))
        self.login.setStyleSheet("background-color: rgb(238, 186, 43);")
        self.login.setObjectName("login")
        Login.setCentralWidget(self.centralwidget)

        self.retranslateUi(Login)
        QtCore.QMetaObject.connectSlotsByName(Login)

    def retranslateUi(self, Login):
        _translate = QtCore.QCoreApplication.translate
        Login.setWindowTitle(_translate("Login", "Banco Assemble"))
        self.user.setHtml(_translate("Login", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Segoe UI\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.login.setText(_translate("Login", "Login"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    w = QtWidgets.QMainWindow()
    ui = Ui_Login()
    ui.setupUi(w)
    w.show()
    sys.exit(app.exec_())