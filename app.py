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


@app.route('/', methods=['GET', 'POST'])
def index():
    decoded_message = ''
    encoded_message = ''
    error_message = ''
    
    if request.method == 'POST':
        morse_code = request.form.get('morse_code', '').strip()
        action = request.form.get('action', '')
        
        if action == 'decode':
            if not is_valid_morse_code(morse_code):
                error_message = "Invalid Morse code input. Please enter valid Morse code."
            else:
                decoded_message = decode_morse_code(morse_code)
        
        elif action == 'encode':
            if is_valid_morse_code(morse_code):
                error_message = "Don't try that its not how you encode something!"
            else:
                encoded_message = encode_text_to_morse(morse_code)
                print(encoded_message)
    
    return render_template('index.html', decoded_message=decoded_message, encoded_message=encoded_message, error_message=error_message)

app.run()