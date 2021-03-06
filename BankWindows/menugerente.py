# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'menugerente.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from requests import options
from CadastroCliente import Ui_CadastroCliente as CadastroCliente
from ViewCliente import Ui_ViewCliente as ViewCliente

class Ui_Gerente(object):
    def options (self,x):
        if x == 1:
            self.window1 = QtWidgets.QMainWindow()
            self.ui = CadastroCliente()
            self.ui.setupUi (self.window1)
            self.window1.show()
        elif x == 2:
            self.window2 = QtWidgets.QMainWindow()
            self.ui = ViewCliente()
            self.ui.setupUi (self.window2)
            self.window2.show()

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(500, 500)
        MainWindow.setMaximumSize(QtCore.QSize(500, 500))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(0, 0, 501, 511))
        self.label.setStyleSheet("background-image: url(MenuGerente.png);")
        self.label.setText("")
        self.label.setObjectName("label")
        self.nametext = QtWidgets.QTextBrowser(self.centralwidget)
        self.nametext.setGeometry(QtCore.QRect(50, 50, 401, 71))
        font = QtGui.QFont()
        font.setPointSize(24)
        self.nametext.setFont(font)
        self.nametext.setStyleSheet("background-color: rgb(238, 186, 43);")
        self.nametext.setObjectName("nametext")
        self.clientcreator = QtWidgets.QPushButton(self.centralwidget)
        self.clientcreator.clicked.connect(lambda: self.options(1))
        self.clientcreator.setGeometry(QtCore.QRect(39, 370, 121, 111))
        self.clientcreator.setStyleSheet("background-color: rgb(238, 186, 43);\n"
"background-image: url(Cliente.png);\n"
"")
        self.clientcreator.setText("")
        self.clientcreator.setObjectName("clientcreator")
        self.clientview = QtWidgets.QPushButton(self.centralwidget)
        self.clientview.clicked.connect(lambda: self.options(2))
        self.clientview.setGeometry(QtCore.QRect(189, 370, 121, 111))
        self.clientview.setStyleSheet("background-color: rgb(238, 186, 43);\n"
"background-image: url(listaclientegerente.png);")
        self.clientview.setText("")
        self.clientview.setObjectName("clientview")
        self.emprestimo = QtWidgets.QPushButton(self.centralwidget)
        self.emprestimo.setGeometry(QtCore.QRect(340, 370, 121, 111))
        self.emprestimo.setStyleSheet("background-color: rgb(238, 186, 43);\n"
"background-image: url(EmprestimoIcon.png);")
        self.emprestimo.setText("")
        self.emprestimo.setObjectName("emprestimo")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Banco Assemble"))
        self.nametext.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Segoe UI\'; font-size:24pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Bem vindo, Gerente </p></body></html>"))

