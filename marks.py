
def calculate_grade(marks):
    if marks >= 90:
        return "A+"
    elif marks >= 80:
        return "A"
    elif marks >= 70:
        return "B"
    elif marks >= 60:
        return "C"
    elif marks >= 50:
        return "D"
    else:
        return "F"


def calculate_percentage(marks, maximum_marks=100):
    if maximum_marks <= 0:
        raise ValueError("Maximum marks must be greater than zero.")

    return (marks / maximum_marks) * 100


def get_result(marks, passing_marks=50):
    if marks >= passing_marks:
        return "Pass"
    else:
        return "Fail"