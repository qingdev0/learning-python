# remember that tuple is immutable


# create empty tuple
my_tuple = tuple()
my_tuple

my_tuple = ()
my_tuple

my_tuple = ("M. Jackson", 1958, True)
my_tuple

# tuple with single element
my_tuple = ("self_taught",)
my_tuple
# not tuple
my_tuple = ("self_taught")
my_tuple

# tuple is immutable
my_tuple = ("1984", "Brave New World", "Fahrenheit 451")
my_tuple
my_tuple[1]
my_tuple[1] = "Handmaid's Tale"
# exception: TypeError: 'tuple' object does not support item assignment


"New" in my_tuple
"1984" not in my_tuple

