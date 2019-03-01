
import numpy as np

def quantization(sample, sf, ba, QCa, QCb):
    scaled_sample = sample / sf
    result = np.floor(2**float(ba-1)*QCa*scaled_sample * QCb)

    return result
