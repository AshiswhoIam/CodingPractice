#Making a digital clock program with PyQt5
import sys
from PyQt5.QtWidgets import QApplication,QWidget,QLabel,QVBoxLayout
from PyQt5.QtCore import QTimer,QTime,Qt
from PyQt5.QtGui import  QFont,QFontDatabase
class DigitalClock(QWidget):
    def __init__(self):
        super().__init__()
        self.time_label = QLabel(self)
        self.timer = QTimer(self)
        self.initUI()

    def initUI(self):
        self.setWindowTitle("Personal Digital Clock")
        self.setGeometry(700,200,500,200)
        
        vbox=QVBoxLayout()
        #adding laBel to layout manager
        vbox.addWidget(self.time_label)
        self.setLayout(vbox)
        self.time_label.setAlignment(Qt.AlignCenter)

        self.time_label.setStyleSheet("font-size: 100px;"
                                      "color: #4169E1")
        self.setStyleSheet("background-color: black;")


        font_id=QFontDatabase.addApplicationFont("Gui&Api\\Marosdiac.ttf")
        font_fam= QFontDatabase.applicationFontFamilies(font_id)[0]
        this_font=QFont(font_fam,100)
        self.time_label.setFont(this_font)
        #connection slot for updating
        self.timer.timeout.connect(self.auto_time)
        #1000ms
        self.timer.start(1000)

        self.auto_time()
    
    def auto_time(self):
        current_time=QTime.currentTime().toString("hh:mm:ss AP")
        self.time_label.setText(current_time)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    clock=DigitalClock()
    clock.show()
    #method to start event loop of main app and handle other events mouse clicks etc
    sys.exit(app.exec_())
   

