'''Without a loop'''

ingredients = ["milk", "sugar", "vanilla extract", "dough", "chocolate"]
print(ingredients[0])
print(ingredients[1])
print(ingredients[2])
print(ingredients[3])
print(ingredients[4])
#milk
#sugar
#vanilla extract
#dough
#chocolate

'''For Loops'''

'''Simple Sample Loop'''
board_games = ["Settlers of Catan", "Carcassone", "Power Grid", "Agricola", "Scrabble"]

sport_games = ["football", "hockey", "baseball", "cricket"]

#Can be one line
for game in board_games: print(game)
#Or indented
for game in sport_games:
  print(game)


'''Ranged Loops'''
six_steps = range(6)
# six_steps is now a collection with 6 elements:
# 0, 1, 2, 3, 4, 5
for temp in range(6):
  print("Learning Loops!")
# Output: Learning Loops!
# Learning Loops!
# Learning Loops!
# Learning Loops!
# Learning Loops!
# Learning Loops!

#To track our progress
for temp in range(6):
  print("Loop is on iteration number " + str(temp + 1))
#Output:
#Loop is on iteration number 1
#Loop is on iteration number 2
#Loop is on iteration number 3
#Loop is on iteration number 4
#Loop is on iteration number 5
#Loop is on iteration number 6

promise = "I will finish the python loops module!"

for temp in range(5):
  print(promise)

'''While Loops'''

#Format:
# while <conditional statement>:
#   <action>


count = 0 #initialized to 0
while count <= 3: #condition statement
  # Loop Body
  print(count)
  count += 1

  #Output:
  # 0
  # 1
  # 2
  # 3

#Can be in one line
  count = 0
  while count <= 3: print(count); count += 1

  # While Loop Walkthrough
  # count = 0
  # print("Starting While Loop")
  # while count <= 3:
  #   # Loop Body
  #   # Print if the condition is still true
  #   print("Loop Iteration - count <= 3 is still true")
  #   # Print the current value of count
  #   print("Count is currently " + str(count))
  #   # Increment count
  #   count += 1
  #   print(" ----- ")
  # print("While Loop ended")

  # My code:
  countdown = 10
  while countdown >= 0:
    print(countdown)
    countdown -= 1
  print("We have liftoff!")


  python_topics = ["variables", "control flow", "loops", "modules", "classes"]
  length = len(python_topics)
  index = 0

  while index < length:
    print("I am learning about", python_topics[index])
    index += 1
    #Output
#I am learning about variables
#I am learning about control flow
#I am learning about loops
#I am learning about modules
#I am learning about classes

#Mix 2 lists with a loop
students_period_A = ["Alex", "Briana", "Cheri", "Daniele"]
students_period_B = ["Dora", "Minerva", "Alexa", "Obie"]

for student in students_period_A:
  students_period_B.append(student)
print(students_period_B)

'''Break exits the loop to quit searching'''
#Loop stops when value matches
dog_breeds_available_for_adoption = ["french_bulldog", "dalmatian", "shihtzu", "poodle", "collie"]
dog_breed_I_want = "dalmatian"

for dog_breed in dog_breeds_available_for_adoption:
  print(dog_breed)
  if dog_breed == dog_breed_I_want:
    print("They have the dog I want!")
    break

'''Continue in a loop skips something but doesn't break'''
#skipping ages under 21
ages = [12, 38, 34, 26, 21, 19, 67, 41, 17]

for i in ages:
  if i < 21:
    continue
  print(i)
  123456
  ages = [12, 38, 34, 26, 21, 19, 67, 41, 17]

  for i in ages:
    if i < 21:
      continue
    print(i)

  #Output:
  #38
  #34
  #26
  #21
  #67
  #41

'''Nested Loops'''

#Summing all the data into scoops_sold
#initiate at 0
sales_data = [[12, 17, 22], [2, 10, 3], [5, 12, 13]]
scoops_sold = 0

