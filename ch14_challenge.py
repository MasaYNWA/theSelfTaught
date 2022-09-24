class Square(object):
    square_list = []

    def __init__(self, s1):
        self.s1 = s1
        self.square_list.append(self)

    def __repr__(self):
        return "{} by {} by {} by {}".format(self.s1, self.s1, self.s1, self.s1)

a_square = Square(10)
a_square2 = Square(20)
a_square3 = Square(30)

print(a_square)
print(a_square2)
print(a_square3)

def true_or_false(a, b):
   return a is b

print(true_or_false("a", "a"))