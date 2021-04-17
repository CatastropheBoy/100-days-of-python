import requests
import smtplib
from bs4 import BeautifulSoup

headers = {
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.128 Safari/537.36",
    "Accept-Language":"en-US,en;q=0.9"
}

url = "https://smile.amazon.com/Instant-Pot-Plus-60-Programmable/dp/B08PQ2KWHS/"

resp = requests.get(url, headers=headers)
soup = BeautifulSoup(resp.text, "html.parser")

price = float(soup.find(name="span", id="newBuyBoxPrice").getText()[1::])
target = 100

if price <= target:
    g_email = "rynoqa7@gmail.com"
    g_pass = "Silence0!"
    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()
        connection.login(user=g_email, password=g_pass)
        connection.sendmail(
            from_addr=g_email, 
            to_addrs="adoubtfullogic@gmail.com", 
            msg=f"Subject: Instant Pot Price at target!\n\n The instant pot is priced below ${price} \n{url}"
        )