import numpy as np
import scipy
import matplotlib.pyplot as plt

DATA = scipy.io.loadmat('hw1-1.mat', squeeze_me=True)
DURATION = DATA['duration']
FS = DATA['fs']
PHASE = DATA['phase']
RANGE_FFT = DATA['RangeFFT']
WAVELENGTH_mm = 4  # Wavelength of mmWave signals in mm
WAVELENGTH_m = WAVELENGTH_mm / 1000  # Wavelength of mmWave signals in m
SAMPLING_RATE = 500  # Sampling rate in Hz


def respiration_cycles(phase: np.ndarray = PHASE) -> float:
    """
    Calculate the number of respiration cycles
    :param phase: The phase signal
    :return: The number of respiration cycles
    """
    # Calculate the FFT of the phase signal
    fft_result = np.fft.fft(phase)

    # Calculate the corresponding frequencies
    frequencies = np.fft.fftfreq(len(phase), 1 / FS)

    # Find the index corresponding to the peak frequency
    lower_freq_limit = 0.0000001
    upper_freq_limit = 5
    mask = (frequencies >= lower_freq_limit) & (frequencies <= upper_freq_limit)

    # Find the index of the maximum value within the specified frequency range
    peak_index = np.argmax(np.abs(fft_result[mask]))

    # Calculate the corresponding frequency of the peak
    peak_frequency = frequencies[mask][peak_index]

    # Calculate the number of respiration cycles
    number_of_respiration_cycles = peak_frequency * DURATION

    return number_of_respiration_cycles


def heart_rate(phase: np.ndarray = PHASE) -> float:
    """
    Calculate the heart rate (BPM)
    :param phase: The phase signal
    :return: The heart rate in beats per minute
    """
    # Calculate the FFT of the phase signal
    fft_result = np.fft.fft(phase)

    # Calculate the corresponding frequencies
    frequencies = np.fft.fftfreq(len(phase), 1 / FS)

    # Find the index corresponding to the peak frequency
    # Assuming heart rate is in a higher frequency range.
    lower_freq_limit = 1 
    upper_freq_limit = 2
    mask = (frequencies >= lower_freq_limit) & (frequencies <= upper_freq_limit)

    # Find the index of the maximum value within the specified frequency range
    peak_index = np.argmax(np.abs(fft_result[mask]))

    # Calculate the corresponding frequency of the peak
    peak_frequency = frequencies[mask][peak_index]

    # Calculate the heart rate
    heart_rate_in_bpm = peak_frequency * 60

    return heart_rate_in_bpm


def extract_phase_signal(range_fft_data):
    # Perform the necessary processing to obtain the phase signal
    phase_signal = np.angle(range_fft_data)
    return phase_signal


if __name__ == '__main__':
    print(respiration_cycles())
    print(heart_rate())
    phase_signal = extract_phase_signal(RANGE_FFT)
    print(respiration_cycles(phase_signal))
    print(heart_rate(phase_signal))
