class Item:
    def __init__(self, name, **data) -> None:
        print(name)

        for i, j in data.items():
            print(i, j)


if __name__ == '__main__':
    Item("Bharavi", age = 28, white = 67)