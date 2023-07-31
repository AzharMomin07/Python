import numpy as np

b = np.array([1, 2, 3, 4, 5])

v = b.view()

b[4] = 6  # change in original data and also copy data
print("print b", b)

print()

print(" print view:", v)
