from dotenv import load_dotenv

import mysql.connector
import os

load_dotenv()

connection = mysql.connector.connect(
    host=os.getenv("MYSQL_HOST"),
    user=os.getenv("MYSQL_USER"),
    password=os.getenv("MYSQL_PASSWORD"),
    database=os.getenv("MYSQL_DATABASE")
)

cursor = connection.cursor()

def search_by_id(eid: str | int) -> list | str:
    cursor.execute("select * from employees where eid = %s",  (eid,))
    result = cursor.fetchall()

    if not result:
        return f"Employee {eid} not found"

    return result

def search_by_name(name: str) -> list | str:
    cursor.execute("select * from employees where name = %s",  (name,))
    result = cursor.fetchall()

    if not result:
        return f"Employee {name} not found"

    return result

def search_by_department(department: str) -> list | str:
    cursor.execute("select * from employees where department = %s", (department,))
    result = cursor.fetchall()

    if not result:
        return f"Employee {department} not found"

    return result

def search_by_employee_salary_grater_than(employee_salary: str | int) -> list | str:
    cursor.execute("select * from employees where salary > %s", (employee_salary,))
    result = cursor.fetchall()

    if not result:
        return f"Employee {employee_salary} not found"

    return result

def search_by_employee_salary_lesser_than(employee_salary: str | int) -> list | str:
    cursor.execute("select * from employees where salary < %s", (employee_salary,))
    result = cursor.fetchall()

    if not result:
        return f"Employee {employee_salary} not found"

    return result

def search_by_employee_salary_equal_to(employee_salary: str | int) -> list | str:
    cursor.execute("select * from employees where salary = %s", (employee_salary,))
    result = cursor.fetchall()

    if not result:
        return f"Employee {employee_salary} not found"

    return result

if __name__ == '__main__':
    try:
        employee_id = int(input("Enter employee ID: "))
        print(search_by_id(employee_id))
    except ValueError:
        print("Invalid Employee ID")

    employee_name = input("Enter employee name: ").strip().capitalize()

    if not employee_name:
        print("Invalid name")
    else:
        print(search_by_name(employee_name))

    print(search_by_department("IT"))
    print(search_by_employee_salary_grater_than(50000))
    print(search_by_employee_salary_lesser_than(50000))
    print(search_by_employee_salary_equal_to(50000))