import numpy as np

# Array Iterating: Going through an array or it's elements.

# 1-D array
print("1-D array:")
_1d_array = np.array([1, 2, 3, 4, 5, 6])
for i in _1d_array:
    print(i)

# 2-D array
print("\n2-D array:")
_2d_array = np.array([[1, 2, 3],
                      [4, 5, 6],
                      [7, 8, 9]])
for i in _2d_array:
    print(i)

# Iterate down to the scalars:

# Iterating Arrays Using nditer()
for x in np.nditer(_2d_array):
    print(x)
# Normal Iterating
for row in _2d_array:
    for column in row:
        print(column)

# 3-D array
print("\n3-D array:")
_3d_array = np.array([[[11, 12, 13],
                       [14, 15, 16],
                       [17, 18, 19]],

                      [[21, 22, 23],
                       [24, 25, 26],
                       [27, 28, 29]],

                      [[31, 32, 33],
                       [34, 35, 36],
                       [37, 38, 39]]])
for i in _3d_array:
    print(i)

# Iterate down to the scalars:

# Normal Iterating
for array in _3d_array:
    for row in array:
        for column in row:
            print(column)

# Iterating Arrays Using nditer()
for x in np.nditer(_3d_array):
    print(x)
