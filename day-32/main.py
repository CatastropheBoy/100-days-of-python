import smtplib
import datetime as dt
import random

g_email = "rynoqa7@gmail.com"
g_pass = "Silence0!"
# y_email = "rynoqa@yahoo.com"
# y_pass = "sqiwcfsoxlohcguh"
# y_connection = smtplib.SMTP("smtp.mail.yahoo.com")


with open("quotes.txt") as f:
    quotes = f.readlines()

now = dt.datetime.now()
current_weekday = now.weekday()

if current_weekday == 2:
    quote = random.choice(quotes)
    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()
        connection.login(user=g_email, password=g_pass)
        connection.sendmail(
            from_addr=g_email, 
            to_addrs="rynoqa@yahoo.com", 
            msg=f"Subject: Motivational Quote\n\n {quote}"
        )

