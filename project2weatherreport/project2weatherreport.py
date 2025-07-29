
import requests as req 
import win32com.client as win
import json


city = input("Enter city: ")
url = f"http://api.weatherapi.com/v1/current.json?key=eb16634fa28347c69fa143944241612&q={city}"
r = req.get(url)
data = json.loads(r.text)

# Check if 'current' key exists
if "current" in data:
    print("temperature in celsius:")
    print(data["current"]["temp_c"])
    print("\n")
    print("temperature in fahrenheit:")
    print(data["current"]["temp_f"])
    print("\n")

else:
    print("Error fetching weather data:")
    print(data.get("error", {}).get("message", "Unknown error."))
