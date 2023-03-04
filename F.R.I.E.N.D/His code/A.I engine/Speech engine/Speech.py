import pyttsx3
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('John', voices[1].id)
def speak(audio):
    engine.say(audio)
    engine.runAndWait()
speak('Hello World')