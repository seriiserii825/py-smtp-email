import os
import pandas
import datetime as dt
import smtplib

today = dt.datetime.now()
today_tuple = (today.month, today.day)

data = pandas.read_csv("birthdays.csv")
birthdays_dict = {(row.month, row.day): row for (index, row) in data.iterrows()}

if today_tuple in birthdays_dict:
    birthday = birthdays_dict[today_tuple]
    name = birthday['name']
    email = birthday['email']
    with open('letter.txt') as file:
        letter = file.read()
        letter = letter.replace("[NAME]", name)
    with open('form.txt', 'w') as file:
        file.write(letter)
    command = f"mutt -s 'Subject ' {email} < form.txt"
    os.system(command)

my_email = "seriiburduja@gmail.com"
password = "" #password from google app https://myaccount.google.com/apppasswords
connection = smtplib.SMTP("smtp.gmail.com")
connection.starttls()
connection.login(user=my_email, password=password)
connection.sendmail(from_addr=my_email, to_addrs="seriiburduja@yandex.ru", msg="Subject:Hello\n\nThis is the body of my email")
connection.close()


