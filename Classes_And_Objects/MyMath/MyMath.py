class MyMath:
    def __init__(self, *details) -> None:
        self.my_details = details

    def Add(self):
        total = 0
        for iv in self.my_details:
            total += iv

        return total

    def Sup(self):
        total = 0
        for iv in self.my_details:
            total -= iv
        return total

    def Mul(self):
        total = 1
        for iv in self.my_details:
            total *= iv
        return total

    def Dev(self):
        if 0 in self.my_details[1:]:
            return "Cannot divide by zero"

        total = self.my_details[0]
        for iv in self.my_details[1:]:
            total /= iv
        return round(total, 3)

    def Modules(self):
        if 0 in self.my_details[1:]:
            return "Cannot divide by zero"

        total = self.my_details[0]
        for iv in self.my_details[1:]:
            total %= iv
        return round(total, 3)

    def factoriel(self):
        if not self.my_details:
            return "No number provided for factorial"
        n = self.my_details[0]
        if not isinstance(n, int) or n < 0:
            return "Factorial only supports non-negative integers"

        fact = 1
        for ir in range(1, n + 1):
            fact *= ir
            print(f"{ir}! = {fact}")
        return fact


if __name__ == '__main__':
    i = MyMath(2, 3)
    print(i.Modules())