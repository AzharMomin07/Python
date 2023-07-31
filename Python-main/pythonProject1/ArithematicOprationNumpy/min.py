import numpy as np

a = np.array([1, 2, 3, 4])
b = np.array([[1, 5, 3, 4], [2, 7, 3, 4]])
print(np.min(a))
print(np.min(b, axis=1))  # row wise min
print(np.min(b, axis=0))  # col wise min
