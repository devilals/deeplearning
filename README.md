# Deep-Learning
Projects from Deep Learning Nanodegree on Udacity

The first week was an overview and for appreciating the algorithms there is reference to the style transfer algorithm. I tried the pre-trained algorithm and here are some results.

# Training the Neural Net

### Overfitting and Underfitting
When the training error is high and the test error is high --> Underfitting

When the training error is low and the test error is high --> Overfitting

Q: What is Bias and Variance?  
A: 

### Early Stopping  
This is basically stopping the epoch when the test error starts to increase...

### Regularization   
L1 Regularization - Add lambda times the sum of absolute values of the weights to the error  
L2 Regularization - Add lambda times the sum of square of the values of the weights to the error   
Lambda can be chosen

### Dropout
A probablity for each node get dropped in a particular epoch. This method is very common and useful.

### Local Minima
To avoid local minima one method is to start at random points and there would be chances of getting to a global minima or a good local minima.

### Batch vs Stochastic Gradient Descent
Using the input data in multiple epochs help, in general, fit the model better.

### Learning Rate Decay
Large learning rate --> the model may not converge at a minima   
Small learning rate --> The training may be slow.


