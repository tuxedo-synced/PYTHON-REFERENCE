import sys
from PyQt5.QtWidgets import QApplication , QMainWindow , QLabel , QLineEdit , QWidget
from PyQt5.QtGui import QIcon , QFont

class Calculator(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setGeometry(460,200,480,480)
        self.setWindowTitle("CALCULATOR")
        self.setWindowIcon(QIcon(r"Project_On_PyQt5\calculator logo.jpg"))
        self.initUI()
    def initUI(self):
        self.all_clear = QLabel("C",self)
        self.one_side_clear = QLabel("x",self)
        self.plus = QLabel("+",self)
        self.minus = QLabel("-",self)
        self.division = QLabel("/",self)
        self.multiplication = QLabel("*",self)
        self.equals = QLabel("=",self)
        self.one = QLabel("1",self)
        self.two = QLabel("2",self)
        self.three = QLabel("3",self)
        self.four = QLabel("4",self)
        self.five = QLabel("5",self)
        self.six = QLabel("6",self)
        self.seven = QLabel("7",self)
        self.eight = QLabel("8",self)
        self.nine = QLabel("9",self) 
        self.zero = QLabel("0",self) 
        self.zero.setGeometry(0,106,120,96)
        self.all_clear.setGeometry(120,106,120,96)
        self.one_side_clear.setGeometry(240,106,120,96)
        self.plus.setGeometry(360,106,120,96)
        self.one.setGeometry(0,202,120,96)
        self.two.setGeometry(120,202,120,96)
        self.three.setGeometry(240,202,120,96)
        self.minus.setGeometry(360,202,120,96)
        self.four.setGeometry(0,298,120,96)
        self.five.setGeometry(120,298,120,96)
        self.six.setGeometry(240,298,120,96)
        self.multiplication.setGeometry(360,298,120,96)
        self.seven.setGeometry(0,394,120,96)
        self.eight.setGeometry(120,394,120,96)
        self.nine.setGeometry(240,394,120,96)
        self.division.setGeometry(360,394,120,96)
        self.equals.setGeometry(360,0,120,106)


        self.setStyleSheet("""
            QLabel{
                background-color: red;
                qproperty-alignment: AlignCenter;   
            }
            """)
#  qproperty-alignment: AlignCenter; this is used to elign every label created .

def main():
    app = QApplication(sys.argv)
    main_window = Calculator()
    main_window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()