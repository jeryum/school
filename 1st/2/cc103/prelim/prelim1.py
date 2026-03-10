name = input("Enter Student Name: ")
student_id = input("Enter Student ID: ")
age = input("Enter Age: ")
score1 = int(input("Enter Exam Score 1: "))
score2 = int(input("Enter Exam Score 2: "))
score3 = int(input("Enter Exam Score 3: "))


print("")
print("-----Student Information-----")
print("Name:", name)
print("Student ID:", student_id)
print("Age:", age)

print("")
total = score1 + score2 + score3
average = total / 3

if average >= 75:
    status = "passed"
else:
    status = "failed"
print("-----Exam Results-----")
print("Total Score:", total)
print("Average Score:", average)
print("Status:", status)