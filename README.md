# Deep-Learning
Projects from Deep Learning Nanodegree on Udacity

The first week was an overview and for appreciating the algorithms there is reference to the style transfer algorithm. I tried the pre-trained algorithm and here are some results.

# Anaconda and Environment Setup

If you are seeing the following "conda command not found" and are using ZShell, you have to do the following:

Add export PATH="/Users/username/anaconda/bin:$PATH" to your .zsh_config file.


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

### Momentum
How to overcome local minima?  
The momentum will push away from the local minima and lead to the global minima  
Beta is the momentum and the value is between 0 and 1. Momentum is used to calculate the step based on previous steps.
The step(n) = step(n) + beta*step(n-1) + beta^2 * step(n-2) + beta^3 * step(n-3) + ...

## Neural Noise
Noise in the input data? Clean up the input data or use it in such a way that the noise is less.


