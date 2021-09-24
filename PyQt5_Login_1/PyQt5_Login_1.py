#pip install PyQt5
#pip install pymysql
from PyQt5 import QtWidgets, QtGui, QtCore
from PyQt5.QtWidgets import QDialog, QApplication, QStackedWidget, QWidget
from PyQt5.QtWidgets import QMessageBox
from PyQt5.QtGui import QCursor, QIcon
import random
import pymysql
import sys

class MyWindow(QDialog):
    def __init__(self):
        QDialog.__init__(self)
        self.setFixedSize(400, 650)
        self.setWindowTitle("MY APP")
        self.styleSheet = """
            QLineEdit{
                border-radius: 5px;
                padding: 3px 6px;
                color: black;
                background-color: White;
            }
            QLineEdit:hover{
                border: 3px solid  #1E90FF;
            }
            QLabel{
                color: grey;
                font-size: 15px;
            }
        """
        app.setStyleSheet(self.styleSheet)

        #Background image
        background_image = QtWidgets.QLabel(self)
        background_image.setPixmap(QtGui.QPixmap(r"images\bg.jpg"))
        background_image.setGeometry(0, 0, 400, 650)

        #label
        label1 = QtWidgets.QLabel(self)
        label1.setText("<h5>HELLO</h5>")
        label1.setGeometry(10, 20, 200, 60)
        label1.setStyleSheet("color: white;" +
        "font-size: 55px;")

        label1 = QtWidgets.QLabel(self)
        label1.setText("To Continue Login here..")
        label1.setGeometry(13, 60, 200, 40)
        label1.setStyleSheet("color: white;" +
        "font-size: 15px;")

        #Facebook_button
        fb_btn = QtWidgets.QPushButton(self)
        fb_btn.setText(" Sign in")
        fb_btn.setGeometry(30, 600, 100, 30)
        fb_btn.setIcon(QIcon(r"icons\fb_icon.png"))
        fb_btn.setStyleSheet("*{background-color: #273c75;" +
        "color: white;" +
        "border-radius: 4px;}")
        fb_btn.setCursor(QCursor(QtCore.Qt.PointingHandCursor))
        fb_btn.clicked.connect(self.fb)
        
        #Twitter_button
        twitter_btn = QtWidgets.QPushButton(self)
        twitter_btn.setText(" Sign in")
        twitter_btn.setGeometry(145, 600, 100, 30)
        twitter_btn.setIcon(QIcon(r"icons\Twitter1_icon.png"))
        twitter_btn.setStyleSheet("*{background-color: #00BFFF;" +
        "color: white;" +
        "border-radius: 4px;}" +
        "*:hover{background-color: #1DA1F2;}")
        twitter_btn.setCursor(QCursor(QtCore.Qt.PointingHandCursor))
        twitter_btn.clicked.connect(self.twit)
        
        #Instagram_button
        insta_btn = QtWidgets.QPushButton(self)
        insta_btn.setText(" Sign in")
        insta_btn.setGeometry(260, 600, 100, 30)
        insta_btn.setIcon(QIcon(r"icons\insta_icon.ico"))
        insta_btn.setStyleSheet("*{background-color: #FF3399;" +
        "color: white;" +
        "border-radius: 4px;}" +
        "*:hover{background-color: #FF69B4;}")
        insta_btn.setCursor(QCursor(QtCore.Qt.PointingHandCursor))
        insta_btn.clicked.connect(self.ins)

        #line edit boxes
        l1 = QtWidgets.QLabel("Email Id", self)
        l1.setGeometry(22, 185, 150, 15)
        self.e1 = QtWidgets.QLineEdit(self)
        self.e1.setGeometry(20, 205, 350, 40)

        l2 = QtWidgets.QLabel("Username", self)
        l2.setGeometry(22, 260, 150, 15)
        self.e2 = QtWidgets.QLineEdit(self)
        self.e2.setGeometry(20, 280, 350, 40)

        l3 = QtWidgets.QLabel("Password", self)
        l3.setGeometry(22, 335, 150, 15)
        self.e3 = QtWidgets.QLineEdit(self)
        self.e3.setGeometry(20, 355, 350, 40)
        self.e3.setEchoMode(QtWidgets.QLineEdit.Password)

        #Login button
        login_btn = QtWidgets.QPushButton(self)
        login_btn.setGeometry(20, 470, 350, 40)
        login_btn.setText("Log in")
        login_btn.setStyleSheet("*{background-color: #1E90FF;" +
        "border: 2px #1E90FF;" +
        "border-radius: 6px;" +
        "color: white;" +
        "font-size: 18px;" +
        "font-family: times;}" +
        "*:hover{background-color: #404040;}")
        login_btn.setCursor(QCursor(QtCore.Qt.PointingHandCursor))
        login_btn.clicked.connect(self.login)

        #Forgotton password
        f_password = QtWidgets.QPushButton("forgotton password?", self)
        f_password.setGeometry(240, 405, 130, 20)
        f_password.setStyleSheet("*{background-color: transparent;" +
        "color: white;" +
        "font-size: 14px;}" +
        "*:hover{color: #A9A9A9;}")
        f_password.setCursor(QCursor(QtCore.Qt.PointingHandCursor))
        f_password.clicked.connect(self.password_forgotton)

        #create an account
        line = QtWidgets.QLabel(self)
        line.setText("<hr>")
        line.setGeometry(20, 530, 350, 10)
        acc = QtWidgets.QLabel("Create an account here", self)
        acc.setGeometry(120, 555, 350, 30)
        acc.setStyleSheet("font-size: 15px;" +
        "color: white;")

    def ins(self):       
        insta = InstagramWindow()
        widget.addWidget(insta)
        widget.setCurrentIndex(widget.currentIndex()+1)

    def fb(self):       
        facebook = FacebookWindow()
        widget.addWidget(facebook)
        widget.setCurrentIndex(widget.currentIndex()+1)

    def twit(self):       
        twitter = TwitterWindow()
        widget.addWidget(twitter)
        widget.setCurrentIndex(widget.currentIndex()+1)

    def password_forgotton(self):
        forg = Forgotton_Password()
        widget.addWidget(forg)
        widget.setCurrentIndex(widget.currentIndex()+1)

    def login(self):
        if (self.e1.text() or self.e2.text() or self.e3.text()) =='':
            QtWidgets.QMessageBox.warning(self, "WARNING..", "          All fields must be required            ")
        else:
            data = pymysql.connect(host="localhost",user="root",password="",database="PyQt5")
            cur = data.cursor()
            cur.execute("select * from pyqt5_login where email=%s and username=%s and password=%s",(self.e1.text(),self.e2.text(),self.e3.text()))
            res = cur.fetchone()
            if res == None:
                QtWidgets.QMessageBox.critical(self, "ERROR", "    Incorrect Username or Email or Password    ")
            else:
                self.calc()
                self.e1.setText("")
                self.e2.setText("")
                self.e3.setText("")
            data.close()


