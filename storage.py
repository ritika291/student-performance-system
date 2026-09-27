
import csv
import os

FILE_NAME = "students.txt"


def load_students():
    students = []

    if not os.path.exists(FILE_NAME):
        return students

    with open(FILE_NAME, "r", newline="", encoding="utf-8") as file:
        reader = csv.reader(file)

        for row in reader:
            if len(row) < 4:
                continue

            try:
                student = {
                    "name": row[0],
                    "roll_no": row[1],
                    "marks": float(row[2]),
                    "grade": row[3]
                }
                students.append(student)

            except ValueError:
                continue

    return students


def save_students(students):
    with open(FILE_NAME, "w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)

        for student in students:
            writer.writerow([
                student["name"],
                student["roll_no"],
                student["marks"],
                student["grade"]
            ])