'''String methods all have the same syntax:
string_name.string_method(arguments)

'Hello world'.upper()#'HELLO WORLD'
'Hello world'.lower()#'hello world'
'Hello world'.title()#'Hello World'
'Hello world'.split()#['Hello', 'world']
' '.join(['Hello', 'world'])#'Hello world'
'Hello world'.replace('H', 'J')#'Jello world'
'   Hello world   '.strip()#'Hello world'
'{} {}.format('Hello', 'world')#'Hello world'
'''

'''.lower()'''
favorite_song = 'SmOoTH'
favorite_song_lowercase = favorite_song.lower()
print(favorite_song_lowercase)
# => 'smooth'

#string methods create new strings, not hashable.
print(favorite_song)
# => 'SmOoTH'

poem_title = "spring storm"
poem_author = "William Carlos Williams"

poem_title_fixed = poem_title.title()
print(poem_title_fixed)#Output: Sprint Storm

poem_author_fixed = poem_author.upper()
print(poem_author_fixed)

'''.split()
string_name.split(delimiter)
'''
man_its_a_hot_one = "Like seven inches from the midday sun"
print(man_its_a_hot_one.split())
# => ['Like', 'seven', 'inches', 'from', 'the', 'midday', 'sun']

greatest_guitarist = "santana"
print(greatest_guitarist.split('n'))
# => ['sa', 'ta', 'a']
print(greatest_guitarist.split('a'))
# => ['s', 'nt', 'n', '']

authors = "Audre Lorde,Gabriela Mistral,Jean Toomer,An Qi,Walt Whitman,Shel Silverstein,Carmen Boullosa,Kamala Suraiyya,Langston Hughes,Adrienne Rich,Nikki Giovanni"

author_names = authors.split(',')
print(author_names)
#Output: 123456
authors = "Audre Lorde,Gabriela Mistral,Jean Toomer,An Qi,Walt Whitman,Shel Silverstein,Carmen Boullosa,Kamala Suraiyya,Langston Hughes,Adrienne Rich,Nikki Giovanni"

#Separate out the names
author_names = authors.split(',')
#Output:
#['Audre Lorde', 'Gabriela Mistral', 'Jean Toomer', 'An Qi', 'Walt Whitman', 'Shel Silverstein', 'Carmen Boullosa', 'Kamala Suraiyya', 'Langston Hughes', 'Adrienne Rich', 'Nikki Giovanni'

#Choose only the last names. The index goes
# outside the method, because inside the method is counting the spaces between words.
author_last_names = []
for name in author_names:
    author_last_names.append(name.split()[-1])

print(author_last_names)
#Output ['Lorde', 'Mistral', 'Toomer', 'Qi', 'Whitman', 'Silverstein', 'Boullosa', 'Suraiyya', 'Hughes', 'Rich', 'Giovanni']

'''Splitting escape sequences:
\n Newline
\t Horizontal tab'''

smooth_chorus = \
"""And if you said, "This life ain't good enough."
I would give my world to lift you up
I could change my life to better suit your mood
Because you're so smooth"""

chorus_lines = smooth_chorus.split('\n')
#=> ['And if you said,
# "This life ain\'t good enough."',
# 'I would give my world to lift you up',
# 'I could change my life to better suit your mood',
# "Because you're so smooth"]

spring_storm_text = \
"""The sky has given over
its bitterness.
Out of the dark change
all day long
rain falls and falls
as if it would never end.
Still the snow keeps
its hold on the ground.
But water, water
from a thousand runnels!
It collects swiftly,
dappled with black
cuts a way for itself
through green ice in the gutters.
Drop after drop it falls
from the withered grass-stems
of the overhanging embankment."""
spring_storm_lines = spring_storm_text.split('\n')
print(spring_storm_lines)

'''.join()'''
#'delimiter'.join(list_you_want_to_join)
#.join() string method acts on the delimiter you want to join so you
# have to give it the whole thing in the argument as a list of strings.

my_munequita = ['My', 'Spanish', 'Harlem', 'Mona', 'Lisa']
#What you join with goes before the .join().
#in this case you use a space.
print(' '.join(my_munequita))
# => 'My Spanish Harlem Mona Lisa'

#With the list as a variable:
reapers_line_one_words = ["Black", "reapers", "with", "the", "sound", "of", "steel", "on", "stones"]
reapers_line_one = ' '.join(reapers_line_one_words)
print(reapers_line_one)

