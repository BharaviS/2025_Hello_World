import json

try:
    Filename = "JSON\\profile.json"
    user_profile = {
        "name": "Bharavi",
        "age": 25,
        "email": "bharavi@mymail.com",
        "number": "+91 9381153646",
        "skills": ["Python", "Pandas", "JSON"],
        "address": {"city": "Guntur", "pincode": 520002},
        "active": True
    }
except Exception as er:
    print(f"Unexpected Error: {er}")

def write_json():
    try:
        with open(Filename, mode="w") as file:
            json.dump(user_profile, file, indent=4)
        print(f"'{Filename}' file created successfully.")
    except Exception as e:
        print(f"Unexpected Error: {e}")

def read_json():
    try:
        with open(Filename, mode="r") as file:
            date = json.load(file)

        address = date.get("address", {})
        print("Profile Details:")
        print(f"Name: {date['name']}")
        print(f"Age: {date['age']}")
        print(f"Email: {date['email']}")
        print(f"Mobile: {date['number']}")
        print(f"Skills: {', '.join(date['skills'])}")
        print(f"City: {address.get('city')}")
        print(f"Pincode: {address.get('pincode')}")
        print(f"Active: {'Yes' if date['active'] else 'No'}")
    except FileNotFoundError:
        print(f"Error: File not found.")
    except json.JSONDecodeError:
        print(f"Error: File is not valid JSON.")
    except Exception as e:
        print(f"Unexpected Error: {e}")

def update_json():
    try:
        with open(Filename, mode="r") as file:
            data = json.load(file)

        data["skills"].append("Threading")
        data["active"] = True
        data["address"]["pincode"] = 522007

        with open(Filename, mode="w") as file:
            json.dump(data, file, indent=4)

        print("Data updated successfully!")
    except FileNotFoundError:
        print(f"Error: File not found.")
    except json.JSONDecodeError:
        print(f"Error: File is not valid JSON.")
    except Exception as e:
        print(f"Unexpected Error: {e}")

def delete_json():
    try:
        with open(Filename, mode="r") as file:
            data = json.load(file)

        data["skills"].remove("Threading")

        with open(Filename, mode="w") as file:
            json.dump(data, file, indent=4)

        print("Data updated successfully!")
    except FileNotFoundError:
        print(f"Error: File not found.")
    except json.JSONDecodeError:
        print(f"Error: File is not valid JSON.")
    except Exception as e:
        print(f"Unexpected Error: {e}")

if __name__ == "__main__":
    try:
        #write_json()
        #update_json()
        #delete_json()
        read_json()
    except Exception as er:
        print(f"Unexpected Error: {er}")