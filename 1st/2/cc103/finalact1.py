from abc import ABC, abstractmethod
import math

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius ** 2


class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width


class Triangle(Shape):
    def __init__(self, base, height):
        self.base = base
        self.height = height

    def area(self):
        return 0.5 * self.base * self.height


def main():
    while True:
        print("\n=== Shape Area Calculator ===")
        print("1 - Circle")
        print("2 - Rectangle")
        print("3 - Triangle")
        print("4 - Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            radius = float(input("Enter radius: "))
            shape = Circle(radius)
            print("Area of Circle:", shape.area())

        elif choice == "2":
            length = float(input("Enter length: "))
            width = float(input("Enter width: "))
            shape = Rectangle(length, width)
            print("Area of Rectangle:", shape.area())

        elif choice == "3":
            base = float(input("Enter base: "))
            height = float(input("Enter height: "))
            shape = Triangle(base, height)
            print("Area of Triangle:", shape.area())

        elif choice == "4":
            print("Exiting program...")
            break

        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
