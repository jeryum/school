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


scores = [score1, score2, score3]

print("")
print("-----Score Evaluation-----")

exam = 1
for s in scores:
    if s >= 75:
        result = "PASSED"
    else:
        result = "FAILED"
    print("Exam", exam, ":", s, result)
    exam += 1


highest = scores[0]
lowest = scores[0]

for s in scores:
    if s > highest:
        highest = s
    if s < lowest:
        lowest = s


menu = ("View Student Information", "View Scores and Average", "Exit")

while True:
    print("")
    print("-----MENU-----")
    print("1.", menu[0])
    print("2.", menu[1])
    print("3.", menu[2])

    choice = input("Select option: ")

    if choice == "1":
        print("")
        print("-----Student Information-----")
        print("Name:", name)
        print("Student ID:", student_id)
        print("Age:", age)
        print("Status:", status)

    elif choice == "2":
        print("")
        print("-----Scores-----")
        print("Scores:", scores)
        print("Highest Score:", highest)
        print("Lowest Score:", lowest)
        print("Average Score:", average)

    elif choice == "3":
        print("")
        print("Program Ended. Thank you!")
        break

    else:
        print("Invalid option")