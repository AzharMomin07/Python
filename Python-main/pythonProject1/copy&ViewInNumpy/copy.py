import numpy as np

a = np.array([1, 2, 3, 4, 5])

co = a.copy()

a[4] = 6  # it's changes original data not a copy data

print("print a:", a)

print("print copy:", co)