#Iterate through first level of 2D list
for location in sales_data:
  #Iterate through second of 2D list
  for scoops in location:
    #Aggregate total in variable
    scoops_sold += scoops
#Print total
print(scoops_sold)

'''List Comprehensions 
new_list = [<expression> for <element> in <collection>]'''
#If we wanted to create a list where everything is doubled:
#The long way:
# numbers = [2, -1, 79, 33, -45]
# doubled = []
#
# for number in numbers:
#   doubled.append(number * 2)
#
# print(doubled) #[4, -2, 158, 66, -90]

#The list comprehension shortcut:
numbers = [2, -1, 79, 33, -45]
doubled = [num * 2 for num in numbers]
print(doubled)

#Nesting the long way:
# grades = [90, 88, 62, 76, 74, 89, 48, 57]
# scaled_grades = []
#
# for g in grades:
#   scaled_grades = (g + 10)
# print(scaled_grades)

grades = [90, 88, 62, 76, 74, 89, 48, 57]
scaled_grades = [grade + 10 for grade in grades] #variable = Do-the-thing FOR iteration
print(scaled_grades)

'''Conditional List Comprehensions'''

#the long way
# numbers = [2, -1, 79, 33, -45]
# only_negative_doubled = []
#
# for num in numbers:
#   if num < 0:
#     only_negative_doubled.append(num * 2)
#
# print(only_negative_doubled) #[-2, -90]

negative_doubled = [num * 2 for num in numbers if num < 0] #variable = Do-the-thing FOR iteration IF Condition
print(negative_doubled) #[-2, -90]

#If-Else List Comprehensions look different
numbers = [2, -1, 79, 33, -45]
doubled = [num * 2 if num < 0 else num * 3 for num in numbers ] #variable = Do-the-thing IF condition, ELSE Do-a-different-thing FOR iteration
print(doubled)

#Spot the differences:
numbers = [2, -1, 79, 33, -45]

no_if = [num * 2 for num in numbers] #variable = Do-The_Thing FOR iteration
if_only = [num * 2 for num in numbers if num < 0] #variable = Do-The_Thing FOR iteration IF condition
if_else = [num * 2 if num < 0 else num * 3 for num in numbers] #variable = Do-The_Thing IF condition ELSE Do-a-different-thing FOR iteration

#Strange If/Only:
heights = [161, 164, 156, 144, 158, 170, 163, 163, 157]
can_ride_coaster = [height for height in heights if height > 161] # First height means add the item to the list, FOR iteration IF condition
print(can_ride_coaster)

#Exercise
single_digits = list(range(10))
#print(single_digits)
squares = []

for digit in single_digits:
  squares.append(digit * digit)
  print(digit)
  digit += 1
print(squares)

cubes = [digit ** 3 for digit in single_digits]
print(cubes)

#Exercise
#Carly's Cuts
hairstyles = ["bouffant", "pixie", "dreadlocks", "crew", "bowl", "bob", "mohawk", "flattop"]
prices = [30, 25, 40, 20, 20, 35, 50, 35]
last_week = [2, 3, 5, 8, 4, 4, 6, 2]
total_price = 0

#Calculate total of prices
for price in prices:
  total_price += price
#print(total_price)

#Take average of prices
average_price = total_price / len(prices)
print("Average Haircut Price:", average_price)

#Lower all prices by $5
new_prices = [i - 5 for i in prices]
#print(new_prices)

#Declare new var for revenue
total_revenue = 0

#Sum the prices * number of cuts in new var
for i in range(len(hairstyles)):
  for price in prices:
    total_revenue += prices[i] * last_week[i]
print("Total Revenue:",total_revenue)

#Take the daily average
average_daily_revenue = total_revenue / 7
print(average_daily_revenue)

#Compile advertising list of cuts that now cost less than $30
cuts_under_30 = [hairstyles[i] for i in range(len(new_prices)) if new_prices[i] <= 30]
print(cuts_under_30)