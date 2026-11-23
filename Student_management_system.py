students = []

# Add Student
def student_add():
    name = input("Enter the name: ")
    id = int(input("Enter the id: "))
    age = int(input("Enter the age: "))
    grade = input("Enter the grade: ")

    student = {
        "name": name,
        "id": id,
        "age": age,
        "grade": grade
    }

    students.append(student)
    print("Student added successfully!")


# View Students
def view_student():
    if len(students) == 0:
        print("No student found")
    else:
        for student in students:
            print(student)


# Update Student
def update_student():
    student_id = int(input("Enter the id: "))

    for student in students:
        if student["id"] == student_id:
            student["name"] = input("Enter the student's new name: ")
            student["age"] = int(input("Enter the new age: "))
            student["grade"] = input("Enter the new grade: ")

            print("Student updated successfully!")
            return

    print("Student not found")


# Remove Student
def remove_student():
    student_id = int(input("Enter the student id: "))

    for student in students:
        if student["id"] == student_id:
            students.remove(student)
            print("Student removed successfully!")
            return

    print("Student not found")


# Main Menu
while True:
    print("\n----- Student Management System -----")
    print("1. Add Student")
    print("2. View Student")
    print("3. Update Student")
    print("4. Remove Student")
    print("5. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        student_add()

    elif choice == 2:
        view_student()

    elif choice == 3:
        update_student()

    elif choice == 4:
        remove_student()

    elif choice == 5:
        print("Exit")
        break

    else:
        print("Invalid choice!")