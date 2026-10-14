import json
import os

FILE_NAME = "students.json"
SUBJECTS = ["Python", "DBMS", "Machine Learning", "Maths", "DSA"]


def load_students():
    if os.path.exists(FILE_NAME):
        try:
            with open(FILE_NAME, "r") as file:
                return json.load(file)
        except (json.JSONDecodeError, OSError):
            print("Warning: Records could not be loaded.")
    return []


def save_students(students):
    with open(FILE_NAME, "w") as file:
        json.dump(students, file, indent=4)


def calculate_grade(percentage):
    if percentage >= 90:
        return "A+"
    elif percentage >= 80:
        return "A"
    elif percentage >= 70:
        return "B"
    elif percentage >= 60:
        return "C"
    elif percentage >= 40:
        return "D"
    else:
        return "F"


def add_student(students):
    name = input("Enter student name: ").strip()
    roll = input("Enter roll number: ").strip()

    if not name or not roll:
        print("Name and roll number cannot be empty.")
        return

    if any(s["roll"] == roll for s in students):
        print("This roll number already exists.")
        return

    marks = {}

    for subject in SUBJECTS:
        while True:
            try:
                score = float(input(f"Enter marks in {subject} (0-100): "))
                if 0 <= score <= 100:
                    marks[subject] = score
                    break
                print("Marks must be between 0 and 100.")
            except ValueError:
                print("Please enter a valid number.")

    total = sum(marks.values())
    percentage = total / len(SUBJECTS)
    passed = all(mark >= 33 for mark in marks.values())
    grade = calculate_grade(percentage) if passed else "F"

    student = {
        "name": name,
        "roll": roll,
        "marks": marks,
        "total": total,
        "percentage": round(percentage, 2),
        "grade": grade,
        "status": "Pass" if passed else "Fail"
    }

    students.append(student)
    save_students(students)
    print("\nStudent record saved successfully!")


def view_students(students):
    if not students:
        print("No student records found.")
        return

    for student in students:
        print("\n------------------------------")
        print("Name:", student["name"])
        print("Roll Number:", student["roll"])
        print("Marks:", student["marks"])
        print("Total:", student["total"], "/", len(SUBJECTS) * 100)
        print("Percentage:", student["percentage"], "%")
        print("Grade:", student["grade"])
        print("Status:", student["status"])


def search_student(students):
    roll = input("Enter roll number to search: ").strip()

    for student in students:
        if student["roll"] == roll:
            view_students([student])
            return

    print("Student not found.")


def show_topper(students):
    if not students:
        print("No student records available.")
        return

    topper = max(students, key=lambda s: s["percentage"])
    print("Topper:", topper["name"])
    print("Percentage:", topper["percentage"], "%")


def main():
    students = load_students()

    while True:
        print("\n===== STUDENT PERFORMANCE ANALYZER =====")
        print("1. Add student")
        print("2. View all students")
        print("3. Search student")
        print("4. Show topper")
        print("5. Exit")

        choice = input("Choose an option (1-5): ").strip()

        if choice == "1":
            add_student(students)
        elif choice == "2":
            view_students(students)
        elif choice == "3":
            search_student(students)
        elif choice == "4":
            show_topper(students)
        elif choice == "5":
            print("Thank you for using the analyzer!")
            break
        else:
            print("Invalid choice. Please select 1-5.")


if __name__ == "__main__":
    main()
    

    

