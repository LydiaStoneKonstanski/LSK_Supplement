def caesar_cipher_decode(text, shift):
    decoded = ''
    shift = -shift
    for char in text:
        if char.isalpha():
            given_code = ord(char)

            if char.isupper():
                start_code = ord('A')
            else:
                start_code = ord('a')

            shift_code = (given_code - start_code - shift) % 26 + start_code
            decoded += chr(shift_code)
        else:
            decoded += char

    return decoded


third_message = "vhfinmxkl atox kxgwxkxw tee hy maxlx hew vbiaxkl hulhexmx. px'ee atox mh kxteer lmxi ni hnk ztfx by px ptgm mh dxxi hnk fxlltzxl ltyx."


def try_them_all(text):
    for i in range(1, 26):
        print(caesar_cipher_decode(text, i))


try_them_all(third_message)


def caesar_cipher_encode(text, shift):
    decoded = ''
    for char in text:
        if char.isalpha():
            given_code = ord(char)

            if char.isupper():
                start_code = ord('A')
            else:
                start_code = ord('a')

            shift_code = (given_code - start_code - shift) % 26 + start_code
            decoded += chr(shift_code)
        else:
            decoded += char

    return decoded

message = "xuo jxuhu! jxyi yi qd unqcfbu ev q squiqh syfxuh. muhu oek qrbu je tusetu yj? y xefu ie! iudt cu q cuiiqwu rqsa myjx jxu iqcu evviuj!"

print(caesar_cipher_decode(message, 10)) #Output: hey there! this is an example of a caesar cipher. were you able to decode it? i hope so! send me a message back with the same offset!

to_vishal = "Hi Vishal, Can you read my super-secret message?"

to_vishal_encoded = caesar_cipher_encode(to_vishal, 10)
print(to_vishal_encoded) #Output: Xy Lyixqb, Sqd oek huqt co ikfuh-iushuj cuiiqwu?

#Testing
print(caesar_cipher_decode(to_vishal_encoded, 10)) #Output: Hi Vishal, Can you read my super-secret message?

first_message = 'jxu evviuj veh jxu iusedt cuiiqwu yi vekhjuud.'
second_message = 'bqdradyuzs ygxfubxq omqemd oubtqde fa oapq kagd yqeemsqe ue qhqz yadq eqogdq!'

print(caesar_cipher_decode(first_message, 10)) #Output: the offset for the second message is fourteen.
print(caesar_cipher_decode(second_message, 14)) #Output: performing multiple caesar ciphers to code your messages is even more secure!

third_message = "vhfinmxkl atox kxgwxkxw tee hy maxlx hew vbiaxkl hulhexmx. px'ee atox mh kxteer lmxi ni hnk ztfx by px ptgm mh dxxi hnk fxlltzxl ltyx."

#Checks every shift option
def try_them_all(text):
    for i in range(1, 26):
        print(caesar_cipher_decoder(text, i))

try_them_all(third_message)

fourth_message = 'txm srom vkda gl lzlgzr qpdb? fepb ejac! ubr imn tapludwy mhfbz cza ruxzal wg zztcgcexxch!'
keyword_to_fourth = 'friends'
alphabet = 'abcdefghijklmnopqrstuvwxyz'


def vigenere_decoder(text, keyword):
    # def vigenere_decode(message, keyword):
    keyword_phrase = ""
    keyword_index = 0

    for char in text:
        if keyword_index >= len(keyword):
            keyword_index = 0
        if char.isalpha():
            keyword_phrase += keyword[keyword_index]
            keyword_index += 1
        else:
            keyword_phrase += char

    decoded_message = ""

    for i in range(len(text)):
        if text[i] in alphabet:
            old_character_index = alphabet.find(text[i])
            offset_index = alphabet.find(keyword_phrase[i])
            new_character = alphabet[(old_character_index + offset_index) % 26]
            decoded_message += new_character
        else:
            decoded_message += text[i]

    return decoded_message

vigenere_message = "txm srom vkda gl lzlgzr qpdb? fepb ejac! ubr imn tapludwy mhfbz cza ruxzal wg zztcgcexxch!"
vigenere_keyword = "friends"

print(vigenere_decoder(vigenere_message, vigenere_keyword))


# key_to_num = []
# decoded = ''
# shift = -
# for char in keyword:
#     if char.isalpha():
#         given_key = ord(char)
#         key_to_num.append(given_key)

# #return key_to_num
#         for char in text:
#             if char.isalpha():
#                 given_key = ord(char)

#                 if char.isupper():
#                     start_code = ord('A')
#                 else:
#                     start_code = ord('a')

# print(vigenere_decoder(fourth_message, keyword_to_fourth))

def vigenere_encoder(text, keyword):
    keyword_phrase = ""
    keyword_index = 0

    for char in text:
        if keyword_index >= len(keyword):
            keyword_index = 0
        if char.isalpha():
            keyword_phrase += keyword[keyword_index]
            keyword_index += 1
        else:
            keyword_phrase += char

    encoded_message = ""

    for i in range(len(text)):
        if text[i] in alphabet:
            old_character_index = alphabet.find(text[i])
            offset_index = alphabet.find(keyword_phrase[i])
            new_character = alphabet[(old_character_index - offset_index) % 26]
            encoded_message += new_character
        else:
            encoded_message += text[i]

    return encoded_message

fifth_message = "Cryptography is fun!"
print(vigenere_encoder(fifth_message, 'potential')) #Output: Cdflgvyrpatf ef mmn!