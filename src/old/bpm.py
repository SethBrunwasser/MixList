import pyaudio
import scipy.io.wavfile as scipy
from pydub import AudioSegment
import os
import numpy as np
import matplotlib.pyplot as plt

def get_bpm():
   return True

def check_filetype(file):
    if file.endswith('.mp3'):
        return False
    else:
        return True

def conform_to_wav(file, cwd):
    if not check_filetype(file):
        print(file)
        sound = AudioSegment.from_file(file, format='mp3')
        sound.export(file, format='wav')
        print('Successfully Converted .mp3 to .wav')

if __name__ == '__main__':
    dir = os.listdir()
    songs = [item for item in dir if '.mp3' in item or '.wav' in item]
    cwd = os.getcwd()
    song = 'inimicvs x octn - trials.wav'

    samplerate, data = scipy.read(cwd + '/' + song)
    print(len(data))

    monoChannel = data.mean(axis=1)

    plt.plot(monoChannel)
    plt.ylabel('sound data range')
    plt.show()

    print(np.where(monoChannel == max(monoChannel)))
    differences = np.diff(monoChannel)
    maxIndex = np.where(differences == max(differences))
    print(maxIndex)
    print(maxIndex[0][0])
    dropIndex = 43*samplerate
    slicedData = monoChannel[:dropIndex]
    plt.plot(slicedData)
    plt.ylabel('sliced data range')
    plt.show()
    #scipy.write(cwd + '/' + 'new_sliced_song.wav', samplerate, slicedData)