class Forgotton_Password(QDialog):
    def __init__(self):
        QDialog.__init__(self)
        self.setFixedSize(400, 650)
        self.setStyleSheet("background-color: white;")
        
        #Image
        self.label = QtWidgets.QLabel(self)
        self.label.setPixmap(QtGui.QPixmap(r'images\password.jpg'))
        self.label.setGeometry(70, 110, 230, 185)

        #Exit Image
        exit_btn = QtWidgets.QPushButton(self)
        exit_btn.setGeometry(330, 20, 50, 50)
        exit_btn.setStyleSheet("*{border-radius: 7px;" +
        "background-color: white;}" +
        "*:hover{background-color: #F5F5F5;}")
        exit_btn.setIcon(QIcon("PyQt5\logout.png"))
        exit_btn.setToolTip("Exit Button")
        exit_btn.setCursor(QCursor(QtCore.Qt.PointingHandCursor))
        exit_btn.clicked.connect(self.gotohome)

        #Title
        self.title = QtWidgets.QLabel('<h2>PASSWORD</h2>', self)
        self.title.setGeometry(10, 5, 300, 60)
        self.title.setStyleSheet("font-size: 30px;" +
        "font-family: times;" +
        "color: gray")
        self.title1 = QtWidgets.QLabel('<h2>Manager</h2>', self)
        self.title1.setGeometry(160, 55, 150, 40)
        self.title1.setStyleSheet("font-size: 20px;" +
        "font-family: times;" +
        "color: darkgray")

        #Line edit boxes and labels
        label1_email = QtWidgets.QLabel('Email ID', self)
        label1_email.setGeometry(22, 290, 150, 15)
        label1_email.setStyleSheet("font-size: 15px;")
        self.email_id = QtWidgets.QLineEdit(self)
        self.email_id.setGeometry(20, 310, 350, 40)
        self.email_id.setStyleSheet("*{border: 2px solid #C0C0C0;" +
        "border-radius: 5px;" +
        "background-color: #F5F5F5;}" +
        "*:hover{border: 2px solid #808080; background-color: white;}")

        label2_username = QtWidgets.QLabel('Username', self)
        label2_username.setGeometry(22, 360, 150, 15)
        label2_username.setStyleSheet("font-size: 15px;")
        self.user_name = QtWidgets.QLineEdit(self)
        self.user_name.setGeometry(20, 380, 350, 40)
        self.user_name.setStyleSheet("*{border: 2px solid #C0C0C0;" +
        "border-radius: 5px;" +
        "background-color: #F5F5F5;}" +
        "*:hover{border: 2px solid #808080; background-color: white;}")

        label3_otp = QtWidgets.QLabel('Enter OTP Here', self)
        label3_otp.setGeometry(22, 430, 150, 15)
        label3_otp.setStyleSheet("font-size: 15px;")

        self.otp = QtWidgets.QLineEdit(self)
        self.otp.setGeometry(20, 450, 170, 40)
        self.otp.setStyleSheet("*{border: 2px solid #C0C0C0;" +
        "border-radius: 5px;" +
        "background-color: #F5F5F5;}" +
        "*:hover{border: 2px solid #808080; background-color: white;}")

        otp_btn = QtWidgets.QPushButton('Send', self)
        otp_btn.setGeometry(230, 450, 130, 40)
        otp_btn.setStyleSheet("*{background-color: #E0E0E0;" +
        "color: #202020;" +
        "font-size: 14px;" +
        "border: 3px solid #808080;" +
        "border-radius: 20px;}" +
        "*:hover{background-color: #808080; color: white;}")
        otp_btn.setCursor(QCursor(QtCore.Qt.PointingHandCursor))
        otp_btn.clicked.connect(self.send_otp)

        label3_newpass = QtWidgets.QLabel('New Password', self)
        label3_newpass.setGeometry(22, 500, 150, 15)
        label3_newpass.setStyleSheet("font-size: 15px;")
        self.newpassword_ = QtWidgets.QLineEdit(self)
        self.newpassword_.setGeometry(20, 520, 350, 40)
        self.newpassword_.setStyleSheet("*{border: 2px solid #C0C0C0;" +
        "border-radius: 5px;" +
        "background-color: #F5F5F5;}" +
        "*:hover{border: 2px solid #808080; background-color: white;}")

        #Next button
        nxt_btn = QtWidgets.QPushButton('RESET PASSWORD' ,self)
        nxt_btn.setGeometry(20, 585, 350, 40)
        nxt_btn.setStyleSheet("*{background-color: #404040;" +
        "color: white;" +
        "border-radius: 5px;" +
        "font-size: 15px;" +
        "font-family: Verdana}" +
        "*:hover{background-color: #606060;}")
        nxt_btn.setCursor(QCursor(QtCore.Qt.PointingHandCursor))
        nxt_btn.clicked.connect(self.reset_function)
        self.show()

        #def random_num(self):
        self.otp_num = random.randint(4512, 8652)
    
    def gotohome(self):
        home = MyWindow()
        widget.addWidget(home)
        widget.setCurrentIndex(widget.currentIndex()+1)

    def send_otp(self):
        if True:
            dbase = pymysql.connect(host="localhost",user="root",password="",database="PyQt5")
            myCursor = dbase.cursor()
            myCursor.execute("select * from pyqt5_login where username=%s and email=%s",(self.user_name.text(),self.email_id.text()))
            ans = myCursor.fetchone()
            if ans == None:
                QtWidgets.QMessageBox.critical(self, 'ERROR', "     Please Enter The Valid Email or Username   ")
                self.email_id.setText("")
                self.user_name.setText("")
            else:
                #self.random_num()
                #print(self.otp_num)
                QtWidgets.QMessageBox.information(self, "OTP VERIFICATION", f"            Your OTP is {self.otp_num}               ")
            dbase.close()
        else:
            pass

    def reset_function(self):
        #self.random_num()
        if self.email_id.text() == "" or self.user_name.text() == "" or self.otp.text() == "" or self.newpassword_.text() == "":
            QtWidgets.QMessageBox.warning(self, 'WARNING', "     All Fields Must Be Required    ")
        else:
            if self.otp.text() == f'{self.otp_num}':           
                d_base = pymysql.connect(host="localhost",user="root",password="",database="PyQt5")
                my_Cursor = d_base.cursor()
                my_Cursor.execute("update pyqt5_login set password=%s where username=%s",(self.newpassword_.text(),self.user_name.text()))
                d_base.commit()
                d_base.close()
                QtWidgets.QMessageBox.information(self, 'PASSWORD MANAGER', "        Password Reset is Successfull!!        ")
                self.otp.setStyleSheet("border: 2px solid #C0C0C0;")
                self.email_id.setText("")
                self.user_name.setText("")
                self.otp.setText("")
                self.newpassword_.setText("")
            else:
                QtWidgets.QMessageBox.critical(self, 'ERROR', "        Invalid OTP        ")
                self.otp.setStyleSheet("border: 2px solid red;")
                self.newpassword_.setText("")
                

