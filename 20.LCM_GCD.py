import numpy as np

array_1 = np.array([1, 2, 3, 4])
array_2 = np.array([5, 6, 7, 8])

### Finding Lowest Common Multiple(LCM).

# for digits:
print(np.lcm(4, 8))                 # output: 8    

# for arrays:
print(np.lcm(array_1, array_2))     # output: [ 5  6 21  8]

### Finding Greatest Common Denominator(GCD) also known as Highest Common Factor(HCF).

# for digits:
print(np.gcd(4, 8))                 # output: 4 

# for arrays:
print(np.gcd(array_1, array_2))     # output: [1 2 1 4]