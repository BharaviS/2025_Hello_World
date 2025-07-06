import pandas as pd

data = {
    "Name": ["Bharavi", "Bharani", "Charan", "Sai", "Sinu"],
    "Age": [25, 23, 24, 26, 25],
    "City": ["Guntur", "Germany","Vijayawada", "Hyderabad", "Vizag"],
    "Snacks": ["sandwich", "Pizza","Noodles", "Manchurian", "Fried rice"]
}

df = pd.DataFrame(data)

df["Hobby"] = ["Gaming", "Cricket", "Reading", "Dancing", "Singing"]
print(df, "\n")

new_row = {"Name": "Tarun", "Age": 22, "City": "Delhi", "Snacks": "Burger", "Hobby": "Photography"}
df.loc[len(df)] = new_row

print(df, "\n")

df.loc[df["Name"] == "Sai", "Snacks"] = "Biryani"
print(df, "\n") #This is not working. Siri can you please help me hear

df.drop(columns="City", inplace=True)
print(df, "\n")

df = df[df["Name"] != "Charan"]
#df.drop(index=2, inplace=True)
print(df, "\n")

print(df[(df["Age"].between(23, 25)) & (df["Snacks"].str.contains("a"))])