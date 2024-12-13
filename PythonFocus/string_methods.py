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