import numpy as np

s = np.array([1, 2, 3, 4, 5, 6, 7])

print(s)

print(s.ndim)

s1 = np.array([[1, 2, 3], [2, 3, 4]])

print(s1)
print("print 2 to 5:", s[1:6])
print("Step function:", s[::2])  # jump 2 step

print(s1[0, 1:])

