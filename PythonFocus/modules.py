'''Import modules'''
# from datetime import datetime
# current_time = datetime.now()
# print(current_time)
#
# #Exercise
# # Import random below:
# import random
#
# # Create random_list below:
# #.randint() accepts two arguments for start and stop
# random_list = [random.randint(1, 101)for i in range(101)]
# #print(random_list)

# Create randomer_number below:
#.random_choice() takes list as argument.
# randomer_number = random.choice(random_list)

# Print randomer_number below:
# print(randomer_number)

'''Aliasing for long or conflicting import names:
import module_name as name_you_pick_for_the_module
OR 
import * (wildcard)'''

#random.sample takes a list and randomly selects k items from it
# new_list = random.sample(list, k)
# #for example:
# nums = [1, 2, 3, 4, 5]
# sample_nums = random.sample(nums, 3)
# print(sample_nums) # 2, 5, 1

'''Aliasing'''
#import codecademylib3_seaborn
#from matplotlib import pyplot as plt
#import random

# numbers_a = range(1, 13)
# numbers_b = random.sample(range(1001), 12)
#print(numbers_b)
#plt.plot(numbers_a, numbers_b)
#plt.show()

'''Decimals'''
# Import Decimal below:
from decimal import Decimal

# Fix the floating point math below:
two_decimal_points = Decimal('0.2') + Decimal('0.69')
print(two_decimal_points)

four_decimal_points = Decimal('0.53') * Decimal('0.65')
print(four_decimal_points)

'''The scope of files as modules'''
#Say you had a file called library in which there was a function calles always_three.
# Import library below:
#from library import always_three

# Call your function below:
#return(always_three())

'''Datetime'''
# from datetime import datetime
#
# birthday = datetime(1994, 2, 15, 4, 25, 12) #arguments year, month, day, hour, minutes, and second
#
# print("Birthday Year is:", birthday.year)
# print("Month is:", birthday.month)
# print(birthday.day)
# print(birthday.hour)
# print(birthday.weekday) #returns a number
# print(datetime.now) #Gives right now
# print(datetime (2018, 1, 1) - datetime(2017, 1, 1)) #Only subtract
#
# parsed_date = datetime.strptime("January 15, 2018", %b, %d, %Y) #From the MDN docs.
