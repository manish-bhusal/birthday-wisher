import pandas
import datetime as dt
import smtplib
import random

MY_EMAIL = "myemail@gmail.com"
PASSWORD = "**********"

now = dt.datetime.now()
month = now.month
day = now.day

data = pandas.read_csv("birthdays.csv")

random_from_123 = random.randint(1, 3)

for index, row in data.iterrows():
    if row.month == month and row.day == day:
        with open(f"letter_templates/letter_{random_from_123}.txt") as birthday_file:
            wishes = birthday_file.read()
            wishes = wishes.replace("[NAME]", f"{row.naame}")
        with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
            connection.starttls()
            connection.login(user=MY_EMAIL, password=PASSWORD)
            connection.sendmail(from_addr=MY_EMAIL, to_addrs=row.email,
                                msg=f"Subject:Birthday Wish\n\n{wishes}")
