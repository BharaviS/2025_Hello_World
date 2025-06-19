class NagitiveValueError(Exception):
    """Raised with input value is nagitive"""
    pass

def sq_root(x):
    if x < 0:
        raise NagitiveValueError("cannot take sequare root of a nagitive number")
    return x**0.5

try:
    num = int(input("Enter a value: "))
    print(sq_root(num))
except NagitiveValueError as e:
    print(f"You entered negitive number {e}, please enter a valid number.")
except ValueError:
    print("Invalid input: Please enter a number.")