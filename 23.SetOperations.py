import numpy as np

# Create two arrays
array1 = np.array([1, 2, 3, 4, 5])
array2 = np.array([4, 5, 6, 7, 8])

# Union of two sets
print(f"Union of the two arrays: {np.union1d(array1, array2)}")     # Output: Union of the two arrays: [1 2 3 4 5 6 7 8]

# Intersection of two sets
print(f"Intersection of the two arrays: {np.intersect1d(array1, array2)}")      # Output: Intersection of the two arrays: [4 5]

# Difference between two sets (elements in set1 but not in set2)
print(f"Difference between the two arrays: {np.setdiff1d(array1, array2)}")      # Output: Difference between the two arrays: [1 2 3]

# Symmetric difference between two sets (elements that are in either set but not in both)
print(f"Symmetric difference between the two arrays: {np.setxor1d(array1, array2)}")        # Output: Symmetric difference between the two arrays: [1 2 3 6 7 8]
