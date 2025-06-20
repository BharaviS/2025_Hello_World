class InputValidationError(Exception):
    pass

def validate_user(name, age):
    if name == "":
        raise InputValidationError("Name cannot be empty.")
    elif name.isnumeric():
       raise InputValidationError("Name must contain letter.")

    if age < 0 or age > 130:
        raise InputValidationError("Invalid age range.")

    return f"Your name is: {name}\nYour age is: {age}"

try:
    my_name = input("Enter your name: ")
    my_age = int(input("Enter your age: "))
    print(validate_user(my_name, my_age))
except InputValidationError as e:
    print("Exception: ", e)
except ValueError:
    print("Invalid input: please enter a number.")