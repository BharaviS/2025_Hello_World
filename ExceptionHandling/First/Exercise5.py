#Errors
class EmptyNameError(Exception):
    pass

class InvalidNameError(Exception):
    pass

#Rise error condieation
def myname(name):
    if name == "":
        raise EmptyNameError("Please enter your name")
    elif name.isdigit():
        raise InvalidNameError("Name cannot be a number.")
    return f"Your name is {name}"

#Input string
try:
    name = input("Enter yor name: ")
    print(myname(name))
except EmptyNameError as e:
    print("Custom Exception:", e)
except InvalidNameError as e:
    print("Custom Exception:", e)