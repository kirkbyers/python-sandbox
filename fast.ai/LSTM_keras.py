from theano.sandbox import cuda
cuda.use('gpu1')

from pathlib import Path

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
cs = 40
bs = 64
n_hidden = 512

sentences = []
next_chars = []
for i in range(0, len(idx) - cs+1):
	sentences.append(idx[i: i + cs])
	next_chars.append(idx[i+1: i+cs+1])

sentences = np.concatenate([[np.array(o)] for o in sentences[:-2]])
next_chars = np.concatenate([[np.array(o)] for o in next_chars[:-2]])

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

path_to_wgts = Path('fast_ai.h5')
if path_to_wgts.is_file():
	model.load_weights('fast_ai.h5')
else:
	f = open('fast_ai.h5', 'w+')

for i in range(11):
	model.fit(sentences, np.expand_dims(next_chars, -1), batch_size=bs, nb_epoch=1)
	model.save_weights('fast_ai.h5')

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
get_next_x(seed_text, 1000)
