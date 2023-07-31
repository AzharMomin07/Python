import numpy as np

a = np.array([1, 2, 3, 4], np.int32)  # Memory management is on your hand
print(a)

# Array
b = np.array([1, 2, 3, 4])
print(b)
print(type(b))

# List
c = [1, 2, 3, 4]
print(c)
print(type(c))

y = np.array([1, 2, 3, 4, 5])
print(y)

# array user input

l = []

for i in range(1, 5):
    int_1 = int(input("enter:"))
    l.append(int_1)
    print(np.array(l))
