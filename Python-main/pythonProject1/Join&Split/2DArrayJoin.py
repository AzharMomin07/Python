import numpy as np

s = np.array([[1, 2], [5, 6]])
k = np.array([[3, 4], [7, 8]])
print(s)
print()
print(k)
print("Axis 1 wised:")
c = np.concatenate((s, k), axis=1)  # using axis 1
print(c)
print("Axis 0 wised:")
c1 = np.concatenate((s, k), axis=0)  # using axis 0
print(c1)
