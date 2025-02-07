import sys
from PyQt5.QtWidgets import QApplication, QMainWindow,QLabel,QPushButton


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Basic GUI Window")
        self.setGeometry(700,200,700,700)
        self.button= QPushButton("Click Here!",self)
        self.label=QLabel("hello",self)
        self.initUI()
    #need self because else its local
    def initUI(self):
        self.button.setGeometry(250, 250, 200, 100)
        self.button.setStyleSheet("font-size: 40px;")
        self.button.clicked.connect(self.on_click)
        self.label.setGeometry(300, 150, 100, 100)
        self.label.setStyleSheet("font-size: 40px;")
  

    def on_click(self):
        print("Button Clicked!")
        self.button.setText("Clicked")
        self.button.setDisabled(True)
        self.label.setText("Bye!!")


def main():
    app = QApplication(sys.argv)
    window= MainWindow()
    window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()