import numpy as np
# Slicing arrays:   [start:end]
array = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9])

print(array[1:5])                   # output: [2 3 4 5]
print(array[4:])                    # output: [5 6 7 8 9]
print(array[:4])                    # output: [1 2 3 4]

# Negative Slicing:
print(array[-3:-1])                 # output: [7 8]

# Step:     [start:end:step]
print(array[1:5:2])                 # output: [2 4]
print(array[::2])                   # output: [1 3 5 7 9]

# Slicing 2-D Arrays:   [ArrayIndex, start:end]
array2 = np.array([[1, 2, 3, 4, 5],
                   [6, 7, 8, 9, 10]])

print(array2[1, 1:3])               # output: [7 8]
print(array2[0:2, 1:3])             # output: [[2 3]
                                    #          [7 8]]

# Slicing 2-D Arrays with Steps:   [ArrayIndex, start:end:step]
print(array2[0:2, 1:4:2])           # output: [[2 4]
                                    #          [7 9]]
print(array2[0:2, ::2])             # output: [[ 1  3  5]
                                    #          [ 6  8 10]]
