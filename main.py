import os
import random
import pandas

import datetime as dt

now = dt.datetime.now()
# print(f"now: {now}")
# print(f"now.year: {now.year}")
# print(f"now.month: {now.month}")
# print(f"now.day: {now.day}")
# print(f"now.hour: {now.hour}")
# print(f"now.minute: {now.minute}")
# print(f"now.second: {now.second}")
# print(f"now.date(): {now.date()}")
# print(f"now.time(): {now.time()}")
#
# birthday = dt.datetime(year=1990, month=1, day=1)
# print(f"birthday: {birthday}")

# with open('quotes.txt') as file:
#     quotes = file.readlines()
#
# quote = random.choice(quotes)
# with open('form.txt', 'w') as file:
#     file.write(quote)
#
# current_weekday = now.weekday()
#
# week_days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
# current_weekday = week_days[current_weekday]

current_month = now.month
current_day = now.day

data = pandas.read_csv("birthdays.csv")
all_birthdays = data.to_dict(orient="records")

for birthday in all_birthdays:
    if birthday["month"] == current_month and birthday["day"] == current_day:
        name = birthday['name']
        email = birthday['email']
        with open('letter.txt') as file:
            letter = file.read()
            letter = letter.replace("[NAME]", name)
        with open('form.txt', 'w') as file:
            file.write(letter)
        command = f"mutt -s 'Subject ' {email} < form.txt"
        os.system(command)

