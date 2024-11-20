1 == 1  # Evaluates to True as the operands are the same

1 != 1  # Evaluates to False as the operands are the same

2 != 4  # Evaluates to True as the operands are different

3 == 5  # Evaluates to False as the operands are different

'7' == 7  # Evaluates to False as the operands are different types

"""Boolean variables can be created in several ways. 
The easiest way is to simply assign True or False to a variable:"""
set_to_true = True
set_to_false = False
"""You can also set a variable equal to a boolean expression."""
bool_one = 5 != 7
bool_two = 1 + 1 != 2
bool_three = 3 * 3 == 9

"""These variables now contain boolean values, so when you reference 
them they will only return the True or False values of the expression 
they were assigned."""
print(bool_one)    # True

print(bool_two)    # False

print(bool_three)  # True

my_baby_bool = "true"
print(type(my_baby_bool)) #str

my_baby_bool_two = True
print(type(my_baby_bool_two)) #bool
