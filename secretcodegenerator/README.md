
# Morse Code Encoder/Decoder with Random String Manipulation

This Python script allows you to encode and decode messages using **Morse code**. It also has the ability to encode/modify messages by randomly manipulating letters in a custom way.

## Features

- **Morse Code Encoding and Decoding**: It will convert the text to Morse code and vice versa.
- **Custom Random String Manipulation**: It alter words by randomly changing their letters for obfuscation.
- **Easy to use**: Give message as input, choose your operation, and let the script handle the rest.


## How to Run

```bash
python morse_random.py
```

## How It Works

1. The script prompts for a message input.
2. You can choose to:
    - Encode or decode a message using **Morse code**.
    - Encode or decode using a **random string manipulation** technique.
3. Based on your choices, it will either:
    - Convert the text into Morse code or decode the Morse code back to plain text.
    - Modify the letters of each word randomly for encoding and reverse the transformation for decoding.

### Example Output

```bash
Enter message: Hello World
Enter 1 for normal coding enter 2 for morse coding: 1
Enter 1 for coding 0 for decoding: 1
hTleo llWor d!gs
```

For Morse Code:
```bash
Enter message: Hello World
Enter 2 for morse coding: 2
Enter 1 for encoding, 0 for decoding: 1
Encoded Morse Code: .... . .-.. .-.. ---   .-- --- .-. .-.. -.. 
```
