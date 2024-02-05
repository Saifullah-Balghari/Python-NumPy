import numpy as np

# Reshaping means changing the number of elements of an array.

_1d_array = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])

# Reshaping 1-D array to 2-D array

_2d_array = _1d_array.reshape(4, 3)  # Means--> 4 arrays, each with 3 elements:
print(_2d_array)

# Reshaping 1-D array to 3-D array
_3d_array = _1d_array.reshape(2, 3, 2)  # Means--> 2 arrays that contains 3 arrays, each with 2 elements:
print(_3d_array)
