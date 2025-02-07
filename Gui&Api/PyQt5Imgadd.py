#intro doing a window in pyqt5
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow,QLabel
from PyQt5.QtGui import QPixmap


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Basic GUI Window")
        #self.setGeometry(x,y,width,height)
        self.setGeometry(700,200,700,700)
        
        label=QLabel(self)
        label.setGeometry(0,0,700,700)

        pixmap=QPixmap("Gui&Api\\Icon.jpg")
        label.setPixmap(pixmap)

        #scale image
        label.setScaledContents(True)

        #to move the image
        #label.setGeometry(0,0,label.width(),label.height())
        label.setGeometry(self.width()-label.width(),
                          self.height()-label.height(),
                          label.width(),label.height())
        
        #For centering  self.width()-label.width()//2

def main():
    #passing the arg allows pyqt to process command lines 
    app = QApplication(sys.argv)
    window= MainWindow()
    window.show()
    #waits for user input and handles events
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()