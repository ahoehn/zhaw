import numpy as np

x = np.zeros(10)  # Create a 1-D array of 10 zeros
x = np.zeros(10).reshape(5, 2)  # Create a 5 row times 2 column matrix of zeros
x = np.ones([5, 2])  # Create a 5 row times 2 column matrix of 1s
x = np.linspace(0, 2, 10)  # Create a 1-D array from 0 to 1 included with 10 equidistant floats
print(x)
x = np.array([1, 2, 3, 4, 5], ndmin=3)  # Create a 3D array based on a list
print(x)
x = np.ones([5, 5, 5])  # 5x5x cube filled with ones
print(x)
print(x.ndim)  # nr of dimension
print(x.sum())  # sum of all values
print('mean', x.mean())
print(x.mean(axis=0))  # Get mean in 2-D array for all columns
