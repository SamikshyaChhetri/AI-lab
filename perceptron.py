# Source code:
import numpy as np

# Define activation function (Step function)
def step_function(x):
    return 1 if x >= 0 else 0

# Define perceptron for AND gate
def perceptron_AND(input_data, weights):
    weighted_sum = np.dot(input_data, weights)
    return step_function(weighted_sum)

# Initialize input data and corresponding outputs for AND gate
X = np.array([[0, 0], [0, 1], [1, 0], [1, 1]])
Y = np.array([0, 0, 0, 1])

# Initialize weights and bias
weights = np.array([0.5, 0.5])
bias = -1

# Train the perceptron for AND gate
def train_perceptron_AND(X, Y, weights, bias, learning_rate=0.1, epochs=100):
    for epoch in range(epochs):
        for i in range(len(X)):
            input_data = X[i]
            target_output = Y[i]
            output = perceptron_AND(input_data, weights) + bias
            error = target_output - output
            weights += learning_rate * error * input_data
            bias += learning_rate * error
    return weights, bias

# Train the perceptron
weights, bias = train_perceptron_AND(X, Y, weights, bias)

# Test the AND gate with all possible inputs
for i in range(len(X)):
    output = perceptron_AND(X[i], weights) + bias
    print("Input:", X[i], "Output:", output)
