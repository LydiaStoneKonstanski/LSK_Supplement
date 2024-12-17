
dirty_harry = "Go ahead, make my day."
split_hairs = dirty_harry.split("a")
print(split_hairs) #Output: ['Go ', 'he', 'd, m', 'ke my d', 'y.']

greeting = ["Hello", "my", "name", "is", "Earl"]
print('_'.join(greeting))

#list_of_lines = when_you_are_old.split('\n')

user_name = ":::::::: Eloise :::::::::::"
user_name_fixed = user_name.strip(':').strip()
print(user_name_fixed)

my_dict = {"name": "Ankit", "country": "India"}
my_delim = ":::"
x = my_delim.join(my_dict)

print(x)

def caesar_cipher(text, shift):
    """Encrypts or decrypts text using the Caesar cipher."""

    result = ""
    for char in text:
        if char.isalpha():
            # Get the ASCII value of the character
            char_code = ord(char)

            # Determine whether the character is uppercase or lowercase
            if char.isupper():
                start_code = ord('A')
            else:
                start_code = ord('a')

            # Shift the character code and wrap around if necessary
            shifted_code = (char_code - start_code + shift) % 26 + start_code

            # Convert the shifted code back to a character
            result += chr(shifted_code)
        else:
            # Leave non-alphabetic characters as they are
            result += char

    return result

def main():
    """Prompts the user for input and performs encryption/decryption."""

    while True:
        choice = input("Do you want to encrypt or decrypt? (e/d/q): ")
        if choice == 'e':
            text = input("Enter text to encrypt: ")
            shift = int(input("Enter shift value (1-25): "))
            print("Encrypted text:", caesar_cipher(text, shift))
        elif choice == 'd':
            text = input("Enter text to decrypt: ")
            shift = int(input("Enter shift value (1-25): "))
            print("Decrypted text:", caesar_cipher(text, -shift))
        elif choice == 'q':
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()

