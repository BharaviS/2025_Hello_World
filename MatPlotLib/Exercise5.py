import matplotlib.pyplot as plt

friends = ["Bharavi", "Bharani", "Charan", "Sai", "Srinu"]
snacks = [10, 6, 8, 12, 7]
col = ["skyblue", "red", "blue", "green", "orange"]

plt.bar(friends, snacks, color=col, edgecolor='black', linewidth=1.2, width=0.5)
plt.grid(axis='y', linestyle=':', linewidth=0.7)

plt.title("🍿 Party Snack Counter 🍩", fontsize=16, color="darkgreen")
plt.xlabel("Friends 🧑‍🤝‍🧑", fontsize=12)
plt.ylabel("Snacks Eaten 🍕", fontsize=12)

plt.yticks(range(0, 15, 1))

for i in range(len(snacks)):
	plt.text(i, snacks[i] + 0.2, str(snacks[i]), ha='center', fontsize=10, color='purple')

plt.show()