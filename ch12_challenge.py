import math

class Apple(object):
    def __init__(self, colour, size, weight, kind):
        self.colour = colour
        self.size = size
        self.weight = weight
        self.kind = kind

class Circle(object):
    def __init__(self, radius):
        self.radius = float(radius)

    def area(self):
        return math.pi * self.radius ** 2

class Triangle(object):
    def __init__(self, bottom, height):
        self.bottom = float(bottom)
        self.height = float(height)

    def area(self):
        return self.bottom * self.height / 2

class Hexagon(object):
    def __init__(self, s1, s2, s3, s4, s5, s6):
        self.s1 = s1
        self.s2 = s2
        self.s3 = s3
        self.s4 = s4
        self.s5 = s5
        self.s6 = s6

    def calculate_perimeter(self):
        return self.s1 + self.s2 + self.s3 + self.s4 + self.s5 + self.s6

circle = Circle(5)
print(circle.area())

triangle = Triangle(4, 5)
print(triangle.area())

hexagon = Hexagon(1, 2, 3, 4, 5, 6)
print(hexagon.calculate_perimeter())
