import numpy as np

a = np.array([1, 2, 3, 4, 5, 4, 7])

b = np.where(a == 4)  # index position wise search

b1 = np.where((a / 2) == 0)  # index position wise search

b2 = np.where((a % 2) == 0)  # index position wise search

print(b)
print(b1)
print(b2)

