import sys

print("sys version: ", sys.version)

i = 0

while True:
    print("hello")
    if i == 5:
        sys.exit()
    else:
        i += 1