class InvalidGradeError(ValueError):
    """Raised when an unknown grade letter is supplied."""

class Demo:
    def __init__(self, res: str):
        self.__res = res.upper()

    @property
    def grade(self) -> int | str:
        grade_map = {"O": 10, "S": 9, "A": 8,"B": 7, "C": 6, "D": 5, "F": 0}

        try:
            return grade_map[self.__res]
        except KeyError:  # letter not in the map
            raise InvalidGradeError("Grade must be one of O, S, A, B, C, D, F.")

class Syear:
    def __init__(self):
        _subjects = []

    @property
    def sem_1(self) -> int | float:
        _subjects = [("Subject 1", 3), ("Subject 2", 3), ("Subject 3", 3),
                     ("Subject 4", 3), ("Subject 5", 3), ("Subject 6", 3),
                     ("Subject 7", 2), ("Subject 8", 2), ("Subject 9", 2)]
        total_points = 0
        total_cradits = 0

        for names, cradits in _subjects:
            while True:
                try:
                    mark = input(f"Enter your grade for {names}: ").strip()
                    if not mark:
                        raise ValueError("Grade cannot be blank.")

                    if not mark.isalpha():
                        raise ValueError("\nGrade must be a letter (O, S, A, B, etc.).")

                    sm = Demo(mark)
                    total_points += sm.grade*cradits
                    total_cradits += cradits
                    break
                except (ValueError, InvalidGradeError) as ve:
                    print(f"Invalid input: {ve}")

        return round(total_points / total_cradits, 2)

    @property
    def sem_2(self) -> int | float:
        _subjects = [("Subject 1", 3), ("Subject 2", 3), ("Subject 3", 3),
                     ("Subject 4", 3), ("Subject 5", 3), ("Subject 6", 3),
                     ("Subject 7", 2), ("Subject 8", 2), ("Subject 9", 2)]
        total_points = 0
        total_cradits = 0

        for names, cradits in _subjects:
            while True:
                try:
                    mark = input(f"Enter your grade for {names}: ").strip()
                    if not mark:
                        raise ValueError("Grade cannot be blank.")

                    if not mark.isalpha():
                        raise ValueError("\nGrade must be a letter (O, S, A, B, etc.).")

                    sm = Demo(mark).grade
                    total_points += sm * cradits
                    total_cradits += cradits
                    break
                except (ValueError, InvalidGradeError) as ve:
                    print(f"Invalid input: {ve}")

        return round(total_points / total_cradits, 2)


if __name__ == '__main__':
    i = Syear()
    print(f"Invalid input: {i.sem_1}")