# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'menupadrao.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.uic import loadUi

class Ui_menugerente(object):
    def setupUi(self, menu):
        menu.setObjectName("menu")
        menu.resize(500, 500)
        menu.setMaximumSize(QtCore.QSize(500, 500))
        self.centralwidget = QtWidgets.QWidget(menu)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(0, 0, 501, 511))
        self.label.setStyleSheet("background-image: url(:/Menu Gerente/MenuGerente.png);")
        self.label.setText("")
        self.label.setObjectName("label")
        self.nametext = QtWidgets.QTextBrowser(self.centralwidget)
        self.nametext.setGeometry(QtCore.QRect(50, 50, 401, 31))
        self.nametext.setStyleSheet("background-color: rgb(238, 186, 43);")
        self.nametext.setObjectName("nametext")
        self.withdrawbutton = QtWidgets.QPushButton(self.centralwidget)
        self.withdrawbutton.setGeometry(QtCore.QRect(39, 370, 121, 111))
        self.withdrawbutton.setStyleSheet("background-color: rgb(238, 186, 43);\n"
"background-image: url(:/InternalMenu/Withdrawbutton.png);")
        self.withdrawbutton.setText("")
        self.withdrawbutton.setObjectName("withdrawbutton")
        self.depositbutton = QtWidgets.QPushButton(self.centralwidget)
        self.depositbutton.setGeometry(QtCore.QRect(189, 370, 121, 111))
        self.depositbutton.setStyleSheet("background-color: rgb(238, 186, 43);\n"
"background-image: url(:/InternalMenu/depositbutton.png);")
        self.depositbutton.setText("")
        self.depositbutton.setObjectName("depositbutton")
        self.extractbutton = QtWidgets.QPushButton(self.centralwidget)
        self.extractbutton.setGeometry(QtCore.QRect(340, 370, 121, 111))
        self.extractbutton.setStyleSheet("background-color: rgb(238, 186, 43);\n"
"background-image: url(:/InternalMenu/ExtractButton.png);")
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
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:11pt;\">Bem vindo, </span></p></body></html>"))
        #self.balancetext.setHtml(_translate("menu", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
#"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
#"p, li { white-space: pre-wrap; }\n"
#"</style></head><body style=\" font-family:\'Segoe UI\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
#"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:16pt;\">R$:</span></p></body></html>"))

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    w = QtWidgets.QMainWindow()
    ui = Ui_menugerente()
    ui.setupUi(w)
    w.show()
    sys.exit(app.exec_())