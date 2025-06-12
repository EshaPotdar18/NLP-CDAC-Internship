from gtts import gTTS
# Texto que deseas convertir a habla
texto = "mera naam esha hai"

# Crear un objeto gTTS
tts = gTTS(text=texto, lang='hi')

# Guardar el archivo de audio
tts.save("naam.wav")