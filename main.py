
from student import (
    add_student,
    view_students,
    search_student,
    update_student,
    delete_student
)
from analysis import show_performance_report


def show_menu():
    print("\n====================================")
    print("   STUDENT PERFORMANCE SYSTEM")
    print("====================================")
    print("1. Add Student")
    print("2. View All Students")
    print("3. Search Student")
    print("4. Update Student")
    print("5. Delete Student")
    print("6. Performance Report")
    print("7. Exit")
    print("====================================")


def main():
    while True:
        show_menu()
        choice = input("Enter your choice (1-7): ").strip()

        if choice == "1":
            add_student()

        elif choice == "2":
            view_students()

        elif choice == "3":
            search_student()

        elif choice == "4":
            update_student()

        elif choice == "5":
            delete_student()

        elif choice == "6":
            show_performance_report()

        elif choice == "7":
            print("Thank you for using Student Performance System!")
            break

        else:
            print("Invalid choice! Please enter a number from 1 to 7.")


if __name__ == "__main__":
    main()