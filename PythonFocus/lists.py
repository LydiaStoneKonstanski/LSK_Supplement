ints_and_strings = [1, 2, 3, "four", "five", "hotdog"]

sam_height_and_testscore = ["Sam", 67, 85.5, True] #list can be any datatype

my_empty_list = [] #empty lists

''''''
append_example = [ 'This', 'is', 'an', 'example']
append_example.append('list')

print(append_example)


'''Using Methods with lists'''
example_list = [1, 2, 3, 4]

#Using Append
example_list.append(5)
# print(example_list)

#Using Remove
example_list.remove(5)
# print(example_list)

'''append'''
orders = ["daisies", "periwinkle"]

print(orders)

orders.append("tulips")
orders.append("roses")

print(orders)

'''Concatenating lists'''
orders = ["daisy", "buttercup", "snapdragon", "gardenia", "lily"]

# Create new orders here:
new_orders = ['lilac', 'iris']

# Combine the two orders lists
orders_combined = orders + new_orders

# To use concatenation instead of .append() method, must be in list.
broken_prices = [5, 3, 4, 5, 4] + [4]

'''When accessing elements of a list, you must use an int as the index. 
If you use a float, you will get an error. 
This can be especially tricky when using division. 
For example print(calls[4/2]) will result in an error, because 4/2 gets evaluated 
to the float 2.0.

To solve this problem, you can force the result of your division to be an int 
by using the int() function. int() takes a number and cuts off the decimal point. 
For example, int(5.9) and int(5.0) will both become 5. 
Therefore, calls[int(4/2)] will result in the same value as calls[2], 
whereas calls[4/2] will result in an error.'''

employees = ["Michael", "Dwight", "Jim", "Pam", "Ryan", "Andy", "Robert"]

#Access 4th employee and save to a variable
employee_four = (employees[3])
print(employee_four)

#index list out of range Index Error

#print(employees[8])

print(employees[6])

'''Retrieving items from lists by index'''

shopping_list = ["eggs", "butter", "milk", "cucumbers", "juice", "cereal"]

last_element = shopping_list[-1] #retrieves the last item

index5_element = shopping_list[5]

print(last_element, index5_element) # in this case, both the same

'''Replacing items from lists by index'''
garden_waitlist = ["Jiho", "Adam", "Sonny", "Alisha"]

#garden_waitlist[1] = "Calla"
garden_waitlist[-3] = "Calla" # negative index works too

print(garden_waitlist)

garden_waitlist[-1] = 'Alex'

print(garden_waitlist)

'''Removing with .remove() method, removing something that doesn't exist'''
order_list = ["Celery", "Orange Juice", "Orange", "Flatbread"]
print(order_list)

order_list.remove("Flatbread")
print(order_list)

new_store_order_list = ["Orange", "Apple", "Mango", "Broccoli", "Mango"]
print(new_store_order_list)

new_store_order_list.remove("Mango")
print(new_store_order_list) #Only removes one of the duplicates

new_store_order_list.remove("Onions")
print(new_store_order_list) #Value Error, onions weren't on the list

'''2D lists, ie lists of lists, grid structure, tic tac toe'''
heights = [["Jenny", 61], ["Alexus", 70], ["Sam", 67], ["Grace", 64]] #Sub-Lists are comma separated

heights[-1] = ['Vik', 68]

print(heights)

ages = [["Aaron", 15],["Dhruti", 16]]

'''Accessing 2D lists'''

heights = [["Noelle", 61], ["Ali", 70], ["Sam", 67]]
#Access the sublist at index 0, and then access the 1st index of that sublist.
noelles_height = heights[0][1]
print(noelles_height)

'''Element	Index
"Noelle"	heights[0][0] 
61	heights[0][1]
"Ali"	heights[1][0]
70	heights[1][1]
"Sam"	heights[2][0]
67	heights[2][1]
'''

class_name_test = [["Jenny", 90], ["Alexus", 85.5], ["Sam", 83], ["Ellie", 101.5]]
print(class_name_test)

sams_score = class_name_test[2][1] #Accessed by overall index in the first bracket, and sub-list index in the second, NOT COMMA SEPARATED
print(sams_score)

ellies_score = class_name_test[-1][-1]# Can use negative indices as well
print(ellies_score)

'''Removing with the .pop() method'''
data_science_topics = ["Machine Learning", "SQL", "Pandas", "Algorithms", "Statistics", "Python 3"]
#print(data_science_topics)

