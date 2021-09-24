#pip install PyQt5
from PyQt5 import QtWidgets, QtCore, QtGui
from PyQt5.QtWidgets import QMainWindow, QApplication
from PyQt5.QtGui import QCursor, QIcon
import sys


class MyCalculator(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.setFixedSize(400, 650)
        self.setWindowTitle("Calculator")
        self.setStyleSheet("background-color: #202020;")

        self.label_wel = QtWidgets.QLabel("<b>WELCOME</b>", self)
        self.label_wel.setGeometry(15, 10, 300, 60)
        self.label_wel.setStyleSheet("color: #E0E0E0;" +
        "font-size: 40px;" +
        "font-family: Ariel;")
        self.label1_quote = QtWidgets.QLabel("<h5>Focus On Your Work..</h5>", self)
        self.label1_quote.setGeometry(20, 60, 300, 30)
        self.label1_quote.setStyleSheet("color: #E0E0E0;" +
        "font-size: 20px;" +
        "font-family: Ariel;")

        #Result
        self.lab = QtWidgets.QLabel(self) 
        self.lab.setGeometry(40, 190, 300, 70)
        self.lab.setWordWrap(True)
        self.lab.setStyleSheet("background-color: #202020;" +
        "color: #E0E0E0;" +
        "font-size: 40px;")
        self.lab.setAlignment(QtCore.Qt.AlignRight)
        

        #Buttons
        b1 = QtWidgets.QPushButton(self)
        b1.setGeometry(130, 270, 50, 50)
        b1.setStyleSheet("border-radius: 25px;" +
        "background-color: #C0C0C0;" +
        "font-size: 17px;")
        b1.setIcon(QIcon("icons\delete_icon.png"))
        b1.setToolTip("Clear all digits")
        b1.setCursor(QCursor(QtCore.Qt.PointingHandCursor))
        b1.clicked.connect(self.clear)

        b2 = QtWidgets.QPushButton(self)
        b2.setGeometry(210, 270, 50, 50)
        b2.setStyleSheet("border-radius: 25px;" +
        "background-color: #C0C0C0;")
        b2.setIcon(QIcon("icons\clear_icon.png"))
        b2.setToolTip("Clear digit by digit")
        b2.setCursor(QCursor(QtCore.Qt.PointingHandCursor))
        b2.clicked.connect(self.delete)

        b3 = QtWidgets.QPushButton("%", self)
        b3.setGeometry(210, 530, 50, 50)
        b3.setStyleSheet("border-radius: 25px;" +
        "background-color: #E0E0E0;" +
        "font-size: 17px;")
        b3.setCursor(QCursor(QtCore.Qt.PointingHandCursor))
        b3.clicked.connect(self.btn_mod)

        b4 = QtWidgets.QPushButton("+", self)
        b4.setGeometry(290, 270, 50, 50)
        b4.setStyleSheet("border-radius: 25px;" +
        "background-color: orange;" +
        "font-size: 17px;")
        b4.setCursor(QCursor(QtCore.Qt.PointingHandCursor))
        b4.clicked.connect(self.btn_plus)

        b5 = QtWidgets.QPushButton("7", self)
        b5.setGeometry(50, 335, 50, 50)
        b5.setStyleSheet("border-radius: 25px;" +
        "background-color: #E0E0E0;" +
        "font-size: 17px;")
        b5.setCursor(QCursor(QtCore.Qt.PointingHandCursor))
        b5.clicked.connect(self.btn_7)

        b6 = QtWidgets.QPushButton("8", self)
        b6.setGeometry(130, 335, 50, 50)
        b6.setStyleSheet("border-radius: 25px;" +
        "background-color: #E0E0E0;" +
        "font-size: 17px;")
        b6.setCursor(QCursor(QtCore.Qt.PointingHandCursor))
        b6.clicked.connect(self.btn_8)

        b7 = QtWidgets.QPushButton("9", self)
        b7.setGeometry(210, 335, 50, 50)
        b7.setStyleSheet("border-radius: 25px;" +
        "background-color: #E0E0E0;" +
        "font-size: 17px;")
        b7.setCursor(QCursor(QtCore.Qt.PointingHandCursor))
        b7.clicked.connect(self.btn_9)

        b8 = QtWidgets.QPushButton("-", self)
        b8.setGeometry(290, 335, 50, 50)
        b8.setStyleSheet("border-radius: 25px;" +
        "background-color: orange;" +
        "font-size: 18px;")
        b8.setCursor(QCursor(QtCore.Qt.PointingHandCursor))
        b8.clicked.connect(self.btn_minus)

        b9 = QtWidgets.QPushButton("4", self)
        b9.setGeometry(50, 400, 50, 50)
        b9.setStyleSheet("border-radius: 25px;" +
        "background-color: #E0E0E0;" +
        "font-size: 17px;")
        b9.setCursor(QCursor(QtCore.Qt.PointingHandCursor))
        b9.clicked.connect(self.btn_4)

        b10 = QtWidgets.QPushButton("5", self)
        b10.setGeometry(130, 400, 50, 50)
        b10.setStyleSheet("border-radius: 25px;" +
        "background-color: #E0E0E0;" +
        "font-size: 17px;")
        b10.setCursor(QCursor(QtCore.Qt.PointingHandCursor))
        b10.clicked.connect(self.btn_5)

        b11 = QtWidgets.QPushButton("6", self)
        b11.setGeometry(210, 400, 50, 50)
        b11.setStyleSheet("border-radius: 25px;" +
        "background-color: #E0E0E0;" +
        "font-size: 17px;")
        b11.setCursor(QCursor(QtCore.Qt.PointingHandCursor))
        b11.clicked.connect(self.btn_6)

        b12 = QtWidgets.QPushButton("/", self)
        b12.setGeometry(290, 400, 50, 50)
        b12.setStyleSheet("border-radius: 25px;" +
        "background-color: orange;" +
        "font-size: 17px;")
        b12.setCursor(QCursor(QtCore.Qt.PointingHandCursor))
        b12.clicked.connect(self.btn_div)

        b13 = QtWidgets.QPushButton("1", self)
        b13.setGeometry(50, 465, 50, 50)
        b13.setStyleSheet("border-radius: 25px;" +
        "background-color: #E0E0E0;" +
        "font-size: 17px;")
        b13.setCursor(QCursor(QtCore.Qt.PointingHandCursor))
        b13.clicked.connect(self.btn_1)

        b14 = QtWidgets.QPushButton("2", self)
        b14.setGeometry(130, 465, 50, 50)
        b14.setStyleSheet("border-radius: 25px;" +
        "background-color: #E0E0E0;" +
        "font-size: 17px;")
        b14.setCursor(QCursor(QtCore.Qt.PointingHandCursor))
        b14.clicked.connect(self.btn_2)

        b15 = QtWidgets.QPushButton("3", self)
        b15.setGeometry(210, 465, 50, 50)
        b15.setStyleSheet("border-radius: 25px;" +
        "background-color: #E0E0E0;" +
        "font-size: 17px;")
        b15.setCursor(QCursor(QtCore.Qt.PointingHandCursor))
        b15.clicked.connect(self.btn_3)

        b16 = QtWidgets.QPushButton("X", self)
        b16.setGeometry(290, 465, 50, 50)
        b16.setStyleSheet("border-radius: 25px;" +
        "background-color: orange;" +
        "font-size: 17px;")
        b16.setCursor(QCursor(QtCore.Qt.PointingHandCursor))
        b16.clicked.connect(self.btn_mul)

        b17 = QtWidgets.QPushButton(".", self)
        b17.setGeometry(50, 530, 50, 50)
        b17.setStyleSheet("border-radius: 25px;" +
        "background-color: #E0E0E0;" +
        "font-size:18px;")
        b17.setCursor(QCursor(QtCore.Qt.PointingHandCursor))
        b17.clicked.connect(self.btn_point)

        b18 = QtWidgets.QPushButton("0", self)
        b18.setGeometry(130, 530, 50, 50)
        b18.setStyleSheet("border-radius: 25px;" +
        "background-color: #E0E0E0;" +
        "font-size: 17px;")
        b18.setCursor(QCursor(QtCore.Qt.PointingHandCursor))
        b18.clicked.connect(self.btn_0)

        b19 = QtWidgets.QPushButton(self)
        b19.setGeometry(50, 270, 50, 50)
        b19.setStyleSheet("border-radius: 25px;" +
        "background-color: #C0C0C0;")
        b19.setIcon(QIcon("icons\logout_icon.png"))
        b19.setToolTip("Exit Button")
        b19.setCursor(QCursor(QtCore.Qt.PointingHandCursor))
        b19.clicked.connect(self.fac)

        b20 = QtWidgets.QPushButton("=", self)
        b20.setGeometry(290, 530, 50, 50)
        b20.setStyleSheet("border-radius: 25px;" +
        "background-color: orange;" +
        "font-size: 18px;")
        b20.setCursor(QCursor(QtCore.Qt.PointingHandCursor))
        b20.clicked.connect(self.equals)

        #Designer
        kiran = QtWidgets.QLabel("<h3>designed by</h3>", self)
        kiran.setGeometry(150, 600, 200, 20)
        kiran.setStyleSheet("color: #615F5F")
        nm = QtWidgets.QLabel("KIRANKILVA", self)
        nm.setGeometry(165, 625, 100, 10)
        nm.setStyleSheet("color: #4A4747")

    #Buttons function
    def btn_1(self):
        text = self.lab.text()
        self.lab.setText(text + "1")
    def btn_2(self):
        text = self.lab.text()
        self.lab.setText(text + "2")
    def btn_3(self):
        text = self.lab.text()
        self.lab.setText(text + "3")
    def btn_4(self):
        text = self.lab.text()
        self.lab.setText(text + "4")
    def btn_5(self):
        text = self.lab.text()
        self.lab.setText(text + "5")
    def btn_6(self):
        text = self.lab.text()
        self.lab.setText(text + "6")
    def btn_7(self):
        text = self.lab.text()
        self.lab.setText(text + "7")
    def btn_8(self):
        text = self.lab.text()
        self.lab.setText(text + "8")
    def btn_9(self):
        text = self.lab.text()
        self.lab.setText(text + "9")
    def btn_0(self):
        text = self.lab.text()
        self.lab.setText(text + "0")
    def btn_plus(self):
        text = self.lab.text()
        self.lab.setText(text + "+")
    def btn_minus(self):
        text = self.lab.text()
        self.lab.setText(text + "-")
    def btn_mul(self):
        text = self.lab.text()
        self.lab.setText(text + "*")
    def btn_div(self):
        text = self.lab.text()
        self.lab.setText(text + "/")
    def btn_point(self):
        text = self.lab.text()
        self.lab.setText(text + ".")
    def btn_mod(self):
        text = self.lab.text()
        self.lab.setText(text + "%")
    def clear(self):
        self.lab.setText("")
    def fac(self):
        self.close()
    def equals(self):
        answer = self.lab.text()
        try:
            self.lab.setText(str(eval(answer)))
        except:
            self.lab.setText("Error")
    def delete(self):
        text = self.lab.text()
        self.lab.setText(text[:len(text)-1])

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    win = MyCalculator()
    win.show()
    sys.exit(app.exec_())
