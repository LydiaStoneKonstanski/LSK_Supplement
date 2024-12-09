'''Instance Variables
We’ve learned so far that a class is a schematic for a data type and an object is an
instance of a class, but why is there such a strong need to differentiate the two if
each object can only have the methods and class the class has? This is because each
instance of a class can hold different kinds of data.

The data held by an object is referred to as an instance variable.
Instance variables aren’t shared by all instances of a class — they are variables that
are specific to the object they are attached to.'''

class Shouter:
    def __init__(self):
        print("HELLO?!")

shout1 = Shouter()
# prints "HELLO?!"

shout2 = Shouter()
# prints "HELLO?!"

class Circle:
    pi = 3.14

    def __init__(self, diameter):
        self.diameter = diameter
        print(f"New circle with diameter: {self.diameter}")


# Create a circle teaching_table with diameter 36
teaching_table = Circle(36)


class Circle:
    pi = 3.14

    def area(self, radius):
        return Circle.pi * radius ** 2


circle = Circle()
pizza_area = circle.area(12 / 2)
teaching_table_area = circle.area(36 / 2)
round_room_area = circle.area(11460 / 2)


class DistanceConverter:
    kms_in_a_mile = 1.609

    def how_many_kms(self, miles):
        return miles * self.kms_in_a_mile


converter = DistanceConverter()
kms_in_5_miles = converter.how_many_kms(5)
print(kms_in_5_miles)


# prints "8.045"


# Instance Variables
# Store class defined
class Store:
    def __init__(self):
        return None


# Two objects of Store class created
alternative_rocks = Store()
isabelles_ices = Store()

#
alternative_rocks.store_name = "Alternative Rocks"
isabelles_ices.store_name = "Isabelle's Ices"


# Attribute functions
class NoCustomAttributes:
    pass


attributeless = NoCustomAttributes()

try:
    attributeless.fake_attribute


except AttributeError:
    print("This text gets printed!")

# prints "This text gets printed!"

'''What if we aren’t sure if an object has an attribute or not? 
Preview: Docs Returns True if an object has an attribute and False otherwise.
hasattr()
 will return True if an object has a given attribute and False otherwise. If we want to get the actual value of the attribute, 
Preview: Docs Returns the value of the named property in the specified object.
getattr()
 is a Python function that will return the value of a given object and attribute. In this function, we can also supply a third argument that will be the default if the object does not have the given attribute.'''

# getattr(object, “attribute”, default) has three parameters (one of which is optional):

hasattr(attributeless, "fake_attribute")
# returns False

getattr(attributeless, "other_fake_attribute", 800)
# returns 800, the default value


'''hasattr()'''
# a variable with different data types: Dict, string, int, and list
can_we_count_it = [{'s': False}, "sassafrass", 18, ["a", "c", "s", "d", "s"]]

# iterate through with hasattr() to check whether the data type has .count function.
for element in can_we_count_it:
    if hasattr(element, 'count'):
        print(str(type(element)) + " has the count attribute!")
    else:
        print(str(type(element)) + " does not have the count attribute :(")
'''
Output:
<class 'dict'> does not have the count attribute :(
<class 'str'> has the count attribute!
<class 'int'> does not have the count attribute :(
<class 'list'> has the count attribute!
'''

'''Self: Since we can already use 
Preview: Docs Loading link description
dictionaries
 to store key-value pairs, using objects for that purpose is not really useful. Instance 
Preview: Docs A variable is used to store data that will be used by the program. This data can be a number, a string, a Boolean, a list or some other data type. Every variable has a name which can consist of letters, numbers, and the underscore character . The equal sign = is used to assign a value to a variable. After the initial assignment is made, the value of a variable can be updated to new values as needed. A variable can have a short name (like x and y) or a more descriptive name (age, grade, grocerylist). Rules for Python variables: - A variable name must start with a letter or the underscore character. It cannot start with a number. - A variable name can only contain alpha-numeric characters and underscores (A-z, 0-9, and _). - Variable names are case-sensitive (num, Num, and NUM are three different variables).
variables
 are more powerful when you can guarantee a rigidity to the data the object is holding.

This convenience is most apparent when the constructor creates the instance variables using the arguments passed into it. If we were creating a search engine and wanted to create a class to hold each search entry, we could do so like this:
'''


