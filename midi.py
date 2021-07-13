from mido import Message, MidiFile, MidiTrack
import random

mid = MidiFile()
track = MidiTrack()
mid.tracks.append(track)

ticksDict = {'unidad': 1920, 'mitad': 960, 'cuarto': 480, 'octavo': 240}
rhythmDict = {'unidad': 4, 'mitad': 2, 'cuarto': 1, 'octavo': .5}
probability = {'unidad': 1, 'mitad': 2, 'cuarto': 4, 'octavo': 6}
rhythmicNames = ['unidad', 'mitad', 'cuarto', 'octavo']
soloRhythm = []
sum = 0

track.append(Message('program_change', program=29, time=0))

def addNote(note):
    ticks = ticksDict[note]
    track.append(Message('note_on', note=59, velocity=100, time=0))
    track.append(Message('note_off', note=59, velocity=100, time=ticks))
    
while sum < 16:
    newNote = random.choice(rhythmicNames)
    filter = random.randint(1,10)
    if filter <= probability[newNote]:
        value = rhythmDict[newNote]
        sum += value
        if sum > 16:
            sum -= value
        else:
            soloRhythm.append(newNote)
            addNote(newNote)
        
    
print(soloRhythm)
mid.save('gtr_solos/gtr_solo_01.mid')

