from MyMath import *

a = int(input("Entter any value: "))
b = int(input("Entter any value: "))

val = MyMath(a, b)

print(f"{a}+{b}={val.Add()}")
print(f"{a}-{b}={val.Sup()}")
print(f"{a}*{b}={val.Mul()}")
print(f"{a}/{b}={val.Dev()}")
print(f"{a}%{b}={val.Mul()}")