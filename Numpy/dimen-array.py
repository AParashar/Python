# One Dimensional Array
import numpy as np

array_1 = np.array([1, 2, 3])

print(array_1)
print(array_1[2])
print(type(array_1))      # nd Array
print(array_1.ndim)       # Dimension of Array
print(array_1.shape)      # Shape of Array => 1 dimension and three elements in that dimension


# Two dimensional Array 
array_2 = np.array([[1, 2, 3], [4, 5, 6]])
print(array_2)
print(array_2.ndim)
print(array_2.shape)


# Three Dimensional Array
array_3 = np.array([[1, 2, 3, 4, 6], [4, 5, 6, 5, 6], [4, 5, 6, 5, 0], [4, 5, 6, 5, 8]])
print(array_3.ndim)
print(array_3.shape)
print(array_3[1][1])      # Access a given element