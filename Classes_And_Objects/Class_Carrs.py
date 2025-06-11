class Cars:
    def __init__(self, Carname: str, Prise: int, Color: str) -> None:
        self.car: str = Carname
        self.prise: int = Prise
        self.color: str = Color

    def CarName(self) -> str:
        return self.car

    def CarPrise(self) -> int:
        return self.prise

    def CarColor(self) -> str:
        return self.color

    def main(self) -> str:
        return f"{self.car}, ${self.prise}, {self.color}"

    def __str__(self) -> str:
        return f"{self.car}, ${self.prise}, {self.color}"

if __name__ == "__main__":
    car1 = Cars("BMW", 200, "grean")
    print(f"Car name is: {car1.CarName()}")
    print(f"Car prise is: ${car1.CarPrise()}")
    print(f"Car color is: {car1.CarColor()}")
    print("*********************************")
    print(f"cars data:\n{car1.main()}")