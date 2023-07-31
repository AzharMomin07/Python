import numpy as np

var = np.array([1, 2, 3, 455777, 5])
print("Data Types:", var.dtype)

v = np.array([1.5, 2.2, 3.9, 45577.7, 5.5])
print("Data Types:", v.dtype)

a = np.array(["a", "e", "e"])
print("Data Types:", a.dtype)

# conversion of integer to Float and again int

A = np.array([1, 2, 3, 4])
B = np.float32(A)
C = np.int_(B)
print("data type:", A.dtype)
print("data type", B.dtype)
print("Data type:", C.dtype)
print(A)
print(B)
print(C)
