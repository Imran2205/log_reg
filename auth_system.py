import sys

from PyQt5 import QtWidgets
from PyQt5.QtWidgets import *

import log_or_reg
import login
import register
import success
import re
import pandas as pd
import os


class Success(QMainWindow, success.Ui_MainWindow):
    def __init__(self, parent=None):
        super(Success, self).__init__(parent)
        self.setupUi(self)
        self.pushButton_done.clicked.connect(self.done)

    def show_me(self):
        self.show()

    def done(self):
        self.close()


class RegisterUIClass(QMainWindow, register.Ui_MainWindow):
    def __init__(self, parent=None):
        super(RegisterUIClass, self).__init__(parent)
        self.setupUi(self)
        self.pushButton_login.clicked.connect(self.login_func)
        self.info = {
        }
        self.comboBox_gender.addItem('Male')
        self.comboBox_gender.addItem('Female')
        self.pushButton_register.clicked.connect(self.register_func)
        self.db = pd.read_csv('info.csv')
        self.success = Success()

    def register_func(self):
        self.db = pd.read_csv('info.csv')
        self.info['Name'] = self.lineEdit_name.text()
        self.info['Email'] = self.lineEdit_email.text()
        self.info['Age'] = self.spinBox_age.value()
        self.info['Gender'] = self.comboBox_gender.currentText()
        self.info['University'] = self.lineEdit_university.text()
        password = self.lineEdit_password.text()
        confirm_password = self.lineEdit_confirm_password.text()
        blank_error = False
        name_error = False
        email_error = False
        email_exists = False
        for val in self.info.values():
            if val == '':
                blank_error = True
                break
        if password == '' or confirm_password == '':
            blank_error = True

        if blank_error:
            self.label_confirm_password_error.setText("Please fill up all the fields")
        else:
            self.label_confirm_password_error.setText("")
            names = self.info['Name'].split()
            new_name = ''
            for i, name in enumerate(names):
                for j, c in enumerate(name):
                    if 'Z' >= c >= 'A' or 'z' >= c >= 'a':
                        pass
                    else:
                        name_error = True
                        break
                    if j == 0:
                        if 'z' >= c >= 'a':
                            name = chr(ord(c) - 32) + name[1:]
                if name_error:
                    break
                names[i] = name
                new_name = new_name + names[i] + ' '
            if name_error:
                self.label_name_error.setText("Please enter a valid name")
            else:
                self.label_name_error.setText("")
                self.info['Name'] = new_name
                checker1 = r'[A-Za-z0-9._%+-]+@ulkasemi\.com$'
                checker2 = r'[A-Za-z0-9._%+-]+@gfoundties\.com$'
                if re.match(checker1, self.info['Email']) or re.match(checker2, self.info['Email']):
                    if self.info['Email'] in list(self.db['Email']):
                        email_exists = True
                else:
                    email_error = True
                if email_error:
                    self.label_email_error.setText("Please enter a valid email")
                elif email_exists:
                    self.label_email_error.setText("This email already exists in database")
                else:
                    self.label_email_error.setText("")
                    if self.info['Age'] <= 0:
                        self.label_age_error.setText("Please enter a valid age")
                    else:
                        self.label_age_error.setText("")
                        if password == confirm_password:
                            while True:
                                if len(password) < 8:
                                    self.label_confirm_password_error.setText(
                                        "Password must contain at least 8 characters")
                                    break
                                if not re.search('[A-Z]', password):
                                    self.label_confirm_password_error.setText(
                                        "Password must contain at least 1 uppercase character")
                                    break
                                if not re.search('[a-z]', password):
                                    self.label_confirm_password_error.setText(
                                        "Password must contain at least 1 lowercase character")
                                    break
                                if not re.search('[0-9]', password):
                                    self.label_confirm_password_error.setText(
                                        "Password must contain at least 1 number")
                                    break
                                if not re.search('[~!@#$%^&*?><]', password):
                                    self.label_confirm_password_error.setText(
                                        "Password must contain at least 1 special character(~!@#$%^&*<>?)")
                                    break
                                else:
                                    self.label_confirm_password_error.setText("")
                                    self.info['Password'] = password
                                    for key in self.info.keys():
                                        self.info[key] = [self.info[key]]
                                    df = pd.DataFrame(self.info)
                                    df.to_csv('info.csv', mode='a', header=False)
                                    self.success.show_me()
                                    self.clear_n_close()
                                    break
                        else:
                            self.label_confirm_password_error.setText("Password did not match")

    def login_func(self):
        self.clear_n_close()

    def clear_n_close(self):
        self.db = pd.read_csv('info.csv')
        self.lineEdit_name.setText("")
        self.lineEdit_email.setText("")
        self.lineEdit_university.setText("")
        self.lineEdit_password.setText("")
        self.lineEdit_confirm_password.setText("")
        self.spinBox_age.setValue(0)
        self.comboBox_gender.setCurrentText('Male')
        self.label_name_error.setText("")
        self.label_email_error.setText("")
        self.label_age_error.setText("")
        self.label_gender_error.setText("")
        self.label_university_error.setText("")
        self.label_password_error.setText("")
        self.label_confirm_password_error.setText("")
        self.info = {

        }
        self.close()

    def show_me(self):
        self.show()


