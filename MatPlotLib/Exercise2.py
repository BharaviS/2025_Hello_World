import matplotlib.pyplot as plt

x = ["Bharavi", "Bharani", "Charan", "Sai", "Srinu"]
y = [50, 20, 30, 80, 70]

plt.plot(x, y, label="Scores", color='gray', marker="o", linestyle='--', markersize=7.5)
plt.grid(True, linestyle=':', linewidth=0.5)

plt.title("Marks")
plt.xlabel("Students")
plt.ylabel("Scores")
plt.xticks(rotation=0)
plt.yticks(range(0, 101, 10))

plt.legend()

plt.show()