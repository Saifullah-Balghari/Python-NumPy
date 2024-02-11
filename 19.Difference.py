import numpy as np

arr = np.array([[1, 2, 3],
                [4, 5, 6],
                [7, 8, 9]])

# Difference of all elements in the array
total_diff = np.diff(arr)
print(f"Total Difference:\n{total_diff} ")

### Difference along a specific axis

# Axis 0 represents columns.
column_diff = np.diff(arr, axis=0)
print(f"Column-wise Difference:\n{column_diff} ")

# Axis 1 represents rows.
row_diff = np.diff(arr, axis=1)
print(f"Row-wise Difference:\n{row_diff} ")

### Difference of elements in a specific column or row

# Difference of elements in the third column
diff_column_2 = np.diff(arr[:, 2])  
print(f"Difference of elements in the third column: {diff_column_2} ")

# Difference of elements in the second row
diff_row_1 = np.diff(arr[1, :])  
print(f"Difference of elements in the second row: {diff_row_1} ")
