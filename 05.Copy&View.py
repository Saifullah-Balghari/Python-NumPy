import numpy as np

original_array = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9])

# Copy: new copy of the original array.
copied_array = original_array.copy()
copied_array[5] = 10   # changes in the copy will not affect the original and vise-versa.

print(f"Original array: {original_array} \n Copied array: {copied_array}\n")

# View: just a view of the original array
array_view = original_array.view()
array_view[5] = 10     # changes to the view will change the original and vise-versa as it is just a view, not a new array.
print(f"Original array: {original_array} \n Viewed array: {array_view}\n")

# print(copied_array.base)
# print(array_view.base)
