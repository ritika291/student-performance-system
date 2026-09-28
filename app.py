
from flask import Flask, render_template, request, redirect, url_for, flash
from storage import load_students, save_students
from marks import calculate_grade, calculate_percentage, get_result

app = Flask(__name__)
app.secret_key = "student-performance-local-app"


@app.route("/")
def home():
    students = load_students()
    query = request.args.get("q", "").strip().lower()

    if query:
        students = [
            s for s in students
            if query in s["name"].lower()
            or query in s["roll_no"].lower()
        ]

    all_students = load_students()
    total = len(all_students)
    average = (
        sum(s["marks"] for s in all_students) / total
        if total else 0
    )
    passed = sum(1 for s in all_students if get_result(s["marks"]) == "Pass")

    return render_template(
        "index.html",
        students=students,
        total=total,
        average=round(average, 2),
        passed=passed,
        failed=total - passed,
        query=query
    )


@app.route("/add", methods=["POST"])
def add_student():
    name = request.form.get("name", "").strip()
    roll_no = request.form.get("roll_no", "").strip()

    try:
        marks = float(request.form.get("marks", ""))
        if not 0 <= marks <= 100:
            raise ValueError
    except ValueError:
        flash("Marks must be a number between 0 and 100.", "error")
        return redirect(url_for("home"))

    if not name or not roll_no:
        flash("Name and roll number are required.", "error")
        return redirect(url_for("home"))

    students = load_students()

    if any(s["roll_no"].lower() == roll_no.lower() for s in students):
        flash("This roll number already exists.", "error")
        return redirect(url_for("home"))

    students.append({
        "name": name,
        "roll_no": roll_no,
        "marks": marks,
        "grade": calculate_grade(marks)
    })
    save_students(students)

    flash("Student added successfully!", "success")
    return redirect(url_for("home"))


@app.route("/update/<roll_no>", methods=["POST"])
def update_student(roll_no):
    students = load_students()

    for student in students:
        if student["roll_no"] == roll_no:
            name = request.form.get("name", "").strip()

            try:
                marks = float(request.form.get("marks", ""))
                if not name or not 0 <= marks <= 100:
                    raise ValueError
            except ValueError:
                flash("Enter a name and valid marks (0–100).", "error")
                return redirect(url_for("home"))

            student["name"] = name
            student["marks"] = marks
            student["grade"] = calculate_grade(marks)
            save_students(students)
            flash("Student updated successfully!", "success")
            break
    else:
        flash("Student not found.", "error")

    return redirect(url_for("home"))


@app.route("/delete/<roll_no>", methods=["POST"])
def delete_student(roll_no):
    students = load_students()
    updated = [s for s in students if s["roll_no"] != roll_no]

    if len(updated) == len(students):
        flash("Student not found.", "error")
    else:
        save_students(updated)
        flash("Student deleted successfully.", "success")

    return redirect(url_for("home"))


if __name__ == "__main__":
    app.run(debug=True)