import numpy as np

# Joining Arrays: merging two or more numpy arrays into on array


# joining two 1-D arrays into one array using the concatenate() function.
array1 = np.array([1, 2, 3, 4])
array2 = np.array([5, 6, 7, 8])

array3 = np.concatenate((array1, array2))  # also we can np.hstack((array1, array2))
print(array3)        # output: [1 2 3 4 5 6 7 8]

# joining two 2-D arrays into one array using the concatenate() function.
array4 = np.array([[1, 2],
                   [3, 4]])
array5 = np.array([[5, 6],
                   [7, 8]])

array6 = np.concatenate((array4, array5), axis=0)
print(array6)
# output:
# [[1 2]
#  [3 4]
#  [5 6]
#  [7 8]]
array7 = np.concatenate((array4, array5), axis=1)  # joins along rows (axis=1)
print(array7)
# output:
# [[1 2 5 6]
#  [3 4 7 8]]

array8 = np.array([1, 2, 3])
array9 = np.array([4, 5, 6])

array10 = np.stack((array8, array9), axis=1)   # also we can np.dstack((array1, array2))
print(array10)
