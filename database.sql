-- 1. Create Database
CREATE DATABASE IF NOT EXISTS student_db;

-- 2. Select Database
USE student_db;

-- 3. Create Table
CREATE TABLE IF NOT EXISTS students (
    student_id INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(100) NOT NULL,
    age INT,
    course VARCHAR(100),
    email VARCHAR(100)
);

-- 4. Display Tables
SHOW TABLES;

-- 5. Describe Table
DESCRIBE students;

-- 6. Insert Sample Records
INSERT INTO students (name, age, course, email)
VALUES
('Aryan', 22, 'Data Science', 'aryan@gmail.com'),
('Rahul', 23, 'Python', 'rahul@gmail.com'),
('Priya', 21, 'Java', 'priya@gmail.com');

-- 7. Display Records
SELECT * FROM students;