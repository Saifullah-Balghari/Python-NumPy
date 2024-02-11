import numpy as np

arr = np.array([[1, 2, 3],
                [4, 5, 6],
                [7, 8, 9]])

# Product of all elements in the array.
total_product = np.prod(arr)
print(f"Total Product: {total_product} ")

### Product along a specific axis.

# Axis 0 represents columns.
column_product = np.prod(arr, axis=0)
print(f"Column-wise Product: {column_product} ")

# Axis 1 represents rows.
row_product = np.prod(arr, axis=1)
print(f"Row-wise Product: {row_product} ")

### Product of elements in a specific column or row.

# Product of elements in the third column.
product_column_2 = np.prod(arr[:, 2])  
print(f"Product of elements in the third column: {product_column_2} ")

# Product of elements in the second row.
product_row_1 = np.prod(arr[1, :])  
print(f"Product of elements in the second row: {product_row_1} ")