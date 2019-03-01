
from scipy import signal
import numpy as np

def prototype_filter():
    lowpass_points_number = 512
    Fs = np.pi
    pass_frequency = Fs/128 # as the bandwidth is pi/64, and it is symmetrical around 0
    stop_frequency = np.pi/32

    h = signal.remez(lowpass_points_number, [0, pass_frequency/2, stop_frequency/2, Fs/2], [2, 0], fs=Fs)
    return h



