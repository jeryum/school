# Step 1 – Create a Class
class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        print("The animal makes a sound.")


# Step 2 – Create Objects
a1 = Animal("Buddy")
a2 = Animal("Milo")

a1.speak()
a2.speak()


# Step 3 – Create a Child Class (Inheritance)
class Dog(Animal):
    def speak(self):
        print(self.name, "says Bark Bark!")  # Step 8: changed sound


# Step 4 – Test Dog
d1 = Dog("Max")
d1.speak()


# Step 5 – Create Another Child Class
class Cat(Animal):
    def speak(self):
        print(self.name, "says Meow!")


# Step 6 – Test Cat
c1 = Cat("Luna")
c1.speak()


# Step 7 – Student Task (New Animal Class)
class Cow(Animal):
    def speak(self):
        print(self.name, "says Moo!")


x1 = Cow("Bella")
x1.speak()
