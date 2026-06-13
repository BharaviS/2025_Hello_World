CREATE DATABASE mysql_learning;

CREATE TABLE employees (
    eid INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    department VARCHAR(50),
    salary DECIMAL(10, 2),
    joining_date DATE
);

INSERT INTO employees (name, department, salary, joining_date)
VALUES
('Ram', 'IT', 50000, '2024-01-15'),
('Ravi', 'HR', 40000, '2024-02-10'),
('Kiran', 'Sales', 45000, '2024-03-05'),
('Sai', 'IT', 70000, '2024-01-20'),
('Anu', 'Finance', 55000, '2024-04-12'),
('Priya', 'HR', 42000, '2024-05-01'),
('Venu', 'Sales', 48000, '2024-02-18'),
('Teja', 'IT', 65000, '2024-03-22');

SELECT * FROM employees;

CREATE TABLE departments (
    dept_id INT AUTO_INCREMENT PRIMARY KEY,
    dept_name VARCHAR(50) NOT NULL
);

INSERT INTO departments (dept_name)
VALUES
('IT'),
('HR'),
('Sales'),
('Finance');

SELECT * FROM departments;