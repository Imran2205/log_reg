# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'login.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.tableWidget_information = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget_information.setObjectName("tableWidget_information")
        self.tableWidget_information.setColumnCount(0)
        self.tableWidget_information.setRowCount(0)
        self.gridLayout.addWidget(self.tableWidget_information, 8, 0, 1, 3)
        self.label_error = QtWidgets.QLabel(self.centralwidget)
        self.label_error.setText("")
        self.label_error.setObjectName("label_error")
        self.gridLayout.addWidget(self.label_error, 3, 1, 1, 2)
        self.lineEdit_email = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_email.setEchoMode(QtWidgets.QLineEdit.Normal)
        self.lineEdit_email.setObjectName("lineEdit_email")
        self.gridLayout.addWidget(self.lineEdit_email, 1, 1, 1, 2)
        self.label_heading = QtWidgets.QLabel(self.centralwidget)
        self.label_heading.setStyleSheet("\n"
"font: 75 18pt \"Century Schoolbook L\";")
        self.label_heading.setAlignment(QtCore.Qt.AlignCenter)
        self.label_heading.setObjectName("label_heading")
        self.gridLayout.addWidget(self.label_heading, 0, 1, 1, 1)
        self.label_email = QtWidgets.QLabel(self.centralwidget)
        self.label_email.setObjectName("label_email")
        self.gridLayout.addWidget(self.label_email, 1, 0, 1, 1)
        self.lineEdit_password = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_password.setEchoMode(QtWidgets.QLineEdit.Password)
        self.lineEdit_password.setObjectName("lineEdit_password")
        self.gridLayout.addWidget(self.lineEdit_password, 2, 1, 1, 2)
        self.pushButton_register = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_register.setObjectName("pushButton_register")
        self.gridLayout.addWidget(self.pushButton_register, 6, 2, 1, 1)
        self.pushButton_login = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_login.setObjectName("pushButton_login")
        self.gridLayout.addWidget(self.pushButton_login, 4, 1, 1, 2)
        self.label_password = QtWidgets.QLabel(self.centralwidget)
        self.label_password.setObjectName("label_password")
        self.gridLayout.addWidget(self.label_password, 2, 0, 1, 1)
        self.label_create_account_text = QtWidgets.QLabel(self.centralwidget)
        self.label_create_account_text.setObjectName("label_create_account_text")
        self.gridLayout.addWidget(self.label_create_account_text, 6, 1, 1, 1)
        self.label_user_information = QtWidgets.QLabel(self.centralwidget)
        self.label_user_information.setStyleSheet("font: 75 20pt \"MS Shell Dlg 2\";")
        self.label_user_information.setAlignment(QtCore.Qt.AlignCenter)
        self.label_user_information.setObjectName("label_user_information")
        self.gridLayout.addWidget(self.label_user_information, 7, 1, 1, 1)
        self.pushButton_clear = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_clear.setObjectName("pushButton_clear")
        self.gridLayout.addWidget(self.pushButton_clear, 9, 0, 1, 1)
        self.pushButton_close = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_close.setObjectName("pushButton_close")
        self.gridLayout.addWidget(self.pushButton_close, 9, 2, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_heading.setText(_translate("MainWindow", "LOG IN"))
        self.label_email.setText(_translate("MainWindow", "Email"))
        self.pushButton_register.setText(_translate("MainWindow", "Register"))
        self.pushButton_login.setText(_translate("MainWindow", "Login"))
        self.label_password.setText(_translate("MainWindow", "Password"))
        self.label_create_account_text.setText(_translate("MainWindow", "Dont have an account? Clik the button to"))
        self.label_user_information.setText(_translate("MainWindow", "User Information"))
        self.pushButton_clear.setText(_translate("MainWindow", "Clear"))
        self.pushButton_close.setText(_translate("MainWindow", "Close"))