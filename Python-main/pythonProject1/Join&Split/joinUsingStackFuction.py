import numpy as np

s = np.array([1, 2, 5, 6])
k = np.array([3, 4, 7, 8])
print(s)
print()
print(k)
print(" h wised:")
c = np.hstack((s, k))  # using h height wised data distributed
print(c)
print(" d wised:")
c1 = np.dstack((s, k))  # using d row wised array distributing
print(c1)
print(" v wised:")
c2 = np.vstack((s, k))  # using h column wised data distributed
print(c2)
