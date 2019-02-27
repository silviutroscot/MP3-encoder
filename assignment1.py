import numpy as np
from scipy.io import wavfile

def scaled_fft_db(x):
    # generate 512 point Hann window
    N = len(x)    # number of samples
    n = np.arange(N)

    # Compute the constant c for the Hann window
    w_cos = np.cos((2 * np.pi * n)/(N - 1))
    sum_sq = np.sum((w_cos/2)**2)
    c = np.sqrt((N-1)/sum_sq)

    # Apply the Hanning window
    x = x * c/2 * (1 - np.cos(2 * np.pi * n/(N - 1)))
    # compute the rfft of the input, weighted by the 512 points Hann window
    weighted_input_fft = np.abs(np.fft.rfft(x))

    # convert the amplitude to dBs for the non-zero samples
    non_zero_indices = np.where(weighted_input_fft != 0)[0]
    weighted_input_fft_in_db = 20*np.log10(weighted_input_fft[non_zero_indices])
    # normalize to have the maximum magnitude=96 dB
    weighted_input_fft_in_db = 96-max(weighted_input_fft_in_db) + weighted_input_fft_in_db
    
    return weighted_input_fft_in_db