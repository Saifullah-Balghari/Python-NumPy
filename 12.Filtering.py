import numpy as np

# Filtering: making a new array out of some elements from an array.

original_array = np.arange(11, 21)

# Method 1
filter1 = [True, False, True, True, False, True, False, True, True, False]
# filtered_array1 is created by selecting elements from original_array where the corresponding value in filter1 is True
filtered_array1 = original_array[filter1]

print(filtered_array1)   # output: [11 13 14 16 18 19]

# Method 2

filter2 = original_array % 2 == 0  # returns true if the element is even
# filtered_array2 is created by selecting elements from original_array where the corresponding value in filter1 is True
filtered_array2 = original_array[filter2]
print(filtered_array2)
