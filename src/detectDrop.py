
import matplotlib.pyplot as plt, IPython.display as ipd
from ipywidgets import interact
import numpy as np
import scipy
from scipy import signal
from scipy.io import wavfile
import librosa, librosa.display


# Trials
# 40 seconds is Drop
# 120 BPM

# 14 seconds is Drop
song = "Baauer - Yaow!.mp3"

y, sr = librosa.load(song)

tempo, beat_times = librosa.beat.beat_track(y=y, sr=sr, start_bpm=60, units='time')

'''
plt.figure(figsize=(14, 5))
librosa.display.waveplot(y, alpha=0.6)
plt.vlines(beat_times, -1, 1, color='r')
plt.ylim(-1, 1)
plt.show()
'''

D = librosa.stft(y)
times = librosa.frames_to_time(np.arange(D.shape[1]))
plt.figure()
ax1 = plt.subplot(2, 1, 1)
librosa.display.specshow(librosa.amplitude_to_db(D, ref=np.max),
                          y_axis='log', x_axis='time')
plt.title('Power spectrogram')

onset_env = librosa.onset.onset_strength(y=y, sr=sr)
plt.subplot(2, 1, 2, sharex=ax1)
plt.plot(times, 2 + onset_env / onset_env.max(), alpha=0.8,
          label='Mean (mel)')

onset_env = librosa.onset.onset_strength(y=y, sr=sr,
                                          aggregate=np.median,
                                          fmax=8000, n_mels=256)
plt.plot(times, 1 + onset_env / onset_env.max(), alpha=0.8,
          label='Median (custom mel)')

onset_env = librosa.onset.onset_strength(y=y, sr=sr,
                                          feature=librosa.cqt)
plt.plot(times, onset_env / onset_env.max(), alpha=0.8,
          label='Mean (CQT)')
plt.legend(frameon=True, framealpha=0.75)
plt.ylabel('Normalized strength')
plt.yticks([])
plt.axis('tight')
plt.tight_layout()

plt.show()