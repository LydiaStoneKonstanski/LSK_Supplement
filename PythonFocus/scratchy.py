
dirty_harry = "Go ahead, make my day."
split_hairs = dirty_harry.split("a")
print(split_hairs) #Output: ['Go ', 'he', 'd, m', 'ke my d', 'y.']

greeting = ["Hello", "my", "name", "is", "Earl"]
print('_'.join(greeting))

#list_of_lines = when_you_are_old.split('\n')

user_name = ":::::::: Eloise :::::::::::"
user_name_fixed = user_name.strip(':').strip()
print(user_name_fixed)

my_dict = {"name": "Ankit", "country": "India"}
my_delim = ":::"
x = my_delim.join(my_dict)

print(x)