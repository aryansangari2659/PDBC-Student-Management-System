# PDBC Student Management System

## Project overview

This project demonstrates Python Database Connectivity (PDBC) by connecting a Python desktop application to a MySQL database. The application manages student records using CRUD operations.

## Features

- Add a student
- Display all student records
- Select a student from the table
- Update student details
- Delete a student after confirmation
- Refresh the student records displayed in the GUI

## Technologies used

- Python
- MySQL 8.0
- MySQL Connector/Python
- Tkinter for the graphical user interface
- MySQL Workbench for database creation and inspection
- Visual Studio Code (or another Python editor)

## Project structure

```text
PDBC_Student_Management/
├── main.py          # Command-line CRUD application
├── gui_app.py       # Tkinter GUI application
├── database.sql     # Database and table creation script (if saved)
├── requirements.txt # Python package dependencies
└── README.md        # Project documentation
```

## Prerequisites

1. Python 3.11 or a compatible Python 3 version.
2. MySQL Server 8.0 running locally.
3. A MySQL account with permission to create/use the project database.
4. Tkinter available in the Python installation.

## Database setup

Open MySQL Workbench and run:

```sql
CREATE DATABASE IF NOT EXISTS student_db;

USE student_db;

CREATE TABLE IF NOT EXISTS students (
    student_id INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(100) NOT NULL,
    age INT,
    course VARCHAR(100),
    email VARCHAR(100)
);
```

Optional sample records:

```sql
INSERT INTO students (name, age, course, email)
VALUES
('Aryan', 22, 'Data Science', 'aryan@gmail.com'),
('Rahul', 23, 'Python', 'rahul@gmail.com'),
('Priya', 21, 'Java', 'priya@gmail.com');
```

If you have already created the database and table, do not run duplicate sample inserts unless you want additional records.

## Installation

Open a terminal in the project folder and run:

```powershell
python -m pip install -r requirements.txt
```

## Configure the database connection

Open `main.py` and `gui_app.py`. Update the connection settings to match your local MySQL setup:

```python
con = mysql.connector.connect(
    host="localhost",
    user="root",
    password="YOUR_MYSQL_PASSWORD",
    database="student_db"
)
```

Replace `YOUR_MYSQL_PASSWORD` with your own MySQL password. Do not publish or share your real password. For a more secure version, load credentials from environment variables rather than storing them directly in source code.

## Run the applications

Command-line version:

```powershell
python main.py
```

Graphical version:

```powershell
python gui_app.py
```

## CRUD operations

| Operation | SQL statement | Application action |
|---|---|---|
| Create | INSERT | Add a student |
| Read | SELECT | Display student records |
| Update | UPDATE | Modify student details |
| Delete | DELETE | Remove a student record |

## Important implementation notes

- `mysql.connector.connect()` establishes the connection to MySQL.
- `connection.cursor()` creates a cursor used to execute SQL statements.
- `cursor.execute()` executes a SQL statement.
- `connection.commit()` saves INSERT, UPDATE, and DELETE changes.
- `fetchone()` retrieves one result row; `fetchall()` retrieves all result rows.
- `AUTO_INCREMENT` generates unique student IDs. Deleting a row does not normally cause MySQL to reuse its ID. Gaps in IDs are expected.

## Troubleshooting

### Access denied for user

Check the MySQL username and password in the connection settings. Confirm that the MySQL Server service is running.

### Cannot connect to MySQL server

Check that the MySQL80 Windows service is running and that the host and port are correct (the default MySQL port is usually 3306).

### ModuleNotFoundError: No module named 'mysql'

Install the connector using:

```powershell
python -m pip install mysql-connector-python
```

### Tkinter is unavailable

Tkinter normally comes with the standard Windows Python installer. Check it with:

```powershell
python -m tkinter
```

## Project learning outcomes

This project demonstrates how to connect Python to MySQL, execute SQL statements from Python, manage persistent records, and build a simple database-driven desktop application.

## Author

Aryan Sangari
