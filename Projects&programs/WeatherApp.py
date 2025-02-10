#A weather application using PyQt5
import sys
import requests
from PyQt5.QtWidgets import QApplication,QWidget,QLabel,QLineEdit,QPushButton,QVBoxLayout
from PyQt5.QtCore import Qt
from dotenv import load_dotenv
import os


dotenv_path = ".env"
load_dotenv()

class WeatherApplication(QWidget):

     #constructor and initializations
    def __init__(self):
        super().__init__()
        self.city_label = QLabel("Enter the Desired City",self)
        self.city_input = QLineEdit(self)
        self.get_weather_button=QPushButton("Getting the weather",self)
        #alt 0176 for degree
        self.temp_label = QLabel(self)
        self.emoji = QLabel(self)
        self.description_label= QLabel(self)


        self.initUI()
     #Overall UI methood
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

        #CSS here
        self.setStyleSheet("""
                         QWidget {
                              background: qlineargradient(x1:0, y1:0, x2:1, y2:1, 
                              stop:0 #74ebd5, stop:1 #ACB6E5); /* Gradient sky blue */
                           }
                         QLabel, QPushButton{
                                font-family: Arial;
                                   
                           }

                         QLabel#city_label{
                                font-size: 20px;
                                font-style: italic;
                                font-weight: bold;
                                color: #00008B;   
                           }
                         QLineEdit#city_input{
                                font-size: 30px;
                                background-color: #FFFFFFCC;
                                border-radius: 10px;
                                padding: 5px;
                                border: 2px solid black;
                           
                           }
                         QPushButton{
                                font-size: 20px;
                                font-weight: bold;       
                                background-color: #00008B;
                                border-radius: 10px;
                                padding: 10px;
                                color:#FFFAF0;
                                border: 2px solid black;
                           }
                         QPushButton:hover {
                                background-color: #4682B4;
                           }
                         QLabel#temp_label{
                                font-size: 65px;
                                color: #00008B;
                           }
                         QLabel#emoji{
                                font-size: 100px;
                                font-family: Segoe UI emoji; 
                           }
                         QLabel#description_label{
                                font-size: 45px;
                                color:  #00008B;
                           }
                       
                           """)
        #Connection made for on click of the button
        self.get_weather_button.clicked.connect(self.get_weather)                  

    def get_weather(self):
          #Using Personal Api key for data retrieval .env file
          city=self.city_input.text()
          api_key = os.getenv("API_KEY")
          if not api_key:
               print("An issue occured with the api key not found.")
               return

          url= f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}"
          
          #Exception handling in try catch
          try:
               response = requests.get(url)
               #raises exception if any http errors
               response.raise_for_status()
               data=response.json()
               if data["cod"]==200:
                    self.display_weather(data)
          except requests.exceptions.HTTPError as http_error:
               match response.status_code:
                    case 400:
                         self.display_err("Client side error occured")
                    case 401:
                         self.display_err("Client side error occured\n unauthorized access")  
                    case 402:
                         self.display_err("Client side error occured\n  payment is needed")   
                    case 403:
                         self.display_err("Client side error occured\n  necessary perms not had")
                    case 404:
                         self.display_err("Client side error occured\n  request not found")
                    case 500:
                         self.display_err("Server side\n  internal error occured")
                    case 501:
                         self.display_err("Server side internal error\n  occured not implemented")
                    case 502:
                         self.display_err("Server side internal error\n  occured BAD GATEWAY")
                    case 503:
                         self.display_err("Server side internal error\n  its down panic")
                    case 504:
                         self.display_err("Server side err timeout")
                    case _:
                         self.display_err("Some HTTP error happened\n http_error")

          except requests.exceptions.ConnectionError:
               self.display_err("Connection error has been lost\n Check your wifi")
          except requests.exceptions.Timeout:
               self.display_err("Timeout error \n your request timed")
          except requests.exceptions.TooManyRedirects:
               self.display_err("Too many redirects error \n Check URL")    
          except requests.exceptions.RequestException as req_error:
               self.display_err(f"Request Error: \n {req_error}")    
     #error displaying method
    def display_err(self,msg):
          self.temp_label.setStyleSheet("font-size:20px;")
          self.temp_label.setText(msg)
          #clear msg when getting an error so doesnt re-appear
          self.emoji.clear()
          self.description_label.clear()
     #Displaying the weather itself
    def display_weather(self,data):
          self.temp_label.setStyleSheet("font-size:45px;")
          temprature_data= data["main"]["temp"]
          real_temp=temprature_data-273.15
          wid=data["weather"][0]["id"]
          weather_description=data["weather"][0]["description"]

          
          self.temp_label.setText(f"{real_temp:.0f}°C")
          self.emoji.setText(self.get_w_emoji(wid))

          self.description_label.setText(weather_description)

     #Codes by temperature per Openweather
    def get_w_emoji(self,wid):
         if wid >= 200 and wid <=232:
              return "⛈️"
         elif 300<=wid<=321:
              return"🌤️"
         elif 500<=wid<=531:
              return"🌧️"
         elif 600<=wid<=622:
              return"❄️"
         elif 701<=wid<=741:
              return"🌫️"
         elif wid==762:
              return"🌋"
         elif wid==771:
              return"💨"
         elif wid==781:
              return"🌪️"
         elif wid==800:
              return"☀️"
         elif 801 <= wid <=804:
              return"☁️"
         else:
              return"🥷"


if __name__ == "__main__":
    app = QApplication(sys.argv)
    wApp = WeatherApplication()
    wApp.show()
    #method to start event loop of main app and handle other events mouse clicks etc
    sys.exit(app.exec_())