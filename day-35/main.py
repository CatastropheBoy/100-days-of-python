import requests
import os
from twilio.rest import Client
from twilio.rest.api.v2010.account import message
from twilio.http.http_client import TwilioHttpClient


url = 'https://api.openweathermap.org/data/2.5/onecall'
api_key = "PLACEHOLDER"
account_sid = "ACfb5127ee0fb81c3d8bbdc9f1d7b47ccb"
auth_token = "PLACEHOLDER"

params = {
    "lat": 37.728359,
    "lon": -122.158607,
    "exclude": "current,minutely,daily",
    "appid": api_key
}

resp = requests.get(url=url, params=params)
resp.raise_for_status()

weather_data = resp.json()
next_12_hours = [_ for _ in weather_data['hourly'][:12]]

will_rain = False
for hour in next_12_hours:
    condition_code = hour['weather'][0]['id']
    if condition_code < 800:
        will_rain = True

if will_rain:
    proxy_client = TwilioHttpClient()
    proxy_client.session.proxies = {'https' : os.environ['https_proxy']}

    client = Client(account_sid, auth_token, http_client=proxy_client)
    message = client.messages \
                .create(
                     body="It's going to rain today, bring an umbrella. ☔",
                     from_='+13218061994',
                     to='+14156225197'
                 )
    print(message.status)