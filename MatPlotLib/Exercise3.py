import matplotlib.pyplot as plt

friends = ["Bharavi", "Bharani", "Charan", "Sai", "Srinu"]
laughter_score = [50, 20, 30, 80, 70]

plt.plot(friends, laughter_score, label="Laughter Level 😂", color='orange', marker="*", linestyle='--', markersize=7.5)
plt.grid(True, linestyle=":", linewidth=1)

plt.title("Siri's Laughter Meter 😂", fontsize = 14, color="purple")
plt.xlabel("Friends", fontsize=12)
plt.ylabel("Laughter Score", fontsize=12)

plt.xticks(rotation=0)
plt.yticks(range(0, 110, 10))

plt.legend(loc='upper center')

plt.show()