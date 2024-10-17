import os
import random

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

with open('quotes.txt') as file:
    quotes = file.readlines()

quote = random.choice(quotes)
with open('form.txt', 'w') as file:
    file.write(quote)

current_weekday = now.weekday()

week_days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
current_weekday = week_days[current_weekday]

command = f"mutt -s 'Subject \"{current_weekday}\"' seriiburduja@gmail.com < form.txt"
# os.system(command)

