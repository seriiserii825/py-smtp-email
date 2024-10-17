# import os
#
# command = f"mutt -s 'Subject here' seriiburduja@gmail.com < form.txt"
# os.system(command)

import datetime as dt

now = dt.datetime.now()
print(f"now: {now}")
print(f"now.year: {now.year}")
print(f"now.month: {now.month}")
print(f"now.day: {now.day}")
print(f"now.hour: {now.hour}")
print(f"now.minute: {now.minute}")
print(f"now.second: {now.second}")
print(f"now.date(): {now.date()}")
print(f"now.time(): {now.time()}")

birthday = dt.datetime(year=1990, month=1, day=1)
print(f"birthday: {birthday}")


