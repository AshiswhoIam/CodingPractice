import sys
from PyQt5.QtWidgets import QApplication, QMainWindow,QRadioButton,QButtonGroup

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Basic GUI Window Learning Radiobuttons")
        self.setGeometry(700,200,700,700)
        #radio obj creation
        self.radio1=QRadioButton("Visa",self)
        self.radio2=QRadioButton("MasterCard",self)
        self.radio3=QRadioButton("GiftCards",self)
        self.radio4=QRadioButton("In store",self)
        self.radio5=QRadioButton("Online",self)
        self.button_grp1=QButtonGroup(self)
        self.button_grp2=QButtonGroup(self)
        
        self.initUI()

    def initUI(self):
        self.radio1.setGeometry(0,0,300,50)
        self.radio2.setGeometry(0,50,300,50)
        self.radio3.setGeometry(0,100,300,50)
        self.radio4.setGeometry(0,150,300,50)
        self.radio5.setGeometry(0,200,300,50)

        self.setStyleSheet("QRadioButton{"
                           "font-size: 20px;"
                           "font-family: Arial;"
                           "padding:10px;"
                           "}")
        self.button_grp1.addButton(self.radio1)
        self.button_grp1.addButton(self.radio2)
        self.button_grp1.addButton(self.radio3)
        self.button_grp2.addButton(self.radio4)
        self.button_grp2.addButton(self.radio5)

        self.radio1.toggled.connect(self.radio_buttonchange)
        self.radio2.toggled.connect(self.radio_buttonchange)
        self.radio3.toggled.connect(self.radio_buttonchange)
        self.radio4.toggled.connect(self.radio_buttonchange)
        self.radio5.toggled.connect(self.radio_buttonchange)

    def radio_buttonchange(self):
        storage= self.sender()
        if storage.isChecked():
            print(f"{storage.text()} has been selected")


def main():
    app = QApplication(sys.argv)
    window= MainWindow()
    window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()