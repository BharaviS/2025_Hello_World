import pandas as pd

data = {
    "Name": ["Bharavi", "Bharani", "Charan", "sai", "Sinu"],
    "Age": [25, 23, 24, 26, 25],
    "City": ["Guntur", "Germany","Vijayawada", "Hyderabad", "Vizag"],
    "Snacks": ["sandwich", "Pizza","Noodles", "Manchurian", "Fried rice"]
}

df = pd.DataFrame(data)

print("\nFriends Info DataFrame:")
print(df)

print("\nColumns:", df.columns.tolist())
print("\nShape:", df.shape)
print("\nData Types:\n", df.dtypes)
print("\nDescribe:\n", df.describe(include='all'))
