from record import RecAUD
import glob
import numpy as np
import librosa
import math
from plot import plot_magnitude_spectrum

def note_transposition(file_name):
    musicalNoteDict = {0: 'A', 1: 'A#', 2: 'B', 3: 'C', 4: 'C#', 5: 'D', 6: 'D#', 7: 'E', 8: 'F', 9: 'F#', 10: 'G', 11: 'G#'}

    note_array, sr = librosa.load(f'//Users//shayaangandhi//Documents//python//MusicTransciption//{file_name}')
    note_ft = np.fft.fft(note_array)


    magnitude_spectrum = np.abs(note_ft)
    frequency = np.linspace(0, sr, len(magnitude_spectrum))
    f_ratio = 0.5

    

    
    #Check if there may exist multiple fundamental freqeuncies
    secondMaxIndex = -1
    maxIndex = -1
    secondMaxVal = -1
    maxVal = -1
    for i in range(len(magnitude_spectrum[:int(len(frequency) * f_ratio)])):
        if magnitude_spectrum[i] > maxVal:
            maxIndex = i
            maxVal = magnitude_spectrum[i]
        elif magnitude_spectrum[i] > secondMaxVal:
            secondMaxIndex = i
            secondMaxVal = magnitude_spectrum[i]
    

    #print((maxVal,frequency[maxIndex]), (secondMaxVal, frequency[secondMaxIndex]))
    chord = False

    #200 are chose kinda randomely lol
    if maxVal - secondMaxVal < 200:
        chord = True

    #Individual Notes

    if not chord:
        fundamental_frequency = frequency[maxIndex]
        keyNumber = round((12*(math.log((fundamental_frequency)/440, 2))) + 49)
        note = musicalNoteDict[(keyNumber-1)%12]
        octave = ((keyNumber - 1) // 12) + 1
        #print((note, octave))
        return [(note, octave)]
        

    threshold = 300

    frequencies_played = []
    keys_played = []
    notes_played = []

    for i in range(len(magnitude_spectrum[:int(len(frequency) * f_ratio)])):
        if magnitude_spectrum[i] > threshold:
            frequencies_played.append(frequency[i])
            keyNumber = round((12*(math.log((frequency[i])/440, 2))) + 49)
            if keyNumber not in keys_played:
                keys_played.append(keyNumber)
            note = musicalNoteDict[(keyNumber-1)%12]
            octave = ((keyNumber - 1) // 12) + 1
            if (note, octave) not in notes_played:
                notes_played.append((note, octave))

    #print(frequencies_played)
    #print(keys_played)
    #print(notes_played)

    #plot_magnitude_spectrum(note_ft, 'note', sr, f_ratio)


    return notes_played