#You can join with any string, so in this case we use a comma
santana_songs = ['Oye Como Va', 'Smooth', 'Black Magic Woman', 'Samba Pa Ti', 'Maria Maria']
santana_songs_csv = ','.join(santana_songs)
print(santana_songs_csv)
# => 'Oye Como Va,Smooth,Black Magic Woman,Samba Pa Ti,Maria Maria'

#You can also join using escape sequences as delimeter.
smooth_fifth_verse_lines = ['Well I\'m from the barrio', 'You hear my rhythm on your radio', 'You feel the turning of the world so soft and slow', 'Turning you \'round and \'round']
smooth_fifth_verse = '\n'.join(smooth_fifth_verse_lines)

print(smooth_fifth_verse)
#Output:
#Well I'm from the barrio
# You hear my rhythm on your radio
# You feel the turning of the world so soft and slow
# Turning you 'round and 'round

#William Carlos Williams Winter Trees
winter_trees_lines = ['All the complicated details',
                      'of the attiring and',
                      'the disattiring are completed!',
                      'A liquid moon', 'moves gently among',
                      'the long branches.',
                      'Thus having prepared their buds',
                      'against a sure winter', 'the wise trees',
                      'stand sleeping in the cold.']
winter_trees_full = '\n'.join(winter_trees_lines)

print(winter_trees_full)
# All the complicated details
# of the attiring and
# the disattiring are completed!
# A liquid moon
# moves gently among
# the long branches.
# Thus having prepared their buds
# against a sure winter
# the wise trees
# stand sleeping in the cold.

'''.strip()
takes all the whitespace at the beginning and end'''

featuring = "           rob thomas                 "
print(featuring.strip())
# => 'rob thomas'

#You can also strip out other things if they are provided as the argument.
featuring = "!!!rob thomas       !!!!!"
print(featuring.strip('!'))
# => 'rob thomas

#Strip out the weird spaces, join on newlines.
love_maybe_lines = ['Always    ', '     in the middle of our bloodiest battles  ', 'you lay down your arms', '           like flowering mines    ','\n' ,'   to conquer me home.    ']
#You can't call .strip() directly on the list
love_maybe_lines_stripped = [line.strip() for line in love_maybe_lines]
#Then join things
love_maybe_full = '\n'.join(love_maybe_lines_stripped)

print(love_maybe_full)

#You can call .strip() more than once
user_name = ":::::::: Eloise :::::::::::"
user_name_fixed = user_name.strip(':').strip()
print(user_name_fixed) #Output: Eloise




'''Replace
string_name.replace(substring_being_replaced, new_substring)
'''

with_spaces = "You got the kind of loving that can be so smooth"
with_underscores = with_spaces.replace(' ', '_')
print(with_underscores)
# 'You_got_the_kind_of_loving_that_can_be_so_smooth'

#Replace Tomer with Toomer
toomer_bio = \
"""
Nathan Pinchback Tomer, who adopted the name Jean Tomer early in his literary career, was born in Washington, D.C. in 1894. Jean is the son of Nathan Tomer was a mixed-race freedman, born into slavery in 1839 in Chatham County, North Carolina. Jean Tomer is most well known for his first book Cane, which vividly portrays the life of African-Americans in southern farmlands.
"""

toomer_bio_fixed = toomer_bio.replace('Tomer', 'Toomer')
print(toomer_bio_fixed)





'''.find() turns up the first index number of the
thing you are looking for'''
print('smooth'.find('t'))
# => '4'

print("smooth".find('oo'))
# => '2'

#Gabriela Mistral’s poem God Wills It.
god_wills_it_line_one = "The very earth will disown you"

disown_placement = (god_wills_it_line_one.find('disown'))
print(disown_placement)#=> 20




'''.format()'''
def favorite_song_statement(song, artist):
  return "My favorite song is {} by {}.".format(song, artist)
print(favorite_song_statement("Smooth", "Santana"))
# => "My favorite song is Smooth by Santana."


def poem_title_card(title, poet):
  return 'The poem "{}" is written by {}.'.format(title, poet)

print(poem_title_card("I Hear America Singing", "Walt Whitman")
)

#Including keywords with the arguments
def favorite_song_statement(song, artist):
  return "My favorite song is {song} by {artist}.".format(song=song, artist=artist)

