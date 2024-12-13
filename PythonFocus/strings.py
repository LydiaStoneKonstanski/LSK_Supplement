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

first_name = "Bob"
last_name = "Daily"

#first_name[0] = "R" #1263457
first_name = "Bob"
last_name = "Daily"

#first_name[0] = "R"
'''
Output:
Traceback (most recent call last):
  File "/home/ccuser/workspace/introduction-to-strings-immutable-strings/script.py", line 4, in <module>
    first_name[0] = "R"
    ~~~~~~~~~~^^^
TypeError: 'str' object does not support item assignment
'''
fixed_first_name = 'R' + first_name[1:]
print(fixed_first_name)

'''Escaping characters'''

#This messes up the string:
#favorite_fruit_conversation = "He said, "blueberries are my favorite!""

#the \ fixes it
favorite_fruit_conversation = "He said, \"blueberries are my favorite!\""

password = "theycallme\"crazy\"91"

def print_each_letter(word):
  for letter in word:
    print(letter)

favorite_color = "blue"
print_each_letter(favorite_color)
# => 'b'
# => 'l'
# => 'u'
# => 'e'

def get_length(word):
  char = 0
  for letter in word:
    char += 1
  return char

'''Counting things'''
favorite_fruit = "blueberry"
counter = 0
for character in favorite_fruit:
  if character == "b":
    counter = counter + 1
print(counter)

def letter_check(word, letter):
  count = 0
  for i in word:
    if i == letter:
      return True

  return False


def contains(big_string, little_string):
  return (little_string in big_string)


def common_letters(string_one, string_two):
  common = []
  for i in string_one:
    if (i in string_two) and not (i in common):
      common.append(i)
  return common


def username_generator(first_name, last_name):
  username = first_name[:3] + last_name[:4]
  return username
print(username_generator("Abe", "Simpson"))

def password_generator(user_name):
#   password = user_name[-1]
#   password += user_name[:6]
#   return password

    password = ""
    for i in range(0, len(user_name)):
        password += user_name[i-1]
    return password

print(password_generator(username_generator("Abe", "Simpson")))
