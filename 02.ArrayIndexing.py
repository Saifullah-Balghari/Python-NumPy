import numpy as np


"""Accessing 1-D array"""

_1d_array = np.array([1, 2, 3])
# ArrayName[index number]
# e.g:
print(_1d_array[2])


"""Accessing 2-D array"""

_2d_array = np.array([[1, 2, 3],
                      [4, 5, 6],
                      [7, 8, 9]])
# ArrayName[RowIndex, ColumnIndex]
# e.g:
print(_2d_array[2, 2])


"""Accessing 3-D array"""

array3 = np.array([[[11, 12, 13],
                    [14, 15, 16],
                    [17, 18, 19]],
                   [[21, 22, 23],
                    [24, 25, 26],
                    [27, 28, 29]],
                   [[31, 32, 33],
                    [34, 35, 36],
                    [37, 38, 39]]])
# ArrayName[ArrayIndex, RowIndex, ColumnIndex]
# e.g:
print(array3[1, 1, 1])
