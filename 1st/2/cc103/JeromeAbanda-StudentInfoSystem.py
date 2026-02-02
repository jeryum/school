def display_menu():
    print("\n=== Student Information Management System ===")
    print("1. Add student record")
    print("2. Display student records")
    print("3. Add subject")
    print("4. Display subjects")
    print("5. Exit")


def determine_pass_fail(grade):
    if grade >= 75:
        return "Passed"
    else:
        return "Failed"


def add_student_record(students):
    name = input("Enter student name: ").strip()

    if name == "":
        print("Name cannot be empty.")
        return

    if name in students:
        print("Student already exists.")
        return

    try:
        grade = float(input("Enter student grade: "))
        if grade < 0 or grade > 100:
            print("Grade must be between 0 and 100.")
            return
    except ValueError:
        print("Invalid grade input.")
        return

    students[name] = grade
    print("Student record added successfully.")


def display_student_records(students):
    if not students:
        print("No student records found.")
        return

    print("\n--- Student Records ---")
    for name, grade in students.items():
        status = determine_pass_fail(grade)
        print(f"Name: {name} | Grade: {grade} | Status: {status}")


def add_subject(subjects):
    subject = input("Enter subject name: ").strip()

    if subject == "":
        print("Subject name cannot be empty.")
        return

    subjects.add(subject)
    print("Subject added successfully.")


def display_subjects(subjects):
    if not subjects:
        print("No subjects added yet.")
        return

    print("\n--- Subject List ---")
    for subject in subjects:
        print(subject)


def main():
    students = {}
    subjects = set()

    while True:
        display_menu()
        choice = input("Choose an option (1-5): ").strip()

        if choice == "1":
            add_student_record(students)
        elif choice == "2":
            display_student_records(students)
        elif choice == "3":
            add_subject(subjects)
        elif choice == "4":
            display_subjects(subjects)
        elif choice == "5":
            print("Exiting program. Goodbye!")
            break
        else:
            print("Invalid choice. Please select from 1 to 5.")


main()
