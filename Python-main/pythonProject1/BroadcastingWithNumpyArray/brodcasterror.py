import numpy as np

a = np.array([1, 2, 3, 4])
b = np.array([1, 2, 3])  # if you want remove broadcasting error then you write array same size
print(a + b)
