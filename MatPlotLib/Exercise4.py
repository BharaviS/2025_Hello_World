import matplotlib.pyplot as plt

friends = ["Bharavi", "Bharani", "Charan", "Sai", "Srinu"]
snacks = [10, 6, 8, 12, 7]

plt.bar(friends, snacks, color='skyblue', edgecolor='black', linewidth=1.2)

plt.title("🍿 Party Snack Counter 🍩", fontsize=16, color="darkgreen")
plt.xlabel("Friends 🧑‍🤝‍🧑", fontsize=12)
plt.ylabel("Snacks Eaten 🍕", fontsize=12)

plt.grid(axis='y', linestyle=':', linewidth=0.7)
plt.yticks(range(0, 15, 1))

for i in range(len(snacks)):
    plt.text(i, snacks[i] + 0.2, str(snacks[i]), ha='center', fontsize=10, color='purple')

plt.tight_layout()
plt.show()
