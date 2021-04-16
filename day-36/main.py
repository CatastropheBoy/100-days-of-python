import requests
from datetime import datetime
from alpha_vantage.timeseries import TimeSeries
from twilio.rest import Client
from twilio.rest.api.v2010.account import message



STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"

## STEP 1: Use https://www.alphavantage.co
# When STOCK price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").

alphav_key= "PLACEHOLDER"

ts= TimeSeries(alphav_key, output_format="pandas")
data = ts.get_daily(STOCK)
yesterday_close = data[0]["4. close"][1]
day_before_close = data[0]["4. close"][2]
price_change = abs(yesterday_close - day_before_close) / yesterday_close * 100
if price_change > 5:
    news_endpoint = "https://newsapi.org/v2/everything"
    news_api_key = "PLACEHOLDER"
    news_params = {
        "qInTitle": COMPANY_NAME,
        "pageSize": 3,
        "apiKey": news_api_key
    }

    news_resp = requests.get(news_endpoint, params=news_params)
    news_data = news_resp.json()["articles"]

    account_sid = "ACfb5127ee0fb81c3d8bbdc9f1d7b47ccb"
    auth_token = "PLACEHOLDER"
    for article in range(len(news_data)):

        client = Client(account_sid, auth_token)
        message = client.messages \
                    .create(
                            body=f"{STOCK}: {price_change}\nHeadline: {news_data[article]['title']}\nBrief: {news_data[article]['description']}",
                            from_='+13218061994',
                            to='+14156225197'
                    )