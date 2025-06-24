class InvalidNameError(Exception): pass
class InvalidEmailError(Exception): pass

def user_name_validation(name: str) -> str:
    if not name.strip():
        raise InvalidNameError("Please enter your user name.")

    if any(char.isdigit() for char in name):
        raise  InvalidNameError("User name must contains alphabets.")

    special: str = "`~!@#$%^&*()><,.?/:;|{}[]+=-_"
    if any(char in special for char in name):
        raise InvalidNameError(f"Your user name does not contain special characters.")

    return name

def user_email_validation(mail: str) -> str:
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


if __name__ == '__main__':
    try:
        Uname: str = input("Enter your user name: ").strip()
        Name: str = user_name_validation(Uname)

        Email: str = input("Enter your Email id: ").strip()
        Mail: str = user_email_validation(Email)

        print(f"Your user name {Name} is valid.")
        print(f"Your email id {Mail} is valid.")

    except (InvalidNameError, InvalidEmailError) as e:
        print("Exception:", e)