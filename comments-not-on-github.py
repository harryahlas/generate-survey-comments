#https://pub.towardsai.net/word-level-text-generation-dd61a5a0313d
import os
os.chdir("C:\\Users\\hahla\\Desktop\\github\\comments-not-on-github")


from tensorflow.keras.preprocessing.sequence import pad_sequences
from tensorflow.keras.layers import Embedding, LSTM, Dense, Dropout, Bidirectional
from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.models import Sequential
from tensorflow.keras.optimizers import Adam
from tensorflow.keras import regularizers
import tensorflow.keras.utils as ku 
import numpy as np
tokenizer = Tokenizer()
data = open('comments-not-on-github.txt').read()
corpus = data.lower().split("\n")
tokenizer.fit_on_texts(corpus)
total_words = len(tokenizer.word_index) + 1
# create input sequences using list of tokens
input_sequences = []
for line in corpus:
 token_list = tokenizer.texts_to_sequences([line])[0]
 for i in range(1, len(token_list)):
  n_gram_sequence = token_list[:i+1]
  input_sequences.append(n_gram_sequence)
# pad sequences 
max_sequence_len = max([len(x) for x in input_sequences])
input_sequences = np.array(pad_sequences(input_sequences, maxlen=max_sequence_len, padding='pre'))
# create predictors and label
predictors, label = input_sequences[:,:-1],input_sequences[:,-1]
label = ku.to_categorical(label, num_classes=total_words)
model = Sequential()
model.add(Embedding(total_words, 100, input_length=max_sequence_len-1))
model.add(Bidirectional(LSTM(150, return_sequences = True)))
model.add(Dropout(0.2))
model.add(LSTM(100))
model.add(Dense(total_words/2, activation='relu', kernel_regularizer=regularizers.l2(0.01)))
model.add(Dense(total_words, activation='softmax'))
model.compile(loss='categorical_crossentropy', optimizer='adam', metrics=['accuracy'])
model = Sequential()
model.add(Embedding(total_words, 100, input_length=max_sequence_len-1))
model.add(Bidirectional(LSTM(150, return_sequences = True)))
model.add(Dropout(0.2))
model.add(LSTM(100))
model.add(Dense(total_words/2, activation='relu', kernel_regularizer=regularizers.l2(0.01)))
model.add(Dense(total_words, activation='softmax'))
model.compile(loss='categorical_crossentropy', optimizer='adam', metrics=['accuracy'])
print(model.summary())

history = model.fit(predictors, label, epochs=100, verbose=1)
model.save('seq2seq50')

seed_text = "my manager is good at"
seed_text = "I should be paid more."
seed_text = "The customer service"
seed_text = "My benefits are good but I wish there was better life insurance."
next_words = 20
  
for _ in range(next_words):
 token_list = tokenizer.texts_to_sequences([seed_text])[0]
 token_list = pad_sequences([token_list], maxlen=max_sequence_len-1, padding='pre')
 predicted = model.predict_classes(token_list, verbose=0)
 output_word = ""
 for word, index in tokenizer.word_index.items():
  if index == predicted:
   output_word = word
   break
 seed_text += " " + output_word
print(seed_text)

from tensorflow import keras
model = keras.models.load_model('seq2seq50')


def print_next_words(seed_text,number_of_words_to_predict):
  for _ in range(number_of_words_to_predict):
   token_list = tokenizer.texts_to_sequences([seed_text])[0]
   token_list = pad_sequences([token_list], maxlen=max_sequence_len-1, padding='pre')
   predicted = model.predict_classes(token_list, verbose=0)
   output_word = ""
   for word, index in tokenizer.word_index.items():
    if index == predicted:
     output_word = word
     break
   seed_text += " " + output_word
  print(seed_text)


print_next_words("hello there", 3)

  
