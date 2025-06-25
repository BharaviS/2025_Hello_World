from datetime import datetime
import csv

try:
    Today = datetime.now().strftime("%d-%m-%Y")
    Time = datetime.now().strftime("%I:%M:%S %p")
    Filename = "users.csv"
except Exception as er:
    print(f"Unexpected error: {er}")

def write_csv():
    try:
        global Today, Time, Filename
        with open(Filename, mode="w", newline="") as file:
            writer = csv.writer(file)
            writer.writerow(["Name", "Email", "Joined_Date"])
            writer.writerow(["Bharavi", "bharavi@mymail.com", Today])
        print("CSV file created and first user written.")
    except Exception as e:
        print(f"Unexpected error: {e}")

def read_csv():
    try:
        global Filename
        with open(Filename, mode="r") as file:
            reader = csv.reader(file)
            print(f"\nCurrent CSV Data:")
            for row in reader:
                print(" | ".join(row))
    except Exception as e:
        print(f"Unexpected error: {e}")

def append_csv():
    try:
        with open(Filename, mode="a", newline="") as file:
            writer = csv.writer(file)
            writer.writerow(["Charai", "Chari@mymail.com", Today])
            writer.writerow(["Sai", "sai@mymail.com", Today])
        print("More users appended to CSV.")
    except Exception as e:
        print(f"Unexpected error: {e}")

if __name__ == "__main__":
    try:
        #write_csv()
        #append_csv()
        read_csv()
    except Exception as er:
        print(f"Unexpected error: {er}")