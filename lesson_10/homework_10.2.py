from abc import ABC, abstractmethod
import math

class Figure(ABC):

    @abstractmethod
    def get_area(self):
        pass

    @abstractmethod
    def get_perimeter(self):
        pass

class Circle(Figure):
    def __init__(self, radius):
        self.__radius = radius

    def get_area(self):
        return math.pi * self.__radius ** 2
    def get_perimeter(self):
        return 2 * math.pi * self.__radius

class Rectangle(Figure):
    def __init__(self, length, width):
        self.__length = length
        self.__width = width

    def get_area(self):
        return self.__length * self.__width

    def get_perimeter(self):
        return 2 * (self.__length + self.__width)

class Square(Figure):
    def __init__(self, side):
        self.__side = side

    def get_area(self):
        return self.__side ** 2

    def get_perimeter(self):
        return 4 * self.__side

circle = Circle(5)
rectangle = Rectangle(4, 6)
square = Square(3)

figures = [circle, rectangle, square]

for figure in figures:
    print("Фігура:", figure.__class__.__name__)
    print("Площа:", figure.get_area())
    print("Периметр:", figure.get_perimeter())
    print("_"*30)
