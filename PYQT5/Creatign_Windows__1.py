import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtGui import QIcon
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("My first GUI")
        self.setGeometry(480,100,960,850)   # parameters 0,0 -> top left corner position , 500,500 -> width , height .
        self.setWindowIcon(QIcon("PYQT5/levi_acremen.jpg"))
    
def main():
    app = QApplication(sys.argv)    # sys.argv -> this allow python pass list of command line arguments .
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()

#   my screen resolution --> 1920x1080


