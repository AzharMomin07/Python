import numpy as np

a = np.array([1, 2, 3, 4, 5, 6])
print(a)
b = np.array_split(a, 3)
print(b)
print(type(b))
print("print in array change list to array")
print(b[0])
