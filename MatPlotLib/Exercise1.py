import matplotlib.pyplot as plt

x = [1, 2, 3, 4, 5]
y = [10, 20, 15, 25, 30]

plt.plot(x, y, label="Sales", color='blue', marker='o', linestyle='--')


plt.title("Monthly Sales Report")
plt.xlabel("Month")
plt.ylabel("Sales")

plt.legend()

plt.show()