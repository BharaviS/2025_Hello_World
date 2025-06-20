class InvalidAgrError(Exception):
    pass

def check_age(age):
    if age < 0:
        raise InvalidAgrError("Age cannot be negative.")
    elif age > 130:
        raise InvalidAgrError("Are you a time traveler.")
    return f"Valid age: {age}"

try:
    age = int(input("Enter your age: "))
    print(check_age(age))
except InvalidAgrError as e:
    print("Exception: ", e)
except ValueError:
    print("Invalid input: please enter a number.")
