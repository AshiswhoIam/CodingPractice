#intro doing a window in pyqt5
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow,QCheckBox
from PyQt5.QtCore import Qt


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Basic GUI Window Learning CheckBox")
        self.setGeometry(700,200,700,700)
        #first arg txt of box
        self.checkbox = QCheckBox("Is it raining today?",self)
        self.initUI()

    def initUI(self):
        self.checkbox.setGeometry(10,0,500,100)
        self.checkbox.setStyleSheet("font-size: 40px;"
                                    "font-family: Arial;")
        self.checkbox.setChecked(False)
        self.checkbox.stateChanged.connect(self.checkbox_change)
    
    def checkbox_change(self,state):
        #state val 2, un ->0
        #print(state)

        if state == Qt.Checked: 
            print("It is raining.!")
        else: 
            print("it is not raining.")

def main():
    app = QApplication(sys.argv)
    window= MainWindow()
    window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()