# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'saque.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.uic import loadUi

class Ui_saque(object):
    def setupUi(self, saque):
        saque.setObjectName("saque")
        saque.resize(400, 100)
        saque.setMinimumSize(QtCore.QSize(400, 100))
        saque.setMaximumSize(QtCore.QSize(400, 100))
        self.centralwidget = QtWidgets.QWidget(saque)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(0, 0, 411, 111))
        self.label.setStyleSheet("background-image: url(Images\Withdraw.png);")
        self.label.setText("")
        self.label.setObjectName("label")
        self.textEdit = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit.setGeometry(QtCore.QRect(100, 20, 201, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.textEdit.setFont(font)
        self.textEdit.setStyleSheet("background-color: rgb(238, 186, 43);")
        self.textEdit.setObjectName("textEdit")
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(100, 60, 60, 34))
        self.pushButton_3.setStyleSheet("background-color: rgb(238, 186, 43);")
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_4 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_4.setGeometry(QtCore.QRect(240, 60, 60, 34))
        self.pushButton_4.setStyleSheet("background-color: rgb(238, 186, 43);")
        self.pushButton_4.setObjectName("pushButton_4")
        saque.setCentralWidget(self.centralwidget)

        self.retranslateUi(saque)
        QtCore.QMetaObject.connectSlotsByName(saque)

    def retranslateUi(self, saque):
        _translate = QtCore.QCoreApplication.translate
        saque.setWindowTitle(_translate("saque", "Saque"))
        self.textEdit.setHtml(_translate("saque", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Segoe UI\'; font-size:11pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:9pt;\"><br /></p></body></html>"))
        self.pushButton_3.setText(_translate("saque", "Saque"))
        self.pushButton_4.setText(_translate("saque", "Voltar"))

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    w = QtWidgets.QMainWindow()
    ui = Ui_saque()
    ui.setupUi(w)
    w.show()
    sys.exit(app.exec_())