class InstagramWindow(QDialog):
    def __init__(self):
        QDialog.__init__(self)
        self.setFixedSize(400, 650)
        #self.setWindowTitle("CREATE AN ACCOUNT")
        self.setStyleSheet("background-color: white;")

        #instagram logo
        insta_logo = QtWidgets.QLabel(self)
        insta_logo.setPixmap(QtGui.QPixmap(r"images/instalogo.png"))
        insta_logo.setGeometry(70, 20, 325, 100)

        #line edit boxes and labels
        username_label = QtWidgets.QLabel('Username', self)
        username_label.setGeometry(22, 177, 150, 20)
        username_label.setStyleSheet("font-size: 15px;")
        self.line1 = QtWidgets.QLineEdit(self)
        self.line1.setGeometry(20, 200, 350, 40)
        self.line1.setStyleSheet("*{border: 2px solid #C0C0C0;" +
        "border-radius: 5px;" +
        "background-color: #F5F5F5;}" +
        "*:hover{border: 2px solid #FF69B4; background-color: white;}")

        email_label = QtWidgets.QLabel('Email Id', self)
        email_label.setGeometry(22, 257, 150, 20)
        email_label.setStyleSheet("font-size: 15px;")
        self.line2 = QtWidgets.QLineEdit(self)
        self.line2.setGeometry(20, 280, 350, 40)
        self.line2.setStyleSheet("*{border: 2px solid #C0C0C0;" +
        "border-radius: 5px;" +
        "background-color: #F5F5F5;}" +
        "*:hover{border: 2px solid #FF69B4; background-color: white;}")

        password_label = QtWidgets.QLabel('Password', self)
        password_label.setGeometry(22, 337, 150, 20)
        password_label.setStyleSheet("font-size: 15px;")
        self.line3 = QtWidgets.QLineEdit(self)
        self.line3.setGeometry(20, 360, 350, 40)
        self.line3.setStyleSheet("*{border: 2px solid #C0C0C0;" +
        "border-radius: 5px;" +
        "background-color: #F5F5F5;}" +
        "*:hover{border: 2px solid #FF69B4; background-color: white;}")

        confirm_label = QtWidgets.QLabel('Verify Password', self)
        confirm_label.setGeometry(22, 417, 150, 20)
        confirm_label.setStyleSheet("font-size: 15px;")
        self.line4 = QtWidgets.QLineEdit(self)
        self.line4.setGeometry(20, 440, 350, 40)
        self.line4.setStyleSheet("*{border: 2px solid #C0C0C0;" +
        "border-radius: 5px;" +
        "background-color: #F5F5F5;}" +
        "*:hover{border: 2px solid #FF69B4; background-color: white;}")

        #push button
        btn = QtWidgets.QPushButton('Create an Account', self)
        btn.setGeometry(20, 550, 350, 40)
        btn.setStyleSheet("*{background-color: #FF3399;;" +
        "border-radius: 5px;" +
        "color: white;" +
        "font-size: 15px;}"
        "*:hover{background-color: #FF69B4;}")
        btn.setCursor(QCursor(QtCore.Qt.PointingHandCursor))
        btn.clicked.connect(self.CreateanAccount)

        exit_btn_1 = QtWidgets.QPushButton("Go to home", self)
        exit_btn_1.setGeometry(150, 605, 90, 20)
        exit_btn_1.setStyleSheet("*{background-color: white;" +
        "border: none;"
        "color: gray;" +
        "font-size: 15px;" +
        "font-family: Verdena;}" +
        "*:hover{color: black;}")
        exit_btn_1.setCursor(QCursor(QtCore.Qt.PointingHandCursor))
        exit_btn_1.clicked.connect(self.home1)
        self.show()

    def home1(self):
        exit1 = MyWindow()
        widget.addWidget(exit1)
        widget.setCurrentIndex(widget.currentIndex()+1)

    def CreateanAccount(self):
        if (self.line1.text() or self.line2.text() or self.line3.text() or self.line4.text()) == '':
            QtWidgets.QMessageBox.warning(self, 'WARNING..', "      All fields must be Required         ")
        elif self.line3.text() == self.line4.text():
            db = pymysql.connect(host="localhost",user="root",password="",database="PyQt5")
            mycur = db.cursor()
            mycur.execute("select * from pyqt5_login where username=%s and email=%s", (self.line1.text(),self.line2.text()))
            result = mycur.fetchone()
            if result != None:
                QtWidgets.QMessageBox.warning(self, "WARNING", "Username or EmailID already exist's , Please try with another")
            else:
                mycur.execute("insert into pyqt5_login (username,email,password) values (%s,%s,%s)",(self.line1.text(),self.line2.text(),self.line3.text()))
                db.commit()
                db.close()
                QtWidgets.QMessageBox.information(self, "Account Info", "   Account Created Successful!!   ")
                self.line1.setText("")
                self.line2.setText("")
                self.line3.setText("")
                self.line4.setText("")
        else:
            QtWidgets.QMessageBox.warning(self, "Account Info", "    Password and verify password din't matched    ")


