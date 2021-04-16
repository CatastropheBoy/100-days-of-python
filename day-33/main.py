from time import sleep, time
import requests
from datetime import datetime
import smtplib


MY_LAT = 37.728359 # Your latitude
MY_LONG = -122.158607 # Your longitude


def iss_near():
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data = response.json()

    iss_latitude = float(data["iss_position"]["latitude"])
    iss_longitude = float(data["iss_position"]["longitude"])

    if MY_LAT - 5 <= iss_latitude <= MY_LAT + 5 and MY_LONG - 5 <= iss_longitude <= MY_LONG + 5:
        return True
    return False


def dark_outside():
    parameters = {
        "lat": MY_LAT,
        "lng": MY_LONG,
        "formatted": 0,
    }

    response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
    response.raise_for_status()
    data = response.json()
    sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])
    time_now = datetime.now().hour
    
    if time_now >= sunset or time_now <= sunrise:
        return True
    return False

while True:
    if iss_near() and dark_outside():
        with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
            g_email = "rynoqa7@gmail.com"
            g_pass = "Silence0!"
            connection.starttls()
            connection.login(user=g_email, password=g_pass)
            connection.sendmail(
                from_addr=g_email, 
                to_addrs="adoubtfullogic@gmail.com", 
                msg=f"Subject: ISS is overhead!\n\n Go outside and look, dingus."
            )
    sleep(60)



        






# Then send me an email to tell me to look up.
# BONUS: run the code every 60 seconds.