#With keywords you don't need the arguments to be in order
def poem_description(publishing_date, author, title, original_work):
  poem_desc = "The poem {title} by {author} was originally published in {original_work} in {publishing_date}.".format(publishing_date=publishing_date, author=author, title=title, original_work=original_work)
  return poem_desc

my_beard_description = poem_description (
    author = "Shel Silverstein",
    title = "My Beard",
    original_work = "Where the Sidewalk Ends",
    publishing_date = "1974")


'''FORMATTING PROJECT'''
highlighted_poems = ("Afterimages:Audre Lorde:1997,  "
                     "The Shadow:William Carlos Williams:1915, "
                     "Ecstasy:Gabriela Mistral:1925,   "
                     "Georgia Dusk:Jean Toomer:1923,   "
                     "Parting Before Daybreak:An Qi:2014, "
                     "The Untold Want:Walt Whitman:1871, "
                     "Mr. Grumpledump's Song:Shel Silverstein:2004, "
                     "Angel Sound Mexico City:Carmen Boullosa:2013, "
                     "In Love:Kamala Suraiyya:1965, "
                     "Dream Variations:Langston Hughes:1994, "
                     "Dreamwood:Adrienne Rich:1987")

#print(highlighted_poems)

highlighted_poems_list = highlighted_poems.split(',')
#print(highlighted_poems_list)

highlighted_poems_stripped = [space.strip() for space in highlighted_poems_list ]
#print(highlighted_poems_stripped)

highlighted_poems_details = []
for detail in highlighted_poems_stripped:
  highlighted_poems_details.append(detail.split(':'))
#print(highlighted_poems_details)

titles = []
poets = []
dates = []

for poem in highlighted_poems_details:
   titles.append(poem[0])
   poets.append(poem[1])
   dates.append(poem[2])

for i in range(0, len(highlighted_poems_details)):
  print('The poem {} was published by {} in {}.'.format(titles[i], poets[i], dates[i]))

