
# Speak Out - Text to Speech in Python

This is a basic **Text-to-Speech (TTS)** Python program using the built-in **Microsoft Speech API (SAPI)** via the `win32com.client` module.

## Features


- Interactive console interface
- Speaks whatever you type
- Says "Power on" when you start
- Quits nicely when you type `x`

## Requirements

- Windows OS (uses Windows SAPI)
- Python installed
- `pywin32` library


##  How It Works

- On startup, the program says "Power on!! you can type now".
- You can type anything and the program will read it aloud.
- To quit, type `x`.

##  Example Output

```bash
welcome to Speak out
What can i speak for you: Hello world
(Speaks: Hello world)
What can i speak for you: x
(Speaks: Powering off)
```
