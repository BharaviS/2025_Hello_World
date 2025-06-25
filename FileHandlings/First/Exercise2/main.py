from datetime import datetime
import csv

try:
    Date = datetime.now().strftime("%d-%m-%Y")
    time = datetime.now().strftime("%I:%M:%S %p")
    file = "users.csv"
except Exception as er:
    print(f"Unexpected error: {er}")

def date():
    global Date
    print(Date)

if __name__ == "__main__":
    try:
        date()
    except Exception as er:
        print(f"Unexpected error: {er}")