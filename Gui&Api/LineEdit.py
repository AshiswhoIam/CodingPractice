import sys
from PyQt5.QtWidgets import QApplication, QMainWindow,QLineEdit,QPushButton



class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Basic GUI Window Learning CheckBox")
        self.setGeometry(700,200,700,700)
        self.line_edit= QLineEdit(self)
        self.button= QPushButton("Submit",self)
        self.initUI()

    def initUI(self):
        self.line_edit.setGeometry(10,10,200,40)
        self.line_edit.setStyleSheet(
                           "font-size: 20px;"
                           "font-family: Arial;"
                           "padding:10px;"
                           )
        self.button.setGeometry(210,10,100,40)
        self.button.setStyleSheet(
                           "font-size: 20px;"
                           "font-family: Arial;"
                           "padding:10px;"
                           )
        self.button.clicked.connect(self.submit)
        self.line_edit.setPlaceholderText("Enter Your name")
    
    def submit(self):
        text=self.line_edit.text()
        print(f"hello {text}")

        


def main():
    app = QApplication(sys.argv)
    window= MainWindow()
    window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()