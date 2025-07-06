import pandas as pd

data = {
    "Name": ["Bharavi", "Bharani", "Charan", "sai", "Sinu"],
    "Age": [25, 23, 24, 26, 25],
    "City": ["Guntur", "Germany","Vijayawada", "Hyderabad", "Vizag"],
    "Snacks": ["sandwich", "Pizza","Noodles", "Manchurian", "Fried rice"]
}

df = pd.DataFrame(data)

print(df["Name"], "\n")
print(df.Name, "\n")
print(df[["Name", "City"]], "\n")
print(df.iloc[0], "\n")
print(df.iloc[1:4], "\n")
print(df.loc[0], "\n")
print(df.loc[2:4], "\n")
print(df[df["Age"] > 24], "\n")
print(df[df["City"] == "Vizag"], "\n")


df_index = df.set_index("Name")
df_name = input("Enter your name: ")
df_name = df_name[0].upper() + df_name[1:].lower()
try:
    print(df_index.loc[df_name], "\n")
except KeyError:
    print(f"Name '{df_name}' is not found.\n")

#🧠Challenge: 🔥 Print names of all friends who like snacks that contain the letter "i" (hint: use .str.contains())
print(df[df["Snacks"].str.contains("i")], "\n")