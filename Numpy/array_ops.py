# Array operations
import numpy as np 


# Data Types
array1 = np.array([[11, 14], [11, 14]], dtype=np.int)
# array1 = np.array([[11, 14], [11, 14]], dtype=np.float)
print(array1.dtype)

# Arithmetic Array Operations
array2 = np.array([[29, 36], [21, 78]], dtype=np.float)

# Addition
print(array1 + array2)
print(np.add(array1, array2))

# Subtration
print(array1 - array2)
print(np.subtract(array1, array2))

# Multiplication
print(array1 * array2)
print(np.multiply(array1, array2))

# Division
print(array1/array2)
print(np.divide(array1, array2))

# Square Root
print(np.sqrt(array1))

# Exponential Function
print(np.exp(array1))
