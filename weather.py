import sys
import requests
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QLineEdit, QVBoxLayout
from PyQt5.QtCore import Qt
import winsound
from dotenv import load_dotenv
import os

class WeatherApp(QWidget):
  def __init__(self):
    super().__init__()
    self.city_label = QLabel("Enter city name: ", self)
    self.city_input = QLineEdit(self)
    self.get_weather_button = QPushButton("Get Weather", self)
    self.temperature_label = QLabel(self)
    self.emoji_label = QLabel(self)
    self.description_label = QLabel(self)
    self.initUI()

  def initUI(self):
    self.setWindowTitle("Weather App")

    vbox = QVBoxLayout()
    vbox.addWidget(self.city_label)
    vbox.addWidget(self.city_input)
    vbox.addWidget(self.get_weather_button)
    vbox.addWidget(self.temperature_label)
    vbox.addWidget(self.emoji_label)
    vbox.addWidget(self.description_label)

    self.setLayout(vbox)

    self.city_label.setAlignment(Qt.AlignCenter)
    self.city_input.setAlignment(Qt.AlignCenter)
    self.temperature_label.setAlignment(Qt.AlignCenter)
    self.emoji_label.setAlignment(Qt.AlignCenter)
    self.description_label.setAlignment(Qt.AlignCenter)

    self.city_label.setObjectName("label")
    self.city_input.setObjectName("input")
    self.get_weather_button.setObjectName("button")
    self.temperature_label.setObjectName("temperature")
    self.emoji_label.setObjectName("emoji")
    self.description_label.setObjectName("description")

    self.setStyleSheet("""
        QLabel, QPushButton{font-family: calibri;}
        QLabel#label{font-size: 40px;
                     font-style: italic;}
        QLineEdit#input{font-size: 30px;}
        QPushButton#button{font-size: 27px;
                           font-weight: bold;}
        QLabel#temperature{font-size: 75px}
        QLabel#emoji{font-size: 100px;
                     font-family: Segoe UI emoji;}
        QLabel#description{font-size: 50px}
                        """)
    
    self.get_weather_button.clicked.connect(self.get_weather)
    
  def get_weather(self):
    winsound.Beep(1000, 200) 
    load_dotenv()
    api_key = os.getenv("OPENWEATHER_API_KEY")
    city = self.city_input.text()
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}"

    try:
      response = requests.get(url)
      response.raise_for_status()
      data = response.json()
      print(data)
      if data["cod"] == 200:
        self.display_weather(data)

    except requests.exceptions.HTTPError as http_error:
      match response.status_code:
        case 400:
          self.display_error("Bad Request:\nPlease check your input")
        case 401:
          self.display_error("Unauthorized Access:\nInvalid API key")
        case 403:
          self.display_error("Forbidden:\nAccess is denied")
        case 404:
          self.display_error("Not Found:\nCity not found")
        case 500:
          self.display_error("Internal Server Error:\nPlease try again later")
        case 502:
          self.display_error("Bad Gateway:\nInvalid response from server")
        case 503:
          self.display_error("Service Unavaliable:\nServer is down")
        case 504:
          self.display_error("Gateway Timeout:\nNo reponse from the server")
        case _:
          self.display_error(f"HTTP Error Occured:\n{http_error}")
    except requests.exceptions.ConnectionError:
      self.display_error("Connect Error:\nCheck your internet connection")
    except requests.exceptions.Timeout:
      self.display_error("Timeout Error:\nThe request timed out")
    except requests.exceptions.TooManyRedirects:
      self.display_error("Too Many Redirects:\nCheck the URL")
    except requests.exceptions.RequestException as req_error:
      self.display_error(f"Request Error:\n{req_error}")

  def display_error(self, message):
    self.temperature_label.setStyleSheet("font-size: 30px;")
    self.temperature_label.setText(message)
    self.emoji_label.clear()
    self.description_label.clear()

  def display_weather(self, data):
    self.temperature_label.setStyleSheet("font-size: 75px;")
    temperature_k = data["main"]["temp"]
    temperature_c = temperature_k - 273
    self.temperature_label.setText(f"{temperature_c:.0f}℃")

    weather_description = data["weather"][0]["description"]
    self.description_label.setText(weather_description)

    weather_id = data["weather"][0]["id"]
    self.emoji_label.setText(self.get_emoji(weather_id))

  @staticmethod
  def get_emoji(weather_id):
    if 200 <= weather_id <= 232:
      return "⛈"
    elif 300 <= weather_id <= 321:
      return "🌦"
    elif 500 <= weather_id <= 531:
      return "🌧"
    elif 600 <= weather_id <= 622:
      return "❄"
    elif 701 <= weather_id <= 741:
      return "🌫"
    elif weather_id == 762:
      return "🌋"
    elif weather_id == 771:
      return "💨"
    elif weather_id == 781:
      return "🌪"
    elif weather_id == 800:
      return "☀"
    elif 801 <= weather_id <= 804:
      return "☁"
    else:
      return ""

if __name__ == "__main__":
  app = QApplication(sys.argv)
  weather_app = WeatherApp()
  weather_app.show()
  sys.exit(app.exec_())