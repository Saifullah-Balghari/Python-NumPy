import numpy as np 


# Generating Numbers...

# random.randint(range) : Generates a random number between 0 and range.
print(np.random.randint(100))

# random.rand() : Generate a random float between 0 and 1.
print(np.random.rand())

# Generating Arrays...

# random.randint(range, size=(rows, column)) : Generates a 2-D array with random numbers between 0 - 100.
print(np.random.randint(100, size=(3, 5)))     

# random.rand(rows, column) : Generates a 2-D array with random floats between 0 and 1.
print(np.random.rand(3, 5))

# Generating Random Number From An Array...

# choice() : takes an array as a parameter and randomly returns one of the values also we can generate 2-D arrays with the elements of array.
array = [1, 2, 3, 4, 5]
print(np.random.choice(array))
print(np.random.choice(array, size=(3, 5)))