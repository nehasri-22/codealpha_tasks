import glob
import random
from collections import defaultdict
from music21 import converter, instrument, note, chord, stream
notes = []
midi_files = glob.glob("midi_dataset/*.mid")
print("Loading MIDI files...")
for file in midi_files:
    print("Parsing:", file)
    midi = converter.parse(file)
    parts = instrument.partitionByInstrument(midi)
    if parts:
        notes_to_parse = parts.parts[0].recurse()
    else:
        notes_to_parse = midi.flat.notes
    for element in notes_to_parse:
        if isinstance(element, note.Note):
            notes.append(str(element.pitch)
        elif isinstance(element, chord.Chord):
            notes.append('.'.join(str(n) for n in element.normalOrder))
print("Total Notes:", len(notes))
markov_model = defaultdict(list)
for i in range(len(notes) - 1):
    current_note = notes[i]
    next_note = notes[i + 1]
    markov_model[current_note].append(next_note)
print("Markov model created!")
generated_notes = []
current_note = random.choice(notes)
generated_notes.append(current_note)
for i in range(300):
    possible_next_notes = markov_model[current_note]
    if not possible_next_notes:
        break
    next_note = random.choice(possible_next_notes)
    generated_notes.append(next_note)
    current_note = next_note
print("Music generation complete!")
output_notes = []
offset = 0
for pattern in generated_notes:
    if ('.' in pattern) or pattern.isdigit():
        notes_in_chord = pattern.split('.')
        chord_notes = []
        for current_note in notes_in_chord:
            new_note = note.Note(int(current_note))
            new_note.storedInstrument = instrument.Piano()
            chord_notes.append(new_note)
        new_chord = chord.Chord(chord_notes)
        new_chord.offset = offset
        output_notes.append(new_chord)
    else:
        new_note = note.Note(pattern)
        new_note.offset = offset
        new_note.storedInstrument = instrument.Piano()
        output_notes.append(new_note)
    offset += 0.5
midi_stream = stream.Stream(output_notes)
midi_stream.write('midi', fp='generated_music.mid')
print("Generated music saved as generated_music.mid")
