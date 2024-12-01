import win32com.client
import logging
# # Initialize text-to-speech engine
# engine = pyttsx3.init()
# engine.setProperty("rate", 150)  # Speed of speech
# engine.setProperty("volume", 1)  # Volume (0.0 to 1.0)
# # Function to speak text
def say(text):
    """Convert text to speech."""
    try:
        speaker = win32com.client.Dispatch("SAPI.SpVoice")
        voices = speaker.GetVoices()
        speaker.Voice = voices[1]
        speaker.Speak(text)
    except Exception as e:
        logging.error(f"Error in say function: {e}")
        print(f"Error in say function: {e}")
