import requests

#creating a class that helps to get the information
#the class contains the function that retrieves data from the website


class CityInfo:
  def __init__(self, name, latitude, longitude, units="metric"):
	  self.ApiKey = input("Enter your API_KEY...")
	  self.Name = name
	  self.Lat = latitude
	  self.Lon = longitude
	  self.units = units
	  self.GetData() #grabs the get data function every time we instantiate a CityInfo object

  def GetData(self):
    try:
      response = requests.get(f"https://api.openweathermap.org/data/2.5/weather?units={self.units}&lat={self.Lat}&lon={self.Lon}&appid={self.ApiKey}")
      print(response.json())
    except Exception as e:
      print(e)
      print("No internet access")

    self.response_json = response.json()
    self.Temp = self.response_json["main"]["temp"]
    self.Low = self.response_json["main"]["temp_min"]
    self.High = self.response_json["main"]["temp_max"]

  def PrintData(self):
    print(f"Today's weather in {self.Name} is: {self.Temp}\n Today's Low is: {self.Low}\nToday's High is: {self.High}")

Bloem = CityInfo("bloemfontein", -29.087217, 26.154898)
Bloem.PrintData()
