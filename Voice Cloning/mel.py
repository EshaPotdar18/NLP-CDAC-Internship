import librosa
import librosa.display
import matplotlib.pyplot as plt
import numpy as np

# Load the Audio File
audio_path = r"C:\Users\lenovo\Desktop\CDAC Python\Celebrity Audio 2\naam.wav"
audio, sr = librosa.load(audio_path, sr=None)

# Compute the Mel Spectrogram
mel_spectrogram = librosa.feature.melspectrogram(y=audio, sr=sr)

# Visualize the Mel Spectrogram
librosa.display.specshow(librosa.power_to_db(mel_spectrogram, ref=np.max), y_axis='mel', x_axis='time')
plt.colorbar(format='%+2.0f dB')
plt.title('Mel Spectrogram')
plt.show()