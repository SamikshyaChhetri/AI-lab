import numpy as np

# Input data for Hebbian learning
X = np.array([[0, 0], [0, 1], [1, 0], [1, 1]])

# Output data for Hebbian learning
Y = np.array([[0], [0], [0], [1]])

# Define Hebbian learning rule function
def hebbian_learning(X, Y):
    n, m = X.shape
    weights = np.zeros(m)
    
    for i in range(n):
        for j in range(m):
            weights[j] += X[i, j] * Y[i, 0]  # Index Y to get a scalar value
        
    return weights

# Train the Hebbian neural network
weights = hebbian_learning(X, Y)

# Test the AND gate
def and_gate(input_data, weights):
    activation = np.dot(input_data, weights)
    return np.where(activation >= 0.5, 1, 0)

# Test the AND gate with all possible inputs
for i in range(len(X)):
    output = and_gate(X[i], weights)
    print("Input:", X[i], "Output:", output)
