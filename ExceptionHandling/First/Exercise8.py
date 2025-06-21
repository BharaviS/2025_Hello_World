class InvalidEmailError(Exception):
    pass

def validate_email(email):
    if "@" not in email and "." not in email:
        raise InvalidEmailError("Email must contain '@' and '.'")
    elif "@" not in email:
        raise InvalidEmailError("missing '@'")
    elif "." not in email:
        raise InvalidEmailError("missing '.'")
    return email

try:
    Email = input("Enter your email: ").strip()
    i = validate_email(Email.lower())
    print(f"Your email {i} is valid")
except InvalidEmailError as e:
    print("Exception: ", e)