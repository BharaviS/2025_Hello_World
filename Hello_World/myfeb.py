n = int(input("Enter a value: "))
s = 0
r = 1

for i in range(1, n+1):
    print(f"{s}")
    s, r = r, s + r

