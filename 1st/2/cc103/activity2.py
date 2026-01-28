students = [
    (101, "Jerome", 18, "BSIT"),
    (102, "Isabel", 19, "BSCS"),
    (103, "Ella", 20, "BSECE"),
    (104, "John", 21, "BSIT"),
    (105, "Rose", 18, "BSHM")
]

while True:
    print("\n===== Student Records Manager =====")
    print("1. Display all students")
    print("2. Search student by ID")
    print("3. Add new student")
    print("4. Exit")

    choice = input("Enter your choice (1-4): ")

    if choice == "1":
        print("\nID   Name   Age   Course")
        for s in students:
            print(f"{s[0]}  {s[1]}   {s[2]}    {s[3]}")

    elif choice == "2":
        search_id = int(input("Enter Student ID to search: "))
        found = False

        for s in students:
            if s[0] == search_id:
                print("\nStudent Found:")
                print("ID:", s[0])
                print("Name:", s[1])
                print("Age:", s[2])
                print("Course:", s[3])
                found = True
                break

        if not found:
            print("Student not found.")

    elif choice == "3":
        new_id = int(input("Enter ID: "))
        new_name = input("Enter Name: ")
        new_age = int(input("Enter Age: "))
        new_course = input("Enter Course: ")

        students.append((new_id, new_name, new_age, new_course))
        print("New student added successfully.")

    elif choice == "4":
        print("Exiting program. Goodbye!")
        break

    else:
        print("Invalid choice. Please enter 1 to 4.")
