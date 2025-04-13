#Speak Out – Python Text-to-Speech using Windows SAPI#
This is a basic voice assistant created with Python and Microsoft's Speech API (SAPI) on Windows. It lets users input text and listen to it read out.
---
##Features##
Utilizes pywin32 in order to interface with the Windows pre-installed TTS engine
Reads out any text you input
Graciously powers off with a verbal "Powering off" message
Interactive and friendly CLI
---
##Requirements
Python 3.x
Windows OS (as it uses SAPI.SpVoice)
pywin32 module
Install pywin32:
pip install pywin32
---
##How It Works
Initializes the speech engine (SAPI.SpVoice)
Asks user for input repeatedly
Speaks the text typed
Exits when user types x
---
##Sample Run
~~~
bash
What can i speak for you: Hello, how are you? (Speaks: "Hello, how are you?")

What can i speak for you: Have a nice day! (Speaks: "Have a nice day!")

What can i speak for you: x (Speaks: "Powering off")
~~~
---
##Notes
The script works only on Windows because it utilizes SAPI.SpVoice.
To make it cross-platform, you may look into libraries such as pyttsx3.
---
##License
This project is under the MIT License.
