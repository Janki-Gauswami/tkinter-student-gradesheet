# School Report Card App (Tkinter GUI)
A Python-based graphical application built with Tkinter that allows faculty to enter and save student marks and allows students to securely view their report cards.

## Features
 Role-based login for faculty and students

 Faculty interface to input student data and store it persistently

 Student interface to retrieve marks and see results in a table format

 Data saved to file (student_report.txt) to prevent duplication

## Clean and intuitive GUI using Tkinter

## Faculty Login
Faculty must enter their name and date of birth.

The password is a combination of: Name.DateOfBirth

Example: For Name=Ravi, DOB=01-01-2000, password = Ravi.01-01-2000

After successful login, faculty can enter:

Student's full name

Marks for subjects: Maths, Science, English, Social, Hindi, Sanskrit, Drawing

The data is stored in student_report.txt using JSON.

## Student Login
Students must enter:

First Name

Middle Name

Last Name

Roll Number

Password in format: FirstName.LastName.RollNumber

Example: Amit.Shah.12

On correct credentials, student's full result appears below in the GUI:

Individual subject marks

Total Marks

Average Marks



## Notes
All student data is persisted in student_report.txt. Do not delete this file if you wish to retain data between sessions.

The app avoids duplicate entries by updating existing student data based on their full name.

Passwords are simple strings for demo purposes. For production use, consider proper authentication mechanisms.


## How to Run
Make sure you have Python installed (>=3.6 recommended).

Run the app:

````bash

python school_app_gui.py
echo "==============================="
echo "       File Structure"
echo "==============================="


school_app_gui/
│
├── student_report.txt         # Stores all student records in JSON format
├── school_app_gui.py          # Main application code
└── README.md                  # Project documentation


