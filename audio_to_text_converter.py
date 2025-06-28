import speech_recognition as sr

# Initialize recognizer
recognizer = sr.Recognizer()

# Load your audio file (WAV is easiest)
audio_file = r"sample_audio.wav"  # Replace with your file path

with sr.AudioFile(audio_file) as source:
    print("Listening to audio...")
    audio_data = recognizer.record(source)

try:
    # Recognize speech using Google's free API
    print("Transcribing audio...")
    text = recognizer.recognize_google(audio_data)
    print("Transcription:\n", text)

except sr.UnknownValueError:
    print("Sorry, I could not understand the audio.")
except sr.RequestError as e:
    print(f"Could not request results from Google Speech Recognition service; {e}")
