from array import *

vals = array('i', [1,2,3])

print(vals)


Vale = array('i', [5,9,8,4,231])

nowArr = array (Vale.typecode, (a for a in Vale))

for e in Vale:
    print(e)

#user input array
arr = array('i',[])

n = int(input("Enter the length of an array: "))

for i in range (n):
    x = int(input(f"Enter array value {n}: "))
    arr.append(x)

print(arr)

val = int(input("Enter the value for search: "))
print(arr.index(val))