#Remove the Python3 entry, if it's the end it does not need an inmut in the method.
data_science_topics.pop()
#print(data_science_topics)

#Remove the Algorithms entry by specifying the index
data_science_topics.pop(3)
print(data_science_topics)

'''Range to List'''
# Range is exclusive
number_list = range(9)
print(list(number_list))
#[0, 1, 2, 3, 4, 5, 6, 7, 8]

#list() function changes the range to an actual list
zero_to_seven = range(8)
print(list(zero_to_seven))



#range() with 2 inputs indicates the start and stop.
my_list = range(2, 9)
print(list(my_list))
#[2, 3, 4, 5, 6, 7, 8]

#range() with 3 inputs indicates the start the stop, and the skip.
my_range2 = range(2, 9, 2)
print(list(my_range2))
#[2, 4, 6, 8]

#The skip number can be any number that makes sense
my_range3 = range(1, 100, 10)
print(list(my_range3))
#[1, 11, 21, 31, 41, 51, 61, 71, 81, 91]

range_five_three = range(5, 15, 3)

range_diff_five = range(0, 40, 5)

'''len() of lists'''
long_list = [1, 5, 6, 7, -23, 69.5, True, "very", "long", "list", "that", "keeps", "going.", "Let's", "practice", "getting", "the", "length"]

big_range = range(2, 3000, 10)

# Determines the length of the list
long_list_len = len(long_list)
print(long_list_len)

big_range_length = len(big_range)
print(big_range_length)

#The skip did not affect the length
big_range = range(2, 3000, 100)
print(big_range_length)

'''Slicing'''

suitcase = ["shirt", "shirt", "pants", "pants", "pajamas", "books"]

#Slicing first number is beginning and second is one more than the index shown, colon separated.
beginning = suitcase[0:2]
print(beginning)

#It's easiest to think about it as if starting from 1, these numbers frame the wanted numbers.
middle = suitcase[2:4]
print(middle)

last_two_elements = suitcase[-2:]
print(last_two_elements)

slice_off_last_three = suitcase[:-3]
print(slice_off_last_three)

fruits = ["apple", "cherry", "pineapple", "orange", "mango"]
#to slice the first n numbers, leave the first input empty before the colon
fruits[:3] #['apple', 'cherry', 'pineapple']

#to slice the last n numbers, leave the first input empty after the colon
fruits[-2:] #['orange', 'mango']

#to slice from beginning on with negative indice, leave the first input empty before the colon
fruits[:-1] #['apple', 'cherry', 'pineapple', 'orange']

'''.count() returns a value, so we can assign a variable to it'''

#One dimensional example
letters = ["m", "i", "s", "s", "i", "s", "s", "i", "p", "p", "i"]

num_i = letters.count("i")
print(num_i) #4

#Two dimensional example
number_collection = [[100, 200], [100, 200], [475, 29], [34, 34]]

num_pairs = number_collection.count([100, 200])
print(num_pairs) #2


votes = ["Jake", "Jake", "Laurie", "Laurie", "Laurie", "Jake", "Jake", "Jake", "Laurie", "Cassie", "Cassie", "Jake", "Jake", "Cassie", "Laurie", "Cassie", "Jake", "Jake", "Cassie", "Laurie"]

jake_votes = votes.count("Jake")
print(jake_votes)# 9

'''.sort() sorts what is there, does not make new list. Not assigned to a variable '''

names = ["Xander", "Buffy", "Angel", "Willow", "Giles"]
names.sort()
print(names) #['Angel', 'Buffy', 'Giles', 'Willow', 'Xander'] alphabetical order

# Sort backward
names.sort(reverse=True)
print(names) #['Xander', 'Willow', 'Giles', 'Buffy', 'Angel']



# Checkpoint 1 & 2
addresses = ["221 B Baker St.", "42 Wallaby Way", "12 Grimmauld Place", "742 Evergreen Terrace", "1600 Pennsylvania Ave", "10 Downing St."]

#You have to do 2 steps. print(addressess.sort()) returns None
addresses.sort()
#print(addresses)

# Checkpoint 3
names = ["Ron", "Hermione", "Harry", "Albus", "Sirius"]
names.sort()


# Checkpoint 4 & 5
cities = ["London", "Paris", "Rome", "Los Angeles", "New York"]
#Does not sort cities, because you can't save it to a variable
sorted_cities = cities.sort()
#print(sorted_cities)
cities.sort(reverse=True)
print(cities)

