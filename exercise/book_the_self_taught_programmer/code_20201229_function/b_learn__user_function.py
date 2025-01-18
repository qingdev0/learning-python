############
# function #
############


def func_01(x):
    """
    document: one argument sample function
    """
    return x + 1


# calling function
result_01 = func_01(4)
if result_01 == 5:
    print("result is 5.")
else:
    print("result is not 5.")


def func_02():
    """
    document: none-argument sample function
    """
    return 1 + 1


# calling function
result_02 = func_02()
print(result_02)


def func_03(x, y, z):
    """
    document: 3-argument sample function
    """
    return x + y + z


# calling function
result_03 = func_03(1, 2, 3)
print(result_03)


def func_04():
    """
    document: without "return" statement, return "None"
    """
    z = 1 + 1


# calling function
result_04 = func_04()
print(result_04)


def even_odd(x):
    """document
    code reuse
    """
    if x % 2 == 0:
        print("even")
    else:
        print("odd")


# calling function
even_odd(7)
even_odd(8)


def f(x, y=10):
    """document:
    required parameter: x
    optional parameter: y
    """
    return x + y


# calling function
print(f(4))


x = 100
y = 100


def f():
    """document:
    global scope variable : x
    local  scope variable : y
    """
    global x
    x += 1
    print(x)
    y = 10
    y += 1
    print(y)


# calling function
f()
print(x)
print(y)
