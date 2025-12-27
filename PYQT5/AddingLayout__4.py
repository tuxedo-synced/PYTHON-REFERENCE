import sys
from PyQt5.QtWidgets import (QApplication, QMainWindow, QLabel,
                            QWidget, QVBoxLayout, QHBoxLayout, QGridLayout)

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setGeometry(460,550,1000,500)   # parameters 0,0 -> top left corner position , 500,500 -> width , height .
        self.initUI()
    def initUI(self):
        central_widget = QWidget()    # widget object created
        self.setCentralWidget(central_widget)   # the widget created is added to main window
        
        label1 = QLabel("#1",self)
        label2 = QLabel("#2",self)
        label3 = QLabel("#3",self)
        label4 = QLabel("#4",self)
        label5 = QLabel("#5",self)

        label1.setStyleSheet("background-color: red;")
        label2.setStyleSheet("background-color: yellow;")
        label3.setStyleSheet("background-color: blue;")
        label4.setStyleSheet("background-color: green;")
        label5.setStyleSheet("background-color: purple;")
        
        # vbox = QVBoxLayout()    # for horizontal use QVBoxLayout .

        # vbox.addWidget(label1)
        # vbox.addWidget(label2)
        # vbox.addWidget(label3)
        # vbox.addWidget(label4)
        # vbox.addWidget(label5)

        # central_widget.setLayout(vbox)

        # grid = QGridLayout()

        # grid.addWidget(label1,0,0) # label_variable , row , coloumn 
        # grid.addWidget(label2,3,3)      
        # grid.addWidget(label3,0,2)      
        # grid.addWidget(label4,1,0)      
        # grid.addWidget(label5,1,2)     

        # central_widget.setLayout(grid) 
    
def main():
    app = QApplication(sys.argv)    # sys.argv -> this allow python pass list of command line arguments .
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()