class SearchEngineEntry:
    def __init__(self, url):
        self.url = url


codecademy = SearchEngineEntry("www.codecademy.com")
wikipedia = SearchEngineEntry("www.wikipedia.org")

print(codecademy.url)
# prints "www.codecademy.com"

print(wikipedia.url)
# prints "www.wikipedia.org"

'''In the preceding code sample, we define a SearchEngineEntry class, which contains a constructor with two parameters, self and url. Inside the constructor body, we create an instance variable named self.url and assign it the value of the url parameter that is passed into the constructor.

We then create the codecademy instance of SearchEngineEntry by passing the URL as an argument to the constructor. After codecademy is defined, printing codecademy.url shows that the URL has been assigned to the url instance variable of codecademy. Similarly, wikipedia.url holds the value that was passed into the constructor when wikipedia was defined.

Since the self keyword refers to the object and not the class being called, we can define a .secure() method on the SearchEngineEntry class that returns the secure link to an entry.'''


class SearchEngineEntry:
    secure_prefix = "https://"

    def __init__(self, url):
        self.url = url

    def secure(self):
        return "{prefix}{site}".format(prefix=self.secure_prefix, site=self.url)


codecademy = SearchEngineEntry("www.codecademy.com")
wikipedia = SearchEngineEntry("www.wikipedia.org")

print(codecademy.secure())
# prints "https://www.codecademy.com"

print(wikipedia.secure())
# prints "https://www.wikipedia.org"

'''Learn
Introduction to Classes
Self
Since we can already use 
Preview: Docs Loading link description
dictionaries
 to store key-value pairs, using objects for that purpose is not really useful. Instance 
Preview: Docs A variable is used to store data that will be used by the program. This data can be a number, a string, a Boolean, a list or some other data type. Every variable has a name which can consist of letters, numbers, and the underscore character . The equal sign = is used to assign a value to a variable. After the initial assignment is made, the value of a variable can be updated to new values as needed. A variable can have a short name (like x and y) or a more descriptive name (age, grade, grocerylist). Rules for Python variables: - A variable name must start with a letter or the underscore character. It cannot start with a number. - A variable name can only contain alpha-numeric characters and underscores (A-z, 0-9, and _). - Variable names are case-sensitive (num, Num, and NUM are three different variables).
variables
 are more powerful when you can guarantee a rigidity to the data the object is holding.

This convenience is most apparent when the constructor creates the instance variables using the arguments passed into it. If we were creating a search engine and wanted to create a class to hold each search entry, we could do so like this:
'''
class SearchEngineEntry:
  def __init__(self, url):
    self.url = url

codecademy = SearchEngineEntry("www.codecademy.com")
wikipedia = SearchEngineEntry("www.wikipedia.org")

print(codecademy.url)
# prints "www.codecademy.com"

print(wikipedia.url)
# prints "www.wikipedia.org"


'''
In the preceding code sample, we define a SearchEngineEntry class, which contains a constructor with 
two parameters, self and url. Inside the constructor body, we create an instance variable named self.url 
and assign it the value of the url parameter that is passed into the constructor.
We then create the codecademy instance of SearchEngineEntry by passing the URL as an argument to the 
constructor. After codecademy is defined, printing codecademy.url shows that the URL has been assigned 
to the url instance variable of codecademy. Similarly, wikipedia.url holds the value that was passed 
into the constructor when wikipedia was defined.

Since the self keyword refers to the object and not the class being called, we can define a .secure() method 
on the SearchEngineEntry class that returns the secure link to an entry.
'''
class SearchEngineEntry:
  secure_prefix = "https://"
  def __init__(self, url):
    self.url = url

  def secure(self):
    return "{prefix}{site}".format(prefix=self.secure_prefix, site=self.url)

codecademy = SearchEngineEntry("www.codecademy.com")
wikipedia = SearchEngineEntry("www.wikipedia.org")

