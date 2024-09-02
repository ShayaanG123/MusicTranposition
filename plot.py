
import numpy as np
import matplotlib.pyplot as plt



def plot_magnitude_spectrum(ft, title, sr, f_ratio = 1):
    magnitude_spectrum = np.abs(ft)

    plt.figure(figsize = (18,5))
    frequency = np.linspace(0, sr, len(magnitude_spectrum))
    num_frequency_bins = int(len(frequency) * f_ratio)

    plt.plot(frequency[:num_frequency_bins], magnitude_spectrum[:num_frequency_bins])
    plt.xlabel('Frequency')
    plt.title(title)

    plt.show()