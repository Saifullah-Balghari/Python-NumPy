import numpy as np 

# Basic Arthimatic operations using NumPy ufuncs.

array_1 = np.array([1, 2, 3, 4])
array_2 = np.array([5, 6, 7, 8])

# Addition:
print(np.add(array_1, array_2))                  # Output: [ 6  8 10 12]

# Subtraction:
print(np.subtract(array_1, array_2))             # Output: [-4 -4 -4 -4]

# Multiplication:
print(np.multiply(array_1, array_2))             # Output: [ 5 12 21 32]

# Division:
array_1 = np.array([10, 15, 30, 40, 50, 60])
array_2 = np.array([2, 3, 10, 8, 2, 6])

print(np.divide(array_1, array_2))               # Output: [ 5.  5.  3.  5. 25. 10.]

# Reminder:
array_1 = np.array([10, 20, 30, 40, 50, 60])
array_2 = np.array([3, 5, 10, 8, 2, 16])

print(np.remainder(array_1, array_2))            # Output: [ 1  0  0  0  0 12]

# Absolute:
array = np.array([-3, -2, -1, 0, 1, 2, 3])

print(np.absolute(array))                        # Output: [3 2 1 0 1 2 3]
 
# Power:
numbers = np.array([9, 8, 7, 6, 5])
powers = np.array([2, 3, 2, 4, 2])

print(np.power(numbers, powers))                 # Output: [  81  512  49  1296  25 ]

# quotient and mod:
array_1 = np.array([10, 20, 30, 40, 50, 60])
array_2 = np.array([3, 5, 10, 8, 2, 16])

print(np.divmod(array_1, array_2))