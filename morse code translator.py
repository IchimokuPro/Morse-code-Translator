morse_code_dict = {
    'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.',
    'F': '..-.', 'G': '--.', 'H': '....', 'I': '..', 'J': '.---',
    'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---',
    'P': '.--.', 'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-',
    'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-', 'Y': '-.--',
    'Z': '--..',
    '1': '.----', '2': '..---', '3': '...--', '4': '....-', '5': '.....',
    '6': '-....', '7': '--...', '8': '---..', '9': '----.', '0': '-----',
    ' ': '/'
}

def text_to_morse(text):
    morse_code = []
    for char in text.upper():
        if char in morse_code_dict:
            morse_code.append(morse_code_dict[char])
        else:
            morse_code.append(char)
    return ' '.join(morse_code)

def morse_to_text(morse):
    morse_dict_reverse = {value: key for key, value in morse_code_dict.items()}
    morse_words = morse.split('/')
    text = []
    for word in morse_words:
        chars = word.split(' ')
        for char in chars:
            if char in morse_dict_reverse:
                text.append(morse_dict_reverse[char])
            else:
                text.append(char)
        text.append(' ')
    return ''.join(text)

if __name__ == "__main__":
    input_text = input("Enter text or Morse code: ")
    if '.' in input_text or '-' in input_text:
        translated_text = morse_to_text(input_text)
        print(f"Translated to text: {translated_text}")
    else:
        morse_code = text_to_morse(input_text)
        print(f"Translated to Morse code: {morse_code}")
