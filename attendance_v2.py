students= {"Dharani", "Dharashini", "Deepan", "Ruthran"}
present = []

while True:
    name = input("Enter name (type done to finish): ")
    name = name.strip().title()

    if name == "Done":
        break

    if name in students:
        present.append(name)
        print(name, "- marked Present")
    else:
        print(name, "- Not found")

print("--- Attendance Report ---")
for student in students:
    if student in present:
        print(student, ": Present")
    else:
        print(student, ": Absent")
