import grade_module

grading_labels = ("Excellent", "Passed", "Failed")

name = input("Enter student name: ")
section = input("Enter section: ")
num_subjects = int(input("Enter number of subjects: "))

grades = []

for i in range(num_subjects):
    grade = float(input(f"Enter grade for subject {i + 1}: "))
    grades.append(grade)

subjects = set()

for i in range(num_subjects):
    subject = input(f"Enter subject name {i + 1}: ")
    subjects.add(subject)

average = grade_module.compute_average(grades)
status = grade_module.determine_status(average)

student_record = {
    "Name": name,
    "Section": section,
    "Grades": grades,
    "Average": average,
    "Status": status
}

print("\nSTUDENT GRADE SUMMARY\n")

for key, value in student_record.items():
    print(f"{key}: {value}")

print(f"\nSubjects: {subjects}")
print(f"Grading Labels: {grading_labels}")
