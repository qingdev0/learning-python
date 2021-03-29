

# Python dictionary is a container of key-value pairs.

# create empty dictionary
my_dict = dict()
my_dict

my_dict = {}
my_dict

fruit_dict = {"Apple":"Red", "Banana":"Yellow"}
fruit_dict


# dictionary is mutable - add
###############################
facts = dict()
facts

facts["code"]
# exception: KeyError: 'code'

facts["code"] = "fun"
facts
facts["code"]

facts["Bill"] = "Gates"
facts
facts["Bill"]

facts["founded"] = 1776
facts
facts["founded"]

"Bill" in facts
"Gates" in facts

# dictionary is mutable - delete
##################################
books = {"Dracula": "Stoker", "1984": "Orwell", "The Trial": "Kafka"}
books

del books["The Trial"]
books

del books["The Trial"]
# exception: KeyError: 'The Trial


################
# code snippet #
################
# 1
rhymes = { "1": "fun"
         , "2": "blue"
         , "3": "me"
         , "4": "floor"
         , "5": "live"
         }

n = input("[read] type a number [1-5]: ")
if n in rhymes:
    rhyme = rhymes[n]
    print(rhyme)
else:
    print("[oops] data not found..")

# 2
rhymes = { 1: "fun"
         , 2: "blue"
         , 3: "me"
         , 4: "floor"
         , 5: "live"
         }

n = int(input("[read] type a number [1-5]: "))
if n in rhymes:
    rhyme = rhymes[n]
    print(rhyme)
else:
    print("[oops] data not found..")



#######
# EOF #
#######