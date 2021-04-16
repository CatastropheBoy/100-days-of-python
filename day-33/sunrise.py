import requests
from datetime import datetime

MY_LAT = 37.728359
MY_LONG = -122.158607

parameters = {
    "lat": MY_LAT,
    "lng": MY_LONG,
    "formatted": 0
}

resp = requests.get(url="https://api.sunrise-sunset.org/json", params=parameters)
resp.raise_for_status()
data = resp.json()

time_now = datetime.now()
print(time_now.hour)
sunrise = data["results"]["sunrise"].split("T")[1].split(":")[0]
sunset = data["results"]["sunset"].split("T")[1].split(":")[0]
