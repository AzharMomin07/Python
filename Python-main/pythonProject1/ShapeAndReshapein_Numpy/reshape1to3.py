import numpy as np

s = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])
new_arr = s.reshape(2,6)
print(new_arr)
print(s)
print(s.dtype)
print(s.ndim)

print()

s1 = s.reshape(2, 3, 2)
print(s1)
print(s1.ndim)

# arr1 = np.array([1, 2, 3, 4])
# arr2 = np.view(arr1)
# arr2[0] = 10
# print(arr1)
# print(arr2)
