# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Extrato.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.uic import loadUi

class Ui_extrato(object):
    def setupUi(self, extrato):
        extrato.setObjectName("extrato")
        extrato.resize(1000, 500)
        extrato.setMinimumSize(QtCore.QSize(1000, 500))
        extrato.setMaximumSize(QtCore.QSize(1000, 500))
        self.centralwidget = QtWidgets.QWidget(extrato)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(0, 0, 1001, 501))
        self.label.setStyleSheet("background-image: url(BankWindows\Images\TelaExtrato.png);")
        self.label.setText("")
        self.label.setObjectName("label")
        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget.setGeometry(QtCore.QRect(50, 50, 901, 391))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(3)
        self.tableWidget.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(883, 452, 97, 38))
        self.pushButton.setStyleSheet("background-color: rgb(238, 186, 43);")
        self.pushButton.setObjectName("pushButton")
        extrato.setCentralWidget(self.centralwidget)

        self.retranslateUi(extrato)
        QtCore.QMetaObject.connectSlotsByName(extrato)

    def retranslateUi(self, extrato):
        _translate = QtCore.QCoreApplication.translate
        extrato.setWindowTitle(_translate("extrato", "Extrato"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("extrato", "Data"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("extrato", "Operação"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("extrato", "Quantidade"))
        self.pushButton.setText(_translate("extrato", "Voltar"))

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    w = QtWidgets.QMainWindow()
    ui = Ui_extrato()
    ui.setupUi(w)
    w.show()
    sys.exit(app.exec_())
