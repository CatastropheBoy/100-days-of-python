from data_manager import DataManager
from flight_search import FlightSearch
from notification_manager import NotificationManager
from flight_data import FlightData

search_api_key = "PLACEHOLDER"
flight_search = FlightSearch(search_api_key)

sheet_url = "https://api.sheety.co/ad1184f211462eda0938cd4bf95b6561/flightDeals/prices"
sheet_token = "PLACEHOLDER"
sheet = DataManager(sheet_url, sheet_token)
data = sheet.get_sheet_data()
# data.fill_city_codes(flight_search)


account_sid = "ACfb5127ee0fb81c3d8bbdc9f1d7b47ccb"
twilio_token = "PLACEHOLDER"
notifier = NotificationManager(account_sid, twilio_token)

for row in data["prices"]:
            search = flight_search.search_flights(row["iataCode"])
            try:
                if search.price < row["lowestPrice"]:
                    message = f"The lowest price is ${search.price} to fly from OAK to {row['iataCode']} from {search.out_date} to {search.return_date}"
                    print(notifier.send_message(message))
            except AttributeError:
                print("No flight found for this destination.")


