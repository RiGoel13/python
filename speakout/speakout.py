import win32com.client as wi

if __name__ == '__main__':
    print("welcome to Speak out")
    
    speak = wi.Dispatch("SAPI.Spvoice")
    speak.Speak("Power on!! you can type now")
    while True:
        x= input("What can i speak for you:")
        if x=="x":
            speak.Speak("Powering off")
            break
        command = f"{x}"
        speak.Speak(command)
        