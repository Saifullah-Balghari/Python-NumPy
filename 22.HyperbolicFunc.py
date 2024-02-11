import numpy as np

# The NumPy hyperbolic functions operate on angles given in radians.
radians = np.array([0, 0.5, 1.0, 1.5])

# Hyperbolic sine of all elements in the array
print(f"Hyperbolic sine of all elements:\n{np.sinh(radians)}")      # Output: [0.         0.52109531 1.17520119 2.12927946]

# Hyperbolic cosine of all elements in the array
print(f"Hyperbolic cosine of all elements:\n{np.cosh(radians)}")      # Output: [1.         1.12762597 1.54308063 2.35240962]

# Hyperbolic tangent of all elements in the array
print(f"Hyperbolic tangent of all elements:\n{np.tanh(radians)}")       # Output: [0.         0.46211716 0.76159416 0.90514825]

# Inverse hyperbolic sine of all elements in the array
print(f"Inverse hyperbolic sine of all elements:\n{np.arcsinh(np.sinh(radians))}")      # Output: [0.  0.5 1.  1.5]

# Inverse hyperbolic cosine of all elements in the array
print(f"Inverse hyperbolic cosine of all elements:\n{np.arccosh(np.cosh(radians))}")      # Output: [0.  0.5 1.  1.5]

# Inverse hyperbolic tangent of all elements in the array
print(f"Inverse hyperbolic tangent of all elements:\n{np.arctanh(np.tanh(radians))}")       # Output: [0.  0.5 1.  1.5]
