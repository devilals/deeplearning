
# coding: utf-8

# # Analyzing IMDB Data in Keras

# In[32]:


# Imports
import numpy as np
import keras
from keras.datasets import imdb
from keras.models import Sequential
from keras.layers import Dense, Dropout, Activation
from keras.preprocessing.text import Tokenizer
import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')

np.random.seed(42)


# ## 1. Loading the data
# This dataset comes preloaded with Keras, so one simple command will get us training and testing data. There is a parameter for how many words we want to look at. We've set it at 1000, but feel free to experiment.

# In[33]:


# Loading the data (it's preloaded in Keras)
(x_train, y_train), (x_test, y_test) = imdb.load_data(num_words=1000)

print(x_train.shape)
print(x_test.shape)


# ## 2. Examining the data
# Notice that the data has been already pre-processed, where all the words have numbers, and the reviews come in as a vector with the words that the review contains. For example, if the word 'the' is the first one in our dictionary, and a review contains the word 'the', then there is a 1 in the corresponding vector.
# 
# The output comes as a vector of 1's and 0's, where 1 is a positive sentiment for the review, and 0 is negative.

# In[34]:


print(x_train[0])
print(y_train[0])


# ## 3. One-hot encoding the output
# Here, we'll turn the input vectors into (0,1)-vectors. For example, if the pre-processed vector contains the number 14, then in the processed vector, the 14th entry will be 1.

# In[35]:


# One-hot encoding the output into vector mode, each of length 1000
tokenizer = Tokenizer(num_words=1000)
x_train = tokenizer.sequences_to_matrix(x_train, mode='binary')
x_test = tokenizer.sequences_to_matrix(x_test, mode='binary')
print(x_train[0])


# And we'll also one-hot encode the output.

# In[36]:


# One-hot encoding the output
num_classes = 2
y_train = keras.utils.to_categorical(y_train, num_classes)
y_test = keras.utils.to_categorical(y_test, num_classes)
print(y_train.shape)
print(y_test.shape)


# ## 4. Building the  model architecture
# Build a model here using sequential. Feel free to experiment with different layers and sizes! Also, experiment adding dropout to reduce overfitting.

# In[67]:


# TODO: Build the model architecture
movieRAnalyzer = Sequential()
print(x_train.shape[1])
movieRAnalyzer.add(Dense(32,input_dim=x_train.shape[1]))
movieRAnalyzer.add(Activation("sigmoid"))
movieRAnalyzer.add(Dense(2))
movieRAnalyzer.add(Activation("sigmoid"))

movieRAnalyzer.add(Dropout(0, noise_shape=None, seed=None))
# TODO: Compile the model using a loss function and an optimizer.
movieRAnalyzer.compile(loss="categorical_crossentropy", optimizer="adam", metrics = ['accuracy'])


# ## 5. Training the model
# Run the model here. Experiment with different batch_size, and number of epochs!

# In[68]:


# TODO: Run the model. Feel free to experiment with different batch sizes and number of epochs.
# Uncomment this line to print the model architecture
movieRAnalyzer.summary()

# Fitting the model
history = movieRAnalyzer.fit(x_train, y_train, batch_size=100, epochs=10, verbose=0)



# ## 6. Evaluating the model
# This will give you the accuracy of the model, as evaluated on the testing set. Can you get something over 85%?

# In[69]:


score = movieRAnalyzer.evaluate(x_test, y_test, verbose=0)
print("Accuracy: ", score[1])

