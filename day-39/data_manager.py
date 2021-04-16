import requests

from flight_search import FlightSearch

class DataManager:
    #This class is responsible for talking to the Google Sheet.
    def __init__(self, sheet, token):
        self.sheet = sheet
        self.token = token
        self.token_header = {"Authorization": f"Bearer {self.token}"}
        self.data = None

    
    def get_sheet_data(self):
        resp = requests.get(url=self.sheet, headers=self.token_header)
        resp.raise_for_status()
        self.data = resp.json()
        return self.data

    def fill_city_codes(self, flight_search):
        if self.data == None:
            self.get_sheet_data()
        for row in self.data["prices"]:
            if row["iataCode"] == "":
                search = flight_search.search_location(row["city"])
                
                params = {
                    "price":{
                        "iataCode": search["locations"][0]["code"]
                    }
                }
                requests.put(url=f"https://api.sheety.co/ad1184f211462eda0938cd4bf95b6561/flightDeals/prices/{row['id']}", json=params, headers=self.token_header)

