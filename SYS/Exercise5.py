import sys

print("Current Recursion Limit:", sys.getrecursionlimit())

sys.setrecursionlimit(2000)
print("New Recursion Limit Set:", sys.getrecursionlimit())

def recursive_count(n):
    if n == 0:
        return "Reached base case!"
    return recursive_count(n - 1)

try:
    print("Starting deep recursion...")
    print(recursive_count(1500)) 
except RecursionError as e:
    print("RecursionError Caught:", e)
