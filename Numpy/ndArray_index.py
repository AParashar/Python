import numpy as np

# Generate random array and perform sacalar multiplication
array = 10*(np.random.random_sample((3, 3)))
print(array)

# Round off array elements
round_off_array = np.around(array)
print(round_off_array)


# Slicing the array
print(round_off_array[:2, 1:7])
print(round_off_array[:-1, -1:-3])      # Same Rank as that of original Array
print(round_off_array[-1, 1: 2])        # One Rank lower