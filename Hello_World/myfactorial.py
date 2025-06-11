import math as mt

n = int(input("Enter a Value: "))
k = n

for i in range(n, 1, -1):
    n = n * (i - 1)
    temp = i -1
    print(f'k value is {k} * {temp}: {n}')

print(f'final {k} is {n}')

a = k
print(f"factorial of {a} is : {mt.factorial(a)}")