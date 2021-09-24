from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QDialog, QLineEdit, QMessageBox, QStackedWidget
from PyQt5.uic import loadUi
from PyQt5.QtGui import QIcon
#import mysql.connector
import webbrowser as web
import random

class Login(QDialog):
    def __init__(self):
        QDialog.__init__(self)
        loadUi(r"UI_Design\MainLogin.ui", self)

        self.signup_btn_red.clicked.connect(self.sign_up)
        self.signin_btn_red.clicked.connect(self.sql_sign_in)
        self.f_pass_btn.clicked.connect(self.forgot)
        self.del_acc_btn.clicked.connect(self.delete)
        self.eye_img.clicked.connect(self.eye_event)
        self.fb_btn.clicked.connect(self.facebook)
        self.insta_btn.clicked.connect(self.instagram)
        self.twitter_btn.clicked.connect(self.twitter)
        self.show_visible = False

    def sign_up(self):
        window = Signup()
        widget.addWidget(window)
        widget.setCurrentIndex(widget.currentIndex() + 1)

    def forgot(self):
        window1 = F_Password()
        widget.addWidget(window1)
        widget.setCurrentIndex(widget.currentIndex() + 1)

    def delete(self):
        window2 = Delete_Account()
        widget.addWidget(window2)
        widget.setCurrentIndex(widget.currentIndex() + 1)

    def eye_event(self):
        if not self.show_visible:
            self.password.setEchoMode(QtWidgets.QLineEdit.Normal)
            self.show_visible = True
            self.eye_img.setIcon(QIcon(r"icons\eye-off_icon.png"))
        else:
            self.password.setEchoMode(QtWidgets.QLineEdit.Password)
            self.show_visible = False
            self.eye_img.setIcon(QIcon(r"icons\eye-on_icon.png"))
        
    def facebook(self):
        web.open('www.facebook.com')

    def instagram(self):
        web.open('www.instagram.com')

    def twitter(self):
        web.open('www.twitter.com')

    #pymysql for signin database logic starts from here
    def sql_sign_in(self):
        if self.username.text() == '' or self.password.text() == '':
            QtWidgets.QMessageBox.warning(self, 'WARNING..', "            All fields must be required!!             ")
        else:
            my_database = mysql.connector.connect(host='localhost',user='root',password='root#123_',database='myapp')
            my_cursor = my_database.cursor()
            my_cursor.execute(f"SELECT * FROM app_data WHERE username='{self.username.text()}' and password='{self.password.text()}'")
            result = my_cursor.fetchone()
            if result == None:
                QtWidgets.QMessageBox.critical(self, 'LOGIN INFO', "          Username doesn't exists           ")
            else:
                QtWidgets.QMessageBox.information(self, 'LOGIN INFO', "          Login Successful!!           ")
                self.username.setText("")
                self.password.setText("")



class Signup(QDialog):
    def __init__(self):
        QDialog.__init__(self)
        loadUi(r"UI_Design\MainSignup.ui", self)

        self.signin_btn_blue.clicked.connect(self.sign_in)
        self.signup_btn_blue.clicked.connect(self.sql_signup)
        self.eye_img.clicked.connect(self.eye_event)
        self.fb_btn.clicked.connect(self.facebook)
        self.insta_btn.clicked.connect(self.instagram)
        self.twitter_btn.clicked.connect(self.twitter)

        self.eye_img.setIcon(QIcon(r"icons\eye-on_icon.png"))
        self.show_visible =False

    def sign_in(self):
        window = Login()
        widget.addWidget(window)
        widget.setCurrentIndex(widget.currentIndex() + 1)

    def eye_event(self):
        if not self.show_visible:
            self.pass_.setEchoMode(QtWidgets.QLineEdit.Normal)
            self.show_visible = True
            self.eye_img.setIcon(QIcon(r"icons\eye-off_icon.png"))
        else:
            self.pass_.setEchoMode(QtWidgets.QLineEdit.Password)
            self.show_visible = False
            self.eye_img.setIcon(QIcon(r"icons\eye-on_icon.png"))

    def facebook(self):
        web.open('www.facebook.com')

    def instagram(self):
        web.open('www.instagram.com')

    def twitter(self):
        web.open('www.twitter.com')

    #pymysql for signup database logic starts from here
    def sql_signup(self):
        if self.user.text()=="" or self.email.text()=="" or self.pass_.text()=="":
            QtWidgets.QMessageBox.warning(self, 'WARNING..', "            All fields must be required!!             ")
        else:
            my_database = mysql.connector.connect(host='localhost',user='root',password='root#123_',database='myapp')
            my_cursor = my_database.cursor()
            my_cursor.execute(f"SELECT * FROM app_data WHERE email='{self.email.text()}'")
            result = my_cursor.fetchone()
            if result != None:
                QtWidgets.QMessageBox.critical(self, 'ACCOUNT INFO', "  User already exists for this email, please try with another ")
                self.user.setText("")
                self.email.setText("")
                self.pass_.setText("")
            else:
                my_cursor.execute("INSERT INTO app_data (username,email,password) VALUES (%s,%s,%s)",(self.user.text(),self.email.text(),self.pass_.text()))
                my_database.commit()
                my_database.close()
                QtWidgets.QMessageBox.information(self, 'ACCOUNT INFO', "            Account Created Successfull!!             ")
                self.user.setText("")
                self.email.setText("")
                self.pass_.setText("")


