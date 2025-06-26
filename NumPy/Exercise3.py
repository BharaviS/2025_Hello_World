import numpy as np

arr1d = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15])

#print(arr1d[::2])

arr2d = np.array([[1, 2, 3], [2, 3, 4], [3, 4, 5]])
n = len(arr2d)

print("#The Diagonal")
for i in range(n):
	for j in range(n):
		if i == j:
			print(arr2d[i][j])

print("\n#The Second Row")
print(arr2d[1])

print("\n#The last column in reverse")
print(arr2d[::-1,-1])

print("\n#The Diagonal")
print(np.diag(arr2d))