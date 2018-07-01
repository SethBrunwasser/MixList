
# This is a utility function that will return the Beats
# Per Minute (BPM) of a song.


import matplotlib.pyplot as plt, IPython.display as ipd
from ipywidgets import interact
import numpy as np
import scipy
from scipy import signal
from scipy.io import wavfile
import librosa, librosa.display
import winsound

# 40 seconds is Drop
# 120 BPM
song = "inimicvs x octn - trials.wav"

songMemba = "MEMBA - Villains & Coins (ft. DESAMPA).mp3"

songYaow = "Baauer - Yaow!.mp3"

y, sr = librosa.load(songYaow)
#sample_rate, data = wavfile.read(song)
y_percussive = librosa.effects.percussive(y)
tempo, beat_times = librosa.beat.beat_track(y=y, sr=sr, start_bpm=60, units='time')
#onset_times = librosa.onset.onset_detect(y_percussive, sr=sr, units='time')
print(tempo)
#print(beat_times)
y2, sr2 = librosa.load(songMemba)
tempo2, beat_times2 = librosa.beat.beat_track(y=y2, sr=sr2, start_bpm=60, units='time')
print(tempo2)

tempoDif = tempo/tempo2
y2_stretch = librosa.effects.time_stretch(y2, tempoDif)
tempoStretched, beat_timesStretched = librosa.beat.beat_track(y=y2_stretch, sr=sr2, start_bpm=60, units='time')
print(tempoStretched)

'''
plt.figure(figsize=(14, 5))
librosa.display.waveplot(y, alpha=0.6)
plt.vlines(beat_times, -1, 1, color='r')
plt.ylim(-1, 1)
plt.show()
'''
clicks = librosa.clicks(beat_timesStretched, sr=sr, length=len(y2_stretch))
yClicks = y2_stretch+clicks
#onsetClicks = librosa.clicks(onset_times, sr=sr, length=len(y))
#yOnsetClicks = y+onsetClicks
#wavfile.write('memba with onset clicks.wav', sr, yOnsetClicks)
#wavfile.write('memba stretched with clicks.wav', sr, yClicks)

'''
print(sample_rate, data.shape)
time = np.arange(0, float(data.shape[0]), 1) / sample_rate
print(data)
plt.subplot(211)
plt.plot(time, data[:,0], linewidth=0.01, alpha=0.7, color='#ff7f00')
plt.xlabel('time')
plt.ylabel('amplitude')
plt.subplot(212)
plt.specgram(data[:,0], Fs=sample_rate)
plt.xlabel('time (seconds)')
plt.ylabel('frequency')
plt.show()
'''