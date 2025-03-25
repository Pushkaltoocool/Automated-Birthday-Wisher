import pandas as pd
import datetime as dt
import smtplib
import random

my_email = "your-email"
password = "your-email-app-password" 

letter_number = random.choice(range(1,4))

with open(f"./letter_templates/letter_{letter_number}.txt", "r") as letter:
    letter_to_email = letter.readlines()


now = dt.datetime.now()
day = now.day
month = now.month

birthdays = pd.read_csv("birthdays.csv").to_dict(orient="records")


for birthday in birthdays:
    if day == birthday["day"] and month == birthday["month"]:
        birthday_guy = birthday["name"]
        delimiter = " "
        final_text = delimiter.join(letter_to_email).replace("[NAME]", birthday_guy )
        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(user=my_email, password=password)
            connection.sendmail(
                from_addr=my_email,
                to_addrs=birthday["email"],
                msg=(f"Subject:Happy Birthday {birthday_guy} \n\n {final_text}")
            )




