import glob
from music21 import converter,instrument,note,chord
import os
import pickle
def getnotes():

    notes=[]
    for midifile in glob.glob('C:/Users/Hideo/Desktop/nottingham-dataset-master/MIDI/*.mid'):
        stream=converter.parse(midifile)
        insts=instrument.partitionByInstrument(stream)
        if insts:
            part=insts.parts[0].recurse()
        else:
            part=stream.flat.notes
        for e in part:
            if isinstance(e,note.Note):
                notes.append(str(e.pitch))
            elif isinstance(e,chord.Chord):
                notes.append(','+str(n) for n in e.normalOrder)
    if not os.path.exists('data'):
        os.mkdir('data')
    with open ('data/notes','wb') as filepath:
        pickle.dump(notes,filepath)
    return notes