import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel
from PyQt5.QtGui import QIcon, QPixmap 
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setGeometry(460,550,1000,500)   # parameters 0,0 -> top left corner position , 500,500 -> width , height .
        label = QLabel(self)
        label.setGeometry(0,0,500,250)
        pixmap = QPixmap(r"PYQT5\levi_acremen.jpg")
        label.setPixmap(pixmap)
        label.setScaledContents(True)
        # label.setGeometry(0,0,label.width(),label.height()) # returns original width , height of label  .
        # label.setGeometry(self.width() - label.width(),0,label.width(),label.height())
        # label.setGeometry(self.width() - label.width(),self.height() - label.height(),label.width(),label.height())
        # label.setGeometry(0,label.height(),label.width(),label.height())
        label.setGeometry((self.width() - label.width())//2,(self.height() - label.height())//2,label.width(),label.height()) 


def main():
    app = QApplication(sys.argv)    # sys.argv -> this allow python pass list of command line arguments .
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()

