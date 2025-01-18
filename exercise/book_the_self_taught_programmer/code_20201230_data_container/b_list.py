# list is one kind of container
# list is iterable
# list is mutable

# create a empty list
fruit_list = list()
fruit_list = []

# create a list and append new elements
fruit_list = ["Apple", "Orange", "Pear"]
fruit_list.append("Banana")
fruit_list.append("Peach")
fruit_list

# data type
mixed_list = []
mixed_list.append(True)
mixed_list.append(100)
mixed_list.append(3.1415926)
mixed_list.append("Something Else")
mixed_list


# list is iterable
fruit_list = ["Apple", "Orange", "Pear"]
fruit_list[0]
fruit_list[1]
fruit_list[2]
fruit_list[3]
# exception: IndexError: list index out of range

###################
# list is mutable #
###################
color_list = ["red", "yellow", "blue"]
color_list
color_list[2] = "green"
color_list
color_list.append("black")
color_list
color_list.pop()
color_list

color_list
item = color_list.pop()
item
color_list

# merge two lists
color_list_a = ["blue", "green", "yellow"]
color_list_b = ["orange", "pink", "black"]
color_list_a + color_list_b

# test using keyword 'in'
color_list = ["blue", "green", "yellow"]
"black" in color_list
"black" not in color_list


################
# code snippet #
################
colors = ["purple", "orange", "green"]
guess = input("[read] guess a color: ")
if guess in colors:
    print("[info] you guessed correctly!")
else:
    print("[oops] wrong! try again please.")
