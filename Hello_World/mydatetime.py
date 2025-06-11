from datetime import *
import pytz
import time

time.sleep(1)
n = datetime.now()
stars = '*'

print(n)
print(f"Today date is {date.today()}")
print(f"current time is {n.strftime("%I:%M:%S %p")}")

print(stars.ljust(59, '*'))

def time_est(my_country, my_city):
    utc = pytz.utc
    my_time = datetime.now(utc)
    time_e = pytz.timezone(f'{my_country}/{my_city}')
    time_n = my_time.astimezone(time_e)
    time_now = time_n.strftime("%I:%M:%S %p")

    return  time_now

country = input("Enter your country: ")
city= input("Enter your country: ")


print(time_est(country, city))

#Time zones
"""import pytz

for tz in pytz.all_timezones:
    print(tz)"""