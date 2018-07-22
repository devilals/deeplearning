## What is Machine Learning
Machine Learning is a field of study that enables computer programs to learn to do something. 
Unlike in traditional programs where the rules are coded for a program to make decisions or achieve something, in machine learning the program learns based on the data to take decisions or achieve something.


### What is Semisupervised Learning?
Semisupervised learning is based on partially labeled data. It is mostly a combination of supervised and unsupervised learnings.
Google photos tags a person in all photos available and it also tags another person in all those same photos available.
It groups a person in all photos - meaning it identifies that person A is in photos 1, 2, 4, 7 etc using unsupervised learning and it identifies that person A with his identity (name etc.) with supervised learning. Then all available photos where person A is present will be tagged with his name. This is an example of semisupervised learning.

### What is Reinforcement Learning?

### Examples of Supervised and Unsupervised learning
Supervised Learning:
1. Linear Regression
2. Neural Networks/Deep Learning
3. Decision Trees
4. Support Vector Machine (SVM)
5. K-Nearest neighbours

Unsupervised Learning:
1. Clustering Algorithms - K-means, Hierarchical Clustering Analysis (HCA)
2. Visualization and Dimensionality reduction - Principal component reduction (PCA), ...
3. Association rule learning


## What are the challenges in Machine Learning
Mainly there are two challenges - bad algorithm and bad data
### Bad Data
Below are the examples of bad data

1. Insufficient quantity of training data
2. Non-representative data - sampling bias
3. Poor Quality data - errors in measurement, poor quality measurement, missing information (say 5% of the customers didn't enter age)
4. Irrelevant Features (garbage in, garbage out)

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



## Trarining, Validation and Test set data
After the model is trained it has to be tested on new data to figure out how the model behaves on the new data.
For this purpose a subset of total data set (usually 20-30% of the total data) is kept aside for test data. This data is for evaluating the model for generalization error or test error.

Validation set: When there is a requirement to tune the hyperparameter and evaluating different models, there is a separate data required to evaluate the different hyperparameter values and then the best one is chosen. For this hyperparameter tuning another set of data is required which is from the training set and is called validation set.
When testing different models, to avoid wasting of too much data in validation another technique is adopted known as cross-validaiton. 
In cross-validaiton, the training data is divided into complimentary subsets and different model is trained and validated on different subset of the data. And finally the best model chosen is trained on full training data. 
Then this best model is tested with test data to know how it generalizes.



