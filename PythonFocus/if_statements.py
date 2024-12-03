user_name = "Mary"
user_name = "angela_catlady_87"

if user_name == "Dave":
  print("Get off my computer Dave!")

if user_name == "angela_catlady_87":
  print("I know it is you, Dave! Go away!")


x = 20
y = 20

# Write the first if statement here:

if x == y:
  print("These numbers are the same")





"""Other Boolean Operators: And, or, not"""
credits = 120

if credits >= 120:
  print("You have enough credits to graduate!")

statement_one = (2 + 2 + 2 >= 6) and (-1 * -1 < 0)

statement_two = (4 * 2 <= 8) and (7 - 1 == 6)

credits = 120
gpa = 3.4

#Use of and
if credits >= 120 and gpa >= 2.0:
  print("You meet the requirements to graduate!")

#Use of or
  statement_one = (2 - 1 > 3) or (-5 * 2 == -10)

  statement_two = (9 + 5 <= 15) or (7 != 4 + 3)

  credits = 118
  gpa = 2.0

  if credits >= 120 or gpa >= 2.0:
      print("You have met at least one of the requirements.")

#Use of not
  credits = 120
  gpa = 1.8

  if not credits >= 120:
      print("You do not have enough credits to graduate.")

  if not gpa >= 2.0:
      print("Your GPA is not high enough to graduate.")

  if not (credits >= 120) and not (gpa >= 2.0):
      print("You do not meet either requirement to graduate!")

#better
credits = 120
gpa = 1.8

if credits < 120:
    print("You do not have enough credits to graduate.")

if gpa < 2.0:
    print("Your GPA is not high enough to graduate.")

if credits < 120 and gpa < 2.0:
    print("You do not meet either requirement to graduate!")

#with else
credits = 120
gpa = 1.9

if (credits >= 120) and (gpa >= 2.0):
  print("You meet the requirements to graduate!")
else: print("You do not meet the requirements to graduate.")

# With elif
grade = 86

if grade >= 90:
  print('A')
elif grade >= 80:
  print('B')
elif grade >= 70:
  print('C')
elif grade >= 60:
  print('D')
else: print('F')

print("I have information for the following planets:\n")

print("   1. Venus   2. Mars    3. Jupiter")
print("   4. Saturn  5. Uranus  6. Neptune\n")

weight = 185
planet = 3

# Write an if statement below:
if planet == 1:
    weight = weight * 0.91
elif planet == 2:
    weight = weight * 0.38
elif planet == 3:
    weight = weight * 2.34
elif planet == 4:
    weight = weight * 1.06
elif planet == 5:
    weight = weight * 0.92
elif planet == 6:
    weight = weight * 1.19

print("Codey's weight is: ", weight)




