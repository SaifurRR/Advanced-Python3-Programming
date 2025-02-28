from decimal import Decimal
from random import randint, choice
import datetime as dt
import custom_module
import pytz

pst_time=pytz.timezone("America/Los_Angeles")
date = dt.date.today()
time = dt.datetime.now(pst_time).time()
print("today's date: {0}".format(date))
print("time now: {0}".format(time))

#time travel cost
base_cost = Decimal('1000.00')
cost_multiplier = Decimal('1000.00')
travel_time = int((dt.timedelta(days = 3*365).days)/365)
total_cost = base_cost+ (cost_multiplier * travel_time)
print(f'total travel cost: ${round(total_cost): .2f}')
#random_year
random_year = randint(2025, 2045)
#random_destinations
destinations = ['Dubai', 'Qatar', 'Australia', 'Canada']
random_destination = choice(destinations)
print(random_destination)

msg = custom_module.generate_time_travel_message(random_year, random_destination, total_cost)
print(msg)


