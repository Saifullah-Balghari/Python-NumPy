import numpy as np

arr = np.array([[1, 2, 3],
                [4, 5, 6],
                [7, 8, 9]])

# Summation of all elements in the array.
total_sum = np.sum(arr)
print(f"Total Sum: {total_sum} ")

### Summation along a specific axis.

# Axis 0 represents columns.
column_sum = np.sum(arr, axis=0)
print(f"Column-wise Sum: {column_sum} ")

# Axis 1 represents rows.
row_sum = np.sum(arr, axis=1)
print(f"Row-wise Sum: {row_sum} ")

### Summation of elements in a specific column or row.

# Sum of elements in the third column.
sum_column_2 = np.sum(arr[:, 2])  
print(f"Sum of elements in the third column: {sum_column_2} ")

# Sum of elements in the second row.
sum_row_1 = np.sum(arr[1, :])  
print(f"Sum of elements in the second row: {sum_row_1} ")
