class Item:
    def __init__(self, name: str, age: int) -> None:
        self.name: str = name
        self.age: int = age

    """def get_info(self) -> tuple:
        return self.name, self.age"""

    def __str__(self):
        return f"Name {self.name}, age {self.age}"

if __name__ == '__main__':
    item = Item("Bharavi", 28)
    print(item)