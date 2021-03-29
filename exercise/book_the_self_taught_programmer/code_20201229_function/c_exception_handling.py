# 1st revision
# exception handling: none
# a = input("type a number : ")
# b = input("type another  : ")
# a = int(a)
# b = int(b)
# print(a / b)
# print(result)


# 2nd revision
# exception handling: ZeroDivisionError: division by zero
# a = input("type a number : ")
# b = input("type another  : ")
# a = int(a)
# b = int(b)
# try:
#     print(a / b)
# except ZeroDivisionError:
#     print("[oops] zero division error: division by zero..")


# 3rd revision
# exception handling: ValueError: invalid literal for int() with base 10: 'string'
try:
    a = input("type a number : ")
    b = input("type another  : ")
    a = int(a)
    b = int(b)
    print(a / b)
except (ZeroDivisionError, ValueError):
    print("[oops] invalid input..")


#######
# EOF #
#######