print(codecademy.secure())
# prints "https://www.codecademy.com"

print(wikipedia.secure())
# prints "https://www.wikipedia.org"


'''Above, we define our.secure() method to take just the one required argument, self. We access both the
class variable self.secure_prefix and the instance variable self.url to return a secure URL.

This is the strength of writing object - oriented programs.We can write our classes
to structure the data that we need and write methods that will interact
with that data in a meaningful way.'''

'''Classes are templates used to define the properties and methods of objects in code'''

'''SELF: Since we can already use dictionaries to store key - value pairs, using objects
for that purpose is not really useful.
Instance variables are more powerful when you can guarantee a rigidity to the data the
object is holding.

This convenience is most apparent when the constructor creates the instance variables
using the arguments passed into it.If we were creating a search engine and wanted to create 
a class to hold each search entry, we could do so like this:'''

#class SearchEngineEntry defined
class SearchEngineEntry:
#constructor contains 2 parameters: self, and url.
  def __init__(self, url):
#inside the constructor body we create an instance variable self.url
    self.url = url

#create codecademy instance of SearchEngineEntry passing URL as argument to the constructor.
codecademy = SearchEngineEntry("www.codecademy.com")
wikipedia = SearchEngineEntry("www.wikipedia.org")

print(codecademy.url)
# prints "www.codecademy.com"

print(wikipedia.url)
# prints "www.wikipedia.org"

#SELF keyword belongs to object, not to the class, so we can define secure() method on SearchEngineEntry class that returns the secure link to an entry.
class SearchEngineEntry:
#.secure() method takes one argument, self.
  secure_prefix = "https://"
  def __init__(self, url):
    self.url = url

  def secure(self):
    return "{prefix}{site}".format(prefix=self.secure_prefix, site=self.url)

codecademy = SearchEngineEntry("www.codecademy.com")
wikipedia = SearchEngineEntry("www.wikipedia.org")

print(codecademy.secure())
# prints "https://www.codecademy.com"

print(wikipedia.secure())
# prints "https://www.wikipedia.org"



class Circle:
#instance variables
  pi = 3.14
#constructor
  def __init__(self, diameter):
    print("Creating circle with diameter {d}".format(d=diameter))
#instance variable
    self.radius = diameter / 2

#method for turning circumference to radius
  def circumference(self):
    return 2 * self.pi * self.radius

#establish instances of circle class with diameter in the argument.
medium_pizza = Circle(12)
teaching_table = Circle(36)
round_room = Circle(11460)

#call circumference method on variables.
print(medium_pizza.circumference())
print(teaching_table.circumference())
print(round_room.circumference())

'''Discovering the hidden attributes'''
class FakeDict:
  pass

fake_dict = FakeDict()
fake_dict.attribute = "Cool"

#use dir() to find all the attributes, even if they weren't in the constructor. the automatic ones have dunders.
print(dir(fake_dict))
# Prints ['__class__',
# '__delattr__',
# '__dict__',
# '__dir__',
# '__doc__',
# '__eq__',
# '__format__',
# '__ge__',
# '__getattribute__',
# '__gt__',
# '__hash__',
# '__init__()',
# '__init_subclass__',
# '__le__', '__lt__',
# '__module__',
# '__ne__',
# '__new__',
# '__reduce__',
# '__reduce_ex__',
# '__repr__',
# '__setattr__',
# '__sizeof__',
# '__str__',
# '__subclasshook__',
# '__weakref__',
# 'attribute']

fun_list = [10, "string", {'abc': True}]

type(fun_list)
# Prints <class 'list'>

print(dir(fun_list))
# Prints ['__add__',
# '__class__',
# [...],
# 'append',
# 'clear',
# 'copy',
# 'count',
# 'extend',
# 'index',
# 'insert',
# 'pop',
# 'remove',
# 'reverse',
# 'sort']


print(dir(5))
def this_function_is_an_object(self, pickles, pantaloons):
  pass
print(dir(this_function_is_an_object))


class User:
    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return "Hiya {}!".format(self.name)


devorah = User("Devorah")
print(devorah)
