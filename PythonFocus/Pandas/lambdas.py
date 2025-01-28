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

