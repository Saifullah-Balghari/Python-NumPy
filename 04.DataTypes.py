import numpy as np
d
# Pre-Defined arrays

# Integer:
array_int8 = np.array([1, 2, 3, 4, 5], dtype=np.int8)
array_int16 = np.array([1, 2, 3, 4, 5], dtype=np.int16)
array_int32 = np.array([1, 2, 3, 4, 5], dtype=np.int32)
array_int64 = np.array([1, 2, 3, 4, 5], dtype=np.int64)

# Unassigned_Integer:
array_uint8 = np.array([1, 2, 3, 4, 5], dtype=np.uint8)
array_uint16 = np.array([1, 2, 3, 4, 5], dtype=np.uint16)
array_uint32 = np.array([1, 2, 3, 4, 5], dtype=np.uint32)
array_uint64 = np.array([1, 2, 3, 4, 5], dtype=np.uint64)

# Floating point:
array_float16 = np.array([1.1, 2.2, 3.3, 4.4, 5.5], dtype=np.float16)
array_float32 = np.array([1.1, 2.2, 3.3, 4.4, 5.5], dtype=np.float32)
array_float64 = np.array([1.1, 2.2, 3.3, 4.4, 5.5], dtype=np.float64)

# Complex Numbers:
array_complex64 = np.array([1 + 2j, 3 + 4j], dtype=np.complex64)
array_complex128 = np.array([1 + 2j, 3 + 4j], dtype=np.complex128)

# Boolean Values:
array_bool = np.array([True, False, True], dtype=np.bool_)

# Strings
array_str = np.array(["Saifullah", "Python", "NumPy"], dtype=np.str_)

# There are some other data types....

# Printing array data types
print(f"DataType: {array_int8.dtype}\n Array: {array_int8}\n")
print(f"DataType: {array_int16.dtype}\n Array: {array_int16}\n")
print(f"DataType: {array_int32.dtype}\n Array: {array_int32}\n")
print(f"DataType: {array_int64.dtype}\n Array: {array_int64}\n")

print(f"DataType: {array_uint8.dtype}\n Array: {array_uint8}\n")
print(f"DataType: {array_uint16.dtype}\n Array: {array_uint16}\n")
print(f"DataType: {array_uint32.dtype}\n Array: {array_uint32}\n")
print(f"DataType: {array_uint64.dtype}\n Array: {array_uint64}\n")

print(f"DataType: {array_float16.dtype}\n Array: {array_float16}\n")
print(f"DataType: {array_float32.dtype}\n Array: {array_float32}\n")
print(f"DataType: {array_float64.dtype}\n Array: {array_float64}\n")

print(f"DataType: {array_complex64.dtype}\n Array: {array_complex64}\n")
print(f"DataType: {array_complex128.dtype}\n Array: {array_complex128}\n")

print(f"DataType: {array_bool.dtype}\n Array: {array_bool}\n")

print(f"DataType: {array_str.dtype}\n Array: {array_str}\n")