'''STRING METHODS PROJECT'''
daily_sales = \
"""Edith Mcbride   ;,;$1.21   ;,;   white ;,; 
09/15/17   ,Herbert Tran   ;,;   $7.29;,; 
white&blue;,;   09/15/17 ,Paul Clarke ;,;$12.52 
;,;   white&blue ;,; 09/15/17 ,Lucille Caldwell   
;,;   $5.13   ;,; white   ;,; 09/15/17,
Eduardo George   ;,;$20.39;,; white&yellow 
;,;09/15/17   ,   Danny Mclaughlin;,;$30.82;,;   
purple ;,;09/15/17 ,Stacy Vargas;,; $1.85   ;,; 
purple&yellow ;,;09/15/17,   Shaun Brock;,; 
$17.98;,;purple&yellow ;,; 09/15/17 , 
Erick Harper ;,;$17.41;,; blue ;,; 09/15/17, 
Michelle Howell ;,;$28.59;,; blue;,;   09/15/17   , 
Carroll Boyd;,; $14.51;,;   purple&blue   ;,;   
09/15/17   , Teresa Carter   ;,; $19.64 ;,; 
white;,;09/15/17   ,   Jacob Kennedy ;,; $11.40   
;,; white&red   ;,; 09/15/17, Craig Chambers;,; 
$8.79 ;,; white&blue&red   ;,;09/15/17   , Peggy Bell;,; $8.65 ;,;blue   ;,; 09/15/17,   Kenneth Cunningham ;,;   $10.53;,;   green&blue   ;,; 
09/15/17   ,   Marvin Morgan;,;   $16.49;,; 
green&blue&red   ;,;   09/15/17 ,Marjorie Russell 
;,; $6.55 ;,;   green&blue&red;,;   09/15/17 ,
Israel Cummings;,;   $11.86   ;,;black;,;  
09/15/17,   June Doyle   ;,;   $22.29 ;,;  
black&yellow ;,;09/15/17 , Jaime Buchanan   ;,;   
$8.35;,;   white&black&yellow   ;,;   09/15/17,   
Rhonda Farmer;,;$2.91 ;,;   white&black&yellow   
;,;09/15/17, Darren Mckenzie ;,;$22.94;,;green 
;,;09/15/17,Rufus Malone;,;$4.70   ;,; green&yellow 
;,; 09/15/17   ,Hubert Miles;,;   $3.59   
;,;green&yellow&blue;,;   09/15/17   , Joseph Bridges  ;,;$5.66   ;,; green&yellow&purple&blue 
;,;   09/15/17 , Sergio Murphy   ;,;$17.51   ;,;   
black   ;,;   09/15/17 , Audrey Ferguson ;,; 
$5.54;,;black&blue   ;,;09/15/17 ,Edna Williams ;,; 
$17.13;,; black&blue;,;   09/15/17,   Randy Fleming;,;   $21.13 ;,;black ;,;09/15/17 ,Elisa Hart;,; $0.35   ;,; black&purple;,;   09/15/17   ,
Ernesto Hunt ;,; $13.91   ;,;   black&purple ;,;   
09/15/17,   Shannon Chavez   ;,;$19.26   ;,; 
yellow;,; 09/15/17   , Sammy Cain;,; $5.45;,;   
yellow&red ;,;09/15/17 ,   Steven Reeves ;,;$5.50   
;,;   yellow;,;   09/15/17, Ruben Jones   ;,; 
$14.56 ;,;   yellow&blue;,;09/15/17 , Essie Hansen;,;   $7.33   ;,;   yellow&blue&red
;,; 09/15/17   ,   Rene Hardy   ;,; $20.22   ;,; 
black ;,;   09/15/17 ,   Lucy Snyder   ;,; $8.67   
;,;black&red  ;,; 09/15/17 ,Dallas Obrien ;,;   
$8.31;,;   black&red ;,;   09/15/17,   Stacey Payne 
;,;   $15.70   ;,;   white&black&red ;,;09/15/17   
,   Tanya Cox   ;,;   $6.74   ;,;yellow   ;,; 
09/15/17 , Melody Moran ;,;   $30.84   
;,;yellow&black;,;   09/15/17 , Louise Becker   ;,; 
$12.31 ;,; green&yellow&black;,;   09/15/17 ,
Ryan Webster;,;$2.94 ;,; yellow ;,; 09/15/17 
,Justin Blake ;,; $22.46   ;,;white&yellow ;,;   
09/15/17,   Beverly Baldwin ;,;   $6.60;,;   
white&yellow&black ;,;09/15/17   ,   Dale Brady   
;,;   $6.27 ;,; yellow   ;,;09/15/17 ,Guadalupe Potter ;,;$21.12   ;,; yellow;,; 09/15/17   , 
Desiree Butler ;,;$2.10   ;,;white;,; 09/15/17  
,Sonja Barnett ;,; $14.22 ;,;white&black;,;   
09/15/17, Angelica Garza;,;$11.60;,;white&black   
;,;   09/15/17   ,   Jamie Welch   ;,; $25.27   ;,; 
white&black&red ;,;09/15/17   ,   Rex Hudson   
;,;$8.26;,;   purple;,; 09/15/17 ,   Nadine Gibbs 
;,;   $30.80 ;,;   purple&yellow   ;,; 09/15/17   , 
Hannah Pratt;,;   $22.61   ;,;   purple&yellow   
;,;09/15/17,Gayle Richards;,;$22.19 ;,; 
green&purple&yellow ;,;09/15/17   ,Stanley Holland 
;,; $7.47   ;,; red ;,; 09/15/17 , Anna Dean;,;$5.49 ;,; yellow&red ;,;   09/15/17   ,
Terrance Saunders ;,;   $23.70  ;,;green&yellow&red 
;,; 09/15/17 ,   Brandi Zimmerman ;,; $26.66 ;,; 
red   ;,;09/15/17 ,Guadalupe Freeman ;,; $25.95;,; 
green&red ;,;   09/15/17   ,Irving Patterson 
;,;$19.55 ;,; green&white&red ;,;   09/15/17 ,Karl Ross;,;   $15.68;,;   white ;,;   09/15/17 , Brandy Cortez ;,;$23.57;,;   white&red   ;,;09/15/17, 
Mamie Riley   ;,;$29.32;,; purple;,;09/15/17 ,Mike Thornton   ;,; $26.44 ;,;   purple   ;,; 09/15/17, 
Jamie Vaughn   ;,; $17.24;,;green ;,; 09/15/17   , 
Noah Day ;,;   $8.49   ;,;green   ;,;09/15/17   
,Josephine Keller ;,;$13.10 ;,;green;,;   09/15/17 ,   Tracey Wolfe;,;$20.39 ;,; red   ;,; 09/15/17 ,
Ignacio Parks;,;$14.70   ;,; white&red ;,;09/15/17 
, Beatrice Newman ;,;$22.45   ;,;white&purple&red 
;,;   09/15/17, Andre Norris   ;,;   $28.46   ;,;   
red;,;   09/15/17 ,   Albert Lewis ;,; $23.89;,;   
black&red;,; 09/15/17,   Javier Bailey   ;,;   
$24.49   ;,; black&red ;,; 09/15/17   , Everett Lyons ;,;$1.81;,;   black&red ;,; 09/15/17 ,   
Abraham Maxwell;,; $6.81   ;,;green;,;   09/15/17   
,   Traci Craig ;,;$0.65;,; green&yellow;,; 
09/15/17 , Jeffrey Jenkins   ;,;$26.45;,; 
green&yellow&blue   ;,;   09/15/17,   Merle Wilson 
;,;   $7.69 ;,; purple;,; 09/15/17,Janis Franklin   
;,;$8.74   ;,; purple&black   ;,;09/15/17 ,  
Leonard Guerrero ;,;   $1.86   ;,;yellow  
;,;09/15/17,Lana Sanchez;,;$14.75   ;,; yellow;,;   
09/15/17   ,Donna Ball ;,; $28.10  ;,; 
yellow&blue;,;   09/15/17   , Terrell Barber   ;,; 
$9.91   ;,; green ;,;09/15/17   ,Jody Flores;,; 
$16.34 ;,; green ;,;   09/15/17,   Daryl Herrera 
;,;$27.57;,; white;,;   09/15/17   , Miguel Mcguire;,;$5.25;,; white&blue   ;,;   09/15/17 ,   
Rogelio Gonzalez;,; $9.51;,;   white&black&blue   
;,;   09/15/17   ,   Lora Hammond ;,;$20.56 ;,; 
green;,;   09/15/17,Owen Ward;,; $21.64   ;,;   
green&yellow;,;09/15/17,Malcolm Morales ;,;   
$24.99   ;,;   green&yellow&black;,; 09/15/17 ,   
Eric Mcdaniel ;,;$29.70;,; green ;,; 09/15/17 
,Madeline Estrada;,;   $15.52;,;green;,;   09/15/17 
, Leticia Manning;,;$15.70 ;,; green&purple;,; 
09/15/17 ,   Mario Wallace ;,; $12.36 ;,;green ;,; 
09/15/17,Lewis Glover;,;   $13.66   ;,;   
green&white;,;09/15/17,   Gail Phelps   ;,;$30.52   
;,; green&white&blue   ;,; 09/15/17 , Myrtle Morris 
;,;   $22.66   ;,; green&white&blue;,;09/15/17"""

