import numpy as np 

### Generating Numbers...

# random.randint(range) : Generates a random number between 0 and range.
print(np.random.randint(100))

# random.rand() : Generate a random float between 0 and 1.
print(np.random.rand())

### Generating Arrays...

# random.randint(range, size=(rows, column)) : Generates a 2-D array with random numbers between 0 - 100.
print(np.random.randint(100, size=(3, 5)))     

# random.rand(rows, column) : Generates a 2-D array with random floats between 0 and 1.
print(np.random.rand(3, 5))

### Generating Random Number From An Array...

# choice() : takes an array as a parameter and randomly returns one of the values also we can generate 2-D arrays with the elements of array.
array1 = np.array([1, 2, 3, 4, 5])
print(np.random.choice(array1))
print(np.random.choice(array1, size=(3, 5)))

### Data distribution: a list of all possible values, and how often each value occurs.

array2 = np.array([8, 7, 6, 9])
chances = [0.3, 0.2, 0.5, 0.0]
print(np.random.choice(array2, p=chances, size=(3, 5)))

### Shuffle or Permutation : Randomly changes the arrangment of an array.

array3 = np.array([5, 4, 3, 2, 1])
# Shuffle modifies the original array.
np.random.shuffle(array3)
print(array3)

# Permutation generates a new array from the original array.
array4 = np.random.permutation(array3)
print(array4)