import requests
from datetime import datetime

APP_ID = "APP_ID"
API_KEY = "API_KEY"

SHEETY_TOKEN = "SHEETY_TOKEN"

def post_workout():

    workout = input("Describe your workout: ")

    headers = {
        "x-app-id": APP_ID,
        "x-app-key": API_KEY
    }

    params = {
        "query": workout,
        "gender": "male",
        "weight_kg": 130,
        "age": 34
    }

    endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"

    resp = requests.post(url=endpoint, headers=headers, json=params)
    print(resp.text)
    return resp.json()


def add_workout():
    workout = post_workout()
    now = datetime.now()
    current_date = now.strftime("%Y/%m/%d")
    current_time = now.strftime("%H:%M")

    url = 'https://api.sheety.co/ad1184f211462eda0938cd4bf95b6561/workoutTracking/workouts'

    headers = {
        "Authorization": f"Bearer {SHEETY_TOKEN}"
    }

    params = {
        "workout":{
            "date": current_date,
            "time": current_time,
            "exercise": workout["exercises"][0]["name"].title(),
            "duration": workout["exercises"][0]["duration_min"],
            "calories": workout["exercises"][0]["nf_calories"]
        }
    }
    requests.post(url=url, json=params, headers=headers)


if __name__ == "__main__":
    add_workout()
