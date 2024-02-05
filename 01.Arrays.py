import numpy as np

# Array

# arr1 = np.array([1, 2, 3, 4, 5])
#
# arr = [1, 2, 3, 4, 5]
# arr2 = np.array(arr)
#
# print(arr1)          # output: [1 2 3 4 5]
# print(type(arr1))    # output: <class 'numpy.ndarray'>
#
# print(arr2)          # output: [1 2 3 4 5]
# print(type(arr2))    # output: <class 'numpy.ndarray'>

#  Types Of Arrays

# 0-Dimension array

# arr = np.array(42)
# print(arr)            # output: 42

# 1-Dimension array
#
# arr = np.array([1, 2, 3, 4, 5])
# print(arr)              # output: [1 2 3 4 5]

# 2-Dimension array

# arr = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
# print(arr)              # output: [[1 2 3]
#                         #          [4 5 6]
#                         #          [7 8 9]]

# 3-Dimension array

# arr = np.array([[[1, 2, 3],
#                  [4, 5, 6],
#                  [7, 8, 9]],
#                 [[1, 2, 3],
#                  [4, 5, 6],
#                  [7, 8, 9]]])
# print(arr)                  # output: [[[1 2 3]
#                             #           [4 5 6]
#                             #           [7 8 9]]
#                             #
#                             #          [[1 2 3]
#                             #           [4 5 6]
#                             #           [7 8 9]]]
#

# Checking no of dimensions in an array using ndim attribute.

# a = np.array(42)
# b = np.array([1, 2, 3, 4, 5])
# c = np.array([[1, 2, 3], [4, 5, 6]])
# d = np.array([[[1, 2, 3], [4, 5, 6]], [[1, 2, 3], [4, 5, 6]]])
#
# print(a.ndim)       # 0
# print(b.ndim)       # 1
# print(c.ndim)       # 2
# print(d.ndim)       # 3


# Higher Dimensional Arrays:
#   An array can have any number of dimensions.
#    When the array is created, you can define the number of dimensions by using the ndmin argument.

# arr = np.array([1, 2, 3, 4], ndmin=5)
#
# print(arr)          # output: [[[[[1 2 3 4]]]]]
# print('number of dimensions :', arr.ndim)         # output: number of dimensions : 5