'''sorted() differs from sort() because 
1) it comes before a list instead of after 
as all built-in functions do. 
2 )It generates a new list rather than modifying the one that already exists.
'''
games = ["Portal", "Minecraft", "Pacman", "Tetris", "The Sims", "Pokemon"]

games_sorted = sorted(games)
print(games) #['Portal', 'Minecraft', 'Pacman', 'Tetris', 'The Sims', 'Pokemon']
print()
print(games_sorted) #['Minecraft', 'Pacman', 'Pokemon', 'Portal', 'Tetris', 'The Sims']

'''.insert(index, value)'''
inventory = ["twin bed", "twin bed", "headboard", "queen bed", "king bed", "dresser", "dresser", "table", "table", "nightstand", "nightstand", "king bed", "king bed", "twin bed", "twin bed", "sheets", "sheets", "pillow", "pillow"]
inventory.insert(10, "19th Century Bed Frame")

inventory = ["twin bed", "twin bed", "headboard", "queen bed", "king bed", "dresser", "dresser", "table", "table", "nightstand", "nightstand", "king bed", "king bed", "twin bed", "twin bed", "sheets", "sheets", "pillow", "pillow"]

inventory_len = len(inventory)
print(inventory_len)

#Don't forget that you can just call for the index
first = inventory[0]
last = inventory[-1]
inventory_2_6 = inventory[2:6]
first_3 = inventory[0:3]
twin_beds = inventory.count("twin bed")
removed_item = inventory[4]
inventory.insert(10, "19th Century Bed Frame")

inventory.sort()
print(inventory)

inventory = sorted(inventory)

new_list = [1, 2, 3, 4, 5, 6]
last_three = new_list[-3:]

'''Pizza Project using lists'''
toppings = ["pepperoni", "pineapple", "cheese", "sausage", "olives", "anchovies", "mushrooms"]

prices = [2, 6, 1, 3, 2, 7, 2]

#How many times does 2 appear?
num_two_dollar_slices = prices.count(2)
#print(num_two_dollar_slices)

#How many pizzas?
num_pizzas = len(toppings)
#print(num_pizzas)

print("We sell", num_pizzas, "different kinds of pizza!")

#combine as 2d list
pizza_and_prices = [
  [2,"pepperoni"],
  [6,"pineapple"],
  [1, "cheese"],
  [3, "sausage"],
  [2,"olives"],
  [7, "anchovies"],
  [2, "mushrooms"]
  ]
#print(pizza_and_prices)

#Sort by price
pizza_and_prices = sorted(pizza_and_prices)
print(pizza_and_prices)

#Store Cheapest as a variable
cheapest_pizza = pizza_and_prices[0]
#print(cheapest_pizza)

#Most Expensive Pizza
priciest_pizza = pizza_and_prices[-1]
#print(priciest_pizza)

#Anchovies got soldout, remove from menu
pizza_and_prices.pop()

#Add new menu item at the right place
pizza_and_prices.insert(-2, [2.5, "peppers"])
#print(pizza_and_prices)

three_cheapest = pizza_and_prices[0:3]
print(three_cheapest)

'''zip() Makes Lists into Tuples'''
names = ["Jenny", "Alexus", "Sam", "Grace"]
heights = [61, 70, 67, 64]
names_and_heights = zip(names, heights)
#print(names_and_heights) #Output: <zip object at 0x7f1631e86b48>
converted_list = list(names_and_heights)
print(converted_list)#[('Jenny', 61), ('Alexus', 70), ('Sam', 67), ('Grace', 64)]


owners = ["Jenny", "Alexus", "Sam", "Grace"]
dogs_names = ["Elphonse", "Dr. Doggy DDS", "Carter", "Ralph"]
names_and_dogs_names = zip(owners, dogs_names)

list_of_names_and_dogs_names = list(names_and_dogs_names)
print(list_of_names_and_dogs_names)

'''Tuples'''

my_tuple = ('abc', 123, 'def', 456, 789, 'ghi')

print(my_tuple[0])
print(my_tuple[3:5])

print(len(my_tuple))

print(my_tuple.index('abc'))
print(my_tuple.index(789))

#print(max(my_tuple)) #Error because it must be all one type

#print(min(my_tuple)) #Error because it must be all one type

print(my_tuple.count('ghi'))
