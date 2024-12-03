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

def trip_planner_welcome(name):
  print(f'Welcome to tripplanner v1.0 {name}.')

trip_planner_welcome('Lydia')

def estimated_time_rounded(estimated_time):
  rounded_time = round(estimated_time)
  return rounded_time

estimate = estimated_time_rounded(3.5)

def destination_setup(origin, destination, estimated_time, mode_of_transport = 'Car'):

  print(f'Your trip starts off in {origin}')
  print(f'And you are traveling to {destination}.')
  print(f'You will be traveling by {mode_of_transport}')
  print(f'It will take approximately', str(f'{estimated_time}'), 'hours')

destination_setup('Philadelphia', 'Nashville', estimate)

'''Lambda Functions:
Lambda can put a function inside a variable. Lambda functions are most commonly used as arguments 
to higher-order functions such as map(), 
filter(), and sorted(). Higher-order functions are functions that can accept other functions, 
such as lambda functions, as arguments.'''
#lambda [arguments]: [expression]

# Regular function
def square(x):
    return x ** 2

# Lambda function
square_lambda = lambda x: x ** 2

# Lambda function to print a name
#greeting = lambda name: f"Hello, {name}!"
#print(greeting("Alice"))  # Output: Hello, Alice!

numbers = [1, 2, 3, 4, 5]
squared = list(map(lambda x: x ** 2, numbers))
print(squared)  # Output: [1, 4, 9, 16, 25]

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
print(even_numbers)  # Output: [2, 4, 6, 8, 10]


students = [('Alice', 'A', 15), ('Bob', 'B', 12), ('Charlie', 'A', 20)]
sorted_students = sorted(students, key=lambda x: x[2])
print(sorted_students)
# Output: [('Bob', 'B', 12), ('Alice', 'A', 15), ('Charlie', 'A', 20)]

# List of numbers
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Use a lambda function to filter out odd numbers
evens = list(filter(lambda x: x % 2 == 0, numbers))

# Use a lambda function to square each number
squares = list(map(lambda x: x ** 2, numbers))

# Print the results
print("Original numbers:", numbers)
print("Even numbers:", evens)
print("Squared numbers:", squares)

# Try creating your own lambda function!
words = [('brick', 29, 'a'),('goggles', 12, 'o'),('apple', 8, 'e'),('produce', 5, 'x')]
sorted_words = sorted(words, key=lambda x:x[2])

print(sorted_words)

'''map()
Readability: map() can make our code more concise and easier to read, 
especially for simple operations on iterables.

Memory Efficiency: map() returns an iterator, which means it doesn’t 
create the entire result list in memory at once. This can be beneficial when working with large datasets.

Functional Programming: map() encourages a functional programming style, 
which can lead to more maintainable and testable code.

Remember that map() returns an iterator. If you need a list, wrap it with list().

USE map() WHEN:

We need to apply a function to every item in an iterable.
We want to transform data without explicitly writing a for loop.
We’re working with large datasets and want to avoid creating intermediate lists.

While map() is powerful, there also are alternatives:

List Comprehensions: Often more readable for simple operations.
doubled = [x * 2 for x in numbers] 

Generator Expressions: Similar to list comprehensions but return an iterator.
doubled = (x * 2 for x in numbers) 

For Loops: More verbose but sometimes clearer for complex operations.
doubled = [] 
for x in numbers: 
   doubled.append(x * 2) '''


def double(x):
    return x * 2
numbers = [1, 2, 3, 4, 5]
doubled_numbers = map(double, numbers)

print(list(doubled_numbers))  # Output: [2, 4, 6, 8, 10]

'''Map() with other built-ins'''
# Converting strings to integers
str_nums = ['1', '2', '3', '4', '5']
int_nums = list(map(int, str_nums))

print(int_nums)  # Output: [1, 2, 3, 4, 5]

# Finding the length of strings
words = ['apple', 'banana', 'cherry']
word_lengths = list(map(len, words))

print(word_lengths)  # Output: [5, 6, 6]

'''Map() with Lambda functions'''
numbers = [1, 2, 3, 4, 5]
doubled = list(map(lambda x: x * 2, numbers))

print(doubled)  # Output: [2, 4, 6, 8, 10]

'''Multiple iterables with map()'''
list1 = [1, 2, 3]
list2 = [10, 20, 30]
result = list(map(lambda x, y: x + y, list1, list2))

print(result)  # Output: [11, 22, 33]

'''Map() to try'''
# Sample list of names
names = ['Alice', 'Bob', 'Charlie', 'David', 'Eve']

# Using map with a lambda function to get the length of each name
name_lengths = list(map(lambda x: len(x), names))

# Using map with a defined function to capitalize each name
def capitalize_name(name):
    return name.upper()

capitalized_names = list(map(capitalize_name, names))

# Print the results
print("Original names:", names)
print("Name lengths:", name_lengths)
print("Capitalized names:", capitalized_names)

'''REVERSE A STRING'''
backward = list(map(lambda name: name[::-1], names))
print(backward)

def f_to_c(f_temp):
  c_temp = (f_temp - 32) * (5/9)
  return c_temp
f100_in_celcius = f_to_c(100)
print(f100_in_celcius)

def c_to_f(c_temp):
  f_temp = c_temp * (9/5) + 32
  return f_temp
c0_in_fahrenheit = c_to_f(0)
print(c0_in_fahrenheit)

# Uncomment this when you reach the "Use the Force" section

train_mass = 22680
train_acceleration = 10
train_distance = 100
bomb_mass = 1

def get_force(mass, acceleration):
  return mass * acceleration

train_force = get_force(train_mass, train_acceleration)

print(train_force)

print(f'The GE train supplies {train_force} Newtons of force')

def get_energy(mass, c = 3*10**8):
  return mass * c**2

bomb_energy = get_energy(bomb_mass)
print(f'A 1kg bomb supplies {bomb_energy} Joules.')

def get_work(mass, acceleration, distance):
  return get_force(mass, acceleration) * distance

train_work = get_work(train_mass, train_acceleration, train_distance)

print(f'The GE train does {train_work} Joules of work over {train_distance} meters.')