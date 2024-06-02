import speech_recognition as sr
import pyttsx3
import datetime

def initialize_engine():
    """Initialize the text-to-speech engine."""
    engine = pyttsx3.init()
    engine.setProperty('rate', 150)  # Set the speaking rate (words per minute)
    return engine

def speak(text):
    """Convert text to speech."""
    engine.say(text)
    engine.runAndWait()

def listen_command():
    """Listen for voice command and convert it to text."""
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        recognizer.adjust_for_ambient_noise(source)  # Adjust for ambient noise
        audio = recognizer.listen(source)

    try:
        print("Recognizing...")
        command = recognizer.recognize_google(audio)
        print("You said:", command)
        return command.lower()
    except sr.UnknownValueError:
        print("Sorry, I didn't catch that.")
        return ""
    except sr.RequestError:
        print("Sorry, there was an error with the speech recognition service.")
        return ""

def process_command(command):
    """Process the user's voice command."""
    if "weather" in command:
        response = "The weather forecast for today is sunny."
    elif "play" in command:
        response = "Playing your favorite song."
    elif "my birthday" in command:
        response = "Your birthday date is January 1, 2003."  # Replace with your actual birthday date
    elif "university" in command:
        response = "You attend International University of Karachi (Dawood)."  # Replace with your university name
    elif "today's date" in command:
        today_date = datetime.date.today().strftime("%B %d, %Y")
        response = f"Today's date is {today_date}."
    else:
        response = "Sorry, I didn't understand that command."

    return response

if __name__ == "__main__":
    engine = initialize_engine()

    speak("Hello! I'm your voice assistant. How can I help you today?")

    while True:
        command = listen_command()
        response = process_command(command)
        speak(response)
