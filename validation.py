
def get_valid_marks(prompt="Enter marks (0-100): "):
    while True:
        try:
            marks = float(input(prompt))

            if 0 <= marks <= 100:
                return marks
            else:
                print("Marks must be between 0 and 100.")

        except ValueError:
            print("Invalid input! Please enter a number.")


def get_non_empty_text(prompt):
    while True:
        value = input(prompt).strip()

        if value:
            return value

        print("This field cannot be empty.")


def get_roll_number(prompt="Enter roll number: "):
    return get_non_empty_text(prompt)