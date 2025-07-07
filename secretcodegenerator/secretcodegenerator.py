
import random
import string
MORSE_CODE_DICT = {
    'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.',
    'F': '..-.', 'G': '--.', 'H': '....', 'I': '..', 'J': '.---',
    'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---',
    'P': '.--.', 'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-',
    'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-', 'Y': '-.--',
    'Z': '--..', '1': '.----', '2': '..---', '3': '...--',
    '4': '....-', '5': '.....', '6': '-....', '7': '--...',
    '8': '---..', '9': '----.', '0': '-----', ',': '--..--',
    '.': '.-.-.-', '?': '..--..', '/': '-..-.', '-': '-....-',
    '(': '-.--.', ')': '-.--.-'
}

# Encoding function
def morse(word):
    cipher = ''
    for letter in word:
        if letter != ' ':
            cipher += MORSE_CODE_DICT.get(letter.upper(), '') + ' '
        else:
            cipher += ' '
    return cipher.strip()

# Decoding function
def dmorse(morse_code):
    morse_code += ' '
    decipher = ''
    citext = ''
    for letter in morse_code:
        if letter != ' ':
            citext += letter
        else:
            if citext != '':
                decipher += list(MORSE_CODE_DICT.keys())[list(MORSE_CODE_DICT.values()).index(citext)]
                citext = ''
            else:
                decipher += ' '
    return decipher




def ran():
 ra=random.choice(string.ascii_letters)
 return ra

st=input("Enter message: ")
words= st.split(" ")
morsecode=int(input("Enter 1 for normal coding enter 2 for morse coding: "))
if(morsecode==1):
 coding=int(input("enter 1 for coding 0 for decoding: "))
 if(coding==1): 
  neword=[]
  ran1=str()
  ran2=str()
  for word in words:
    si =  ran()+ran()+ran()+word[1:] + word[0] +ran()+ran()+ran()
    neword.append(si)
  print (" ".join(neword))    
  
 else: 
    neword=[]
    for word in words:
     si = word[3:-3]
     si = si[-1] + si[:-1]
     neword.append(si)
    print (" ".join(neword)) 
    
else: 
 coding = int(input("Enter 1 for encoding, 0 for decoding: "))
 if (coding == 1):
    words = st.split(" ")
    neword = [morse(word) for word in words]
    print("Encoded Morse Code:", "  ".join(neword))  # Double space between words
 else:
    words = st.strip().split("  ")  # Split by double space (between words)
    neword = [dmorse(word.strip()) for word in words]
    print("Decoded Text:", " ".join(neword))