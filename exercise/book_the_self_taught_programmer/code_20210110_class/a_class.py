##############
# practice 1 #
##############

class Orange:
    def __init__(self, weight, color):
        self.weight = weight
        self.color = color
        print("[info] a class instance is created.")

orange_1 = Orange(10, "dark orange")

print(orange_1)

print(orange_1.weight)
print(orange_1.color)


orange_1.weight = 100
orange_1.color = "light orange"

print(orange_1.weight)
print(orange_1.color)

orange_1 = Orange( 4, "light orange")
orange_2 = Orange( 8, "dark orange")
orange_3 = Orange(12, "yellow")




# revision 2
##############
class Orange:
    def __init__(self, weight, color):
        # weight is in ounce
        self.weight = weight
        self.color = color
        # define + default
        self.mold = 0
        print("[info] a class instance is created.")
    def rot(self, days, temperature):
    # create a method to change instance variable in magic method
        self.mold = days * temperature

orange_1 = Orange(6, "orange")
print(orange_1.mold)

orange_1.rot(10, 98)
print(orange_1.mold)

##############
# practice 2 #
##############
class Rectangle():
    def __init__(self, a_width, b_length):
        self.width = a_width
        self.length = b_length
    def area(self):
    # create a method for a match calculation
        return self.width * self.length
    def resize(self, a_width, b_length):
    # create a method for reloading init variables
        self.width = a_width
        self.length = b_length

rectangle_1 = Rectangle(10, 20)
print(rectangle_1.area())

rectangle_1.resize(20, 40)
print(rectangle_1.area())



##############
# practice 3 #
##############
from math import pi
class Circle():
    def __init__(self, a_radius):
        self.radius = float(a_radius)
    def area(self):
        return pi * self.radius**2

circle_1 = Circle(10)
print(circle_1.area())

#######
# EOF #
#######
