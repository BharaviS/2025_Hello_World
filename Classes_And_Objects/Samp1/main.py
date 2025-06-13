class Marks:
    def __init__(self, name: str, **details: float) -> None:
        self.__name = name
        self.__marks = details

    def get_name(self) -> str:
        return self.__name

    def get_marks(self) -> float:
        total: float = 0.0
        for subjects, marks in self.__marks.items():
            total = total + marks
        return round((total/len(self.__marks)), 2)

    def get_subjects_marks(self) -> list[str]:
            return [f"{subjects}: {marks}" for subjects, marks in self.__marks.items()]

    def get_grade(self) -> str:
        avg = self.get_marks()
        if avg >= 90:
            return "A+"
        elif avg >= 80:
            return "A"
        elif avg >= 70:
            return "B"
        elif avg >= 60:
            return "C"
        else:
            return "F"

class StudentsData:
    def __init__(self, students: int) -> None:
        self.__students = students
        self.__mystudents = []

    def get_names(self) -> None:
        for i in range(1, self.__students + 1):
            name = input(f"\nEnter name for student {i}: ")
            subject = ["Maths", "Science"]

            subject_marks = {}
            for sub in subject:
                while True:
                    try:
                        mark = float(input(f"Enter marks for {sub}: "))
                        subject_marks[sub] = mark
                        break
                    except ValueError:
                        print("Please enter a valid number.")


            student = Marks(name, **subject_marks)
            self.__mystudents.append(student)

    def get_total_marks(self) -> None:
        for student in self.__mystudents:
            print(f"\nStudent name: {student.get_name()}")
            for line in student.get_subjects_marks():
                print(line)
            print(f"Average Marks: {student.get_marks()}")
            print(f"Grade: {student.get_grade()}")

if __name__ == '__main__':
    v = StudentsData(1)
    v.get_names()
    v.get_total_marks()




    """v = Marks("Bharavi", Maths = 10, English = 20)
    print(f"Student name: {v.name}")
    print(f"Student marks:")
    for line in v.get_subjects_marks():
        print(f"{line}")
    print(f"Total marks: {v.get_marks()}")"""