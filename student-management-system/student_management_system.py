# Student Management System

FILE_NAME = "students.txt"

students = []


def show_menu():
    print("\n===== Student Management System =====")
    print("1. Add Student")
    print("2. View Students")
    print("3. Search Student")
    print("4. Delete Student")
    print("5. Save Students to File")
    print("6. Load Students from File")
    print("7. Exit")


def add_student(students):
    name = input("Enter student name: ").strip().title()
    if not name:
        print("Student name cannot be empty.")
        return

    try:
        age = int(input("Enter student age: ").strip())
    except ValueError:
        print("Invalid age! Please enter a valid number.")
        return

    course = input("Enter student course: ").strip().title()
    if not course:
        print("Student course cannot be empty.")
        return

    student = {
        "name": name,
        "age": age,
        "course": course
    }

    students.append(student)
    print("Student added successfully!")


def view_students(students):
    if not students:
        print("No students found.")
        return

    print("\n--- Student Records ---")

    for index, student in enumerate(students, start=1):
        print(f"\nStudent {index}")
        print(f"Name   : {student['name']}")
        print(f"Age    : {student['age']}")
        print(f"Course : {student['course']}")


def search_student(students):
    search_name = input("Enter student name to search: ").strip().title()

    for student in students:
        if student["name"] == search_name:
            print("\nStudent Found")
            print(f"Name   : {student['name']}")
            print(f"Age    : {student['age']}")
            print(f"Course : {student['course']}")
            return

    print("Student not found.")


def delete_student(students):
    delete_name = input("Enter student name to delete: ").strip().title()

    for student in students:
        if student["name"] == delete_name:
            students.remove(student)
            print("Student deleted successfully!")
            return

    print("Student not found.")


def save_students(students):
    with open(FILE_NAME, "w") as file:
        for student in students:
            file.write(
                f"{student['name']},{student['age']},{student['course']}\n"
            )

    print("Students saved to file successfully!")


def load_students(students):
    try:
        students.clear()

        with open(FILE_NAME, "r") as file:
            for line in file:
                try:
                    name, age, course = line.strip().split(",")

                    student = {
                        "name": name,
                        "age": int(age),
                        "course": course
                    }

                    students.append(student)

                except ValueError:
                    print(f"Skipping invalid record: {line.strip()}")

        print("Students loaded from file successfully!")

    except FileNotFoundError:
        print("No saved student file found.")


while True:
    show_menu()

    choice = input("Enter your choice (1-7): ").strip()

    if choice == "1":
        add_student(students)

    elif choice == "2":
        view_students(students)

    elif choice == "3":
        search_student(students)

    elif choice == "4":
        delete_student(students)

    elif choice == "5":
        save_students(students)

    elif choice == "6":
        load_students(students)

    elif choice == "7":
        print("Thank you for using Student Management System.")
        print("Goodbye!")
        break

    else:
        print("Invalid choice! Please enter a number between 1 and 7.")