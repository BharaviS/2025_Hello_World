import matplotlib.pyplot as plt

snack_counts = [2, 3, 3, 4, 4, 4, 5, 5, 5, 5, 6, 6, 6, 7, 7, 8, 8, 8, 9, 10]

plt.hist(snack_counts, bins=8, color='orange', edgecolor='black')
plt.grid(axis='y', linestyle=':', linewidth=0.5)

plt.title("🍿 Party Snack Count Distribution", fontsize=14, color="teal")
plt.xlabel("Snacks Taken", fontsize=12)
plt.ylabel("Number of People", fontsize=12)

plt.xticks(range(min(snack_counts), max(snack_counts)+1))

plt.show()