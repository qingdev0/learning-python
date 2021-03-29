# inheritance of method or variable: parent class => child class

class Shape():
    def __init__(self, v_width, v_length):
        self.width = v_width
        self.length = v_length
    def print_size(self):
        print("""{} by {}
              """.format(self.width, self.length))

my_shape = Shape(20, 25)
my_shape.print_size()

###############
# child class #
###############
# pass (parent) class name as argument to (child) class
# 1st form: inherit only
class Square(Shape):
    # placeholder, no operation(NOP)
    pass

a_square = Square(20, 20)
a_square.print_size()

# 2nd form: inherit, and create new
class Square(Shape):
    def area(self):
        return self.width * self.length

a_square = Square(20, 20)
print(a_square.print_size())
print(a_square.area())

# 3rd form: inherit, and override old - aka. method overriding
class Shape():
    def __init__(self, v_width, v_length):
        self.width = v_width
        self.length = v_length
    def print_size(self):
        print("""{} by {}
              """.format(self.width, self.length))

class Square(Shape):
    def area(self):
        return self.width * self.length
    def print_size(self):
        print("""I am {} by {}""".format(self.width, self.length))

a_square = Square(15, 25)
a_square.area()
a_square.print_size()



#######
# EOF #
#######