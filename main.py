import os
import random
import pandas
import datetime as dt

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

# import datetime as dt
#
# now = dt.datetime.now()
# current_month = now.month
# current_day = now.day
#
# data = pandas.read_csv("birthdays.csv")
# all_birthdays = data.to_dict(orient="records")
#
# for birthday in all_birthdays:
#     if birthday["month"] == current_month and birthday["day"] == current_day:
#         name = birthday['name']
#         email = birthday['email']
#         with open('letter.txt') as file:
#             letter = file.read()
#             letter = letter.replace("[NAME]", name)
#         with open('form.txt', 'w') as file:
#             file.write(letter)
#         command = f"mutt -s 'Subject ' {email} < form.txt"
#         os.system(command)
#
