from music_app.programme.utils import *
import numpy as np
import tensorflow as tf


def train():
    notes=getnotes()
    num_pitch=len(set(notes))
    network_input,network_output=prepare_sequence(notes,num_pitch)
    filepath = 'weight-{epoch:02d}-{loss:.4f}.hdf5'
    checkpoint=tf.keras.callbacks.ModelCheckpoint{
        filepath,
        moniter='loss'

    }







def prepare_sequence(notes,num_pitch):
    sequence_length=100
    pitch_name=sorted(set(notes))
    pitch_to_int= dict((pitch,num) for (num,pitch) in enumerate(pitch_name))
    network_input,network_output=[],[]
    for i in range(len(notes)-sequence_length):
        network_input.append(pitch_to_int[a] for a in notes[i:i+sequence_length])
        network_output.append(pitch_to_int[note[i+sequence_length]])
    network_input=np.reshape(network_input,(len(network_input),sequence_length,1))
    network_input=network_input /float(num_pitch)
    network_output=tf.keras.utils.to_categorical(network_output)
    return network_input,network_output
