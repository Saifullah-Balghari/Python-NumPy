import numpy as np

## Arrays

array = np.array([1, 2, 3, 4, 5])
print(array)                # output: [1 2 3 4 5]
print(type(array))          # output: <class 'numpy.ndarray'>

array = [1, 2, 3, 4, 5]
array = np.array(array)
print(array)                # output: [1 2 3 4 5]
print(type(array))          # output: <class 'numpy.ndarray'>

## Types Of Arrays

# 0-Dimension array

_0D_array = np.array(42)
print(_0D_array)            # output: 42

# 1-Dimension array

_1D_array = np.array([1, 2, 3, 4, 5])
print(_1D_array)            # output: [1 2 3 4 5]

# 2-Dimension array

_2D_array = np.array([[1, 2, 3],
                  [4, 5, 6],
                  [7, 8, 9]])
print(_2D_array)            # output: [[1 2 3]
                            #          [4 5 6]
                            #          [7 8 9]]

# 3-Dimension array

_3D_array = np.array([[[1, 2, 3],
                 [4, 5, 6],
                 [7, 8, 9]],

                [[1, 2, 3],
                 [4, 5, 6],
                 [7, 8, 9]]])
print(_3D_array)            # output: [[[1 2 3]
                            #           [4 5 6]
                            #           [7 8 9]]
                            
                            #          [[1 2 3]
                            #           [4 5 6]
                            #           [7 8 9]]]


## Checking no of dimensions in an array using ndim attribute.

_0D_array = np.array(42)
_1D_array = np.array([1, 2, 3, 4, 5])
_2D_array = np.array([[1, 2, 3], [4, 5, 6]])
_3D_array = np.array([[[1, 2, 3], [4, 5, 6]], [[1, 2, 3], [4, 5, 6]]])

print(_0D_array.ndim)       # output: 0
print(_1D_array.ndim)       # output: 1
print(_2D_array.ndim)       # output: 2
print(_3D_array.ndim)       # output: 3

## Higher Dimensional Arrays:
#  An array can have any number of dimensions.
#  When the array is created, you can define the number of dimensions by using ndmin argument.

_ND_array = np.array([1, 2, 3, 4], ndmin=5)

print(_ND_array)                                        # output: [[[[[1 2 3 4]]]]]
print('Number of Dimensions :', _ND_array.ndim)         # output: number of dimensions : 5
