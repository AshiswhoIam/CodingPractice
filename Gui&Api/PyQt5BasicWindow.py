#intro doing a window in pyqt5
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow,QLabel
from PyQt5.QtGui import QIcon
from PyQt5.QtGui import QFont
from PyQt5.QtCore import Qt

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Basic GUI Window")
        #self.setGeometry(x,y,width,height)
        self.setGeometry(700,200,700,700)
        self.setWindowIcon(QIcon("Gui&Api\\Icon.jpg"))

        #Labels
        label= QLabel("Hello",self)
        label.setFont(QFont("Arial",30))
        label.setGeometry(0,0,500,100)

        #adding css like properties
        label.setStyleSheet("color: #10e36b;" 
                            "background-color: #898ce8;"
                            "font-weight: bold;"
                            "font-style: italic;"
                            "text-decoration: underline;")
        
        #txt align

        #label.setAlignment(Qt.AlignTop)
        #label.setAlignment(Qt.AlignBottom)
        #label.setAlignment(Qt.AlignVCenter)
        
        #label.setAlignment(Qt.AlignRight)
        #label.setAlignment(Qt.AlignHCenter)
        #label.setAlignment(Qt.AlignLeft)

        #combine both
        #label.setAlignment(Qt.AlignHCenter | Qt.AlignTop)
        #or
        label.setAlignment(Qt.AlignCenter)


def main():
    #passing the arg allows pyqt to process command lines 
    app = QApplication(sys.argv)
    window= MainWindow()
    window.show()
    #waits for user input and handles events
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()