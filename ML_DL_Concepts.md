## What is Machine Learning
Machine Learning is a field of study that enables computer programs to learn to do something. 
Unlike in traditional programs where the rules are coded for a program to make decisions or achieve something, in machine learning the program learns based on the data to take decisions or achieve something.


### What is Semisupervised Learning?
Semisupervised learning is based on partially labeled data. It is mostly a combination of supervised and unsupervised learnings.
Google photos tags a person in all photos available and it also tags another person in all those same photos available.
It groups a person in all photos - meaning it identifies that person A is in photos 1, 2, 4, 7 etc using unsupervised learning and it identifies that person A with his identity (name etc.) with supervised learning. Then all available photos where person A is present will be tagged with his name. This is an example of semisupervised learning.

### What is Reinforcement Learning?

## What are the challenges in Machine Learning
Mainly there are two challenges - bad algorithm and bad data
### Bad Data
Below are the examples of bad data

1. Insufficient quantity of training data
2. Non-representative data - sampling bias
3. Poor Quality data - errors in measurement, poor quality measurement, missing information (say 5% of the customers didn't enter age)
4. Irrelevant Features - 

### Bad Algorithm
#### Overfitting the training data

This happens when the model is too complex relative to the amount and noiseness of the training data
- Simply the model : regularlization, controlled by hyperparameter
- Gather more training data
- Reduce the noise in the training data

#### Underfitting the training data
- Selecting more powerful model 
- Feeding better features to the learning algorithm
- Reducing the constraints on the model (reduce regularization hyperparameter)




