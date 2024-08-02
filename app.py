# using re for regex expressions
import re
import colorama

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

# decode morse function based on provided input
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

# encode morse function based on provided input
def encode_text_to_morse(text):
    text = text.upper()
    encoded_message = ' '.join(text_to_morse_code.get(char, '') for char in text if char in text_to_morse_code or char == ' ')
    return encoded_message


while(True):
    # give the user some options and then check their input
    options_input = input(f"{colorama.Fore.BLACK}({colorama.Fore.YELLOW}1{colorama.Fore.BLACK}){colorama.Fore.WHITE} For Encoding\n{colorama.Fore.BLACK}({colorama.Fore.GREEN}2{colorama.Fore.BLACK}){colorama.Fore.WHITE} For Decoding\n{colorama.Fore.BLACK}({colorama.Fore.RED}9{colorama.Fore.BLACK}){colorama.Fore.WHITE} To exit\n{colorama.Fore.BLACK}${colorama.Fore.WHITE}:")
    
    if options_input == "1":
        input_to_encode = input(f"{colorama.Fore.BLUE}What would you like to encode ? ")
        print(f"{colorama.Fore.GREEN}Encoded{colorama.Fore.WHITE} : {encode_text_to_morse(input_to_encode)}")
    elif options_input == "2":
        input_to_decode = input(f"{colorama.Fore.BLUE}What would you like to decode ? ")
        if not is_valid_morse_code(input_to_decode):
            print("Invalid morse code")
        else:
            print(f"{colorama.Fore.RED}Decoded{colorama.Fore.WHITE} : {decode_morse_code(input_to_decode)}")
    elif options_input == "9":
        print(f"{colorama.Fore.RED}Exiting !")
        break
    else:
        print(f"{colorama.Fore.CYAN}Please choose a menu option from above.\n")
