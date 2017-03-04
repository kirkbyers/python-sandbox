import numpy as np
from numpy.random import choice

# Generic Keras imports
import keras
from keras import backend as K
from keras.utils.data_utils import get_file
from keras.utils import np_utils
from keras.utils.np_utils import to_categorical
from keras.models import Sequential, Model
from keras.layers import Input, Embedding, Reshape, merge, LSTM, Bidirectional
from keras.layers import TimeDistributed, Activation, SimpleRNN, GRU
from keras.layers.core import Flatten, Dense, Dropout, Lambda
from keras.regularizers import l2, activity_l2, l1, activity_l1
from keras.layers.normalization import BatchNormalization
from keras.optimizers import SGD, RMSprop, Adam
from keras.utils.layer_utils import layer_from_config
from keras.metrics import categorical_crossentropy, categorical_accuracy
from keras.layers.convolutional import *
from keras.preprocessing import image, sequence
from keras.preprocessing.text import Tokenizer

training_text = open('./The_Call_of_Cthulhu.txt').read()
chars = sorted(list(set(training_text)))
chars.insert(0, '\0')

# Create dict to lookup character index but character
char_indices = dict((c, i) for i, c in enumerate(chars))
# Create dict to lookup index by charater
indices_char = dict((i, c) for i, c in enumerate(chars))
#text converted to indexes
idx = [char_indices[c] for c in training_text]

vocab_size = len(chars)
n_fac = 24
#charater chucks
cs = 20
bs = 64
n_hidden = 256

model = Sequential([
                Embedding(vocab_size, n_fac, input_length=cs),
                LSTM(n_hidden, input_dim=n_fac, return_sequences=True, dropout_U=0.2, dropout_W=0.2, consume_less='gpu'),
                Dropout(0.2),
                LSTM(n_hidden, input_dim=n_fac, return_sequences=True, dropout_U=0.2, dropout_W=0.2, consume_less='gpu'),
                Dropout(0.2),
                TimeDistributed(Dense(vocab_size)),
                Activation('softmax')
        ])

model.compile(loss='sparse_categorical_crossentropy', optimizer=Adam())

model.load_weights('fast_ai.h5')

def get_next (inp):
        idxs = np.array([char_indices[c] for c in inp[-cs:]])[np.newaxis,:]
        preds = model.predict(idxs, verbose=0)[0][-1]
        preds = preds/np.sum(preds)
        return choice(chars, p=preds)

def get_next_x(inp, predict_length):
        result = '' + inp
        for i in range(predict_length):
                result += get_next(result[-cs:])

        return result

seed_text = 'professor had been stricken whilst returning from the Newport boat; falling suddenly, as witnesses said, after having been jostled by'
print(get_next_x(seed_text, 1000))

