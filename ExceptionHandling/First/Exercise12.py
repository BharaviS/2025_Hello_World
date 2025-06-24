#Imports

#Exception classes
class InvalidNameError(Exception): pass
class InvalidEmailError(Exception): pass
class PhoneNumberError(Exception): pass
class WeakPasswordError(Exception): pass

#Name validation
def validate_name(name: str) -> str:
    name = name.strip()

    if not name:
        raise InvalidNameError("Please enter your user name.")

    if any(char.isdigit() for char in name):
        raise  InvalidNameError("User name must contains alphabets.")

    special: str = "`~!@#$%^&*()><,.?/:;|{}[]+=-_"
    if any(char in special for char in name):
        raise InvalidNameError(f"Your user name does not contain special characters.")

    return name

#Email validation
def validate_email(mail: str) -> str:
    mail: str = mail.strip().lower()
    allow_domain = "mymail.com"

    if not mail:
        raise InvalidEmailError("Please enter your Email id.")

    if "@" not in mail and "." not in mail:
        raise InvalidEmailError("'@' and '.' are missing in your email. Please reenter your correct email.")
    if "@" not in mail:
        raise InvalidEmailError("'@' is missing in your email. Please reenter your correct email.")
    if "." not in mail:
        raise InvalidEmailError("'.' is missing in your email. Please reenter your correct email.")

    user, _, domain = mail.partition("@")
    if not user:
        raise InvalidEmailError("User part before '@' cannot be empty.")
    if not any(ch.isalpha() for ch in user):
        raise InvalidEmailError("User part must contain at least one alphabet.")

    if domain != allow_domain:
        raise InvalidEmailError("Your email must ends with 'mymail.com'")


    return mail

#Phone number validation
def validate_phone(number: str, length: int = 10) -> str:
    number = number.strip()

    if not number:
        raise PhoneNumberError("Please enter your mobile number.")

    cleaned = number.replace(" ", "").replace("-", "")
    country = ""

    if cleaned.startswith("+"):
        if " " in number:
            country, cleaned = number.split(None, 1)
            cleaned = cleaned.replace(" ", "").replace("-", "")
        else:
            country = cleaned[:3]
            cleaned = cleaned[3:]

    if not cleaned.isdigit():
        raise PhoneNumberError("Mobile number must contains only digits.")

    if len(cleaned) != length:
        raise PhoneNumberError("Mobile number must contains exactly 10 digits.")

    return (country + " " if country else "") + cleaned

#Password validation
def validate_password(password: str, min_len: int = 8) -> str:
    special = "`~!@#$%^&*()><,.?/:;|{}[]+=-_"

    if not password:
        raise WeakPasswordError(f"Please enter your password.")
    if len(password) < min_len:
        raise WeakPasswordError(f"Password must contains min {min_len} characters.")
    if not any(char.isupper() for char in password):
        raise WeakPasswordError(f"Your password must contains at least one uppercase letter.")
    if not any(char.islower() for char in password):
        raise WeakPasswordError(f"Your password must contains at least one lower letter.")
    if not any(char.isdigit() for char in password):
        raise WeakPasswordError(f"Your password must contains at least one numer.")
    if not any(char in special for char in password):
        raise WeakPasswordError(f"Your password must contains at least one special characters.")

    return password

#main
if __name__ == "__main__":
    try:
        Name: str = validate_name(input("Enter your user name: "))
        Email: str = validate_email(input("Enter your Email id: "))
        Number: str = validate_phone(input("Enter your mobile number: "))
        Password: str = validate_password(input("Enter your password: "))

        print(f"Your name is {Name}.")
        print(f"Your email id is {Email}.")
        print(f"Your email id is {Number}")
        print(f"Your email id is {Password}")
        print("Your datels are valid.")

    except (InvalidNameError, InvalidEmailError, PhoneNumberError, WeakPasswordError) as e:
        print("Exception:", e)