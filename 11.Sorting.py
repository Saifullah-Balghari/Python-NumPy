import numpy as np

# Sorting:  putting elements in an ordered sequence

_1d_array = np.array([3, 7, 8, 6, 4, 5, 2, 0, 1])
print(np.sort(_1d_array))   # output: [0 1 2 3 4 5 6 7 8]

_2d_array = np.array([[2, 4, 0, 3, 1],
                      [8, 6, 7, 9, 5]])
print(np.sort(_2d_array))   # output: [[0 1 2 3 4]
#                                      [5 6 7 8 9]]

_3d_array = np.array([[[2, 4, 0, 3, 1],
                       [8, 6, 7, 9, 5]],

                      [[2, 4, 0, 3, 1],
                       [8, 6, 7, 9, 5]]])
print(np.sort(_3d_array))   # output: [[[0 1 2 3 4]
#                                      [5 6 7 8 9]]
#
#                                     [[0 1 2 3 4]
#                                      [5 6 7 8 9]]]
