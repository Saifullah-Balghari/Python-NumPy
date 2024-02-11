import numpy as np

### Rounding Decimals.

# truncation: Removes the decimal part.
print(np.trunc([-1.1666, 1.6667, 1.5555, -1.5555]))     # output: [-1.  1.  1. -1.] 

# rounding: Normal roundoff.
print(np.around([-1.1666, 1.6667, 1.5555, -1.5555]))    # output: [-1.  2.  2. -2.]

# floor: Rounds to lower digit.
print(np.floor([-1.1666, 1.6667, 1.5555, -1.5555]))     # output: [-2.  1.  1. -2.]

# ceil: Rounds to uppper digit.
print(np.ceil([-1.1666, 1.6667, 1.5555, -1.5555]))      # output: [-1.  2.  2. -1.]
