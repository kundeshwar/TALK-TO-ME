from distutils.cmd import Command
import pyttsx3 as pt
import speech_recognition as sr


listener = pt.init()


speaker = sr.Recognizer()
try:
    with sr.Microphone() as source:
        print("listening pleses speak ....")
        voice = speaker.listen(source)
        Command = speaker.recognize_google(voice)
        print(Command)
        listener.say(Command)
        listener.runAndWait()

        
except:

    listener.say(" I don't understand anythings , please tell me again !")


