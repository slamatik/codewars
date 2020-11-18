from math import pi


class Shape:
    def __lt__(self, other):
        return self.area < other.area


class Square(Shape):
    def __init__(self, side):
        self.area = side ** 2


class Rectangle(Shape):
    def __init__(self, width, height):
        self.area = width * height


class Triangle(Shape):
    def __init__(self, base, height):
        self.area = base * height / 2


class Circle(Shape):
    def __init__(self, r):
        self.area = pi * r ** 2


class CustomShape(Shape):
    def __init__(self, area):
        self.area = area

expected = []
expected.append(Square(1.1234))
print(expected)

