# for loop - iterating

# iterating over a string
name = "Ted"
for character in name:
    print(character)

# iterating over a list
shows = ["GOT", "Narcos", "Vice"]
for object in shows:
    print(object)

# iterating over a tuple
coms = ("A. Development", "Friends", "Always Sunny")
for object in coms:
    print(object)

# iterating over a dictionary
people = { "G. Bluth II": "A. Development"
         , "Barney"     : "HIMYM"
         , "Dennis"     : "Always Sunny"
         }

for object in people:
    print(object)


####################
# uppercase a list #
####################
# revision 1
tv = ["GOT", "Narcos", "Vice"]
i = 0
for object in tv:
    tv[i] = object.upper()
    i += 1
print(tv)                                        # return: ['GOT', 'NARCOS', 'VICE']

# revision 2
tv = ["GOT", "Narcos", "Vice"]
print(enumerate(tv))                             # return: <enumerate object at 0x0000021DC4C96798>
for i, object in enumerate(tv):
    new = tv[i]
    new = new.upper()
    tv[i] = new
print(tv)

# revision 3
tv = ["GOT", "Narcos", "Vice"]
for i, object in enumerate(tv):                  # learn: enumerate() in for-loop <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
    tv[i] = object.upper()
print(tv)


# advanced
################################
# uppercase and merge two lists #
#################################
tv = ["GOT", "Narcos", "Vice"]
coms = ["Arrested Development", "friends", "Always Sunny"]
all_shows = []

for show in tv:
    show = show.upper()
    all_shows.append(show)

for show in coms:
    show = show.upper()
    all_shows.append(show)

print(all_shows)





#########
# range #
#########

for i in range(1,5):
    n = i ** i
    print(n)




#######
# EOF #
#######