class FacebookWindow(QDialog):
    def __init__(self):
        QDialog.__init__(self)
        self.setFixedSize(400, 650)
        #self.setWindowTitle("CREATE AN ACCOUNT")
        self.setStyleSheet("background-color: white;")

        #facebook Logo
        self.fb_logo = QtWidgets.QLabel(self)
        self.fb_logo.setPixmap(QtGui.QPixmap(r"images\facebooklogo.png"))
        self.fb_logo.setGeometry(10, 30, 400, 100)

        #line edit boxes and labels
        fb_username_label = QtWidgets.QLabel('Username', self)
        fb_username_label.setGeometry(22, 177, 150, 20)
        fb_username_label.setStyleSheet("font-size: 15px;")
        self.fb_line1 = QtWidgets.QLineEdit(self)
        self.fb_line1.setGeometry(20, 200, 350, 40)
        self.fb_line1.setStyleSheet("*{border: 2px solid #C0C0C0;" +
        "border-radius: 5px;" +
        "background-color: #F5F5F5;}" +
        "*:hover{border: 2px solid #4267B2; background-color: white;}")

        fb_email_label = QtWidgets.QLabel('Email Id', self)
        fb_email_label.setGeometry(22, 257, 150, 20)
        fb_email_label.setStyleSheet("font-size: 15px;")
        self.fb_line2 = QtWidgets.QLineEdit(self)
        self.fb_line2.setGeometry(20, 280, 350, 40)
        self.fb_line2.setStyleSheet("*{border: 2px solid #C0C0C0;" +
        "border-radius: 5px;" +
        "background-color: #F5F5F5;}" +
        "*:hover{border: 2px solid #4267B2; background-color: white;}")

        fb_password_label = QtWidgets.QLabel('Password', self)
        fb_password_label.setGeometry(22, 337, 150, 20)
        fb_password_label.setStyleSheet("font-size: 15px;")
        self.fb_line3 = QtWidgets.QLineEdit(self)
        self.fb_line3.setGeometry(20, 360, 350, 40)
        self.fb_line3.setStyleSheet("*{border: 2px solid #C0C0C0;" +
        "border-radius: 5px;" +
        "background-color: #F5F5F5;}" +
        "*:hover{border: 2px solid #4267B2; background-color: white;}")

        fb_confirm_label = QtWidgets.QLabel('Verify Password', self)
        fb_confirm_label.setGeometry(22, 417, 150, 20)
        fb_confirm_label.setStyleSheet("font-size: 15px;")
        self.fb_line4 = QtWidgets.QLineEdit(self)
        self.fb_line4.setGeometry(20, 440, 350, 40)
        self.fb_line4.setStyleSheet("*{border: 2px solid #C0C0C0;" +
        "border-radius: 5px;" +
        "background-color: #F5F5F5;}" +
        "*:hover{border: 2px solid #4267B2; background-color: white;}")

        #push button
        fb_btn = QtWidgets.QPushButton('Create an Account', self)
        fb_btn.setGeometry(20, 550, 350, 40)
        fb_btn.setStyleSheet("*{background-color: #4267B2;;" +
        "border-radius: 5px;" +
        "color: white;" +
        "font-size: 15px;}"
        "*:hover{background-color: #4169E1;}")
        fb_btn.setCursor(QCursor(QtCore.Qt.PointingHandCursor))
        fb_btn.clicked.connect(self.CreateanfbAccount)

        exit_btn_2 = QtWidgets.QPushButton("Go to home", self)
        exit_btn_2.setGeometry(150, 605, 90, 20)
        exit_btn_2.setStyleSheet("*{background-color: white;" +
        "border: none;"
        "color: gray;" +
        "font-size: 15px;" +
        "font-family: Verdena;}" +
        "*:hover{color: black;}")
        exit_btn_2.setCursor(QCursor(QtCore.Qt.PointingHandCursor))
        exit_btn_2.clicked.connect(self.home2)
        self.show()

    def home2(self):
        exit2 = MyWindow()
        widget.addWidget(exit2)
        widget.setCurrentIndex(widget.currentIndex()+1)

    def CreateanfbAccount(self):
        if (self.fb_line1.text() or self.fb_line2.text() or self.fb_line3.text() or self.fb_line4.text()) == '':
            QtWidgets.QMessageBox.warning(self, 'WARNING..', "      All fields must be Required         ")
        elif self.fb_line3.text() == self.fb_line4.text():
            db = pymysql.connect(host="localhost",user="root",password="",database="PyQt5")
            mycur = db.cursor()
            mycur.execute("select * from pyqt5_login where username=%s and email=%s", (self.fb_line1.text(),self.fb_line2.text()))
            result = mycur.fetchone()
            if result != None:
                QtWidgets.QMessageBox.warning(self, "WARNING", "Username or EmailID already exist's , Please try with another")
            else:
                mycur.execute("insert into pyqt5_login (username,email,password) values (%s,%s,%s)",(self.fb_line1.text(),self.fb_line2.text(),self.fb_line3.text()))
                db.commit()
                db.close()
                QtWidgets.QMessageBox.information(self, "Account Info", "   Account Created Successful!!   ")
                self.fb_line1.setText("")
                self.fb_line2.setText("")
                self.fb_line3.setText("")
                self.fb_line4.setText("")
        else:
            QtWidgets.QMessageBox.warning(self, "Account Info", "    Password and verify password din't matched    ")