class F_Password(QDialog):
    def __init__(self):
        QDialog.__init__(self)
        loadUi(r"UI_Design\Forgotton_Password.ui", self)
        self.get_otp.clicked.connect(self.sql_fpass)
        self.reset_btn.clicked.connect(self.reset)
        self.exit_btn.clicked.connect(self.exit)
        self.eye_img.clicked.connect(self.eye_event)
        self.show_visible = False
        self.otp = random.randint(3256, 8456)

    def eye_event(self):
        if not self.show_visible:
            self.new_pass.setEchoMode(QtWidgets.QLineEdit.Normal)
            self.show_visible = True
            self.eye_img.setIcon(QIcon(r"icons\eye-off_icon.png"))
        else:
            self.new_pass.setEchoMode(QtWidgets.QLineEdit.Password)
            self.show_visible = False
            self.eye_img.setIcon(QIcon(r"icons\eye-on_icon.png"))

    def exit(self):
        win = Login()
        widget.addWidget(win)
        widget.setCurrentIndex(widget.currentIndex()+1)

    #pymysql for forgotton password database logic starts from here
    def sql_fpass(self):
        if self.verify_email.text() == '':
            QtWidgets.QMessageBox.warning(self, 'WARNING..', "            Please enter the Email adress             ")
        else:
            my_database = mysql.connector.connect(host='localhost',user='root',password='root#123_',database='myapp')
            my_cursor = my_database.cursor()
            my_cursor.execute(f"SELECT * FROM app_data WHERE email='{self.verify_email.text()}'")
            result = my_cursor.fetchone()
            if result == None:
                QtWidgets.QMessageBox.critical(self, 'ERROR ', "          Please enter the Valid email adress            ")
            else:
                QtWidgets.QMessageBox.information(self, 'OTP ', f"          Your OTP is {self.otp}          ")
                
    def reset(self):
        if self.otp_entry.text == '' or self.new_pass.text() == '':
            QtWidgets.QMessageBox.warning(self, 'WARNING..', "            All fields must be required!!             ")
        else: 
            if self.otp_entry.text() != f"{self.otp}":
                QtWidgets.QMessageBox.critical(self, 'ERROR..', "          Invalid OTP          ")
            else:
                my_database = mysql.connector.connect(host='localhost',user='root',password='root#123_',database='myapp')
                my_cursor = my_database.cursor()
                my_cursor.execute(f"UPDATE app_data SET password='{self.new_pass.text()}' WHERE email='{self.verify_email.text()}'") 
                my_database.commit()
                my_database.close()
                QtWidgets.QMessageBox.information(self, 'ACCOUNT INFO', "          Your Password has been Changed Successfully          ")
                win = Login()
                widget.addWidget(win)
                widget.setCurrentIndex(widget.currentIndex()+1)
                

class Delete_Account(QDialog):
    def __init__(self):
        QDialog.__init__(self)
        loadUi(r"UI_Design\Delete_account.ui", self)
        #self.del_btn.clicked.connect(self.del_acc)
        self.exit_btn.clicked.connect(self.exit)
        self.eye_img.clicked.connect(self.eye_event)
        self.show_visible = False

    def exit(self):
        win = Login()
        widget.addWidget(win)
        widget.setCurrentIndex(widget.currentIndex()+1)


    def eye_event(self):
        if not self.show_visible:
            self.del_pass.setEchoMode(QtWidgets.QLineEdit.Normal)
            self.show_visible = True
            self.eye_img.setIcon(QIcon(r"icons\eye-off_icon.png"))
        else:
            self.del_pass.setEchoMode(QtWidgets.QLineEdit.Password)
            self.show_visible = False
            self.eye_img.setIcon(QIcon(r"icons\eye-on_icon.png"))

    def del_acc(self):
        if self.del_email.text == '' or self.del_pass.text() == '':
            QtWidgets.QMessageBox.warning(self, 'WARNING', "             All fields must be required!!            ")
        else:
            datab = mysql.connector.connect(host="localhost",user="root",password="root#123_",database="myapp")
            curr = datab.cursor()
            curr.execute(f"SELECT * FROM app_data WHERE email='{self.del_email.text()}' and password='{self.del_pass.text()}'")
            ans = curr.fetchone()
            if ans == None:
                QtWidgets.QMessageBox.warning(self, 'WARNING', "             Invalid Email or Password            ")
            else:
                res = QtWidgets.QMessageBox.question(self, 'ACCOUNT INFO', "            Do You Really Want To Delete Your Account??           ",QMessageBox.Yes|QMessageBox.No,QMessageBox.No)
                if res == QMessageBox.Yes:
                    curr.execute(f"DELETE FROM app_data WHERE email='{self.del_email.text()}' and password='{self.del_pass.text()}'")
                    datab.commit()
                    datab.close()
                    QtWidgets.QMessageBox.information(self, 'ACCOUNT INFO', "               Account Deleted Successfull                ")
                    self.exit()
                


if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    root = Login()
    widget = QStackedWidget()
    widget.addWidget(root)
    widget.setFixedHeight(500)
    widget.setFixedWidth(900)
    widget.show()
    sys.exit(app.exec_())
