sensors =  {"living room": 21, "kitchen": 23, "bedroom": 20, 'pantry': 22}
num_cameras = {"backyard": 6,  "garage": 2, "driveway": 1}

print(sensors)

#writing a dict
translations = {"mountain": 'orod', 'bread': 'bass', 'friend': 'mellon', 'horse': 'roch'}

'''In dictionaries the key cannot be a hashable value type'''
#children = {["Johannes", "Rosmarie", "Eleonore"]: "von Trapp", ["Sonny", "Fredo", "Michael"]: "Corleone"} #Output: Traceback (most recent call last):
#   File "/home/ccuser/workspace/learn-python-dictionaries-dictionaries-introduction-invalid-keys/script.py", line 1, in <module>
#     children = {["Johannes", "Rosmarie", "Eleonore"]: "von Trapp", ["Sonny", "Fredo", "Michael"]: "Corleone"}
#                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
# TypeError: unhashable type: 'list'
#Fixed
children = {"von Trapp": ["Johannes", "Rosmarie", "Eleonore"] , "Corleone": ["Sonny", "Fredo", "Michael"]}

'''You can create an empty dict'''
my_empty_dictionary = {}
'''To add to a dict:
dictionary[key] = value'''

animals_in_zoo = {}
animals_in_zoo['zebras'] = 8
animals_in_zoo['monkeys'] = 12
animals_in_zoo['dinosaurs'] = 0
print(animals_in_zoo) #Output: {'zebras': 8, 'monkeys': 12, 'dinosaurs': 0}

'''To update multiple key/value pairs: .update() method'''
sensors.update({"pantry": 22, "guest room": 25, "patio": 34})

#The new keys and values are comma separated within whiskers
user_ids = {"teraCoder": 9018293, "proProgrammer": 119238}
user_ids.update({'theLooper':138475, 'stringQueen': 85739})
print(user_ids)

'''To change a value, dictionary[same_key] = new_value'''
oscar_winners = {"Best Picture": "La La Land", "Best Actor": "Casey Affleck", "Best Actress": "Emma Stone", "Animated Feature": "Zootopia"}

oscar_winners['Supporting Actress'] = 'Viola Davis'
print(oscar_winners)
oscar_winners['Best Picture'] = 'Moonlight'
print(oscar_winners)

'''Dict comprehensions: 
This dict comprehension:
1) Takes a pair from the iterator of tuples
2) Names the elements in the pair key (the one originally from the names list) and value (the one originally from the heights list)
3) Creates a key : value item in the students dictionary
4) Repeats steps 1-3 for the entire iterator of pairs'''

names = ['Jenny', 'Alexus', 'Sam', 'Grace']
heights = [61, 70, 67, 64]

students = {key:value for key, value in zip(names, heights)}
#students is now {'Jenny': 61, 'Alexus': 70, 'Sam': 67, 'Grace': 64}
 #A longer way:
drinks = ["espresso", "chai", "decaf", "drip"]
caffeine = [64, 40, 0, 120]
zipped_drinks = zip(drinks, caffeine)
drinks_to_caffeine = {key:value for key, value in zipped_drinks}


songs = ["Like a Rolling Stone", "Satisfaction", "Imagine", "What's Going On", "Respect", "Good Vibrations"]
playcounts = [78, 29, 44, 21, 89, 5]
plays = {key:value for key, value in zip(songs, playcounts)}
#print(plays)

#You can use += to change a value.
plays['Purple Haze'] = 1
plays['Respect'] += 5
#print(plays)

#You can use a dict as the value. You can use an empty dict as the value.
library = {'The Best Songs': plays, "Sunday Feelings": {}}
print(library)

'''USING DICTIONARIES
Get a key:'''

zodiac_elements = {"water": ["Cancer", "Scorpio", "Pisces"],
                   "fire": ["Aries", "Leo", "Sagittarius"],
                   "earth": ["Taurus", "Virgo", "Capricorn"],
                   "air":["Gemini", "Libra", "Aquarius"]}
print(zodiac_elements['earth']) #Output: ["Taurus", "Virgo", "Capricorn"]
print(zodiac_elements['fire']) #Output: ["Aries", "Leo", "Sagittarius"]

'''Get an invalid key'''
building_heights = {"Burj Khalifa": 828,
                    "Shanghai Tower": 632,
                    "Abraj Al Bait": 601,
                    "Ping An": 599,
                    "Lotte World Tower": 554.5,
                    "One World Trade": 541.3}

