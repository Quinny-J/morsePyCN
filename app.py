# import flask to handle the web
# using os for file handling and re for regex expressions
from flask import Flask, render_template, request
import re

app = Flask(__name__)

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

# this is the index/main route of your lets say website 
@app.route('/', methods=['GET', 'POST'])
def index():
    # declare our variables for use later
    decoded_message = ''
    encoded_message = ''
    error_message = ''
    
    # check if we get a POST method and assign variable from the form data
    if request.method == 'POST':
        morse_code = request.form.get('morse_code', '').strip()
        action = request.form.get('action', '')
        
        # depending on the action data from the form 
        # do appropriate actions 
        if action == 'decode':
            if not is_valid_morse_code(morse_code): # check if its not valid morse code
                error_message = "Invalid Morse code input. Please enter valid Morse code."
            else:
                decoded_message = decode_morse_code(morse_code)
        
        elif action == 'encode':
            if is_valid_morse_code(morse_code): # check for morse code because you don't want to recode it
                error_message = "Don't try that its not how you encode something!"
            else:
                encoded_message = encode_text_to_morse(morse_code)
                print(encoded_message)
    # render html page from /templates and pass the data needed to display
    return render_template('index.html', decoded_message=decoded_message, encoded_message=encoded_message, error_message=error_message)

# tell flask to run the app or in this case our morsePy script for codenation
app.run()