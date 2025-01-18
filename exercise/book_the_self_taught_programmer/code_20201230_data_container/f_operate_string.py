# string is iterable
######################
author = "Kafka"
author[0]
author[1]
author[2]
author[3]
author[4]

author[5]  # exception: IndexError: string index out of range

author[-1]
author[-2]
author[-3]
author[-4]
author[-5]

# string is immutable
#######################
ff = "F.Fitzgerald"
ff
ff = "F. Scott Fitzgerald"
ff

######################
# concatenate & join #
######################
"cat" + "in" + "hat"

"cat" + " in " + "hat"

# repeat
"Swayer" * 3

# join method
first_three = "abc"
result = "+".join(first_three)
print(result)  # return: a+b+c

words = ["The", "fox", "jumped", "over", "the", "fence", "."]
one_sentence = "".join(words)
print(one_sentence)

words = ["The", "fox", "jumped", "over", "the", "fence", "."]
one_sentence = " ".join(words)
print(one_sentence)


#######################################
# case - sensitivity & capitalization #
#######################################
"we hold these truths...".upper()

"we hold these truths...".lower()

"we hold these truths...".capitalize()

##########
# format #
##########
"William {}".format("Faulkner")

last_name = "Faulkner"
"William {}".format(last_name)

author = "William Faulkner"
year_born = "1897"
"{} was born in {}.".format(author, year_born)

# format - code snippet
#########################
n_1 = input("[read] enter a noun      : ")
v = input("[read] enter a verb      : ")
adj = input("[read] enter an adjective: ")
n_2 = input("[read] enter another noun: ")

r = """The {} {} the {} {}
    """.format(n_1, v, adj, n_2)

print(r)

#########
# split #
#########
"I jumped over the puddle. It was 12 feet!".split(
    "."
)  # return: ['I jumped over the puddle', ' It was 12 feet!']

"Where now? Who now? When now?".split(
    "? "
)  # return: ['Where now', 'Who now', 'When now?']

str_org = "It was bright cold day in April, and the clocks were striking thirteen."
str_new = str_org.split(",")
str_new = str_new[0]
print(str_new)  # return: It was bright cold day in April

##########
# stripe #
##########
s = "   The     "
s = s.strip()
print(s)
# return "The"

###########
# replace #
###########
equ = "All animals are equal."
equ = equ.replace("a", "@")
print(equ)  # return: All @nim@ls @re equ@l.

#################################
# search letter by index method #
#################################

"animal".index("m")  # return: 3

"animal".index("z")  # exception: ValueError: substring not found

try:
    "animal".index("z")
except:
    print("[oops] data not found.")  # return: [oops] data not found.


##############
# in keyword #
##############
"Cat" in "Cat in the hat"
"Cat" in "cat in the hat"

"Potter" not in "Harry"

##########
# escape #
##########

# print("She said "Surely".")                    # exception: SyntaxError: invalid syntax

# backslash
print('She said "Surely".')  # return: She said "Surely".

# works without backslash
print('She said "Surely".')  # return: She said "Surely".
print("She said 'Surely'.")  # return: She said 'Surely'.

##############
# line break #
##############
print("line 1\nline 2\nline 3\nline 4")


###########
# slicing #
###########
fict = ["Tolstoy", "Camus", "Orwell", "Huxley", "Austin"]
fict[0:3]  # return: ['Tolstoy', 'Camus', 'Orwell']


ivan = """In place of death there was light."""

ivan[0:17]  # 'In place of death'
ivan[:17]  # 'In place of death'

ivan[18:33]  # 'there was light'
ivan[18:]  # 'there was light'

ivan[:]  # 'In place of death there was light.'


#######
# EOF #
#######
