from record import RecAUD
import wave
import librosa
import soundfile as sf
import os
from noteTransposition import note_transposition
from graphic import MusicSheet

time_signature = input('What score will you be playing in today? ')
beats_per_measure = int(time_signature[0])
beat_type = time_signature[2]

metronome = input('What metronome pace will you be using bpm? ')

minutes_per_beat = 1/int(metronome)
seconds_per_beat = minutes_per_beat * 60
length_of_measure = beats_per_measure * seconds_per_beat


guiAUD = RecAUD()

# First load the file
file_name = 'test_recording.wav'
audio, sr = librosa.load(f'//Users//shayaangandhi//Documents//python//MusicTransciption//{file_name}')

buffer = round(seconds_per_beat * sr)

samples_total = len(audio)
samples_wrote = 0
counter = 1

#Create Folder for audios
'''
path = '//Users//shayaangandhi//Documents//python//MusicTransciption'
os.chdir(path)
NewFolder = 'splitAudios'
os.makedirs(NewFolder)
'''


while samples_wrote < samples_total:

    #check if the buffer is not exceeding total samples 
    if buffer > (samples_total - samples_wrote):
        buffer = samples_total - samples_wrote

    block = audio[samples_wrote:(samples_wrote + buffer)]
    out_filename = "split_" + str(counter) + "_" + file_name


    # Write segment
    sf.write(out_filename, block, sr)
    counter += 1
    samples_wrote += buffer


    #Move Files to Folder
    '''
    destination = f'//Users//shayaangandhi//Documents//python//MusicTransciption//{NewFolder}'
    os.replace(out_filename, destination)
    '''


sequence_of_notes = []

for i in range(1,counter):
    split_filename = "split_" + str(i) + "_" + file_name
    notes = note_transposition(split_filename)
    print(notes)
    sequence_of_notes.append(notes)

print('\n\n')


notesPlacement = {'A': 11,'A#': 10,'B': 9,'C' : 8,'C#': 7,'D': 6,'D#': 5,'E': 4,'F': 3,'F#': 2,'G': 1,'G#': 0}
occurenceDict = {'A': 0,'A#': 0,'B': 0,'C' : 0,'C#': 0,'D': 0,'D#': 0,'E': 0,'F': 0,'F#': 0,'G': 0,'G#': 0}
if __name__ == "__main__":
    displacement = 5
    app = MusicSheet(time_signature)
    x = 150
    count = 0
    for j in range(len(sequence_of_notes)):
        if sequence_of_notes[j] == []:
            count += 1
        else:
            break
    sequence_of_notes = sequence_of_notes[count:]
    leftSide = 50
    topSide = 60
    for c in range(len(sequence_of_notes)):
        for note, octave in sequence_of_notes[c]:
            position = notesPlacement[note] * displacement
            if occurenceDict[note] != 0:
                occurenceDict[note] -= 1
                continue
            count = 0
            for i in range(1,4):
                for (note_check, octave_check) in sequence_of_notes[c+1]:
                    if note == note_check:
                        count += 1
                        break
                if count != count + i:
                    break
            occurenceDict[note] = count
            print((note, count))
            if count == 0:
                app.draw_quarter_note(x, topSide + 50 + position)
            elif count == 1:
                app.draw_half_note(x, topSide + 50 + position)
            elif count == 2:
                app.draw_dotted_half_note(x, topSide + 50 + position)
            else:
                app.draw_whole_note(x, topSide + 50 + position)
            
        if x >= 700:
            x = 100
            topSide += 200
            app.draw_entire_section(leftSide, topSide, time_signature)

        x += 50

    app.mainloop()

