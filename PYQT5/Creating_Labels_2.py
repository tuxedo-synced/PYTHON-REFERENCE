import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel
from PyQt5.QtGui import QIcon,QFont
from PyQt5.QtCore import Qt 
# the Qt class is used for alignmnets .
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("My first GUI")
        self.setGeometry(700,300,500,1500)   # parameters 0,0 -> top left corner position , 500,500 -> width , height .
        self.setWindowIcon(QIcon("PYQT5/levi_acremen.jpg"))
        label = QLabel("Hello",self)
        label.setFont(QFont("Arial",40))
        label.setGeometry(0,0,500,100)
        label.setStyleSheet("color: blue;"
                            "background-color: green;"
                            "font-style: italic;"
                            "text-decoration: underline;"
                            "font-weight: bold;")
        # label.setAlignment(Qt.AlignTop) # vertically top
        # label.setAlignment(Qt.AlignBottom)  # verticlaly bottom
        # label.setAlignment(Qt.AlignVCenter) # vertically center
        # label.setAlignment(Qt.AlignLeft)   # horizontal left
        # label.setAlignment(Qt.AlignRight)   # horizontal Right
        # label.setAlignment(Qt.AlignHCenter) # horizontal center
        # label.setAlignment(Qt.AlignHCenter | Qt.AlignVCenter) # both flags are implemented here .
        # label.setAlignment(Qt.AlignHCenter | Qt.AlignTop) # both flags are implemented here .
        # label.setAlignment(Qt.AlignHCenter | Qt.AlignBottom) # # both flags are implemented here .

    
def main():
    app = QApplication(sys.argv)    # sys.argv -> this allow python pass list of command line arguments .
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()



