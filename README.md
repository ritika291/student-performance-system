
# Student Performance Management System

## 1. Project Overview
The Student Performance Management System is a Python-based
application used to manage student records and analyse their
academic performance.

It allows users to add, view, search, update and delete student
records. It also calculates grades and generates a performance
report.

## 2. Objectives
- To manage student information digitally.
- To calculate grades based on marks.
- To analyse student performance.
- To reduce manual record-keeping.
- To validate user input.

## 3. Features
1. Add Student
2. View All Students
3. Search Student by Roll Number
4. Update Student Details
5. Delete Student
6. Generate Performance Report
7. Validate marks between 0 and 100
8. Store records in a text file

## 4. Technologies Used
- Python 3
- Visual Studio Code
- CSV module
- File handling
- Functions and modules

## 5. Requirements
- Python 3 installed
- Visual Studio Code or any Python editor

## 6. Project Files
- main.py: Main menu and program execution
- student.py: Student record operations
- marks.py: Grade and result calculations
- validation.py: Input validation
- storage.py: Saving and loading records
- analysis.py: Performance report generation

## 7. How to Run
1. Open the project folder in VS Code.
2. Open the terminal.
3. Run the following command:

   python main.py

4. Select an option from the displayed menu.

## 8. Data Storage
Student records are stored in students.txt.
Each record contains the student name, roll number,
marks and grade.

## 9. Testing
The application was tested for adding, viewing, searching,
updating and deleting student records, as well as generating
performance reports and handling invalid menu choices.
### Automated Testing

The project includes automated unit tests using Python's built-in `unittest` framework.

The tests check:

* Grade calculation for different marks.
* Percentage calculation.
* Pass and fail result determination.

**How to Run Tests**

Open the terminal in the project folder and execute:

```bash
python -m unittest discover -s tests -v
```

**Test Results:** All 6 automated tests passed successfully.

The tests help verify the correctness of the grading, percentage, and result calculation functions.


## 10. Future Enhancements
- Add a graphical user interface.
- Export reports to CSV or PDF.
- Add subject-wise marks.
- Add login and authentication.