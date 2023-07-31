import numpy as np

s = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])
print(s)
print(s.ndim)

print()

s1 = s.reshape(2, 3, 2)
print(s1)
print(s1.ndim)

print()

one = s1.reshape(-1)
print(one)
print(one.ndim)
