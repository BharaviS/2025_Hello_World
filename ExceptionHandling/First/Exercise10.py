class PhoneNumberError(Exception):
    pass

def valid_number(number: str, length: int = 10) -> str:

    if number == "":
        raise PhoneNumberError("Please enter your mobile number.")

    """temp = number.replace(" ", "").replace("-", "")
    country = """

    number = number.strip()

    if number.startswith("+"):
        parts = number.split()

        if len(parts) != 2:
            raise PhoneNumberError("Format should be: +<code> <10-degit-number>.")

        country_code, mobile = parts

        if not mobile.isdigit():
            raise PhoneNumberError("Mobile number must contains only digits.")

        if len(mobile) != length:
            raise PhoneNumberError("Mobile number must contains exactly 10 digits.")

        return f"{country_code} {mobile}"
    else:
        if not number.isdigit():
            raise PhoneNumberError("Mobile number must contains only digits.")

        if len(number) != length:
            raise PhoneNumberError("Mobile number must contains exactly 10 digits.")

    return number

if __name__ == "__main__":
    try:
        Number: int | str = input("Please enter your valid mobile number: ").strip()
        Mob_num = valid_number(Number)
        print(Mob_num)

    except PhoneNumberError as e:
        print("Exception:", e)
