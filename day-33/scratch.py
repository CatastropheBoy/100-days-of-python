import requests

resp = requests.get(url="http://api.open-notify.org/iss-now.json")

resp.raise_for_status()
longitude = resp.json()["iss_position"]["longitude"]
latitude = resp.json()["iss_position"]["latitude"]
iss_position = (longitude, latitude)
print(iss_position)