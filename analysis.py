
from storage import load_students
from marks import get_result


def show_performance_report():
    students = load_students()

    if not students:
        print("No student records found.")
        return

    marks_list = [student["marks"] for student in students]

    total_marks = sum(marks_list)
    average = total_marks / len(marks_list)
    highest = max(marks_list)
    lowest = min(marks_list)

    pass_count = sum(
        1 for marks in marks_list if get_result(marks) == "Pass"
    )
    fail_count = len(students) - pass_count

    if average >= 75:
        performance = "Excellent"
    elif average >= 60:
        performance = "Good"
    elif average >= 50:
        performance = "Average"
    else:
        performance = "Needs Improvement"

    print("\n===== PERFORMANCE REPORT =====")
    print("Total Students:", len(students))
    print("Average Marks:", round(average, 2))
    print("Highest Marks:", highest)
    print("Lowest Marks:", lowest)
    print("Passed Students:", pass_count)
    print("Failed Students:", fail_count)
    print("Overall Performance:", performance)
    print("==============================")