
from storage import load_students, save_students
from validation import get_valid_marks, get_non_empty_text
from marks import calculate_grade


def add_student():
    students = load_students()

    roll_no = get_non_empty_text("Enter roll number: ")

    for student in students:
        if student["roll_no"] == roll_no:
            print("This roll number already exists!")
            return

    name = get_non_empty_text("Enter student name: ")
    marks = get_valid_marks()

    student = {
        "name": name,
        "roll_no": roll_no,
        "marks": marks,
        "grade": calculate_grade(marks)
    }

    students.append(student)
    save_students(students)
    print("Student added successfully!")


def view_students():
    students = load_students()

    if not students:
        print("No student records found.")
        return

    print("\n----- Student Records -----")

    for student in students:
        print("Name:", student["name"])
        print("Roll Number:", student["roll_no"])
        print("Marks:", student["marks"])
        print("Grade:", student["grade"])
        print("---------------------------")


def search_student():
    students = load_students()
    roll_no = get_non_empty_text("Enter roll number to search: ")

    for student in students:
        if student["roll_no"] == roll_no:
            print("\nStudent found!")
            print("Name:", student["name"])
            print("Roll Number:", student["roll_no"])
            print("Marks:", student["marks"])
            print("Grade:", student["grade"])
            return

    print("Student not found.")


def update_student():
    students = load_students()
    roll_no = get_non_empty_text("Enter roll number to update: ")

    for student in students:
        if student["roll_no"] == roll_no:
            print("Current name:", student["name"])
            new_name = get_non_empty_text("Enter new name: ")
            new_marks = get_valid_marks()

            student["name"] = new_name
            student["marks"] = new_marks
            student["grade"] = calculate_grade(new_marks)

            save_students(students)
            print("Student updated successfully!")
            return

    print("Student not found.")


def delete_student():
    students = load_students()
    roll_no = get_non_empty_text("Enter roll number to delete: ")

    for student in students:
        if student["roll_no"] == roll_no:
            students.remove(student)
            save_students(students)
            print("Student deleted successfully!")
            return

    print("Student not found.")