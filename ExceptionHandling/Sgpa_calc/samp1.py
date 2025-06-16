class Demo:
    def __init__(self, res: str):
        self.__res = res.upper()

    @property
    def grade(self) -> int | str:
        grade_map = {
            "O": 10, "S": 9, "A": 8,
            "B": 7, "C": 6, "D": 5, "F": 0
        }

        if self.__res in grade_map:
            return grade_map[self.__res]
        else:
            return "\nPlease check your values...."

class Syear:
    def __init__(self):
        pass

    @property
    def sem_1(self) -> int | float:
        subject = ["English-I", "Subjecr 2"]

        subject_marks = {}
        # Reading values
        for sub in subject:
            while True:
                try:
                    mark = input(f"Enter your grade for {sub}: ").strip()
                    if not mark:
                        raise ValueError("\nGrade cannot be blank.")

                    if not mark.isalpha():
                        raise ValueError("\nGrade must be a letter (O, S, A, B, etc.).")

                    sm = Demo(mark)
                    subject_marks[sub] = sm.grade
                    break
                except ValueError as ve:
                    print(f"Invalid input: {ve}")

        # operation
        __marks = subject_marks
        #sit = {}

        #retyrn
        return subject_marks


if __name__ == '__main__':
    i = Syear()
    print(i.sem_1)


    """try:
        inx = input("Enter your grade: ").strip()

        if not inx:
            raise ValueError("\nGrade cannot be blank.")

        if not inx.isalpha():
            raise ValueError("\nGrade must be a letter (O, S, A, B, etc.).")

        dev = Demo(inx)
        print(f"Your score is: {dev.grade}")
    except ValueError as ve:
        print(f"Invalid input: {ve}")"""