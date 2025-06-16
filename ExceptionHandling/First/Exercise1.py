try:
    x = int("abc")
    print(x)
except ValueError:
    print("Value must be an integer")