import speech_recognition as sr

def speech_to_text():
    """Convert speech to text using microphone input."""
    recognizer = sr.Recognizer()

    with sr.Microphone() as source:
        print("Speak something...")
        recognizer.adjust_for_ambient_noise(source)  # Adjust for background noise
        audio = recognizer.listen(source)  # Listen to speech

    try:
        text = recognizer.recognize_google(audio)  # Convert speech to text
        print("You said:", text)
    except sr.UnknownValueError:
        print("Could not understand the audio")
    except sr.RequestError:
        print("Error connecting to Google API")

# Run the function
speech_to_text()