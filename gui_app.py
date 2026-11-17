import os
import tkinter as tk
from tkinter import ttk, messagebox
import mysql.connector

# Database Connection
def connect_db():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password=os.environ.get("MYSQL_PASSWORD"),
        database="student_db"
    )


# Main Window
root = tk.Tk()
root.title("Student Management System")
root.geometry("950x600")
root.configure(bg="#eef2f7")


# Heading
heading = tk.Label(
    root,
    text="STUDENT MANAGEMENT SYSTEM",
    font=("Arial", 20, "bold"),
    bg="#eef2f7",
    fg="#1e3a5f"
)
heading.pack(pady=15)


# Input Frame
form = tk.Frame(root, bg="white", padx=20, pady=15)
form.pack(fill="x", padx=30)


# Input Fields
labels = ["Student ID", "Name", "Age", "Course", "Email"]
entries = {}

for i, label in enumerate(labels):
    tk.Label(
        form,
        text=label,
        bg="white",
        font=("Arial", 11)
    ).grid(row=i, column=0, padx=10, pady=7, sticky="w")

    entry = tk.Entry(form, width=35, font=("Arial", 11))
    entry.grid(row=i, column=1, padx=10, pady=7)

    entries[label] = entry

# Student ID is read-only
entries["Student ID"].config(state="readonly")


# Clear Input Fields
def clear_fields():
    for entry in entries.values():
        entry.config(state="normal")
        entry.delete(0, tk.END)

    entries["Student ID"].config(state="readonly")


# Load Student Records
def display_students():
    for item in table.get_children():
        table.delete(item)

    try:
        con = connect_db()
        cursor = con.cursor()

        cursor.execute("SELECT * FROM students")
        records = cursor.fetchall()

        for record in records:
            table.insert("", tk.END, values=record)

        cursor.close()
        con.close()

    except mysql.connector.Error as err:
        messagebox.showerror("Database Error", str(err))


# Add Student
def add_student():
    name = entries["Name"].get().strip()
    age = entries["Age"].get().strip()
    course = entries["Course"].get().strip()
    email = entries["Email"].get().strip()

    if not all([name, age, course, email]):
        messagebox.showwarning("Warning", "Fill all fields!")
        return

    try:
        age = int(age)

        if age <= 0:
            raise ValueError

        con = connect_db()
        cursor = con.cursor()

        query = """
        INSERT INTO students (name, age, course, email)
        VALUES (%s, %s, %s, %s)
        """

        cursor.execute(query, (name, age, course, email))
        con.commit()

        cursor.close()
        con.close()

        messagebox.showinfo("Success", "Student added successfully!")

        clear_fields()
        display_students()

    except ValueError:
        messagebox.showerror("Invalid Input", "Enter a valid age.")

    except mysql.connector.Error as err:
        messagebox.showerror("Database Error", str(err))


# Select Student from Table
def select_student(event):
    selected = table.focus()

    if not selected:
        return

    values = table.item(selected, "values")

    clear_fields()

    entries["Student ID"].config(state="normal")
    entries["Student ID"].insert(0, values[0])
    entries["Student ID"].config(state="readonly")

    for i, label in enumerate(["Name", "Age", "Course", "Email"], start=1):
        entries[label].insert(0, values[i])


# Update Student
def update_student():
    student_id = entries["Student ID"].get()
    email = entries["Email"].get().strip()

    if not student_id:
        messagebox.showwarning("Warning", "Select a student first!")
        return

    if not email:
        messagebox.showwarning("Warning", "Enter a new email!")
        return

    try:
        con = connect_db()
        cursor = con.cursor()

        query = """
        UPDATE students
        SET name=%s, age=%s, course=%s, email=%s
        WHERE student_id=%s
        """

        values = (
            entries["Name"].get().strip(),
            int(entries["Age"].get()),
            entries["Course"].get().strip(),
            email,
            int(student_id)
        )

        cursor.execute(query, values)
        con.commit()

        if cursor.rowcount > 0:
            messagebox.showinfo("Success", "Student updated successfully!")
        else:
            messagebox.showinfo("Information", "No changes made.")

        cursor.close()
        con.close()

        clear_fields()
        display_students()

    except (ValueError, TypeError):
        messagebox.showerror("Invalid Input", "Check the student details.")

    except mysql.connector.Error as err:
        messagebox.showerror("Database Error", str(err))


# Delete Student
def delete_student():
    student_id = entries["Student ID"].get()

    if not student_id:
        messagebox.showwarning("Warning", "Select a student first!")
        return

    confirm = messagebox.askyesno(
        "Confirm Delete",
        "Are you sure you want to delete this student?"
    )

    if not confirm:
        return

    try:
        con = connect_db()
        cursor = con.cursor()

        cursor.execute(
            "DELETE FROM students WHERE student_id=%s",
            (int(student_id),)
        )

        con.commit()

        if cursor.rowcount > 0:
            messagebox.showinfo("Success", "Student deleted successfully!")
        else:
            messagebox.showinfo("Information", "Student not found.")

        cursor.close()
        con.close()

        clear_fields()
        display_students()

    except (ValueError, TypeError):
        messagebox.showerror("Invalid Input", "Invalid student ID.")

    except mysql.connector.Error as err:
        messagebox.showerror("Database Error", str(err))


# Button Frame
button_frame = tk.Frame(root, bg="#eef2f7")
button_frame.pack(pady=15)

buttons = [
    ("Add Student", add_student),
    ("Update Student", update_student),
    ("Delete Student", delete_student),
    ("Clear Fields", clear_fields),
    ("Refresh", display_students)
]

for text, command in buttons:
    tk.Button(
        button_frame,
        text=text,
        command=command,
        font=("Arial", 10, "bold"),
        bg="#1e3a5f",
        fg="white",
        padx=12,
        pady=8,
        cursor="hand2"
    ).pack(side="left", padx=6)


# Student Records Table
table_frame = tk.Frame(root)
table_frame.pack(fill="both", expand=True, padx=30, pady=10)

columns = ("ID", "Name", "Age", "Course", "Email")

table = ttk.Treeview(
    table_frame,
    columns=columns,
    show="headings"
)

for column in columns:
    table.heading(column, text=column)
    table.column(column, width=160, anchor="center")

table.pack(fill="both", expand=True)

table.bind("<<TreeviewSelect>>", select_student)


# Initial Data Loading
display_students()

# Run Application
root.mainloop()
