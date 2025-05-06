alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z']
caesar = True


def caesar_cipher(text, shift_amount, cipher_direction):
    end_text = ""
    if cipher_direction == "decode":
        shift_amount *= -1
    for char in text:
        if char in alphabet:
            char_index = alphabet.index(char)

            new_char_index = char_index + shift_amount
            end_text += alphabet[new_char_index] if new_char_index < 26 else alphabet[new_char_index - 26]
        else:
            end_text += char
    print(f"the {cipher_direction}d text is : {end_text}")


while caesar:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    shift = shift % 26
    caesar_cipher(text, shift, direction)
    choice = input("Would you like to encrypt/decrypt again?")
    if choice == "n":
        print("Thanks for using this application")
        caesar = False