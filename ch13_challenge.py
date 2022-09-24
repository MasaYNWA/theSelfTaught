class Shape(object):
    def __init__(self, s1):
        self.s1 = s1

    def what_am_i(self):
        print("i am a shape")

class Rectangle(Shape):
    def __init__(self, width, length):
        self.width = width
        self.length = length

    def calculate_perimeter(self):
        return self.width * 2 + self.length * 2

class Square(Shape):
    def __init__(self, s1):
        self.s1 = s1

    def calculate_perimeter(self):
        return self.s1 * 4
    
    def change_size(self, s1):
        self.s1 += s1

a_rectangle = Rectangle(10, 20)
print(a_rectangle.calculate_perimeter())

a_square = Square(10)
print(a_square.calculate_perimeter())
a_square.change_size(-5)
print(a_square.calculate_perimeter())

a_rectangle.what_am_i()
a_square.what_am_i()


class Horse(object):
    def __init__(self, name, weight, owner):
        self.name = name
        self.weight = weight
        self.owner = owner

class Rider(object):
    def __init__(self, name):
        self.name = name

a_rider = Rider("Jack")
a_horse = Horse("Mee", 200, a_rider)

print(a_horse.owner.name)

