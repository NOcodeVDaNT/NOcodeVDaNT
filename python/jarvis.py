import pyttsx3  # Text-to-Speech
import speech_recognition as sr  # Voice Recognition
import webbrowser  # Web browsing
import datetime  # For date and time



def sptext():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        # Cancel background noise
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)
        try:
            print("Recognizing...")
            data = recognizer.recognize_google(audio)
            return data
        except sr.UnknownValueError:  # Corrected exception name
            print("Sorry, I did not understand that.")
        except sr.RequestError as e:  # Handles API connection issues
            print(f"Request Error: {e}")
            




def speak(text):
    # Initialize the pyttsx3 engine
    engine = pyttsx3.init()

    # Get the list of available voices
    voices = engine.getProperty('voices')
    

    # Select a specific voice (change the index to choose a different one)
    # For example, voices[0] is the default voice, voices[1] is often a different one.
    engine.setProperty('voice', voices[0].id)  # Change index as needed

    # Set speech rate (optional)
    engine.setProperty('rate', 150)

    # Set volume (optional)
    engine.setProperty('volume', 1)  # Volume from 0.0 to 1.0

    # Make the engine say the text
    engine.say(text)

    # Wait until the speech is finished
    engine.runAndWait()
    

    

    # Print all available voices
    for voice in voices:
        print(f"Voice ID: {voice.id}, Name: {voice.name}")


#if __name__ == "__main__":This construct allows you to define code that will only run when the script is executed directly, and not when it is imported as a module.
if __name__ == "__main__":
    
    if "ghost"in sptext().lower():
        
        speak("hi ghost , what can i do for you?")
        
        data1=sptext().lower()
        if "your name" in data1:
            speak("my name is ghost created by another ghost which is GOD for me , nice to meet you")
        elif "time"in data1:
            speak("the current time is " + str(datetime.datetime.now().strftime("%H:%M:%S%p")))
        elif "exit" or "sleep" in data1:
            speak("ok ghost , i will sleep now , good bye")
            
        
    else:
        print("sorry i will not assist you")    
        
        
    


