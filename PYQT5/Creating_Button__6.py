import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QLabel

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setGeometry(700,300,500,500)   # parameters 0,0 -> top left corner position , 500,500 -> width , height .
        self.button = QPushButton("Click me!",self)  # object of QPushButton class
        self.lable = QLabel("Hello!" , self)
        self.initUI()

    def initUI(self):
        self.button.setGeometry(150,200,200,100)
        self.button.setStyleSheet("font-size: 30px;")
        self.button.clicked.connect(self.on_click)
        self.lable.setGeometry(150,300,200,100)
        self.lable.setStyleSheet("font-size: 50px;")


    def on_click(self):
        print("Button is clicked!")
        self.button.setText("Clicked!")
        self.button.setDisabled(True)
        self.lable.setText("Good Job!!!")
    
def main():
    app = QApplication(sys.argv)    # sys.argv -> this allow python pass list of command line arguments .
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()



