import numpy as np
from numpy import random

arr = np.array([1, 4, 9, 16, 25, 36, 49, 64])

print("Mean Values:\n", np.mean(arr))
print("Median Values:\n", np.median(arr))
print("Standard Values:\n", np.std(arr))
print("Variable Values:\n", np.var(arr))
print("Minimum Values:\n", np.min(arr))
print("Maximum Values:\n", np.max(arr))
print("")
print("Rand:\n", random.rand(5))
print("Randint:\n", random.randint(50, size=5))
print("Random:\n", random.normal(50, size=5))
print("")
print("\n", random.rand(10))
print("\n", random.randint(1, 100, size=10))
print("\n", random.normal(50, 10, size=10))
print("")
hist , bins = np.histogram(arr)
print("Histogram:")
print("Frequencies:\n", hist)
print("bin Edges:\n", bin)

a = random.randint(1, 100, size=10)
b = random.randint(1, 100, size=10)

print("Arr:\n", np.mean((a,b)))
print("Mean Values (a, b):\n", np.mean((a,b)))
print("Median Values (a, b):\n", np.median((a,b)))
print("Standard Values (a, b):\n", np.std((a,b)))