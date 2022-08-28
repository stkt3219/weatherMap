import requests
import json
import datetime

user_id = 'sthom317'
user_apiid = 'b9ed65aa5dc84906c55ad92dc85670a2'

zipcode = '30025'
country_code = 'us'

# api call
url = "http://api.openweathermap.org/data/2.5/weather?zip=" + zipcode + "," + country_code + "&appid=" + user_apiid + "&units=imperial"

# get method of requests, returns response obj
response = requests.get(url)
j = response.json()

if j['cod'] != "404":
    i = j['main']

    temp = i["temp"]
    pressure = i["pressure"]

    k = j["wind"]

    wind_speed = k["speed"]
    wind_direct = k["deg"]

    print("Name:            KSU")
    print("\nCurrent Temperature: "+str(temp)+" degrees Fahrenheit ")
    print("\nAtmospheric Pressure: "+str(pressure)+" hPa")
    print("\nWind Speed: "+str(wind_speed)+" mph")
    print("\nWind Direction: "+str(wind_direct))
    print("\nTime of Report: "+str(datetime.datetime.now()))






