# using re for regex expressions
import re

# morse code dictionary
morse_code_dict = {
    '.-': 'A', '-...': 'B', '-.-.': 'C', '-..': 'D', '.': 'E', '..-.': 'F', '--.': 'G', '....': 'H', 
    '..': 'I', '.---': 'J', '-.-': 'K', '.-..': 'L', '--': 'M', '-.': 'N', '---': 'O', '.--.': 'P', 
    '--.-': 'Q', '.-.': 'R', '...': 'S', '-': 'T', '..-': 'U', '...-': 'V', '.--': 'W', '-..-': 'X', 
    '-.--': 'Y', '--..': 'Z',
    '-----': '0', '.----': '1', '..---': '2', '...--': '3', '....-': '4', '.....': '5', 
    '-....': '6', '--...': '7', '---..': '8', '----.': '9',
    '.-.-.-': '.', '--..--': ',', '..--..': '?', '.----.': "'", '-.-.--': '!', '-..-.': '/', 
    '-.--.': '(', '-.--.-': ')', '.-...': '&', '---...': ':', '-.-.-.': ';', '-...-': '=', 
    '.-.-.': '+', '-....-': '-', '..--.-': '_', '.-..-.': '"', '...-..-': '$', '.--.-.': '@'
}

# text to morse code dictionary
text_to_morse_code = {
    'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.', 'G': '--.', 'H': '....',
    'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---', 'P': '.--.',
    'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-',
    'Y': '-.--', 'Z': '--..',
    '0': '-----', '1': '.----', '2': '..---', '3': '...--', '4': '....-', '5': '.....',
    '6': '-....', '7': '--...', '8': '---..', '9': '----.',
    '.': '.-.-.-', ',': '--..--', '?': '..--..', "'": '.----.', '!': '-.-.--', '/': '-..-.',
    '(': '-.--.', ')': '-.--.-', '&': '.-...', ':': '---...', ';': '-.-.-.', '=': '-...-',
    '+': '.-.-.', '-': '-....-', '_': '..--.-', '"': '.-..-.', '$': '...-..-', '@': '.--.-.'
}

# check if its valid morse code by using regex
# https://regexr.com i used this to build the expression
def is_valid_morse_code(morse_code):
    pattern = re.compile(r'^[.\- /]+$')
    return pattern.match(morse_code)

def decode_morse_code(morse_code):
    if not is_valid_morse_code(morse_code):
        return "Invalid Morse code input. Please enter valid Morse code."
    
    words = morse_code.split(' / ')
    decoded_message = []
    for word in words:
        letters = word.split()
        decoded_word = ''.join(morse_code_dict.get(letter, '') for letter in letters)
        decoded_message.append(decoded_word)  
    return ' '.join(decoded_message)

def encode_text_to_morse(text):
    text = text.upper()
    encoded_message = ' '.join(text_to_morse_code.get(char, '') for char in text if char in text_to_morse_code or char == ' ')
    return encoded_message


while(True):
    options_input = int(input("(1) For Encoding\n(2) For Decoding\n(9) To exit\n$:"))

    if int(options_input) == 1:
        input_to_encode = input("What would you like to encode ? ")
        print(f"Encoded : {encode_text_to_morse(input_to_encode)}")
    elif int(options_input) == 2:
        input_to_decode = input("What would you like to decode ? ")
        if not is_valid_morse_code(input_to_decode):
            print("Invalid morse code")
        else:
            print(f"Decoded : {decode_morse_code(input_to_decode)}")
    elif int(options_input) == 9:
        print("Exiting")
        break
    else:
        print("Please choose a menu option from above.\n")
