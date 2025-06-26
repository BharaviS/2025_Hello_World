import numpy as np

arr = np.array([1, 4, 9, 16, 25, 30, 36,49, 64])

print("Original:", arr)
print("Square Root: ", np.sqrt(arr))
print("Power: ", np.power(arr, 2))
print("Exponential:", np.exp(arr))
print("Log:", np.log(arr))
print("")
print("Sin:", np.sin(arr))
print("Cos:", np.cos(arr))
print("Tan:", np.tan(arr))
print("")
print("Round:", np.round(np.tan(arr), 2))
print("Floor:", np.floor(np.tan(arr)))
print("Ceil:", np.ceil(np.tan(arr)))
print("\n")
print("Filtered Array:",arr[arr > 5], arr[(arr > 2) & (arr<10)])

arr[arr < 0] = 0
my_arr = arr
marks = np.where(my_arr % 2 == 0, "Even", "Odd")

print("Filtered Negative Values:", my_arr)
print("Conditional Logic:", marks)