import numpy as np

array = np.array([[12, 32, 21, 25, 13], [0, 2, 5, 7, 9], [1, 3, 6, 8, 6], [9, 13, 15, 71, 31], [2, 13, 14, 16, 7]])
print(array)

# array_0 = np.zeros((4, 4))
# print(array_0)
filter = array < 18
print(filter)               # Returns Boolean Array
# print(array[filter])

# Change elements of Array matching a given condition(filter)
array[filter] = array[filter] + 100
print(array)