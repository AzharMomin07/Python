import numpy as np

S1 = np.array([1, 2, 3, 4], ndmin=4)  # and using ndmin we expand this array to 4*4 matrix
print(S1)
print(S1.ndim)  # using ndim we check how many matrix in this array
print()
print(S1.shape)  # answer is (1, 1, 1, 4) means first array is 1 row second is 1 row third is 1 row and has
# 4 columns in all 4 arrays
