import time

class Car:
    @staticmethod
    def start_car() -> None:
        print("🚗 Starting the car...")

    @staticmethod
    def accelerate_car() -> None:
        print("🏁 Car is moving...")

    @staticmethod
    def brake_car() -> None:
        print("🛑 Stopping the car...")


class BMW(Car):
    def __init__(self, name: str, color: str) -> None:
        self.__name = name
        self.__color = color
        #super().start_car()

    def get_car_name(self) -> str:
        return self.__name

    def get_car_color(self) -> str:
        return self.__color


class Toyota(Car):
    def __init__(self, name: str, color: str) -> None:
        self.__name = name
        self.__color = color

    def get_car_name(self) -> str:
        return f"Car name: {self.__name}"

    def get_car_color(self) -> str:
        return f"Car color: {self.__color}"


if __name__ == '__main__':
    car1 = BMW("320D", "Blue")

    print(f"🚘 Car Name: {car1.get_car_name()}")
    print(f"🎨 Car Color: {car1.get_car_color()}")

    time.sleep(1)
    car1.start_car()
    time.sleep(2)
    car1.accelerate_car()
    time.sleep(3)
    car1.brake_car()
