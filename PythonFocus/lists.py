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

