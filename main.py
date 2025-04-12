import speech_recognition as sr
import webbrowser
import pyttsx3
import musiclibrary
recognizer = sr.Recognizer()
engine = pyttsx3.init()

def speak(text):
    # Converts text to speech.
    engine.say(text)
    engine.runAndWait()
    
def processCommand(c):
    if "open google" in c.lower():
        webbrowser.open("https://google.com")
    elif "open facebook" in c.lower():
        webbrowser.open("https://facebook.com")
    elif "open youtube" in c.lower():
        webbrowser.open("https://youtube.com")
    elif "open linkedin" in c.lower():
        webbrowser.open("https://linkedin.com")

    elif c.lower().startswith("play"):
        song = c.lower().replace("play", "").strip()
        try:
            link = musiclibrary.music[song]
            webbrowser.open(link)
        except KeyError:
            speak(f"Sorry, I couldn't find the song {song}.")

   


if __name__=="__main__":
    speak("Initializing...")
    while True:
        # Listen for the wake word
        # obtain audio from the microphone
        r = sr.Recognizer()

        print("Recognizing...")
        try:
            with sr.Microphone() as source:
                print("Listening...")
                audio = r.listen(source, timeout=2, phrase_time_limit=1)
            word = r.recognize_google(audio)
            if(word.lower() == "python"):
                speak("its on...")
                # Listen for command
                with sr.Microphone() as source:
                    print("Yup...")
                    audio = r.listen(source)
                    command = r.recognize_google(audio)

                    processCommand(command)


        except Exception as e:
            print("Error; {0}".format(e))