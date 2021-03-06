from datetime import date, datetime
from dateutil.relativedelta import relativedelta
import requests
from pprint import pprint

from flight_data import FlightData

class FlightSearch:
    
    def __init__(self, key) -> None:
        self.key = key
        self.endpoint = "tequila-api.kiwi.com/"


    def get_cities(self):
        url = "https://tequila-api.kiwi.com/locations/dump"
        params = {
            "apikey": self.key,
            "location_types": "city"
        }
        return requests.get(url=url, params=params)


    def search_location(self, term):
        url = "https://tequila-api.kiwi.com/locations/query"
        params = {
            "apikey": self.key,
            "term": term
        }
        return requests.get(url=url, params=params).json()


    def search_flights(self, destination):
        now = datetime.now()
        today = now.strftime("%d/%m/%Y")
        six_months_from_today = now + relativedelta(months=6)
        end_date = six_months_from_today.strftime("%d/%m/%Y")
        url = f"{self.endpoint}search"
        headers = {
            "apikey": self.key
        }
        params = {
            "fly_from": "SFO",
            "fly_to": destination,
            "date_from": today,
            "date_to": end_date,
            "nights_in_dst_from": 7,
            "nights_in_dst_to": 28,
            "flight_type": "round",
            "one_for_city": 1,
            "max_stopovers": 0,
            "curr": "GBP"
        }

        response = requests.get(url="https://tequila-api.kiwi.com/v2/search?", headers=headers, params=params)

        try:
            data = response.json()["data"][0]
        except IndexError:

            ##########################
            params["max_stopovers"] = 1
            response = requests.get(
                url="https://tequila-api.kiwi.com/v2/search?",
                headers=headers,
                params=params,
            )
            data = response.json()["data"][0]
            pprint(data)
            flight_data = FlightData(
                price=data["price"],
                origin_city=data["route"][0]["cityFrom"],
                origin_airport=data["route"][0]["flyFrom"],
                destination_city=data["route"][1]["cityTo"],
                destination_airport=data["route"][1]["flyTo"],
                out_date=data["route"][0]["local_departure"].split("T")[0],
                return_date=data["route"][2]["local_departure"].split("T")[0],
                stop_overs=1,
                via_city=data["route"][0]["cityTo"]
            )
            return flight_data
            ###########################
        else:
            flight_data = FlightData(
                price=data["price"],
                origin_city=data["route"][0]["cityFrom"],
                origin_airport=data["route"][0]["flyFrom"],
                destination_city=data["route"][0]["cityTo"],
                destination_airport=data["route"][0]["flyTo"],
                out_date=data["route"][0]["local_departure"].split("T")[0],
                return_date=data["route"][1]["local_departure"].split("T")[0]
            )

            return flight_data
    
    