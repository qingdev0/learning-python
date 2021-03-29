

# example of instance variable:

class Rectangle():
    def __init__(self, v_width, v_length):
        self.width = v_width
        self.length = v_length
    def print_size(self):
        print("""{} by {}
              """.format(self.width, self.length))

my_rectangle = Rectangle(10, 34)
type(my_rectangle)                               # returns: <class '__main__.Rectangle'>
my_rectangle.print_size()


# new concept:- class variable

class Rectangle():
    recs = []
    def __init__(self, v_width, v_length):
        self.width = v_width
        self.length = v_length
        self.recs.append((self.width, self.length))
    def print_size(self):
        print("""{} by {}
              """.format(self.width, self.length))

r1 = Rectangle(10, 24)
r2 = Rectangle(20, 40)
r3 = Rectangle(14, 24)

print(Rectangle.recs)