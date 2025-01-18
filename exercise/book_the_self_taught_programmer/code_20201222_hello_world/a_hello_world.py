#!/usr/bin/env python

# # Writing Python 3 in Python 2.6+
from __future__ import absolute_import, division, print_function, unicode_literals

# These switch to Python 3 meanings for key constructs.
# Now you use print() instead of print statement, unicode strings, imports will always be absolute,
#  and division will create floating-point values as needed (i.e., 1/2 now returns 0.5).


# Use the Interactive Window to develop Python Scripts
# - You can create cells on a Python file by typing "#%%"
# - Use "Shift + Enter " to run a cell, the output will be shown in the interactive window

for i in range(4):
    print("Hello World!")

# >> Hello World!
# >> Hello World!
# >> Hello World!
# >> Hello World!

#########################
# conditional statement #
#########################
# code 01
home = "America"

if home == "America":
    print("Hello, America!")
else:
    print("Hello, World!")

# >> Hello, America!


# code 02
x = 2

if x == 2:
    print("The number is 2.")
if x % 2 == 0:
    print("The number is even.")
if x % 2 != 0:
    print("The number is odd.")

# >> The number is 2.
# >> The number is even.

# code 03
x = 10
y = 11

if x == 10:
    if y == 11:
        print(x + y)

# code 04
home = "Thailand"
home = "Mars"

if home == "Japan":
    print("Hello, Japan!")
elif home == "Thailand":
    print("Hello, Thailand!")
elif home == "India":
    print("Hello, India!")
elif home == "China":
    print("Hello, China!")
else:
    print("Hello, World!")