daily_sales_replaced = daily_sales.replace(';,;', '|')
#print(daily_sales_replaced)

daily_transactions = daily_sales_replaced.split(',')
#print(daily_transactions)

daily_transactions_split = []
for transaction in daily_transactions:
   daily_transactions_split.append(transaction.split('|'))
#print(daily_transactions_split)

transactions_clean = [[item.strip() for item in transaction]
for transaction in  daily_transactions_split]

#print(transactions_clean)

customers = []
sales = []
thread_sold = []

for item in transactions_clean:
  customers.append(item[0])
  sales.append(item[1])
  thread_sold.append(item[2])
# print(customers)
# print(sales)
# print(thread_sold)

total_sales = 0
for sale in sales:
   total_sales += float(sale.strip('$'))
total_sales = round(total_sales , 2)

#print(total_sales) #Output: 1498.74
#print(thread_sold)
thread_sold_split = []
for color in thread_sold:
  if'&' in color:
    split_color = color.split('&')
    thread_sold_split.extend(split_color)
  else: thread_sold_split.append(color)

#print(thread_sold_split)

def color_count(color):
  count = 0
  for item in thread_sold_split:
    if item == color:
      count += 1
  return count

print(color_count('white')) #Expected Output: 28

colors = ['red', 'yellow', 'green', 'white', 'black', 'blue', 'purple']

for listed_color in colors:
  this_color = color_count(listed_color)
  print('The color {} was sold {} times today.'.format(listed_color, this_color))
#Output: The color red was sold 24 times today.
# The color yellow was sold 34 times today.
# The color green was sold 30 times today.
# The color white was sold 28 times today.
# The color black was sold 26 times today.
# The color blue was sold 22 times today.
# The color purple was sold 17 times today.