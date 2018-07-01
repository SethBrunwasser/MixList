import matplotlib.pyplot as plt, IPython.display as ipd
from ipywidgets import interact
import numpy as np
import scipy
from scipy import signal
from scipy.io import wavfile
import librosa, librosa.display
import winsound

# https://librosa.github.io/librosa/generated/librosa.util.match_events.html#librosa.util.match_events

def dtw_table(x, y, distance=None):
    if distance is None:
        distance = scipy.spatial.distance.euclidean
    nx = len(x)
    ny = len(y)
    table = np.zeros((nx+1, ny+1))
    
    # Compute left column separately, i.e. j=0.
    table[1:, 0] = np.inf
        
    # Compute top row separately, i.e. i=0.
    table[0, 1:] = np.inf
        
    # Fill in the rest.
    for i in range(1, nx+1):
        for j in range(1, ny+1):
            d = distance(x[i-1], y[j-1])
            table[i, j] = d + min(table[i-1, j], table[i, j-1], table[i-1, j-1])
    return table

def dtw(x, y, table):
    i = len(x)
    j = len(y)
    path = [(i, j)]
    while i > 0 or j > 0:
        minval = np.inf
        if table[i-1][j-1] < minval:
            minval = table[i-1, j-1]
            step = (i-1, j-1)
        if table[i-1, j] < minval:
            minval = table[i-1, j]
            step = (i-1, j)
        if table[i][j-1] < minval:
            minval = table[i, j-1]
            step = (i, j-1)
        path.insert(0, step)
        i, j = step
    return np.array(path)
y = librosa.feature.chroma_cens(y, sr=sr)
y2 = librosa.feature.chroma_cens(y2_stretch, sr=sr2)
D = dtw_table(y.T, y2.T, distance=scipy.spatial.distance.cityblock)
path = dtw(y.T, y2.T, D)
i1, i2 = librosa.frames_to_samples(path[300])
print(i1, i2)
wavfile.write('yaow common sequence with memba.wav', sr, y[i1:])
wavfile.write('memba common sequence with yaow.wav', sr2, y2_stretch[i2:])
