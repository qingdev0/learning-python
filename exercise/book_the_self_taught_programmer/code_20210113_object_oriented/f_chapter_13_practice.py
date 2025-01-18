# chapter 13


# 1st practice
class Rectangle:
    def __init__(self, v_width, v_length):
        self.width = v_width
        self.length = v_length

    def calculate_perimeter(self):
        return (self.width + self.length) * 2


class Square:
    def __init__(self, v_length):
        self.length = v_length

    def calculate_perimeter(self):
        return self.length * 4


my_rectangle = Rectangle(4, 5)
my_rectangle.calculate_perimeter()

my_square = Square(4)
my_square.calculate_perimeter()


# 2nd practice
class Square:
    def __init__(self, v_length):
        self.length = v_length

    def calculate_perimeter(self):
        return self.length * 4

    def change_size(self, v_new_length):
        self.length = v_new_length


my_square = Square(4)
my_square.calculate_perimeter()

my_square.change_size(8)
my_square.calculate_perimeter()


# 3rd practice - inheritance
class Shape:
    def __init__(self):
        pass

    def what_am_i(self):
        print("[info] I am a shape.")


class Rectangle(Shape):
    def __init__(self):
        pass


my_rectangle = Rectangle()
my_rectangle.what_am_i()


# 4th practice - ownership
class Horse:
    def __init__(self, v_name, v_rider):
        self.name = v_name
        self.rider = v_rider


class Rider:
    def __init__(self, v_name, v_gender):
        self.name = v_name
        self.gender = v_gender


a_rider = Rider("Jack Li", "mail")
a_horse = Horse("King", a_rider)

a_horse.rider.name

#######
# EOF #
#######
