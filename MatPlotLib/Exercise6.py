import matplotlib.pyplot as plt

friends = ["Bharavi", "Bharani", "Charan", "Sai", "Srinu"]
snacks_brought = [5, 2, 4, 8, 3]
colors = ["gold", "lightcoral", "lightskyblue", "lightgreen", "violet"]

explode = [0.1 if s == max(snacks_brought) else 0 for s in snacks_brought]

plt.pie(snacks_brought,
		labels=friends,
		colors=colors,
		explode=explode,
		autopct="%1.1f%%",
		shadow=True,
		startangle=140,
		wedgeprops={"edgecolor": "black", "linewidth": 1})

plt.title("🎉 Party Snack Share 🧁", fontsize=16, color="darkblue")
plt.axis("equal")



plt.legend()
plt.show()