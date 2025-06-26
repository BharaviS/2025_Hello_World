import numpy as np

a = np.arange(1, 25)
a_reshape_2d = a.reshape(2, 12)
a_reshape_3d = a.reshape(2, 3, 4)
#a_flat = a_reshape_2d.flatten()

print("Original:", a)
print("Reshaped 2D (2x12):\n", a_reshape_2d)
print("Reshaped 3D (3x18):\n", a_reshape_3d)
#print(a_flat)

b = np.array([[1 , 2], [3, 4]])
c = np.array([[5 , 6], [7, 8]])

print("Addition:\n", b+c)
print("Subtraction:\n", b-c)
print("Multiplication:\n", b*c)
print("Division:\n", b/c)

d = np.array([[1, 2, 3], [4, 5, 6]])
scalar = 10
vector = np.array([10, 20, 30])

print("Sum:", d.sum())
print("Scalar 10:\n", d[0] + scalar)
print("Vector 10:\n", d + vector)
print("Row-wise max", d.max(axis=1))
print("Column-wise min", d.min(axis=0))