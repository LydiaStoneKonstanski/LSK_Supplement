'''Strings are saved in quotes'''

favorite_word = "beatific"
print(favorite_word)

'''Strings are lists of characters, and thus may be indexed'''
favorite_fruit = "blueberry"
print(favorite_fruit[1])
# Output: l
#print(favorite_fruit[1.5]) #Output type error

my_name = "Lydia"
first_initial = my_name[0]
print(first_initial) #L

'''Slicing a string syntax: string[first_index:last_index]
Slicing index starts at 0 BEFORE the first letter'''

print(favorite_fruit[4:6])
# Output: be
print(favorite_fruit[:4])
# Output: blue
print (favorite_fruit[4:])
# Output: berry

first_name = "Rodrigo"
last_name = "Villanueva"

#OR

new_account = last_name[:5]
#print(new_account) #Output: Villa

temp_password = last_name[2:6]
print(temp_password) #Output: llan

first_name = "Julie"
last_name = "Blevins"

def account_generator(first_name, last_name):
  account_name = first_name[:3] + last_name[:3]
  return account_name

new_account = account_generator(first_name, last_name)

print(new_account)

'''Length of strings'''
favorite_fruit = "blueberry"
length = len(favorite_fruit)
print(length)
# Output: 9

#The space gets counted
fruit_sentence = "I love blueberries"
print(len(fruit_sentence))
# Output: 18

#last_char = favorite_fruit[len(favorite_fruit)]
#print(last_char)# IndexError: string index out of range Because thats an index after the last one.

last_char = favorite_fruit[len(favorite_fruit)-1]
print(last_char)
# Output: y

length = len(favorite_fruit)
last_chars = favorite_fruit[length-4:]
print(last_chars)
# Output: erry

#OR
first_name = "Reiko"
last_name = "Matsuki"

def password_generator(first_name, last_name):
  new_f = first_name[len(first_name) - 3:]
  new_l = last_name[len(last_name) - 3:]
  return new_f + new_l

temp_password = password_generator(first_name, last_name)
print(temp_password)

'''Slicing with indices'''
company_motto = "Copeland's Corporate Company helps you capably cope with the constant cacophony of daily life"

second_to_last = company_motto[-2] #Output: f
final_word = company_motto[-4:] #Output: life
