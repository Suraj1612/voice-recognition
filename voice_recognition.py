import speech_recognition as sr
import pyttsx3 as pt
import pywhatkit as pk

# Initialize recognizer and text-to-speech engine
listening = sr.Recognizer()
engine = pt.init('dummy')

# Function to convert text to speech
def speak(text):
    engine.say(text)
    engine.runAndWait()

# Function to listen for voice commands
def hear():
    cmd = ""  # Initialize cmd with an empty string
    try:
        with sr.Microphone() as mic:
            print('Listening....')
            voice = listening.listen(mic)
            cmd = listening.recognize_google(voice)
            cmd = cmd.lower()
            if 'kodi' in cmd:
                cmd = cmd.replace('kodi', '')
                print(cmd)
    except Exception as e:
        print(f"Error: {e}")
    return cmd

# Function to process and execute commands
def run():
    cmd = hear()
    if cmd:  # Check if cmd is not an empty string
        print(cmd)
        if 'play' in cmd:
            song = cmd.replace('play', '')
            speak('Playing ' + song)
            pk.playonyt(song)
    else:
        print("No valid command heard.")

# Execute the run function
run()
