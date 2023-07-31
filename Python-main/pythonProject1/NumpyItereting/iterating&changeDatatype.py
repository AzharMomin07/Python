import numpy as np

s = np.array([[1, 2, 3], [1, 2, 3]])
print(s)
print(s.ndim)
print()
for i in np.nditer(s, flags=['buffered'], op_dtypes=["S"]):   # change data type in integer to String
    print(i)
