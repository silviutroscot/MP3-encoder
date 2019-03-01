import numpy as np
from scipy.io import wavfile

def subband_filtering(x, h):
    r = h * x
    q = np.arange(64)   
    c = np.sum((-1)**np.arange(8)[:, np.newaxis] * r[q + 64*np.arange(8)[:, np.newaxis]], axis=0)
    s = np.sum(np.cos(np.pi / 64. * (2 * np.arange(32)[:, np.newaxis] + 1) * (np.arange(q.shape[0]) - 16))*c, axis=1)
    return s