#print(building_heights["Landmark 81"])#Output: KeyError: 'Landmark 81'
#To avoid error and check if the key exists:
key_to_check = "Landmark 81"

if key_to_check in building_heights:
  print(building_heights["Landmark 81"]) #Output: False

#OR

zodiac_elements = {"water": ["Cancer", "Scorpio", "Pisces"], "fire": ["Aries", "Leo", "Sagittarius"], "earth": ["Taurus", "Virgo", "Capricorn"], "air":["Gemini", "Libra", "Aquarius"]}
#print(zodiac_elements["energy"]) Output: keyError
key_to_check = 'energy'

if key_to_check in zodiac_elements: print(zodiac_elements["energy"])

zodiac_elements['energy'] = "Not a Zodiac element"
print(zodiac_elements["energy"])

'''get() method'''
building_heights = {"Burj Khalifa": 828, "Shanghai Tower": 632, "Abraj Al Bait": 601, "Ping An": 599, "Lotte World Tower": 554.5, "One World Trade": 541.3}

#this line will return 632:
building_heights.get("Shanghai Tower")

#this line will return None:
building_heights.get("My House")

#You can specify what to return if there is no value in the second argument
print(building_heights.get('Shanghai Tower', 0)) # Prints 632
print(building_heights.get('Mt Olympus', 0)) # Prints 0
print(building_heights.get('Kilimanjaro', 'No Value')) # Prints 'No Value'

#OR
user_ids = {"teraCoder": 100019, "pythonGuy": 182921, "samTheJavaMaam": 123112, "lyleLoop": 102931, "keysmithKeith": 129384}
#Getting a value that does exist
tc_id = user_ids.get('teraCoder', 100000)
print(tc_id) #Output 100019

#Getting a value that does not exist
stack_id = user_ids.get('superStackSmash', 'invalid')
print(stack_id) #Output: 'invalid'

'''Delete a Key with .pop()'''
raffle = {223842: "Teddy Bear",
          872921: "Concert Tickets",
          320291: "Gift Basket",
          412123: "Necklace",
          298787: "Pasta Maker"}
print(raffle.pop(320291, "No Prize"))
# Prints "Gift Basket"
print(raffle)
# Prints {223842: "Teddy Bear", 872921: "Concert Tickets", 412123: "Necklace", 298787: "Pasta Maker"}
print(raffle.pop(100000, "No Prize"))
# Prints "No Prize"
print(raffle)
# Prints {223842: "Teddy Bear", 872921: "Concert Tickets", 412123: "Necklace", 298787: "Pasta Maker"}
print(raffle.pop(872921, "No Prize"))
# Prints "Concert Tickets"
print(raffle)
# Prints {223842: "Teddy Bear", 412123: "Necklace", 298787: "Pasta Maker"}

'''removing items in the dict with .pop()'''
available_items = {"health potion": 10, "cake of the cure": 5, "green elixir": 20, "strength sandwich": 25, "stamina grains": 15, "power stew": 30}
health_points = 20

health_points += available_items.pop("stamina grains", 0)
health_points += available_items.pop("power stew", 0)
health_points += available_items.pop("mystic bread", 0)

print(available_items)
print(health_points)

'''To get all the keys'''
test_scores = {"Grace":[80, 72, 90],
               "Jeffrey":[88, 68, 81],
               "Sylvia":[80, 82, 84],
               "Pedro":[98, 96, 95],
               "Martin":[78, 80, 78],
               "Dina":[64, 60, 75]}
print(list(test_scores)) # Prints ["Grace", "Jeffrey", "Sylvia", "Pedro", "Martin", "Dina"]
 #OR

for student in test_scores.keys():
 print(student)
 #Output:
# Grace
# Jeffrey
# Sylvia
# Pedro
# Martin
# Dina

#OR
user_ids = {"teraCoder": 100019,
            "pythonGuy": 182921,
            "samTheJavaMaam": 123112,
            "lyleLoop": 102931,
            "keysmithKeith": 129384}

num_exercises = {"functions": 10,
                 "syntax": 13,
                 "control flow": 15,
                 "loops": 22,
                 "lists": 19,
                 "classes": 18,
                 "dictionaries": 18}

users = user_ids.keys()
lessons = num_exercises.keys()

print(users) #Output: dict_keys(['teraCoder', 'pythonGuy', 'samTheJavaMaam', 'lyleLoop', 'keysmithKeith'])
print(lessons) #Output: dict_keys(['functions', 'syntax', 'control flow', 'loops', 'lists', 'classes', 'dictionaries'])
