import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLineEdit,QPushButton

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setGeometry(700,300,500,500)   # parameters 0,0 -> top left corner position , 500,500 -> width , height .
        self.line_edit = QLineEdit(self)    # can also QLineEdit("xyz: ",self)
        self.button = QPushButton("Submit",self)
        self.initUI()

    def initUI(self):
        self.line_edit.setGeometry(10,10,200,40)
        self.line_edit.setStyleSheet("font-size: 25px;"
                                    "font-family: Arial;")
        self.button.setGeometry(210,10,100,40)
        self.button.clicked.connect(self.submit)   
        self.line_edit.setPlaceholderText("Enter your name: ")

    def submit(self):
        text = self.line_edit.text()
        print(f"hello {text}")

def main():
    app = QApplication(sys.argv)    # sys.argv -> this allow python pass list of command line arguments .
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()



