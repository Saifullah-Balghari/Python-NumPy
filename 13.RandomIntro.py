import numpy as np 
from numpy import random

# Generating Numbers...
# random.randint(100) : Generates a random number between 0 - 100.
print(random.randint(100))

# random.rand() : Generate a random float between 0 - 1.
print(random.rand())

# Generating Arrays...
# random.randint(range, size=(rows, column)) : Generates a 2-D array with random numbers between 0 - 100.
print(random.randint(100, size=(3, 5)))     