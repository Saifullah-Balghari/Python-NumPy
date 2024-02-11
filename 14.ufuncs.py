import numpy as np

""" 
-> ufuncs stands for "Universal Functions" and they are NumPy functions that operate on the ndarray object
-> ufuncs are used to implement vectorization in NumPy

-> vectorization means performing operations on a group of numbers all at once instead of one by one.

"""
arr1 = [1, 2, 3, 4, 5]
arr2 = [6, 7, 8, 9, 0]

# adding the arr1 and arr2 using pure Python.
result = []
for i in range(len(arr1)):
    result.append(arr1[i] + arr2[i])
print(result)

# adding the arr1 and arr2 using NumPy ufunc: add().
print(np.add(arr1, arr2))
