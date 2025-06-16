class MyDiv:
    def __init__(self, val: int) -> None:
        self.__val = val

    @property
    def result(self) -> int | float| str:
        try:
            r = self.__val
            re = 100/r
            return re
        except ZeroDivisionError:
            return f"Math error: Cannot divide by zero."
        finally:
            print("This block always executes — even if there was an error.")

if __name__ == '__main__':
    try:
        myval = int(input("Enter a value: "))
        si = MyDiv(myval)
        print(f"My value is: {si.result}")
    except ValueError:
        print(f"Invalid input: Not an integer.")