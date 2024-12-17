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