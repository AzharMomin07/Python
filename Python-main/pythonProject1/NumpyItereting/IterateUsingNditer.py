import numpy as np

var = np.array([[1, 2, 3], [4, 5, 6]])
print(var)
print()
print(var.ndim)
print()
for i in np.nditer(var):
    print(i)
