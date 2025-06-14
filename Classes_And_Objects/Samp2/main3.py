import math as mt

class _Circle:
    def __init__(self, radius: int | float) -> None:
        self.__radius: int | float = radius
        self.__pi: float = mt.pi

    @property
    def radius(self) -> int | float:
        return self.__radius

    @radius.setter
    def radius(self, value: int | float) -> None:
        if value <= 0:
            raise ValueError("Radius must be a positive number.")
        self.__radius = value

    @property
    def area(self) -> float:
        return round((self.__pi * self.__radius ** 2), 4)

    @property
    def perimeter(self) -> float:
        return round(2 * self.__pi * self.__radius, 4)

if __name__ == '__main__':
    mycircle = _Circle(21)
    print(f"Area of a circle: {mycircle.area}")
    print(f"Perimeter of a circle: {mycircle.perimeter}")

    print("\n")

    mycircle.radius = 10
    print(f"Updated radius of a circle: {mycircle.radius}")
