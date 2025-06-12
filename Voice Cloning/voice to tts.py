import speech_recognition as sr

# Create a Recognizer Object
recognizer = sr.Recognizer()

# Capture Audio from the Microphone
with sr.Microphone() as source:
    print("Di algo:")
    audio = recognizer.listen(source, timeout=5)

# Recognize Speech using Google Speech API
try:
    texto = recognizer.recognize_google(audio, language="es-ES")
    print(f"Texto reconocido: {texto}")
except sr.UnknownValueError:
    print("No se pudo reconocer el audio")
except sr.RequestError as e:
    print(f"Error en la solicitud a Google API: {e}")