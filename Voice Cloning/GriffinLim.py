import librosa
import librosa.display
import matplotlib.pyplot as plt
import numpy as np
import soundfile as sf

# señal de audio
audio_path = r"C:\Users\lenovo\Desktop\CDAC Python\Celebrity Audio 2\naam.wav"
audio, sr = librosa.load(audio_path, sr=None)

# Calcular el espectrograma mel
mel_spectrogram = librosa.feature.melspectrogram(y=audio, sr=sr)

# Sintetizar la señal de audio con Griffin-Lim
audio_synthesized = librosa.feature.inverse.mel_to_audio(mel_spectrogram, sr=sr, hop_length=512, n_fft=2048)

# Visualizar y reproducir la señal original
librosa.display.waveshow(audio, sr=sr)
plt.title('Original Signal')
plt.show()

# Visualizar y reproducir la señal sintetizada con Griffin-Lim
librosa.display.waveshow(audio_synthesized, sr=sr)
plt.title('Synthesized Signal with Griffin-Lim')
plt.show()

# Guardar la señal sintetizada como archivo de audio WAV
output_path = "naam_Synthesized_griffin_lim.wav"
sf.write(output_path, audio_synthesized, sr)