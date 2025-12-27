import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QCheckBox
from PyQt5.QtCore import Qt
# QtCore module contains non Qt classes relavent to PyQt5 
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setGeometry(700,300,500,500)   # parameters 0,0 -> top left corner position , 500,500 -> width , height .
        self.checkbox = QCheckBox("Do you like food", self)
        self.initUI()

    def initUI(self):
        self.checkbox.setGeometry(10,0,500,100)
        self.checkbox.setStyleSheet("font-size: 50px;"
                                    "font-family: Arial;")
        # self.checkbox.setChecked(True)  # setting checkbox to True before and allowing option to user
        # self.checkbox.setChecked(False)  # setting checkbox to False before and allowing option to user
        self.checkbox.stateChanged.connect(self.checkbox_changed)
    def checkbox_changed(self, state):
        # print(state)    # state =>  0 -> unchecked , 2 -> checked
        # if state == 2:
        #     print("You like food")
        # (or)
        if state == Qt.Checked:
            print("You like food")
        else:
            print("You do not like food")
    
def main():
    app = QApplication(sys.argv)    # sys.argv -> this allow python pass list of command line arguments .
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()



