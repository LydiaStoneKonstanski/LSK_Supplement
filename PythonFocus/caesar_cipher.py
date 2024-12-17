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