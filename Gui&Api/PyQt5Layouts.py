#intro doing a window in pyqt5
import sys
from PyQt5.QtWidgets import (QApplication, QMainWindow,QLabel,QWidget,QVBoxLayout,QHBoxLayout,QGridLayout)



class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Basic GUI Window")
        self.setGeometry(700,200,700,700)

        self.initUI()

    def initUI(self):
        central_widget=QWidget()
        self.setCentralWidget(central_widget)

        label1=QLabel("#1")
        label2=QLabel("#2")
        label3=QLabel("#3")
        label4=QLabel("#4")
        label5=QLabel("#5")

        label1.setStyleSheet("background-color: red;")
        label2.setStyleSheet("background-color: yellow;")
        label3.setStyleSheet("background-color: green;")
        label4.setStyleSheet("background-color: blue;")
        label5.setStyleSheet("background-color: pink;")

        vbox= QVBoxLayout()

        vbox.addWidget(label1)
        vbox.addWidget(label2)
        vbox.addWidget(label3)
        vbox.addWidget(label4)
        vbox.addWidget(label5)

        central_widget.setLayout(vbox)

        #For horizontal 
        #hbox= QHBoxLayout()
        #hbox.addWidget(label1)
        #central_widget.setLayout(hbox)

        #can also use grid
        #grid= QHBoxLayout()
        #grid.addWidget(label1,0,0)
        #grid.addWidget(label2,0,1)
        #grid.addWidget(label3,1,0)
        #central_widget.setLayout(grid)


def main():
    app = QApplication(sys.argv)
    window= MainWindow()
    window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()