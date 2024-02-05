import numpy as np

# Array_Shape: is the number elements a dimension or array has.


# 1-Dimensional array:
_1d_array = np.array([1, 2, 3, 4, 5])
print(_1d_array.shape)      # output: (5,)  --> Array has 5 elements

try:
    # 2-Dimensional array:
    _2d_array = np.array([[1, 2, 3, 4], [5, 6, 7, 8]])
    print(_2d_array.shape)  # output: (2, 4)  --> Array has 2 elements and each has its own 4 elements.

except ValueError as e:
    print("The requested array has an inhomogeneous shape.")
