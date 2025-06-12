from main import *

students = int(input("Enter number of students: "))

v = StudentsData(students)
v.get_names()
v.get_total_marks()