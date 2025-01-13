'''If we had something called real_cool_document.txt with these contents: Wowsers!
We could read that file like this:

with open('real_cool_document.txt') as cool_doc:
  cool_contents = cool_doc.read()
print(cool_contents)

This opens a file object called cool_doc and creates a new indented block
where you can read the contents of the opened file. We then read the contents
of the file cool_doc using cool_doc.read() and save the resulting string into
the variable cool_contents. Then we print cool_contents, which outputs the
statement Wowsers!
'''

'''.READ() puts everything in one line'''
with open('welcome.txt') as text_file:
  text_data = text_file.read()
  print(text_data) #Output: Congratulations on reading your first file at codecademy.com!

'''.READLINES() shows lines as individuals'''

with open('how_many_lines.txt') as lines_doc:
  for line in lines_doc.readlines():
    print(line)
# OUTPUT:
# 1. How many lines do we write on the daily,
#
# 2. Many money, we write many many many
#
# 3. How many lines do you write on the daily,
#
# 4. Say you say many money, you write many many many

with open('just_the_first.txt') as first_line_doc:
  first_line = first_line_doc.readline()
print(first_line)
#Output: You do look, my son, in a moved sort,

'''Writing to a file
With opens and closes the file. If you don't use with you must use close()

The second argument is to write file. The default is 'r' for read.

If the file name exists already 'w' will overwrite the file. 
'a' appends to the file instead of overwriting.
'''
# with open('generated_file.txt', 'w') as gen_file:
#   gen_file.write("What an incredible file!")

# with open('bad_bands.txt','w') as bad_bands_doc:
#   bad_bands_doc.write("Screamo bands are not for me.")

# with open('cool_dogs.txt','a') as cool_dogs_file:
#   cool_dogs_file.write('Air Buddy\n')

'''Opening without "with": '''
# fun_cities_file = open('fun_cities.txt', 'a')
#
# # We can now append a line to "fun_cities".
# fun_cities_file.write("Montréal")
#
# # But we need to remember to close the file
# fun_cities_file.close()

# with open('fun_file.txt') as close_this_file:
#
#   setup = close_this_file.readline()
#   punchline = close_this_file.readline()
#
#   print(setup)

'''Reading CSVs as text'''
# with open('logger.csv') as log_csv_file:
#   print(log_csv_file.read())

# import csv
#
# file_contents = []
# with open('cool_csv.csv', newline='') as cool_csv_file:
#   cool_csv_dict = csv.DictReader (cool_csv_file)
#   for row in cool_csv_dict:
#     file_contents.append(row['Cool Fact'])
#
# print(file_contents)

'''Reading CSVs with other delimeters than commas'''
# import csv
#
# with open('addresses.csv', newline='') as addresses_csv:
#   address_reader = csv.DictReader(addresses_csv, delimiter=';')
#   for row in address_reader:
#     print(row['Address'])

# import csv
#
# isbn_list = []
# with open('books.csv', newline='') as books_csv:
#   books_reader = csv.DictReader(books_csv, delimiter='@')
#   for row in books_reader:
#     isbn_list.append(row['ISBN'])

'''Writing to a CSV'''
# big_list = [{'name': 'Fredrick Stein', 'userid': 6712359021, 'is_admin': False}, {'name': 'Wiltmore Denis', 'userid': 2525942, 'is_admin': False}, {'name': 'Greely Plonk', 'userid': 15890235, 'is_admin': False}, {'name': 'Dendris Stulo', 'userid': 572189563, 'is_admin': True}]
#
# import csv
#
# with open('output.csv', 'w') as output_csv:
#   fields = ['name', 'userid', 'is_admin']
#   output_writer = csv.DictWriter(output_csv, fieldnames=fields)
#
#   output_writer.writeheader()
#   for item in big_list:
#     output_writer.writerow(item)

import csv

access_log = [{'time': '08:39:37', 'limit': 844404, 'address': '1.227.124.181'}, {'time': '13:13:35', 'limit': 543871, 'address': '198.51.139.193'}, {'time': '19:40:45', 'limit': 3021, 'address': '172.1.254.208'}, {'time': '18:57:16', 'limit': 67031769, 'address': '172.58.247.219'}, {'time': '21:17:13', 'limit': 9083, 'address': '124.144.20.113'}, {'time': '23:34:17', 'limit': 65913, 'address': '203.236.149.220'}, {'time': '13:58:05', 'limit': 1541474, 'address': '192.52.206.76'}, {'time': '10:52:00', 'limit': 11465607, 'address': '104.47.149.93'}, {'time': '14:56:12', 'limit': 109, 'address': '192.31.185.7'}, {'time': '18:56:35', 'limit': 6207, 'address': '2.228.164.197'}]

fields = ['time', 'address', 'limit']

with open('logger.csv', 'w') as logger_csv:
  log_writer = csv.DictWriter(logger_csv, fieldnames=fields)

  log_writer.writeheader()
  for item in access_log:
    log_writer.writerow(item)

'''Reading in a JSON file'''

# import json
#
# with open('message.json') as message_json:
#   message = json.load(message_json)
#
# print(message['text'])

'''Writing in a JSON file'''
# turn_to_json = {
#   'eventId': 674189,
#   'dateTime': '2015-02-12T09:23:17.511Z',
#   'chocolate': 'Semi-sweet Dark',
#   'isTomatoAFruit': True
# }

# import json
#
# with open('output.json', 'w') as json_file:
#   json.dump(turn_to_json, json_file)


# import json
#
# data_payload = [
#   {'interesting message': 'What is JSON? A web application\'s little pile of secrets.',
#    'follow up': 'But enough talk!'}
# ]
#
# with open('data.json', 'w') as data_json:
#   json.dump(data_payload, data_json)


Your code is mostly on the right track but has some issues to address for functionality and clarity. Here are the necessary fixes and adjustments:


import csv
import json

compromised_users = []
fields = ['Username']

#Read usernames from passwords.csv
with open('passwords.csv', newline='') as password_file:
    password_csv = csv.DictReader(password_file)
    for line in password_csv:
        compromised_users.append(line['Username'])

#Log compromised usernames to passwords.txt
with open('passwords.txt', 'w') as compromised_user_file:
    compromised_user_file.write("Compromised Usernames:\n")
    for username in compromised_users:
        compromised_user_file.write(f"{username}\n")

#Notify the boss via JSON
with open('boss_message.json', 'w') as boss_message:
    boss_message_dict = {"recipient": "The Boss", "message": "Mission Success"}
    json.dump(boss_message_dict, boss_message)

#Scramble passwords in new_passwords.csv with slash null signature
slash_null_sig = """_  _     ___   __  ____             
/ )( \   / __) /  \(_  _)            
) \/ (  ( (_ \(  O ) )(              
\____/   \___/ \__/ (__)             
 _  _   __    ___  __ _  ____  ____  
/ )( \ / _\  / __)(  / )(  __)(    \ 
) __ (/    \( (__  )  (  ) _)  ) D ( 
\_)(_/\_/\_/ \___)(__\_)(____)(____/ 
        ____  __     __   ____  _  _ 
 ___   / ___)(  )   / _\ / ___)/ )( \
(___)  \___ \/ (_/\/    \\___ \) __ (
       (____/\____/\_/\_/(____/\_)(_/
 __ _  _  _  __    __                
(  ( \/ )( \(  )  (  )               
/    /) \/ (/ (_/\/ (_/\             
\_)__)\____/\____/\____/
"""
with open('new_passwords.csv', 'w') as new_passwords_obj:
    new_passwords_obj.write(slash_null_sig)





