'''Lambda Functions in Pandas
Accepts input, modifies, and returns output. Like a temp function in one line. '''

#add_two stores the function in a variable
#lambda operates like 'def'
# my_input is whatever will be the input
# : acts as 'return'
add_two = lambda my_input : my_input + 2
print(add_two(3)) #5
print(add_two(100)) #102
print(add_two(-2)) #0

is_substring = lambda my_string : my_string in 'This is the master string'
print(is_substring('I')) #FALSE
print(is_substring('am')) #FALSE
print(is_substring('the')) #TRUE
print(is_substring('master')) #TRUE

'''Statements in Lambdas

<WHAT TO RETURN IF STATEMENT IS TRUE> if <IF STATEMENT> else <WHAT TO RETURN IF STATEMENT IS FALSE>'''

check_if_A_grade = lambda grade: 'Got an A!' if grade >=90 else 'Did not get an A...'

contains_a = lambda word : 'a' in word
print(contains_a("banana")) #TRUE
print(contains_a("apple")) #TRUE
print(contains_a("cherry")) #FALSE

long_string = lambda str : len(str) > 12
print(long_string("short")) #FALSE
print(long_string("photosynthesis")) #TRUE

ends_in_a = lambda str : str[-1] == 'a'
print(ends_in_a("data")) #TRUE
print(ends_in_a("aardvark")) #FALSE

double_or_zero = lambda num : num * 2 if num > 10 else 0
print(double_or_zero(15)) #30
print(double_or_zero(5)) #0

even_or_odd = lambda num : 'even' if num % 2 == 0 else 'odd'
print(even_or_odd(10)) #even
print(even_or_odd(5)) #odd

#Using modulo on a number usually returns whether it is evenly divisible if the remainder is 0.
multiple_of_three = lambda num : 'multiple of three' if num % 3 == 0 else "not a multiple"
print(multiple_of_three(9)) #'multiple of three'
print(multiple_of_three(10)) #"not a multiple"

rate_movie = lambda rating : 'I liked this movie' if rating > 8.5 else 'This movie was not very good'
print(rate_movie(9.2)) #'I liked this movie'
print(rate_movie(7.2)) #'This movie was not very good'

#You can use the modulo operator (%) with 10 to find the ones’ place of an integer.
# >>> 41%10
# 1
# >>> 2%10
# 2
# >>> 39%10
# 9
# >>> 103%10
# 3
# >>> 20%10
# 0

ones_place = lambda num : num % 10
print(ones_place(123)) #3
print(ones_place(4)) #4

#You can find the square of a number by multiplying it by itself:

#eight_squared = 8*8
#The value of eight_squared is now 64
#or by using the exponential operator **:
# seven_squared = 7**2
#The value of seven_squared is now 49
double_square = lambda num : (num*num)*2
print(double_square(5)) #50
print(double_square(3)) #18

import random
add_random = lambda num : num + random.randint(1, 10)

print(add_random(5)) #10
print(add_random(100)) #105

stringlambda = lambda x: x.lower()
print(stringlambda("Oh Hi Mark!")) #'oh hi mark!'

#First and last initials of a string
mylambda = lambda str : str[0] + str[-1]
print(mylambda('This is a string')) #Tg

#Comparitive Functions
def myfunction(x):
    if x > 40:
        return 40 + (x - 40) * 1.50
    else:
        return x
#vs
myfunction = lambda x: 40 + (x - 40) * 1.50 if x > 40 else x


mylambda = lambda n : 'Welcome to Battle City!' if n >= 13 else 'You must be 13 or older'
print(mylambda(14))

#Lambda to split
df['Email Provider'] = df.Email.apply(
    lambda x: x.split('@')[-1]
    )


