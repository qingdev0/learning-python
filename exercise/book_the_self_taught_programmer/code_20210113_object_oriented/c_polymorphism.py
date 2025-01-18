print("Hello World!")
print(200)
print(3.14)

type("hello World!")
type(200)
type(3.14)


##############
# pseudocode #
##############
# non-polymorphism designing
shapes = [trl, sql, crl]
for a_shape in shapes:
    if type(a_shape) == "Triangle":
        a_shape.draw_triangle()
    if type(a_shape) == "Square":
        a_shape.draw_square()
    if type(a_shape) == "Circle":
        a_shape.draw_circle()

# polymorphic application
shapes = [trl, sql, crl]
for a_shape in shapes:
    a_shape.draw()

#######
# EOF #
#######
