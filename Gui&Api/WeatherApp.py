import sys
import requests
from PyQt5.QtWidgets import QApplication,QWidget,QLabel,QLineEdit,QPushButton,QVBoxLayout

from PyQt5.QtCore import Qt

class WeatherApplication(QWidget):
    def __init__(self):
        super().__init__()
        self.city_label = QLabel("Enter the desired city",self)
        self.city_input = QLineEdit(self)
        self.get_weather_button=QPushButton("Getting the weather",self)
        #alt 0176 for degree
        self.temp_label = QLabel("70°F",self)
        self.emoji = QLabel("☀️",self)
        self.description_label= QLabel("Sunny",self)


        self.initUI()

    def initUI(self):
        self.setWindowTitle("Weather Application Program")
        vbox = QVBoxLayout()
        vbox.addWidget(self.city_label)
        vbox.addWidget(self.city_input)
        vbox.addWidget(self.get_weather_button)
        vbox.addWidget(self.temp_label)
        vbox.addWidget(self.emoji)
        vbox.addWidget(self.description_label)

        self.setLayout(vbox)

        self.city_label.setAlignment(Qt.AlignCenter)
        self.city_input.setAlignment(Qt.AlignCenter)
        self.temp_label.setAlignment(Qt.AlignCenter)
        self.emoji.setAlignment(Qt.AlignCenter)
        self.description_label.setAlignment(Qt.AlignCenter)

        self.city_label.setObjectName("city_label")
        self.city_input.setObjectName("city_input")
        self.temp_label.setObjectName("temp_label")
        self.get_weather_button.setObjectName("get_weather_button")
        self.emoji.setObjectName("emoji")
        self.description_label.setObjectName("description_label")

        self.setStyleSheet("""
                           
                           
                           
                           
                           
                           
                           
                           
                           
                           
                           
                           
                           """)



if __name__ == "__main__":
    app = QApplication(sys.argv)
    wApp = WeatherApplication()
    wApp.show()
    #method to start event loop of main app and handle other events mouse clicks etc
    sys.exit(app.exec_())