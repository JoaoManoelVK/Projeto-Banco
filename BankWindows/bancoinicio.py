# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'bancoinicio.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.uic import loadUi
from requests import options
from logincliente import Ui_LoginCliente as cliente
from logingerente import Ui_LoginGerente as gerente
from logindiretor import Ui_LoginDiretor as diretor


class Ui_bancoinicio(object):

    def options (self,x):
        if x == 1:
            self.window1 = QtWidgets.QMainWindow()
            self.ui = cliente()
            self.ui.setupUi (self.window1)
            self.window1.show()
        elif x == 2:
            self.window2 = QtWidgets.QMainWindow()
            self.ui = gerente()
            self.ui.setupUi (self.window2)
            self.window2.show()
        else:
            self.window3 = QtWidgets.QMainWindow()
            self.ui = diretor()
            self.ui.setupUi (self.window3)
            self.window3.show()


    def setupUi(self, bancoinicio):
        bancoinicio.setObjectName("bancoinicio")
        bancoinicio.resize(500, 500)
        bancoinicio.setMinimumSize(QtCore.QSize(500, 500))
        bancoinicio.setMaximumSize(QtCore.QSize(500, 500))
        self.centralwidget = QtWidgets.QWidget(bancoinicio)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(0, 0, 500, 500))
        self.label.setStyleSheet("background-image: url(ExternalMenu.png);")
        self.label.setText("")
        self.label.setObjectName("label")
        self.clientebutton = QtWidgets.QPushButton(self.centralwidget)
        self.clientebutton.clicked.connect(lambda: self.options(1))
        self.clientebutton.clicked.connect(lambda: bancoinicio.close())
        self.clientebutton.setGeometry(QtCore.QRect(170, 225, 160, 51))
        self.clientebutton.setStyleSheet("background-color: rgb(238, 186, 43);\n"
"\n"
"")
        self.clientebutton.setObjectName("clientebutton")
        self.gerentebutton = QtWidgets.QPushButton(self.centralwidget)
        self.gerentebutton.clicked.connect(lambda: self.options(2))
        self.gerentebutton.clicked.connect(lambda: bancoinicio.close())
        self.gerentebutton.setGeometry(QtCore.QRect(170, 325, 160, 51))
        self.gerentebutton.setStyleSheet("background-color: rgb(238, 186, 43);")
        self.gerentebutton.setObjectName("gerentebutton")
        self.diretorbutton = QtWidgets.QPushButton(self.centralwidget)
        self.diretorbutton.clicked.connect(lambda: self.options(0))
        self.diretorbutton.clicked.connect(lambda: bancoinicio.close())
        self.diretorbutton.setGeometry(QtCore.QRect(170, 429, 160, 51))
        self.diretorbutton.setStyleSheet("background-color: rgb(238, 186, 43);")
        self.diretorbutton.setObjectName("diretorbutton")
        bancoinicio.setCentralWidget(self.centralwidget)

        self.retranslateUi(bancoinicio)
        QtCore.QMetaObject.connectSlotsByName(bancoinicio)

    def retranslateUi(self, bancoinicio):
        _translate = QtCore.QCoreApplication.translate
        bancoinicio.setWindowTitle(_translate("bancoinicio", "Banco Assemble"))
        self.clientebutton.setText(_translate("bancoinicio", "Cliente"))
        self.gerentebutton.setText(_translate("bancoinicio", "Gerente"))
        self.diretorbutton.setText(_translate("bancoinicio", "Diretor"))

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    w = QtWidgets.QMainWindow()
    ui = Ui_bancoinicio()
    ui.setupUi(w)
    w.show()
    sys.exit(app.exec_())