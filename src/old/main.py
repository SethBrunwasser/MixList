from beatDetector import plot_audio_and_detect_beats
import scipy.io.wavfile as scipy
import os

beatDetector.
song = 'inimicvs x octn - trials.wav'
cwd = os.getcwd()
samplerate, data = scipy.read(cwd + '/' + song)
beatDetector.bpm_list