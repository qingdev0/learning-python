
####################
# string functions #
####################

# length of a string
len("Monty")

# element number of a list
color_list = ["blue", "green", "yellow"]
len(color_list)

########################
# data type conversion #
########################

# convert something to string
str(100)
# exception: none


# convert something to integer
int("100")
int(3.6)
# exception: ValueError: invalid literal for int() with base 10: 'Zero'
int("Zero")

# convert something to float
float(100)
float("100")
# exception: 




################
# code snippet #
################
age = input("Enter your age: ")
int_age = int(age)
if int_age < 40:
    print("You are young!")
else:
    print("Woe, you are old!")



#######
# EOF #
#######