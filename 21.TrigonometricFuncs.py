import numpy as np

# The NumPy Trignometric function takes the input argument in radians, not in degrees.
degrees = np.array([0, 90, 180, 270])
radians = np.deg2rad(degrees)

# Sine of all elements in the array
print(f"Sine of all elements:\n{np.sin(radians)}")     # Output: [ 0.0000000e+00  1.0000000e+00  1.2246468e-16 -1.0000000e+00]

# Cosine of all elements in the array
print(f"Cosine of all elements:\n{np.cos(radians)} ")      # Output: [ 1.0000000e+00  6.1232340e-17 -1.0000000e+00 -1.8369702e-16]

# Tangent of all elements in the array  
print(f"Tangent of all elements:\n{np.tan(radians)} ")      # Output: [ 0.00000000e+00  1.63312394e+16 -1.22464680e-16  5.44374645e+15]

# Arcsine of all elements in the array
print(f"Arcsine of all elements:\n{np.arcsin(np.sin(radians))}")    # Output: [ 0.00000000e+00  1.57079633e+00  1.22464680e-16 -1.57079633e+00]

# Arccosine of all elements in the array
print(f"Arccosine of all elements:\n{np.arccos(np.cos(radians))}")    # Output: [0.         1.57079633 3.14159265 1.57079633]

# Arctangent of all elements in the array
print(f"Arctangent of all elements:\n{np.arctan(np.tan(radians))}")     # Output: [ 0.00000000e+00  1.57079633e+00 -1.22464680e-16  1.57079633e+00]
