import csv
import os
from datetime import datetime

attendance = {"Dharani": "Absent", "Dharshini": "Absent", "Deepan": "Absent", "Ruthran": "Absent"}

def mark_attendance(name):
    name = name.strip().title()
    if name in attendance:
        if attendance[name] != "Absent":
            print(name, "- already marked")
        else:
            time_now = datetime.now().strftime("%I:%M %p")
            attendance[name] = "Present at " + time_now
            print(name, "- marked Present at", time_now)
    else:
        print(name, "- Not found")

def show_report():
    print("--- Attendance Report ---")
    for student in attendance:
        print(student, ":", attendance[student])

def save_to_csv():
    today = datetime.now().strftime("%d-%m-%Y")
    file_exists = os.path.exists("attendance.csv")
    with open("attendance.csv", "a", newline="") as file:
        writer = csv.writer(file)
        if not file_exists:
            writer.writerow(["Name", "Status", "Date"])
        for student in attendance:
            writer.writerow([student, attendance[student], today])
    print("Saved to attendance.csv")

while True:
    name = input("Enter name (type done to finish): ")
    if name.strip().title() == "Done":
        break
    mark_attendance(name)

show_report()
save_to_csv()
