import sys

# Step 1: Reading from stdin (user input)
user_input = input("Enter something: ")
print(f"You entered: {user_input}")

# Step 2: Redirect stdout to a file
original_stdout = sys.stdout  # backup original stdout

with open("output.txt", "w") as f:
    sys.stdout = f  # redirect stdout to file
    print("This will go into the file instead of console.")
    print("Logging info to output.txt")

# Restore original stdout
sys.stdout = original_stdout
print("✅ Output redirection done. Check output.txt")

# Step 3: Redirect stderr and simulate an error
original_stderr = sys.stderr  # backup original stderr

with open("error_log.txt", "w") as f:
    sys.stderr = f  # redirect stderr to file
    print("This is a normal print message.")
    raise ValueError("Something went wrong!")  # This goes to error_log.txt

# Note: The script will stop at raise, so restore stderr if needed earlier