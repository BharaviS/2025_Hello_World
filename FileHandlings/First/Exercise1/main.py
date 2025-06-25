#imports
from datetime import datetime

#global variable
try:
    today = datetime.now().strftime("%d-%m-%Y")
    time = datetime.now().strftime("%I:%M:%S %p")
except Exception as er:
    print(f"Unexpected error: {er}")

#functions
def write_file():
    try:
        global today, time
        with open("dailylog.txt", "w") as file:
            file.write("Name: Bharavi\n")
            file.write(f"Date: {today}\n")
            file.write(f"time: {time}\n")
        print("File 'daily.log' created and written successfully!")
    except FileNotFoundError:
        print("Error: The file path is invalid.")
    except PermissionError:
        print("Error: you dont have permission to write to the location.")
    finally:
        print("File write attempt finished.")

def read_file():
    try:
        with open("dailylog.txt", "r") as file:
            content = file.read()
            print(f"File Content:\n{content}")
    except FileNotFoundError:
        print("Error: The file path is invalid.")
    except PermissionError:
        print("Error: you dont have permission to write to the location.")
    except Exception as e:
        print(f"Unexpected error: {e}")
    finally:
        print("File read attempt finished.")

def append_file():
    try:
        global today, time
        with open("dailylog.txt", "a") as file:
            file.write(f"time: {time}\n")
    except FileNotFoundError:
        print("Error: The file path is invalid.")
    except PermissionError:
        print("Error: you dont have permission to write to the location.")
    except Exception as e:
        print(f"Unexpected error: {e}")
    finally:
        print("File write attempt finished.")

if __name__ == "__main__":
    try:
        #write_file() #Is already executed
        append_file()
        read_file()
    except Exception as er:
        print(f"Unexpected error: {er}")