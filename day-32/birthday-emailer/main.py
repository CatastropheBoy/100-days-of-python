import datetime as dt
import random
import pandas
import os
import smtplib

##################### Extra Hard Starting Project ######################

now = dt.datetime.now()

df = pandas.read_csv("./birthdays.csv")
birthdays = df.to_dict(orient="records")
for birthday in birthdays:
    if birthday['month'] == now.month and birthday['day'] == now.day:
        random_letter = random.choice(os.listdir("./letter_templates"))
        with open(f"./letter_templates/{random_letter}") as f:
            letter = f.read()
        letter = letter.replace("[NAME]", birthday['name'])

        with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
            g_email = "rynoqa7@gmail.com"
            g_pass = "Silence0!"
            connection.starttls()
            connection.login(user=g_email, password=g_pass)
            connection.sendmail(
                from_addr=g_email, 
                to_addrs=birthday['email'], 
                msg=f"Subject: Happy Birthday!\n\n {letter}"
            )