class TwitterWindow(QDialog):
    def __init__(self):
        QDialog.__init__(self)
        self.setFixedSize(400, 650)
        #self.setWindowTitle("CREATE AN ACCOUNT")
        self.setStyleSheet("background-color: white;")

        #facebook Logo
        self.twitter_logo = QtWidgets.QLabel(self)
        self.twitter_logo.setPixmap(QtGui.QPixmap(r"images\twitterlogo.png"))
        self.twitter_logo.setGeometry(30, 30, 400, 100)

        #line edit boxes and labels
        twitter_username_label = QtWidgets.QLabel('Username', self)
        twitter_username_label.setGeometry(22, 177, 150, 20)
        twitter_username_label.setStyleSheet("font-size: 15px;")
        self.twitter_line1 = QtWidgets.QLineEdit(self)
        self.twitter_line1.setGeometry(20, 200, 350, 40)
        self.twitter_line1.setStyleSheet("*{border: 2px solid #C0C0C0;" +
        "border-radius: 5px;" +
        "background-color: #F5F5F5;}" +
        "*:hover{border: 2px solid #00BFFF; background-color: white;}")

        twitter_email_label = QtWidgets.QLabel('Email Id', self)
        twitter_email_label.setGeometry(22, 257, 150, 20)
        twitter_email_label.setStyleSheet("font-size: 15px;")
        self.twitter_line2 = QtWidgets.QLineEdit(self)
        self.twitter_line2.setGeometry(20, 280, 350, 40)
        self.twitter_line2.setStyleSheet("*{border: 2px solid #C0C0C0;" +
        "border-radius: 5px;" +
        "background-color: #F5F5F5;}" +
        "*:hover{border: 2px solid #00BFFF; background-color: white;}")

        twitter_password_label = QtWidgets.QLabel('Password', self)
        twitter_password_label.setGeometry(22, 337, 150, 20)
        twitter_password_label.setStyleSheet("font-size: 15px;")
        self.twitter_line3 = QtWidgets.QLineEdit(self)
        self.twitter_line3.setGeometry(20, 360, 350, 40)
        self.twitter_line3.setStyleSheet("*{border: 2px solid #C0C0C0;" +
        "border-radius: 5px;" +
        "background-color: #F5F5F5;}" +
        "*:hover{border: 2px solid #00BFFF; background-color: white;}")

        twitter_confirm_label = QtWidgets.QLabel('Verify Password', self)
        twitter_confirm_label.setGeometry(22, 417, 150, 20)
        twitter_confirm_label.setStyleSheet("font-size: 15px;")
        self.twitter_line4 = QtWidgets.QLineEdit(self)
        self.twitter_line4.setGeometry(20, 440, 350, 40)
        self.twitter_line4.setStyleSheet("*{border: 2px solid #C0C0C0;" +
        "border-radius: 5px;" +
        "background-color: #F5F5F5;}" +
        "*:hover{border: 2px solid #00BFFF; background-color: white;}")

        #push button
        twitter_btn = QtWidgets.QPushButton('Create an Account', self)
        twitter_btn.setGeometry(20, 550, 350, 40)
        twitter_btn.setStyleSheet("*{background-color: #00BFFF;" +
        "border-radius: 5px;" +
        "color: white;" +
        "font-size: 15px;}"
        "*:hover{background-color: #1DA1F2;}")
        twitter_btn.setCursor(QCursor(QtCore.Qt.PointingHandCursor))
        twitter_btn.clicked.connect(self.CreateantwitterAccount)
        
        exit_btn_3 = QtWidgets.QPushButton("Go to home", self)
        exit_btn_3.setGeometry(150, 605, 90, 20)
        exit_btn_3.setStyleSheet("*{background-color: white;" +
        "border: none;"
        "color: gray;" +
        "font-size: 15px;" +
        "font-family: Verdena;}" +
        "*:hover{color: black;}")
        exit_btn_3.setCursor(QCursor(QtCore.Qt.PointingHandCursor))
        exit_btn_3.clicked.connect(self.home3)
        self.show()

    def home3(self):
        exit3 = MyWindow()
        widget.addWidget(exit3)
        widget.setCurrentIndex(widget.currentIndex()+1)

    def CreateantwitterAccount(self):
        if (self.twitter_line1.text() or self.twitter_line2.text() or self.twitter_line3.text() or self.twitter_line4.text()) == '':
            QtWidgets.QMessageBox.warning(self, 'WARNING..', "      All fields must be Required         ")
        elif self.twitter_line3.text() == self.twitter_line4.text():
            db = pymysql.connect(host="localhost",user="root",password="",database="PyQt5")
            mycur = db.cursor()
            mycur.execute("select * from pyqt5_login where username=%s and email=%s", (self.twitter_line1.text(),self.twitter_line2.text()))
            result = mycur.fetchone()
            if result != None:
                QtWidgets.QMessageBox.warning(self, "WARNING", "Username or EmailID already exist's , Please try with another")
            else:
                mycur.execute("insert into pyqt5_login (username,email,password) values (%s,%s,%s)",(self.twitter_line1.text(),self.twitter_line2.text(),self.twitter_line3.text()))
                db.commit()
                db.close()
                QtWidgets.QMessageBox.information(self, "Account Info", "   Account Created Successful!!   ")
                self.twitter_line1.setText("")
                self.twitter_line2.setText("")
                self.twitter_line3.setText("")
                self.twitter_line4.setText("")
        else:
            QtWidgets.QMessageBox.warning(self, "Account Info", "    Password and verify password din't matched    ")



if __name__ == '__main__':
    app = QApplication(sys.argv)
    root = MyWindow()
    widget = QStackedWidget()
    widget.addWidget(root)
    widget.setFixedWidth(400)
    widget.setFixedHeight(650)
    widget.show()
    sys.exit(app.exec_())
