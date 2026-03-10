class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age


class Student(Person):
    def __init__(self, name, age, grade, fees):
        self.name = name
        self.age = age
        self.grade = grade
        self.__fees = fees


class Teacher(Person):
    def __init__(self, name, age, subject, salary):
        self.name = name
        self.age = age
        self.subject = subject
        self.__salary = salary


class Staff(Person):
    def __init__(self, name, age, department):
        self.name = name
        self.age = age
        self.department = department


class Principal(Staff):
    def __init__(self, name, age, department, bonus):
        self.name = name
        self.age = age
        self.department = department
        self.__bonus = bonus


class Sports:
    def __init__(self, sport_name):
        self.sport_name = sport_name


class Academics:
    def __init__(self, subject_name):
        self.subject_name = subject_name


class SchoolActivity(Sports, Academics):
    def __init__(self, sport_name, subject_name, activity_name):
        self.sport_name = sport_name
        self.subject_name = subject_name
        self.activity_name = activity_name


student1 = Student("Carlos", 16, "11th Grade", 6500)
teacher1 = Teacher("Ms. Reyes", 38, "Physics", 28000)
principal1 = Principal("Mr. Gomez", 55, "Administration", 15000)
activity1 = SchoolActivity("Basketball", "History", "History Quiz Bee")


print("---- Student Details ----")
print("Name:", student1.name)
print("Age:", student1.age)
print("Grade:", student1.grade)
print("Fees (Private):", student1._Student__fees)

print("\n---- Teacher Details ----")
print("Name:", teacher1.name)
print("Age:", teacher1.age)
print("Subject:", teacher1.subject)
print("Salary (Private):", teacher1._Teacher__salary)

print("\n---- Principal Details ----")
print("Name:", principal1.name)
print("Age:", principal1.age)
print("Department:", principal1.department)
print("Bonus (Private):", principal1._Principal__bonus)

print("\n---- School Activity Details ----")
print("Sport Name:", activity1.sport_name)
print("Subject Name:", activity1.subject_name)
print("Activity Name:", activity1.activity_name)
