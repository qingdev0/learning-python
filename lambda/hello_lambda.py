# lambda functions are useful as small, 'throwaway' single-line functions


# standard function
def myfunc(x, y, z):
    result = x + y + z
    return result


# lambda function
lambda x, y, z: x + y + z


# case 1
def second(x):
    return x[0]


a = [(1, 2), (2, 5), (3, 1), (4, 15)]

a.sort(key=second)
print(a)


a.sort(key=lambda x: x[1])
print(a)


# single argument
squared = lambda num: num**2
squared(5)


## multiple arguments
multi = lambda x, y, z: x * y * z
print(multi(10, 20, 30))

# argument having default value
power = lambda x, y=2: x**y
print(power(5, 3))
print(power(5))


## sort list of names
#####################
cmp = [
    "Michael Collins",
    "Richard Gordon",
    "Jack Swigert",
    "Stuart Roosa",
    "Alfred Worden",
    "Ken Mattingly",
    "Ron Evans",
]
print(cmp)
## sort by first name
cmp.sort()
print(cmp)
## sort by last name
cmp.sort(key=lambda x: x.split()[-1])
print(cmp)


## sort a list of tuples
people = [("Steve", 35), ("Karen", 28), ("Gerald", 58), ("Jo", 72)]
print(people)

people.sort()
print(people)

people.sort(key=lambda x: x[1])
print(people)


## sort a list of objects
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __repr__(self):
        return f"{self.name}: {self.age}"


alex = Person("Alex", 16)
mabel = Person("Mabel", 15)
eddie = Person("Eddie", 12)

p = [alex, mabel, eddie]
print(p)
p.sort(key=lambda x: x.name)
print(p)
p.sort(key=lambda x: x.age)
print(p)

############
## filter ##
############
nums = list(range(1, 21))
print("nums:", nums)
evens = list(filter(lambda x: x % 2 == 0, nums))
odds = list(filter(lambda x: x % 2 != 0, nums))
print("evens:", evens)
print("odds:", odds)


from statistics import mean

data = list(range(1, 21))
avg = mean(data)
above_avg = list(filter(lambda x: x > avg, data))

print("data:", data)
print("data avg:", avg)
print("data above avg:", above_avg)

#########
## map ##
#########
## map(function, iterable)
## * Return an iterator that applies function to every item of iterable, yielding the results.
## * Allows quick application of a function to every element of an iterable.
nums = [1, 2, 3, 4]
squared = list(map(lambda x: x**2, nums))
print(squared)


nums = list(range(1, 11))
print(nums)
even = list(map(lambda x: x % 2 == 0, nums))
print(even)


wc_teams = [
    ("Brazil", 21),
    ("Germany", 19),
    ("Italy", 18),
    ("Argentina", 17),
    ("France", 15),
    ("England", 15),
]
print(wc_teams)
new = list(map(lambda team: (team[0], team[1] + 1), wc_teams))
print(new)
