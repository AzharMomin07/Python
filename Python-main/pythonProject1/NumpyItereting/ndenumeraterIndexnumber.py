import numpy as np

i = np.array([[1, 2, 3], [1, 2, 3]])

print(i)
print()
for j, d in np.ndenumerate(i):
    print(j, d)
