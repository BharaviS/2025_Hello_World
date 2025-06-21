class InvalidEmailError(Exception):
    pass

class WeakPasswordError(Exception):
    pass

#for specific mail validation
def validate_email_id(email: str) -> str:
    email = email.strip().strip()
    allow_domain = "mymail.com"

    if not email:
        raise InvalidEmailError("Please enter your valid email id.")

    if "@" in email:
        user_part = email.split("@", 1)[0]
    else:
        user_part = email

    if not any(char.isalpha() for char in user_part):
        raise InvalidEmailError("Username must contain at lest one alphabet.")

    if "@" not in email:
        return f"{user_part}@{allow_domain}"

    user, _, domain = email.partition("@")

    if domain == allow_domain:
        return email

    incomplete_domain = {"", "my", "mail","mymail", "mymail.", ".com", "mail.com"}

    if domain in incomplete_domain or (domain.startswith("mymail")) and not domain.endswith(".com"):
        return f"{user_part}@{allow_domain}"

    raise InvalidEmailError("Please enter a valid email id.")

def validate_password(password: str, min_len: int = 8) -> str:
    special = "`~!@#$%^&*()><,.?/:;|{}[]+=-_"

    if password == "":
        raise WeakPasswordError(f"Please enter your password.")

    if not min_len < len(password):
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

if __name__ == "__main__":
    try:
        EmailId = input("Enter your email id: ").strip()
        Mid = validate_email_id(EmailId)

        Password = input("Enter your password: ").strip()
        Pss = validate_password(Password)

        print(f"Your email {Mid} is valid")
        print(f"Your password {Pss} is valid")
    except (InvalidEmailError, WeakPasswordError) as e:
        print("Exception:", e)