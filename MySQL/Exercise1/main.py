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

for row in cursor.fetchall():
    print(row)