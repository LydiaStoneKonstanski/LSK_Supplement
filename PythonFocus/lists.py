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


broken_prices = [5, 3, 4, 5, 4] + [4]