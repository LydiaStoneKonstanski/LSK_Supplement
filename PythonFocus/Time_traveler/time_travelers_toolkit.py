from datetime import datetime as dt
from decimal import Decimal
from random import (randint, choice)
import custom_module

current_datetime = dt.now()
current_date = current_datetime.strftime("%Y-%m-%d")
current_time = current_datetime.strftime("%H:%M:%S")

print(f"Welcome, Time Traveler! The current date is {current_date} and the time is {current_time}.\n")

base_cost = Decimal('1000.00')
target_year = randint(1900, 2200)
current_year = current_datetime.year
year_difference = abs(target_year - current_year)
#I feel like there should be variation in the cost, but there isn't, because that wasn't instructed. C'est la vie
cost_multiplier = Decimal("1.05")
final_cost = base_cost * cost_multiplier

final_cost = final_cost.quantize(Decimal("0.01"))

destinations = ["Ancient Egypt", "Elizabethan England", "Pre-Columbian Central America", "Cowboy Bebop", "The Triassic Period", "Skynet"]
destination = choice(destinations)

message = custom_module.generate_time_travel_message(target_year, destination, final_cost)

print(message)