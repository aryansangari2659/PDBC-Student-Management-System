import os
import mysql.connector

# Database Connection
con = mysql.connector.connect(
    host="localhost",
    user="root",
    password=os.environ.get("MYSQL_PASSWORD"),
    database="student_db"
)

cursor = con.cursor()

print("Database Connected Successfully! - main.py:14")


# CREATE - Add Student
def add_student():
    name = input("Enter Name: ")
    age = int(input("Enter Age: "))
    course = input("Enter Course: ")
    email = input("Enter Email: ")

    query = """
    INSERT INTO students (name, age, course, email)
    VALUES (%s, %s, %s, %s)
    """

    values = (name, age, course, email)

    cursor.execute(query, values)
    con.commit()

    print("Student Added Successfully! - main.py:34")


# READ - Display Students
def display_students():
    cursor.execute("SELECT * FROM students")

    records = cursor.fetchall()

    print("\n STUDENT RECORDS - main.py:43")

    if not records:
        print("No student records found. - main.py:46")

    for record in records:
        print(record)


# SEARCH - Find Student
def search_student():
    student_id = int(input("Enter Student ID: "))

    query = "SELECT * FROM students WHERE student_id = %s"

    cursor.execute(query, (student_id,))

    record = cursor.fetchone()

    if record:
        print("Student Found: - main.py:63", record)
    else:
        print("Student Not Found! - main.py:65")


# UPDATE - Modify Student
def update_student():
    student_id = int(input("Enter Student ID: "))
    email = input("Enter New Email: ")

    query = """
    UPDATE students
    SET email = %s
    WHERE student_id = %s
    """

    cursor.execute(query, (email, student_id))
    con.commit()

    if cursor.rowcount > 0:
        print("Student Updated Successfully! - main.py:83")
    else:
        print("Student Not Found! - main.py:85")


# DELETE - Remove Student
def delete_student():
    student_id = int(input("Enter Student ID: "))

    query = "DELETE FROM students WHERE student_id = %s"

    cursor.execute(query, (student_id,))
    con.commit()

    if cursor.rowcount > 0:
        print("Student Deleted Successfully! - main.py:98")
    else:
        print("Student Not Found! - main.py:100")


# Main Menu
try:
    while True:

        print("\n===== STUDENT MANAGEMENT SYSTEM ===== - main.py:107")
        print("1. Add Student - main.py:108")
        print("2. Display Students - main.py:109")
        print("3. Search Student - main.py:110")
        print("4. Update Student - main.py:111")
        print("5. Delete Student - main.py:112")
        print("6. Exit - main.py:113")

        choice = input("Enter Your Choice: ")

        if choice == "1":
            add_student()

        elif choice == "2":
            display_students()

        elif choice == "3":
            search_student()

        elif choice == "4":
            update_student()

        elif choice == "5":
            delete_student()

        elif choice == "6":
            print("Exiting Application... - main.py:133")
            break

        else:
            print("Invalid Choice! - main.py:137")

finally:
    cursor.close()
    con.close()
    print("Database Connection Closed. - main.py:142")
