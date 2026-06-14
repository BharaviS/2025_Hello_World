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

cursor.execute("SELECT * FROM employees")
emp_one = cursor.fetchone()
emp_meny = cursor.fetchmany(2)
# emp_set = cursor.fetchsets()
employees = cursor.fetchall()

cursor.execute("SELECT * FROM departments")
departments = cursor.fetchall()

for e_row in employees:
    print(e_row)

print("\n")

for d_row in departments:
    print(d_row)

print("\n")

print(emp_one ,"\n")
print(emp_meny, "\n")

print("\n")