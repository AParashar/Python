import numpy as np

array = 10*(np.random.random_sample((5, 5)))
print(array)
# array = np.ones((4, 4))

# Boolean Array
# print(filter(array > 40))

# Create Array of Indices
row_indices = np.array([0, 2, 2, 4])

col_indices = np.arange(4)

for row, col in zip(row_indices, col_indices):
    print(row, " - ", col)

print(array[row_indices, col_indices])