class LoginUIClass(QMainWindow, login.Ui_MainWindow):
    def __init__(self, parent=None):
        super(LoginUIClass, self).__init__(parent)
        self.setupUi(self)
        self.db = pd.read_csv('info.csv')
        self.register = RegisterUIClass()
        self.pushButton_register.clicked.connect(self.register_func)
        self.pushButton_login.clicked.connect(self.login_func)
        self.pushButton_clear.clicked.connect(self.clear_only)
        self.pushButton_close.clicked.connect(self.clear_n_close)

    def register_func(self):
        self.register.show_me()
        self.clear_n_close()

    def login_func(self):
        self.db = pd.read_csv('info.csv')
        email = self.lineEdit_email.text()
        password = self.lineEdit_password.text()
        if email in list(self.db['Email']):
            self.label_error.setText("")
            ind = list(self.db['Email']).index(email)
            db_pass = list(self.db['Password'])[ind]
            if password == db_pass:
                self.label_error.setText("")
                self.tableWidget_information.setColumnCount(3)
                self.tableWidget_information.setRowCount(1)
                self.tableWidget_information.setItem(0, 0, QTableWidgetItem("Serial No"))
                self.tableWidget_information.setItem(0, 1, QTableWidgetItem("Title"))
                self.tableWidget_information.setItem(0, 2, QTableWidgetItem("Data"))
                for row, key in enumerate(dict(self.db.iloc[ind]).keys()):
                    if key != 'Password' and key != 'Unnamed: 0':
                        self.tableWidget_information.setRowCount(row+1)
                        self.tableWidget_information.setItem(row, 0, QTableWidgetItem(str(row)))
                        self.tableWidget_information.setItem(row, 1, QTableWidgetItem(key))
                        self.tableWidget_information.setItem(row, 2, QTableWidgetItem(str(dict(self.db.iloc[ind])[key])))
            else:
                self.label_error.setText("Password is not correct!")
        else:
            self.label_error.setText("Email is not correct!")

    def show_me(self):
        self.show()

    def clear_n_close(self):
        self.lineEdit_email.setText("")
        self.lineEdit_password.setText("")
        self.label_error.setText("")
        self.tableWidget_information.clear()
        self.close()

    def clear_only(self):
        self.lineEdit_email.setText("")
        self.lineEdit_password.setText("")
        self.label_error.setText("")
        self.tableWidget_information.clear()


class MainUIClass(QMainWindow, log_or_reg.Ui_MainWindow):
    def __init__(self, parent=None):
        super(MainUIClass, self).__init__(parent)
        self.setupUi(self)
        self.info = {

        }
        self.files = os.listdir(os.getcwd())
        if 'info.csv' not in self.files:
            self.info['Name'] = []
            self.info['Email'] = []
            self.info['Age'] = []
            self.info['Gender'] = []
            self.info['University'] = []
            self.info['Password'] = []
            df = pd.DataFrame(self.info)
            df.to_csv('info.csv')
        self.register = RegisterUIClass()
        self.login = LoginUIClass()
        self.pushButton_login.clicked.connect(self.login_func)
        self.pushButton_register.clicked.connect(self.register_func)

    def register_func(self):
        self.register.show_me()

    def login_func(self):
        self.login.show_me()

class Controller:
    def __init__(self):
        pass
    def show_main(self):
        self.window = MainUIClass()
        #self.window.switch_window.connect(self.show_window_main)
        self.window.show()

    """def show_window_main(self):
        self.window_two = MainUIClass()
        self.window.close()
        self.window_two.show()"""

def main():
    app = QtWidgets.QApplication(sys.argv)
    controller = Controller()
    controller.show_main()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()