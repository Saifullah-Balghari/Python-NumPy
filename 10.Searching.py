import numpy as np

# where() method returns the indexes where the matching elements are presented
# e.g:
array = np.array([1, 8, 3, 7, 8, 7, 8])
x = np.where(array == 8)
print(x)

y = np.where(array % 2 == 0)
print(y)    # returns the indexes where the elements are even

z = np.where(array % 2 == 1)
print(z)    # returns the indexes where the elements are odd
