def trip_welcome():
  # Indented code is part of the function body
  print("Welcome to Tripcademy!")
  print("Let's get you to your destination.")

# Unindented code below is not part of the function body and changes the execution flow
print("Woah, look at the weather outside! Don't walk, take the train!")

trip_welcome()

#Output:
# Woah, look at the weather outside! Don't walk, take the train!
# Welcome to Tripcademy!
# Let's get you to your destination.

'''Changing out arguments'''
def generate_trip_instructions(location):
  print(f'Looks like you are planning a trip to visit {location}.')
  print(f'You can use the public subway system to get to {location}.')

# generate_trip_instructions('Central Park')

generate_trip_instructions('Grand Central Station')


'''Using positional arguments'''
def calculate_expenses(plane_ticket_price, car_rental_rate, hotel_rate, trip_time):
    car_rental_total = car_rental_rate * trip_time
    # hotel_coupon = 10
    # hotel_total = (hotel_rate * trip_time) - hotel_coupon
    hotel_total = (hotel_rate * trip_time) - 10
    trip_total = car_rental_total + hotel_total + plane_ticket_price

    return trip_total


print(calculate_expenses(200, 100, 100, 5))

'''Three types of arguments: 
In Python, there are 3 different types of arguments we can give a function.

Positional arguments: arguments that can be called by their position in the function definition.

Keyword arguments: arguments that can be called by their name.

Default arguments: arguments that are given default values.'''

#Above uses Positional arguments.
#Keyword args example, where the definition is in the argument:
# def calculate_taxi_price(rate=0.5, discount=10, miles_to_travel=100):

#Default arguments example, where a default is given, and the values could override or assume the default.
#def calculate_taxi_price(miles_to_travel, rate, discount = 10):
  #print(miles_to_travel * rate - discount )
# Using the default value of 10 for discount.
#calculate_taxi_price(10, 0.5)

# Overwriting the default value of 10 with 20
#calculate_taxi_price(10, 0.5, 20)

def trip_planner(first_destination, second_destination, final_destination = "Codecademy HQ"):
  print('Here is what your trip will look like!')
  print(f'First, we will stop in {first_destination}, then {second_destination}, and lastly {final_destination}.')

#With positional arguments
trip_planner('France', 'Germany', 'Denmark')

trip_planner('Denmark', 'France', 'Germany')

#With Keyword argumants
trip_planner(first_destination = "Iceland", final_destination = "Germany", second_destination = "India")

#With Default arguments
trip_planner('Brooklyn', 'Queens')



'''Built in functions'''
destination_name = "Venkatanarasimharajuvaripeta"
# Built-in function: len()
length_of_destination = len(destination_name)

# Built-in function: print()
print(length_of_destination)

tshirt_price = 9.75
shorts_price = 15.50
mug_price = 5.99
poster_price = 2.00

max_price = max(tshirt_price, shorts_price, mug_price, poster_price)

min_price = min(tshirt_price, shorts_price, mug_price, poster_price)

print(max_price)
print(min_price)

rounded_price = round(tshirt_price, 1)
print(rounded_price)

'''Scope of variables'''
favorite_locations = "Paris, Norway, Iceland"
def print_count_locations():
    print("There are 3 locations")
def show_favorite_locations():
    print("Your favorite locations are: " + favorite_locations)
print_count_locations()
show_favorite_locations()

current_budget = 3500.75
shirt_expense = 9

def print_remaining_budget(budget):
  print("Your remaining budget is: $" + str(budget))

print_remaining_budget(current_budget)

def deduct_expense(budget, expense):
  return(budget - expense)

new_budget_after_shirt = deduct_expense(current_budget, shirt_expense)

print_remaining_budget(new_budget_after_shirt)


def top_tourist_locations_italy():
    first = "Rome"
    second = "Venice"
    third = "Florence"
    return first, second, third

most_popular1, most_popular2, most_popular3 = top_tourist_locations_italy()

print(most_popular1)
print(most_popular2)
print(most_popular3)

#Output:
# Rome
# Venice
# Florence


