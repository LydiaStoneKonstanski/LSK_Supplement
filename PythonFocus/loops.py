'''Without a loop'''

ingredients = ["milk", "sugar", "vanilla extract", "dough", "chocolate"]
print(ingredients[0])
print(ingredients[1])
print(ingredients[2])
print(ingredients[3])
print(ingredients[4])
#milk
#sugar
#vanilla extract
#dough
#chocolate

'''For Loops'''

'''Simple Sample Loop'''
board_games = ["Settlers of Catan", "Carcassone", "Power Grid", "Agricola", "Scrabble"]

sport_games = ["football", "hockey", "baseball", "cricket"]

#Can be one line
for game in board_games: print(game)
#Or indented
for game in sport_games:
  print(game)


'''Ranged Loops'''
six_steps = range(6)
# six_steps is now a collection with 6 elements:
# 0, 1, 2, 3, 4, 5
for temp in range(6):
  print("Learning Loops!")
# Output: Learning Loops!
# Learning Loops!
# Learning Loops!
# Learning Loops!
# Learning Loops!
# Learning Loops!

#To track our progress
for temp in range(6):
  print("Loop is on iteration number " + str(temp + 1))
#Output:
#Loop is on iteration number 1
#Loop is on iteration number 2
#Loop is on iteration number 3
#Loop is on iteration number 4
#Loop is on iteration number 5
#Loop is on iteration number 6

promise = "I will finish the python loops module!"

for temp in range(5):
  print(promise)

'''While Loops'''

#Format:
# while <conditional statement>:
#   <action>


count = 0 #initialized to 0
while count <= 3: #condition statement
  # Loop Body
  print(count)
  count += 1

  #Output:
  # 0
  # 1
  # 2
  # 3

#Can be in one line
  count = 0
  while count <= 3: print(count); count += 1



