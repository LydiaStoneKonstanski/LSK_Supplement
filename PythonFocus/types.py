'''Check Type like this'''

print(type(5))

my_dict = {}
print(type(my_dict))

my_list = []
print(type(my_list))

'''Class: To define'''
class Facade:
  pass

'''Class must be instantiated, like calling a function. Takes a class and turns it into an object'''
facade_instance = Facade()

print(type(facade_instance))
#Prints "class '__main__.Facade'>"

'''Class Variable, a variable available to every instance of the class'''
class Musician:
  title = "Rockstar"

drummer = Musician()
print(drummer.title)
# prints "Rockstar"
 #OR
class Grade:
  minimum_passing = 65

'''Methods are functions that are part of the larger class.
The first argument in a method is always the object that is calling the method. 
Convention recommends that we name this first argument self. 
Methods always have at least this one argument.

Self is implicitly passed, does not need to be called out'''

class Dog:
  dog_time_dilation = 7

  def time_explanation(self):
    print("Dogs experience {} years for every 1 human year.".format(self.dog_time_dilation))

pipi_pitbull = Dog()
pipi_pitbull.time_explanation()
# Prints "Dogs experience 7 years for every 1 human year."

class Rules:
  def washing_brushes(self):
    return 'Point bristles towards the basin while washing your brushes.'

'''Methods with more than one argument'''
class DistanceConverter:
  kms_in_a_mile = 1.609
  def how_many_kms(self, miles):
    return miles * self.kms_in_a_mile

converter = DistanceConverter()
kms_in_5_miles = converter.how_many_kms(5)
print(kms_in_5_miles)
# prints "8.045


#new class
class Circle:
    pi = 3.14
    #Methods are tabbed in
    def area(self, radius):
        return Circle.pi * radius ** 2
#Instantiated on the class level
circle = Circle()
#used on the class level
pizza_area = circle.area(12 / 2)
teaching_table_area = circle.area(36 / 2)
round_room_area = circle.area(11460 / 2)

'''Constructors'''

class Shouter:
    #uses a 'dunder' CONSTRUCTOR 'double underline'
    # make sure phrase is a string
  def __init__(self, phrase):
    print("HELLO?!")
    if type(phrase) == str:

      # then shout it out
      print(phrase.upper())

shout1 = Shouter()
# prints "HELLO?!"

shout2 = Shouter()
# prints "HELLO?!"

shout3 = Shouter("shout")
# prints "SHOUT"

shout4 = Shouter("shout")
# prints "SHOUT"

shout5 = Shouter("let it all out")
# prints "LET IT ALL OUT"

class Circle:
    pi = 3.14

    def __init__(self, diameter):
        #instantiation
        self.diameter = diameter
        print(f"New circle with diameter: {self.diameter}")


# Create a circle teaching_table with diameter 36
teaching_table = Circle(36)


class Student():

    def __init__(self, name, year):
        self.name = name
        self.year = year
        self.grades = []

    def __repr__(self):
        return self.name

    def add_grade(self, grade):
        if type(grade) is Grade:
            self.grades.append(grade)
        else:
            pass


roger = Student('Roger van der Weyden', 10)
sandro = Student('Sandro Botticelli', 12)
pieter = Student('Pieter Bruegel the Elder', 8)


# print(roger, sandro, pieter)

class Grade():
    minimum_passing = 65

    def __init__(self, score):
        self.score = score

    def is_passing(self, grade):
        if grade >= 65:
            print("Student is passing!")
        else:
            print("Study harder")


pieter.add_grade(Grade(100))


