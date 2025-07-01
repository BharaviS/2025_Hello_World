import sys
import random
"""import matplotlib
matplotlib.use('Agg')"""
import matplotlib.pyplot as plt

print("Python Search Path (sys.path):")
for p in sys.path:
	print(p)

print("\nSize of a string in bytes:")
message = "Hello, Bharavi!"
print(f"Size of '{message}':", sys.getsizeof(message), "bytes")

print("\nSize of a list with 1000 random integers.")
big_list = [random.randint(1, 100) for _ in range(1000)]
print("List size:", sys.getsizeof(big_list), "bytes")

plt.hist(big_list, bins=50, color='orange', edgecolor='black')
plt.grid(axis='y', linestyle=':', linewidth=0.5)

plt.title("Size of a list with 1000 ransom integers", fontsize=14, color="teal")
plt.xlabel("50 Random Intervels", fontsize=12)
plt.xticks(range(min(big_list), max(big_list)+1), fontsize=5.9)

plt.show()
#plt.savefig("output_plot.png")

"""plt.savefig(sys.stdout.buffer)
sys.stdout.flush()"""

print("\nExiting the script early using sys.exit()...")
sys.exit("Custom exit message: Done with sys task!")
print("You won't see this message.")