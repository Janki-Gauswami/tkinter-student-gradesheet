import tkinter as tk
from tkinter import messagebox
import json
import os

DATA_FILE = "student_report.txt"
allstudentsgradesheet = {}

# Load existing data
if os.path.exists(DATA_FILE):
    with open(DATA_FILE, "r") as file:
        try:
            allstudentsgradesheet = json.load(file)
        except json.JSONDecodeError:
            allstudentsgradesheet = {}

def save_data():
    with open(DATA_FILE, "w") as file:
        json.dump(allstudentsgradesheet, file)

def faculty_window():
    clear_window()

    tk.Label(root, text="Faculty Portal", font=("Arial", 16, "bold")).pack(pady=10)

    def submit():
        name = fac_name_entry.get()
        dob = fac_dob_entry.get()
        pin = fac_pin_entry.get()

        if pin != f"{name}.{dob}":
            messagebox.showerror("Error", "Invalid Password")
            return

        student_name = student_name_entry.get()
        marks = []
        try:
            for entry in subject_entries:
                marks.append(int(entry.get()))
        except ValueError:
            messagebox.showerror("Error", "Please enter valid integer marks")
            return

        total = sum(marks)
        average = total / len(marks)

        student_data = {
            "Name": student_name,
            "Marks": marks,
            "Total Marks": total,
            "Average": average
        }
        allstudentsgradesheet[student_name] = student_data
        save_data()
        messagebox.showinfo("Success", f"Data saved for {student_name}")

    tk.Label(root, text="Enter Name:").pack()
    fac_name_entry = tk.Entry(root)
    fac_name_entry.pack()

    tk.Label(root, text="Enter Date of Birth (dd-mm-yyyy):").pack()
    fac_dob_entry = tk.Entry(root)
    fac_dob_entry.pack()

    tk.Label(root, text="Enter Password:").pack()
    fac_pin_entry = tk.Entry(root, show="*")
    fac_pin_entry.pack()

    tk.Label(root, text="Enter Student Full Name:").pack()
    student_name_entry = tk.Entry(root)
    student_name_entry.pack()

    subjects = ["Maths", "Science", "English", "Social", "Hindi", "Sanskrit", "Drawing"]
    subject_entries = []
    for subject in subjects:
        tk.Label(root, text=f"Enter marks for {subject}:").pack()
        e = tk.Entry(root)
        e.pack()
        subject_entries.append(e)

    tk.Button(root, text="Submit", command=submit).pack(pady=10)

def student_window():
    clear_window()

    tk.Label(root, text="Student Portal", font=("Arial", 16, "bold")).pack(pady=10)

    def view_result():
        name = student_name_entry.get()
        lname = student_lname_entry.get()
        roll = student_roll_entry.get()
        pin = student_pin_entry.get()

        if pin != f"{name}.{lname}.{roll}":
            messagebox.showerror("Error", "Invalid Password")
            return

        full_name = f"{name} {student_mname_entry.get()} {lname}"
        student = allstudentsgradesheet.get(full_name)

        result_area.delete("1.0", tk.END)

        if not student:
            result_area.insert(tk.END, "STUDENT DETAIL NOT FOUND.\n")
            return

        result_area.insert(tk.END, f"Name: {student['Name']}\n")
        result_area.insert(tk.END, "Subject Marks:\n")
        for subject, mark in zip(["Maths", "Science", "English", "Social", "Hindi", "Sanskrit", "Drawing"], student["Marks"]):
            result_area.insert(tk.END, f"{subject}: {mark}\n")
        result_area.insert(tk.END, f"Total Marks: {student['Total Marks']}\n")
        result_area.insert(tk.END, f"Average: {student['Average']:.2f}\n")

    tk.Label(root, text="Enter First Name:").pack()
    student_name_entry = tk.Entry(root)
    student_name_entry.pack()

    tk.Label(root, text="Enter Middle Name:").pack()
    student_mname_entry = tk.Entry(root)
    student_mname_entry.pack()

    tk.Label(root, text="Enter Last Name:").pack()
    student_lname_entry = tk.Entry(root)
    student_lname_entry.pack()

    tk.Label(root, text="Enter Roll Number:").pack()
    student_roll_entry = tk.Entry(root)
    student_roll_entry.pack()

    tk.Label(root, text="Enter Password:").pack()
    student_pin_entry = tk.Entry(root, show="*")
    student_pin_entry.pack()

    tk.Button(root, text="View Result", command=view_result).pack(pady=10)

    result_area = tk.Text(root, height=15, width=60)
    result_area.pack(pady=10)

def clear_window():
    for widget in root.winfo_children():
        widget.destroy()

def main_menu():
    clear_window()
    tk.Label(root, text="SCHOOL APP", font=("Arial", 20, "bold")).pack(pady=20)
    tk.Label(root, text="Who are you?", font=("Arial", 14)).pack(pady=10)
    tk.Button(root, text="Faculty", width=20, command=faculty_window).pack(pady=5)
    tk.Button(root, text="Student", width=20, command=student_window).pack(pady=5)

# Main app window
root = tk.Tk()
root.title("School Report Card App")
root.geometry("600x700")
main_menu()
root.mainloop()
