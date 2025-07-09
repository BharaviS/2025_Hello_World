import pandas as pd

data = {
    "Name": ["Bharavi", "Bharani", "Charan", "Sai", "Sinu", "Tarun"],
    "Age": [25, 23, 24, 26, 25, 22],
    "City": ["Guntur", "Germany","Guntur", "Germany", "Vizag", "Guntur"],
    "Snacks": ["sandwich", "Pizza","Noodles", "Manchurian", "Fried rice", "Burger"],
    "Amount": [50, 60, 40,70, 30, 90]
}

df = pd.DataFrame(data)

print(df.groupby("City")["Amount"].sum(), "\n")
print(df.groupby("Snacks")["Amount"].mean(), "\n")
print(df.sort_values("Amount"), "\n")
print(df.sort_values(by=["City", "Amount"]), "\n")
print(df.groupby("Snacks")["Amount"].agg(["sum", "mean", "max", "min"]), "\n")

# 🍽️ Which city spent the highest total amount?
city_spending = df.groupby("City")["Amount"].sum()
max_city = city_spending.idxmax()
print("City with highest spending:", max_city)

# 🍕 What is the average amount spent on each snack?
print(df.groupby("Snacks")["Amount"].mean(), "\n")

# 🏙️ Sort the entire DataFrame by City and Amount descending.
print(df.sort_values(by=["City", "Amount"], ascending=[True, False]))